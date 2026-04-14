import sys
sys.path.insert(0, "gen")

from gen.SailingParser import SailingParser
from gen.SailingParserVisitor import SailingParserVisitor
from .ship_state import (
    ShipState, SailState, AnchorState, MooringState, EngineMode,
)
from .evaluator import Environment, ExpressionEvaluator


class SailingCommandVisitor(SailingParserVisitor):

    def __init__(self, state: ShipState = None):
        self.state = state or ShipState()
        self.snapshots: list[dict] = []
        self.env = Environment()

    # ─────────────────────────────────────────────────────────
    # HELPERS
    # ─────────────────────────────────────────────────────────
    def _get_text(self, ctx) -> str:
        return "" if ctx is None else ctx.getText()

    def _get_number(self, token) -> float:
        return 0.0 if token is None else float(token.text)

    def _get_string(self, token) -> str:
        if token is None:
            return ""
        return token.text.strip('"')

    def _take_snapshot(self):
        self.snapshots.append({
            "state": self.state.to_dict(),
            "log": [entry.to_dict() for entry in self.state.log],
        })

    def _sync(self):
        """Przelicza prędkość po każdej komendzie."""
        self.state.recompute_sailing_speed()

    # ★ NOWE: ewaluacja wyrażeń
    def _eval(self, expr_ctx) -> object:
        return ExpressionEvaluator(self.state, self.env).eval(expr_ctx)

    def _eval_number(self, expr_ctx, default: float = 0.0) -> float:
        """Ewaluacja z rzutowaniem na float"""
        if expr_ctx is None:
            return default
        val = self._eval(expr_ctx)
        try:
            return float(val)
        except (TypeError, ValueError):
            raise RuntimeError(f"Oczekiwano liczby, dostałem: {val!r}")

    @staticmethod
    def _kts_to_beaufort(kts: float) -> int:
        table = [1, 3, 6, 10, 16, 21, 27, 33, 40, 47, 55, 63]
        for i, k in enumerate(table):
            if kts < k:
                return i
        return 12

    @staticmethod
    def _beaufort_to_kts(b: int) -> float:
        table = {0: 0, 1: 2, 2: 5, 3: 8, 4: 13, 5: 18,
                 6: 24, 7: 30, 8: 37, 9: 44, 10: 52, 11: 60, 12: 70}
        return float(table.get(min(12, max(0, b)), 10))

    def _compass_to_degrees(self, text: str) -> float:
        mapping = {
            "polnoc": 0, "północ": 0, "n": 0,
            "poludnie": 180, "południe": 180, "s": 180,
            "wschod": 90, "wschód": 90, "e": 90,
            "zachod": 270, "zachód": 270, "w": 270,
            "ne": 45, "polnocnywschod": 45, "północnywschód": 45,
            "nw": 315, "polnocnyzachod": 315, "północnyzachód": 315,
            "se": 135, "poludniowywschod": 135, "południowywschód": 135,
            "sw": 225, "poludniowyzachod": 225, "południowyzachód": 225,
        }
        clean = text.replace(" ", "").lower()
        return mapping.get(clean, 0.0)

    # ─────────────────────────────────────────────────────────
    # PROGRAM
    # ─────────────────────────────────────────────────────────
    def visitProgram(self, ctx: SailingParser.ProgramContext):
        self._sync()
        for child in ctx.command():
            count_before = len(self.snapshots)
            self.visit(child)
            self._sync()
            if len(self.snapshots) == count_before:
                self._take_snapshot()
        return self.state

    # ─────────────────────────────────────────────────────────
    # ★ ZMIENNE
    # ─────────────────────────────────────────────────────────
    def visitAssignVar(self, ctx):
        name = ctx.IDENTIFIER().getText()
        value = self._eval(ctx.expression())
        self.env.set(name, value)
        self.state.add_log(f"niech {name} = {value}", "kontrola")

    # ─────────────────────────────────────────────────────────
    # ŻAGLE
    # ─────────────────────────────────────────────────────────
    def visitSetSail(self, ctx):
        name = self._get_text(ctx.sail())
        key = self.state.normalize_sail_key(name)
        self.state.sails[key].state = SailState.SET
        self.state.sails[key].reef_percent = 0.0
        self.state.add_log(f"Postawiono żagiel: {name}", "żagle")

    def visitSetAllSails(self, ctx):
        for sail in self.state.sails.values():
            sail.state = SailState.SET
            sail.reef_percent = 0.0
        self.state.add_log("Postawiono wszystkie żagle", "żagle")

    def visitSetFullSails(self, ctx):
        for sail in self.state.sails.values():
            sail.state = SailState.SET
            sail.reef_percent = 0.0
        self.state.add_log("Pełne żagle!", "żagle")

    def visitSetStormSails(self, ctx):
        for key in self.state.sails:
            self.state.sails[key].state = SailState.FURLED
        self.state.sails["fok"].state = SailState.REEFED
        self.state.sails["fok"].reef_percent = 60.0
        self.state.add_log("Postawiono żagle sztormowe", "żagle")

    def visitFurlSail(self, ctx):
        name = self._get_text(ctx.sail())
        key = self.state.normalize_sail_key(name)
        self.state.sails[key].state = SailState.FURLED
        self.state.sails[key].angle = 0.0
        self.state.add_log(f"Zwinięto żagiel: {name}", "żagle")

    def visitFurlAllSails(self, ctx):
        for sail in self.state.sails.values():
            sail.state = SailState.FURLED
            sail.angle = 0.0
        self.state.add_log("Zwinięto wszystkie żagle", "żagle")

    def visitReefSail(self, ctx):
        name = self._get_text(ctx.sail())
        key = self.state.normalize_sail_key(name)
        # ★ ctx.value to teraz expression, nie token
        percent = self._eval_number(ctx.value, 50.0) if ctx.value else 50.0
        self.state.sails[key].state = SailState.REEFED
        self.state.sails[key].reef_percent = percent
        self.state.add_log(f"Zrefowano {name} do {percent:g}%", "żagle")

    def visitSetSailAngle(self, ctx):
        name = self._get_text(ctx.sail())
        key = self.state.normalize_sail_key(name)
        angle = self._get_number(ctx.angle)
        self.state.sails[key].angle = angle
        self.state.add_log(f"Ustawiono {name} na {angle}°", "żagle")

    def visitTrimSail(self, ctx):
        name = self._get_text(ctx.sail())
        key = self.state.normalize_sail_key(name)
        self.state.sails[key].sheet_tension = min(100, self.state.sails[key].sheet_tension + 20)
        self.state.add_log(f"Wybrano szoty {name}", "żagle")

    def visitEaseSail(self, ctx):
        name = self._get_text(ctx.sail())
        key = self.state.normalize_sail_key(name)
        self.state.sails[key].sheet_tension = max(0, self.state.sails[key].sheet_tension - 20)
        self.state.add_log(f"Poluzowano szoty {name}", "żagle")

    # ─────────────────────────────────────────────────────────
    # OLINOWANIE
    # ─────────────────────────────────────────────────────────
    def visitTightenRigging(self, ctx):
        elem = self._get_text(ctx.riggingElement())
        self.state.rigging_tension[elem] = min(100, self.state.rigging_tension.get(elem, 50) + 20)
        self.state.add_log(f"Dobito {elem}", "takielunek")

    def visitLoosenRigging(self, ctx):
        elem = self._get_text(ctx.riggingElement())
        self.state.rigging_tension[elem] = max(0, self.state.rigging_tension.get(elem, 50) - 20)
        self.state.add_log(f"Poluzowano {elem}", "takielunek")

    def visitTensionRigging(self, ctx):
        elem = self._get_text(ctx.riggingElement())
        self.state.rigging_tension[elem] = min(100, self.state.rigging_tension.get(elem, 50) + 10)
        self.state.add_log(f"Napięto {elem}", "takielunek")

    def visitHaulRigging(self, ctx):
        elem = self._get_text(ctx.riggingElement())
        self.state.rigging_tension[elem] = min(100, self.state.rigging_tension.get(elem, 50) + 15)
        self.state.add_log(f"Wybrano {elem}", "takielunek")

    def visitTensionRiggingPercent(self, ctx):
        elem = self._get_text(ctx.riggingElement())
        val = self._eval_number(ctx.value)   # ★ expression
        self.state.rigging_tension[elem] = val
        self.state.add_log(f"Napięto {elem} do {val:g}%", "takielunek")

    # ─────────────────────────────────────────────────────────
    # STER
    # ─────────────────────────────────────────────────────────
    def _heading_for_point_of_sail(self, pos_name: str, starboard_tack: bool = True) -> float:
        clean = pos_name.replace(" ", "").lower()
        twa_map = {
            "ostrybejdewind": 35,
            "bejdewind": 45,
            "półwiatr": 90, "polwiatr": 90,
            "półbaksztag": 115, "polbaksztag": 115,
            "baksztag": 135,
            "fordewind": 180,
        }
        twa = twa_map.get(clean, 90)
        wind_from = self.state.wind.direction
        if starboard_tack:
            return (wind_from - twa + 360) % 360
        else:
            return (wind_from + twa) % 360

    def visitSteerPointOfSail(self, ctx):
        name = self._get_text(ctx.pointOfSail())
        self.state.heading = self._heading_for_point_of_sail(name)
        self.state.wind_course = name
        self.state.add_log(f"Ster na {name} (heading {self.state.heading:.0f}°)", "ster")

    def visitCourseToPointOfSail(self, ctx):
        name = self._get_text(ctx.pointOfSail())
        self.state.heading = self._heading_for_point_of_sail(name)
        self.state.wind_course = name
        self.state.add_log(f"Kurs: {name} (heading {self.state.heading:.0f}°)", "nawigacja")

    def visitSteerBoardSide(self, ctx):
        side = self._get_text(ctx.boardSide())
        self.state.rudder_angle = -15 if ("lewa" in side or "bak" in side) else 15
        self.state.add_log(f"Ster na {side}", "ster")

    def visitSteerAngle(self, ctx):
        side = self._get_text(ctx.boardSide())
        angle = self._get_number(ctx.angle)
        sign = -1 if ("lewa" in side or "bak" in side) else 1
        self.state.rudder_angle = sign * angle
        self.state.add_log(f"Ster na {side} {angle}°", "ster")

    def visitSteerStraight(self, ctx):
        self.state.rudder_angle = 0.0
        self.state.add_log("Ster prosto", "ster")

    def visitSteerIntoWind(self, ctx):
        self.state.heading = self.state.wind.direction
        self.state.add_log(f"Ster pod wiatr - martwy kąt (heading {self.state.heading:.0f}°)", "ster")

    def visitSteerWithWind(self, ctx):
        self.state.heading = (self.state.wind.direction + 180) % 360
        self.state.add_log(f"Ster z wiatrem - fordewind (heading {self.state.heading:.0f}°)", "ster")

    def visitTack(self, ctx):
        wind_from = self.state.wind.direction
        delta = (self.state.heading - wind_from + 360) % 360
        self.state.heading = (wind_from - delta + 360) % 360
        self.state.add_log(f"Zwrot przez sztag! Nowy kurs: {self.state.heading:.0f}°", "ster")

    def visitGybe(self, ctx):
        wind_from = self.state.wind.direction
        delta = (self.state.heading - wind_from + 360) % 360
        self.state.heading = (wind_from - delta + 360) % 360
        self.state.add_log(f"Zwrot przez rufę! Nowy kurs: {self.state.heading:.0f}°", "ster")

    def visitTurnThroughSide(self, ctx):
        side = self._get_text(ctx.boardSide())
        if "lewa" in side or "bak" in side:
            self.state.heading = (self.state.heading - 90) % 360
            self.state.rudder_angle = -30
        else:
            self.state.heading = (self.state.heading + 90) % 360
            self.state.rudder_angle = 30
        self.state.add_log(f"Zwrot przez {side}! Nowy kurs: {self.state.heading:.0f}°", "ster")

    def visitBearAway(self, ctx):
        angle = self._get_number(ctx.angle) if ctx.angle else 10.0
        self.state.heading = (self.state.heading + angle) % 360
        self.state.add_log(f"Odpadnięto o {angle}°, kurs: {self.state.heading:.0f}°", "ster")

    def visitHeadUp(self, ctx):
        angle = self._get_number(ctx.angle) if ctx.angle else 10.0
        self.state.heading = (self.state.heading - angle) % 360
        self.state.add_log(f"Ostrzono o {angle}°, kurs: {self.state.heading:.0f}°", "ster")

    def visitCourseToBoardSide(self, ctx):
        side = self._get_text(ctx.boardSide())
        self.state.add_log(f"Kurs na {side}", "ster")

    # ─────────────────────────────────────────────────────────
    # KOTWICA / CUMOWANIE
    # ─────────────────────────────────────────────────────────
    def visitDropAnchor(self, ctx):
        self.state.anchor = AnchorState.DROPPED
        self.state.speed = 0.0
        self.state.add_log("Rzucono kotwicę", "kotwica")

    def visitRaiseAnchor(self, ctx):
        self.state.anchor = AnchorState.RAISED
        self.state.add_log("Podniesiono kotwicę", "kotwica")

    def visitMoor(self, ctx):
        self.state.mooring = MooringState.MOORED
        self.state.speed = 0.0
        self.state.add_log("Zacumowano", "cumowanie")

    def visitCastOff(self, ctx):
        self.state.mooring = MooringState.FREE
        self.state.add_log("Odcumowano", "cumowanie")

    # ─────────────────────────────────────────────────────────
    # KURS KOMPASOWY
    # ─────────────────────────────────────────────────────────
    def visitSetCourseNumeric(self, ctx):
        angle = self._eval_number(ctx.value)   # ★ expression
        self.state.heading = angle % 360
        self.state.add_log(f"Kurs: {self.state.heading:.0f}°", "nawigacja")

    def visitSetCourseCompass(self, ctx):
        text = self._get_text(ctx.compassPoint())
        self.state.heading = self._compass_to_degrees(text)
        self.state.add_log(f"Kurs: {text} ({self.state.heading:.0f}°)", "nawigacja")

    def visitSetCourseWaypoint(self, ctx):
        point = self._get_string(ctx.point)
        self.state.add_log(f"Kurs na punkt: {point}", "nawigacja")

    def visitSetCourseBearing(self, ctx):
        angle = self._get_number(ctx.angle)
        self.state.heading = angle % 360
        self.state.add_log(f"Kurs na namiar: {angle}°", "nawigacja")

    # ─────────────────────────────────────────────────────────
    # NAWIGACJA
    # ─────────────────────────────────────────────────────────
    def visitBearingToPoint(self, ctx):
        point = self._get_string(ctx.point)
        self.state.add_log(f"Namiar na punkt: {point}", "nawigacja")

    def visitSetBearing(self, ctx):
        angle = self._get_number(ctx.angle)
        self.state.add_log(f"Peleng: {angle}°", "nawigacja")

    def visitRequestPosition(self, ctx):
        self.state.add_log(f"Pozycja: {self.state.latitude}, {self.state.longitude}", "nawigacja")

    # ─────────────────────────────────────────────────────────
    # PRĘDKOŚĆ / WIOSŁA
    # ─────────────────────────────────────────────────────────
    def visitStartRowing(self, ctx):
        self.state.rowing = EngineMode.FORWARD_SLOW
        self.state.speed = 2.0
        self.state.add_log("Wiosłowanie rozpoczęte", "prędkość")

    def visitRowFullAhead(self, ctx):
        self.state.rowing = EngineMode.FORWARD_FULL
        self.state.speed = 5.0
        self.state.add_log("Wiosła - cała naprzód!", "prędkość")

    def visitRowSlowAhead(self, ctx):
        self.state.rowing = EngineMode.FORWARD_SLOW
        self.state.speed = 2.0
        self.state.add_log("Wiosła - wolny naprzód", "prędkość")

    def visitRowReverse(self, ctx):
        self.state.rowing = EngineMode.REVERSE
        self.state.speed = -1.0
        self.state.add_log("Wiosła - wstecz!", "prędkość")

    def visitOarsInWater(self, ctx):
        self.state.rowing = EngineMode.FORWARD_SLOW
        self.state.speed = 1.5
        self.state.add_log("Wiosła na wodę", "prędkość")

    def visitOarsUp(self, ctx):
        self.state.rowing = EngineMode.OFF
        self.state.add_log("Wiosła podniesione", "prędkość")

    def visitAllStop(self, ctx):
        for sail in self.state.sails.values():
            sail.state = SailState.FURLED
        self.state.rowing = EngineMode.OFF
        self.state.add_log("STOP!", "prędkość")

    # ─────────────────────────────────────────────────────────
    # FLAGI ŻEGLARSKIE
    # ─────────────────────────────────────────────────────────
    def visitRaiseEnsign(self, ctx):
        self.state.flags["bandera"] = True
        self.state.add_log("Podniesiono banderę", "flagi")

    def visitLowerEnsign(self, ctx):
        self.state.flags["bandera"] = False
        self.state.add_log("Opuszczono banderę", "flagi")

    def visitRaiseClubFlag(self, ctx):
        self.state.flags["klubowa"] = True
        self.state.add_log("Podniesiono flagę klubową", "flagi")

    def visitLowerClubFlag(self, ctx):
        self.state.flags["klubowa"] = False
        self.state.add_log("Opuszczono flagę klubową", "flagi")

    def visitRaiseCourtesyFlag(self, ctx):
        self.state.flags["goscia"] = True
        self.state.add_log("Podniesiono flagę gościa", "flagi")

    def visitLowerCourtesyFlag(self, ctx):
        self.state.flags["goscia"] = False
        self.state.add_log("Opuszczono flagę gościa", "flagi")

    def visitRaiseQuarantineFlag(self, ctx):
        self.state.flags["q"] = True
        self.state.add_log("Podniesiono flagę Q (żółta, prośba o odprawę)", "flagi")

    def visitLowerQuarantineFlag(self, ctx):
        self.state.flags["q"] = False
        self.state.add_log("Opuszczono flagę Q", "flagi")

    def visitRaiseProtestFlag(self, ctx):
        self.state.flags["protestowa"] = True
        self.state.add_log("Podniesiono flagę protestową", "flagi")

    def visitLowerProtestFlag(self, ctx):
        self.state.flags["protestowa"] = False
        self.state.add_log("Opuszczono flagę protestową", "flagi")

    def visitRaisePennant(self, ctx):
        self.state.flags["proporczyk"] = True
        self.state.add_log("Podniesiono proporczyk", "flagi")

    def visitLowerPennant(self, ctx):
        self.state.flags["proporczyk"] = False
        self.state.add_log("Opuszczono proporczyk", "flagi")

    def visitRaiseCustomFlag(self, ctx):
        flag = self._get_string(ctx.flag)
        self.state.flags["custom"].append(flag)
        self.state.add_log(f"Podniesiono flagę: {flag}", "flagi")

    def visitLowerCustomFlag(self, ctx):
        flag = self._get_string(ctx.flag)
        if flag in self.state.flags["custom"]:
            self.state.flags["custom"].remove(flag)
        self.state.add_log(f"Opuszczono flagę: {flag}", "flagi")

    def visitSignalFlags(self, ctx):
        self.state.add_log("Sygnalizacja flagowa", "flagi")

    # ─────────────────────────────────────────────────────────
    # DZIENNIK POKŁADOWY
    # ─────────────────────────────────────────────────────────
    def visitLogMessage(self, ctx):
        msg = self._get_string(ctx.message)
        self.state.add_log(msg, "dziennik")

    def visitLogPosition(self, ctx):
        self.state.add_log(f"Pozycja: {self.state.latitude}, {self.state.longitude}", "dziennik")

    def visitLogWeather(self, ctx):
        self.state.add_log(f"Wiatr: {self.state.wind}, kurs {self.state.heading:.0f}°", "dziennik")

    def visitLogEvent(self, ctx):
        msg = self._get_string(ctx.message)
        self.state.add_log(f"Zdarzenie: {msg}", "dziennik")

    def visitLogShipState(self, ctx):
        self.state.add_log("Zalogowano stan jednostki", "dziennik")

    # ─────────────────────────────────────────────────────────
    # WIATR
    # ─────────────────────────────────────────────────────────
    def visitSetWindDirectionDeg(self, ctx):
        angle = self._eval_number(ctx.angle)
        self.state.wind.direction = angle % 360
        self.state.add_log(f"Wiatr z kierunku {self.state.wind.direction:.0f}°", "wiatr")

    def visitSetWindCompass(self, ctx):
        text = self._get_text(ctx.compassPoint())
        self.state.wind.direction = self._compass_to_degrees(text)
        self.state.add_log(f"Wiatr z kierunku: {text} ({self.state.wind.direction:.0f}°)", "wiatr")

    def visitSetWindSpeed(self, ctx):
        val = self._eval_number(ctx.value)
        self.state.wind.speed = val
        self.state.wind.beaufort = self._kts_to_beaufort(val)
        self.state.add_log(f"Prędkość wiatru: {val:.0f} kn (B{self.state.wind.beaufort})", "wiatr")

    def visitSetWindBeaufort(self, ctx):
        val = int(self._eval_number(ctx.value))
        self.state.wind.beaufort = val
        self.state.wind.speed = self._beaufort_to_kts(val)
        self.state.add_log(f"Siła wiatru: {val} B (~{self.state.wind.speed:.0f} kn)", "wiatr")

    # ─────────────────────────────────────────────────────────
    # RAPORTY
    # ─────────────────────────────────────────────────────────
    def visitReportWind(self, ctx):
        self.state.add_log(f"Raport wiatru: {self.state.wind}", "pogoda")

    def visitReportWeather(self, ctx):
        self.state.add_log(f"Raport pogody: wiatr {self.state.wind}", "pogoda")

    def visitReportDepth(self, ctx):
        self.state.add_log("Raport: głębokość", "pogoda")

    # ─────────────────────────────────────────────────────────
    # ★ KONTROLA PRZEPŁYWU
    # ─────────────────────────────────────────────────────────
    def visitRepeat(self, ctx):
        times = int(self._eval_number(ctx.times))
        times = max(0, min(times, 1000))
        self.state.add_log(f"Powtarzanie {times} razy...", "kontrola")
        for _ in range(times):
            for cmd in ctx.command():
                self.visit(cmd)
                self._sync()
                self._take_snapshot()

    def visitWaitDuration(self, ctx):
        val = self._eval_number(ctx.duration().value)
        unit = self._get_text(ctx.duration().timeUnit())
        self.state.add_log(f"Czekanie {val:g} {unit}...", "kontrola")

    def visitWaitUntil(self, ctx):
        result = self._evaluate_condition(ctx.condition())
        self.state.add_log(
            f"Czekanie na warunek... (aktualnie: {'spełniony' if result else 'nie'})",
            "kontrola"
        )

    # ─────────────────────────────────────────────────────────
    # WARUNKI
    # ─────────────────────────────────────────────────────────
    def _evaluate_condition(self, cond_ctx) -> bool:
        """cond_ctx to ConditionContext, który opakowuje expression."""
        try:
            return bool(self._eval(cond_ctx.expression()))
        except Exception as e:
            self.state.add_log(f"Błąd warunku: {e}", "kontrola")
            return False

    def visitIfCondition(self, ctx):
        if self._evaluate_condition(ctx.condition()):
            self.state.add_log("Warunek spełniony - wykonuję", "kontrola")
            self.visit(ctx.command(0))
            self._sync()
            self._take_snapshot()
        elif len(ctx.command()) > 1:
            self.state.add_log("Warunek niespełniony - alternatywa", "kontrola")
            self.visit(ctx.command(1))
            self._sync()
            self._take_snapshot()
        else:
            self.state.add_log("Warunek niespełniony - pomijam", "kontrola")

    def visitIfConditionBlock(self, ctx):
        # Gramatyka: `JEZELI cond { cmd+ } (INACZEJ { cmd+ })?`
        # ctx.command() zwraca komendy z obu bloków - dzielimy po pozycji tokenu INACZEJ.
        commands = list(ctx.command())
        inaczej_node = ctx.INACZEJ()

        if inaczej_node is None:
            then_cmds = commands
            else_cmds = []
        else:
            inaczej_idx = inaczej_node.getSymbol().tokenIndex
            then_cmds = [c for c in commands if c.stop.tokenIndex < inaczej_idx]
            else_cmds = [c for c in commands if c.start.tokenIndex > inaczej_idx]

        if self._evaluate_condition(ctx.condition()):
            self.state.add_log("Warunek blokowy spełniony", "kontrola")
            for cmd in then_cmds:
                self.visit(cmd)
                self._sync()
                self._take_snapshot()
        elif else_cmds:
            self.state.add_log("Warunek blokowy - blok alternatywny", "kontrola")
            for cmd in else_cmds:
                self.visit(cmd)
                self._sync()
                self._take_snapshot()
        else:
            self.state.add_log("Warunek blokowy niespełniony - pomijam", "kontrola")
