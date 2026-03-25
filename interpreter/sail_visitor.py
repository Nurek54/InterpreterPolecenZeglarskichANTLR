import sys
sys.path.insert(0, "gen")

from gen.SailingParser import SailingParser
from gen.SailingParserVisitor import SailingParserVisitor
from .ship_state import (
    ShipState, SailState, SailInfo, AnchorState, MooringState,
    EngineMode, CannonState, BoardingPhase, TacticMode,
    AlertLevel, CrewStation
)

class SailingCommandVisitor(SailingParserVisitor):

    def __init__(self, state: ShipState = None):
        self.state = state or ShipState()

    def _get_sail_name(self, ctx) -> str:
        return ctx.getText()

    def _get_text(self, ctx) -> str:
        if ctx is None:
            return ""
        return ctx.getText()

    def _get_number(self, token) -> float:
        """Parsuje NUMBER token na float."""
        if token is None:
            return 0.0
        return float(token.text)

    def _get_string(self, token) -> str:
        if token is None:
            return ""
        text = token.text
        return text.strip('"')

    # ─────────────────────────────────────────────────────────────────────
    # PROGRAM / COMMAND
    # ─────────────────────────────────────────────────────────────────────

    def visitProgram(self, ctx: SailingParser.ProgramContext):
        for child in ctx.command():
            self.visit(child)
        return self.state

    # ─────────────────────────────────────────────────────────────────────
    # ŻAGLE
    # ─────────────────────────────────────────────────────────────────────

    def visitSetSail(self, ctx: SailingParser.SetSailContext):
        name = self._get_sail_name(ctx.sail())
        key = self.state.normalize_sail_key(name)
        self.state.sails[key].state = SailState.SET
        self.state.sails[key].reef_percent = 0.0
        self.state.add_log(f"Postawiono żagiel: {name}", "żagle")

    def visitSetAllSails(self, ctx):
        for key, sail in self.state.sails.items():
            sail.state = SailState.SET
            sail.reef_percent = 0.0
        self.state.add_log("Postawiono wszystkie żagle", "żagle")

    def visitSetFullSails(self, ctx):
        for key, sail in self.state.sails.items():
            sail.state = SailState.SET
            sail.reef_percent = 0.0
        self.state.add_log("Pełne żagle!", "żagle")

    def visitSetStormSails(self, ctx):
        for key in self.state.sails:
            self.state.sails[key].state = SailState.FURLED
        self.state.sails["trysel"].state = SailState.SET
        self.state.sails["sztormfok"].state = SailState.SET
        self.state.add_log("Postawiono żagle sztormowe", "żagle")

    def visitFurlSail(self, ctx: SailingParser.FurlSailContext):
        name = self._get_sail_name(ctx.sail())
        key = self.state.normalize_sail_key(name)
        self.state.sails[key].state = SailState.FURLED
        self.state.sails[key].angle = 0.0
        self.state.add_log(f"Zwinięto żagiel: {name}", "żagle")

    def visitFurlAllSails(self, ctx):
        for key, sail in self.state.sails.items():
            sail.state = SailState.FURLED
            sail.angle = 0.0
        self.state.add_log("Zwinięto wszystkie żagle", "żagle")

    def visitReefSail(self, ctx: SailingParser.ReefSailContext):
        name = self._get_sail_name(ctx.sail())
        key = self.state.normalize_sail_key(name)
        percent = self._get_number(ctx.value) if ctx.value else 50.0
        self.state.sails[key].state = SailState.REEFED
        self.state.sails[key].reef_percent = percent
        self.state.add_log(f"Zrefowano {name} do {percent}%", "żagle")

    def visitSetSailAngle(self, ctx: SailingParser.SetSailAngleContext):
        name = self._get_sail_name(ctx.sail())
        key = self.state.normalize_sail_key(name)
        angle = self._get_number(ctx.angle)
        self.state.sails[key].angle = angle
        self.state.add_log(f"Ustawiono {name} na {angle}°", "żagle")

    def visitTrimSail(self, ctx: SailingParser.TrimSailContext):
        name = self._get_sail_name(ctx.sail())
        key = self.state.normalize_sail_key(name)
        self.state.sails[key].sheet_tension = min(100, self.state.sails[key].sheet_tension + 20)
        self.state.add_log(f"Wybrano szoty {name}", "żagle")

    def visitEaseSail(self, ctx: SailingParser.EaseSailContext):
        name = self._get_sail_name(ctx.sail())
        key = self.state.normalize_sail_key(name)
        self.state.sails[key].sheet_tension = max(0, self.state.sails[key].sheet_tension - 20)
        self.state.add_log(f"Poluzowano szoty {name}", "żagle")

    def visitTrimSailToAngle(self, ctx: SailingParser.TrimSailToAngleContext):
        name = self._get_sail_name(ctx.sail())
        key = self.state.normalize_sail_key(name)
        angle = self._get_number(ctx.angle)
        self.state.sails[key].angle = angle
        self.state.add_log(f"Wytrymowano {name} do {angle}°", "żagle")

    def visitEaseSailPercent(self, ctx: SailingParser.EaseSailPercentContext):
        name = self._get_sail_name(ctx.sail())
        key = self.state.normalize_sail_key(name)
        val = self._get_number(ctx.value)
        self.state.sails[key].sheet_tension = val
        self.state.add_log(f"Poluzowano szoty {name} na {val}%", "żagle")

    # ─────────────────────────────────────────────────────────────────────
    # OLINOWANIE
    # ─────────────────────────────────────────────────────────────────────

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
        val = self._get_number(ctx.value)
        self.state.rigging_tension[elem] = val
        self.state.add_log(f"Napięto {elem} do {val}%", "takielunek")

    # ─────────────────────────────────────────────────────────────────────
    # STER
    # ─────────────────────────────────────────────────────────────────────

    def visitSteerWindDirection(self, ctx):
        direction = self._get_text(ctx.windDirection())
        self.state.wind_course = direction
        self.state.add_log(f"Ster na kurs wiatrowy: {direction}", "ster")

    def visitSteerBoardSide(self, ctx):
        side = self._get_text(ctx.boardSide())
        self.state.rudder_angle = -15 if "lewa" in side or "bak" in side else 15
        self.state.add_log(f"Ster na {side}", "ster")

    def visitSteerAngle(self, ctx):
        side = self._get_text(ctx.boardSide())
        angle = self._get_number(ctx.angle)
        sign = -1 if "lewa" in side or "bak" in side else 1
        self.state.rudder_angle = sign * angle
        self.state.add_log(f"Ster na {side} {angle}°", "ster")

    def visitSteerStraight(self, ctx):
        self.state.rudder_angle = 0.0
        self.state.add_log("Ster prosto", "ster")

    def visitTack(self, ctx):
        self.state.heading = (self.state.heading + 90) % 360
        self.state.add_log(f"Zwrot przez sztag! Nowy kurs: {self.state.heading}°", "ster")

    def visitGybe(self, ctx):
        self.state.heading = (self.state.heading + 90) % 360
        self.state.add_log(f"Zwrot przez rufę! Nowy kurs: {self.state.heading}°", "ster")

    def visitBearAway(self, ctx):
        angle = self._get_number(ctx.angle) if ctx.angle else 10.0
        self.state.heading = (self.state.heading + angle) % 360
        self.state.add_log(f"Odpadnięto o {angle}°, kurs: {self.state.heading}°", "ster")

    def visitHeadUp(self, ctx):
        angle = self._get_number(ctx.angle) if ctx.angle else 10.0
        self.state.heading = (self.state.heading - angle) % 360
        self.state.add_log(f"Ostrzono o {angle}°, kurs: {self.state.heading}°", "ster")

    def visitCourseToWindDir(self, ctx):
        direction = self._get_text(ctx.windDirection())
        self.state.wind_course = direction
        self.state.add_log(f"Kurs na {direction}", "ster")

    def visitCourseToBoardSide(self, ctx):
        side = self._get_text(ctx.boardSide())
        self.state.add_log(f"Kurs na {side}", "ster")

    # ─────────────────────────────────────────────────────────────────────
    # KOTWICA
    # ─────────────────────────────────────────────────────────────────────

    def visitDropAnchor(self, ctx):
        self.state.anchor = AnchorState.DROPPED
        self.state.speed = 0.0
        self.state.add_log("Rzucono kotwicę", "kotwica")

    def visitRaiseAnchor(self, ctx):
        self.state.anchor = AnchorState.RAISED
        self.state.chain_length = 0.0
        self.state.add_log("Podniesiono kotwicę", "kotwica")

    def visitPayOutChain(self, ctx):
        length = self._get_number(ctx.length) if ctx.length else 20.0
        self.state.chain_length = length
        self.state.add_log(f"Wytrawiono łańcuch na {length}", "kotwica")

    def visitHaulChain(self, ctx):
        self.state.chain_length = max(0, self.state.chain_length - 10)
        self.state.add_log("Dobrano łańcuch", "kotwica")

    def visitPayOutLine(self, ctx):
        length = self._get_number(ctx.length) if ctx.length else 20.0
        self.state.add_log(f"Wytrawiono linę kotwiczną na {length}", "kotwica")

    # ─────────────────────────────────────────────────────────────────────
    # CUMOWANIE
    # ─────────────────────────────────────────────────────────────────────

    def visitMoor(self, ctx):
        self.state.mooring = MooringState.MOORED
        self.state.speed = 0.0
        self.state.add_log("Zacumowano", "cumowanie")

    def visitCastOff(self, ctx):
        self.state.mooring = MooringState.FREE
        self.state.add_log("Odcumowano", "cumowanie")

    def visitThrowMooringLines(self, ctx):
        self.state.add_log("Rzucono cumy", "cumowanie")

    def visitHaulMooringLines(self, ctx):
        self.state.add_log("Dobrano cumy", "cumowanie")

    def visitThrowGrapplingHooks(self, ctx):
        self.state.grappling_hooks = True
        self.state.add_log("Rzucono haki abordażowe!", "abordaż")

    # ─────────────────────────────────────────────────────────────────────
    # KURS KOMPASOWY
    # ─────────────────────────────────────────────────────────────────────

    def _compass_to_degrees(self, text: str) -> float:
        mapping = {
            "polnoc": 0, "północ": 0,
            "poludnie": 180, "południe": 180,
            "wschod": 90, "wschód": 90,
            "zachod": 270, "zachód": 270,
            "NE": 45, "polnocnywschod": 45, "polnocnywschód": 45,
            "NW": 315, "polnocnyzachod": 315, "polnocnyzachód": 315,
            "SE": 135, "poludniowywschod": 135, "poludniowywschód": 135,
            "SW": 225, "poludniowyzachod": 225, "poludniowyzachód": 225,
        }
        clean = text.replace(" ", "").lower()
        return mapping.get(clean, 0.0)

    def visitSetCourseNumeric(self, ctx):
        angle = self._get_number(ctx.angle)
        self.state.heading = angle % 360
        self.state.add_log(f"Kurs: {self.state.heading}°", "nawigacja")

    def visitSetCourseCompass(self, ctx):
        text = self._get_text(ctx.compassPoint())
        self.state.heading = self._compass_to_degrees(text)
        self.state.add_log(f"Kurs: {text} ({self.state.heading}°)", "nawigacja")

    def visitSetCourseWaypoint(self, ctx):
        point = self._get_string(ctx.point)
        self.state.add_log(f"Kurs na punkt: {point}", "nawigacja")

    def visitSetCourseIsland(self, ctx):
        point = self._get_string(ctx.point)
        self.state.add_log(f"Kurs na wyspę: {point}", "nawigacja")

    def visitSetCoursePort(self, ctx):
        point = self._get_string(ctx.point)
        self.state.add_log(f"Kurs na port: {point}", "nawigacja")

    def visitSetCourseBay(self, ctx):
        point = self._get_string(ctx.point)
        self.state.add_log(f"Kurs na zatokę: {point}", "nawigacja")

    def visitSetCourseHideout(self, ctx):
        point = self._get_string(ctx.point)
        self.state.add_log(f"Kurs na kryjówkę: {point}", "nawigacja")

    def visitSetCourseBearing(self, ctx):
        angle = self._get_number(ctx.angle)
        self.state.heading = angle % 360
        self.state.add_log(f"Kurs na namiar: {angle}°", "nawigacja")

    # ─────────────────────────────────────────────────────────────────────
    # NAWIGACJA
    # ─────────────────────────────────────────────────────────────────────

    def visitBearingToPoint(self, ctx):
        point = self._get_string(ctx.point)
        self.state.add_log(f"Namiar na punkt: {point}", "nawigacja")

    def visitSetBearing(self, ctx):
        angle = self._get_number(ctx.angle)
        self.state.add_log(f"Peleng: {angle}°", "nawigacja")

    def visitReportPosition(self, ctx):
        self.state.add_log("Pozycja zgłoszona", "nawigacja")

    def visitRequestPosition(self, ctx):
        self.state.add_log(f"Pozycja: {self.state.latitude}, {self.state.longitude}", "nawigacja")

    # ─────────────────────────────────────────────────────────────────────
    # PRĘDKOŚĆ / WIOSŁA
    # ─────────────────────────────────────────────────────────────────────

    def visitStartRowing(self, ctx):
        self.state.rowing = EngineMode.FORWARD_SLOW
        self.state.speed = 2.0
        self.state.add_log("Wiosłowanie rozpoczęte", "prędkość")

    def visitRowFullAhead(self, ctx):
        self.state.rowing = EngineMode.FORWARD_FULL
        self.state.speed = 5.0
        self.state.add_log("Wiosła — cała naprzód!", "prędkość")

    def visitRowSlowAhead(self, ctx):
        self.state.rowing = EngineMode.FORWARD_SLOW
        self.state.speed = 2.0
        self.state.add_log("Wiosła — wolny naprzód", "prędkość")

    def visitRowReverse(self, ctx):
        self.state.rowing = EngineMode.REVERSE
        self.state.speed = -1.0
        self.state.add_log("Wiosła — wstecz!", "prędkość")

    def visitOarsInWater(self, ctx):
        self.state.rowing = EngineMode.FORWARD_SLOW
        self.state.add_log("Wiosła na wodę", "prędkość")

    def visitOarsUp(self, ctx):
        self.state.rowing = EngineMode.OFF
        self.state.add_log("Wiosła podniesione", "prędkość")

    def visitFullAhead(self, ctx):
        self.state.speed = 12.0
        self.state.add_log("Cała naprzód!", "prędkość")

    def visitSlowAhead(self, ctx):
        self.state.speed = 4.0
        self.state.add_log("Wolny naprzód", "prędkość")

    def visitMediumAhead(self, ctx):
        self.state.speed = 8.0
        self.state.add_log("Średni naprzód", "prędkość")

    def visitAllStop(self, ctx):
        self.state.speed = 0.0
        self.state.rowing = EngineMode.OFF
        self.state.add_log("STOP!", "prędkość")

    def visitFullSailSpeed(self, ctx):
        for key in self.state.sails:
            self.state.sails[key].state = SailState.SET
        self.state.speed = 12.0
        self.state.add_log("Pełne żagle — pełna prędkość!", "prędkość")

    # ─────────────────────────────────────────────────────────────────────
    # UZBROJENIE / WALKA
    # ─────────────────────────────────────────────────────────────────────

    def visitLoadCannons(self, ctx):
        name = self._get_text(ctx.cannonGroup())
        key = self.state.normalize_cannon_key(name)
        self.state.cannons[key].state = CannonState.LOADED
        self.state.cannons[key].ammo = "kula"
        self.state.add_log(f"Załadowano {name}", "uzbrojenie")

    def visitLoadCannonsAmmo(self, ctx):
        name = self._get_text(ctx.cannonGroup())
        ammo = self._get_text(ctx.ammoType())
        key = self.state.normalize_cannon_key(name)
        self.state.cannons[key].state = CannonState.LOADED
        self.state.cannons[key].ammo = ammo
        self.state.add_log(f"Załadowano {name} ({ammo})", "uzbrojenie")

    def visitAimCannons(self, ctx):
        name = self._get_text(ctx.cannonGroup())
        target = self._get_text(ctx.target())
        key = self.state.normalize_cannon_key(name)
        self.state.cannons[key].state = CannonState.AIMED
        self.state.cannons[key].target = target
        self.state.add_log(f"Wycelowano {name} na {target}", "uzbrojenie")

    def visitAimCannonsAngle(self, ctx):
        name = self._get_text(ctx.cannonGroup())
        angle = self._get_number(ctx.angle)
        key = self.state.normalize_cannon_key(name)
        self.state.cannons[key].state = CannonState.AIMED
        self.state.cannons[key].aim_angle = angle
        self.state.add_log(f"Wycelowano {name} na {angle}°", "uzbrojenie")

    def visitFireCannons(self, ctx):
        name = self._get_text(ctx.cannonGroup())
        key = self.state.normalize_cannon_key(name)
        self.state.cannons[key].state = CannonState.EMPTY
        self.state.cannons[key].ammo = ""
        self.state.cannons[key].target = ""
        self.state.cargo["proch"] = max(0, self.state.cargo["proch"] - 10)
        self.state.cargo["amunicja"] = max(0, self.state.cargo["amunicja"] - 5)
        self.state.add_log(f"OGNIA {name}! 💥", "uzbrojenie")

    def visitFireAll(self, ctx):
        for key in self.state.cannons:
            self.state.cannons[key].state = CannonState.EMPTY
            self.state.cannons[key].ammo = ""
        self.state.cargo["proch"] = max(0, self.state.cargo["proch"] - 30)
        self.state.add_log("OGNIA WSZYSTKIE DZIAŁA! 💥💥💥", "uzbrojenie")

    def visitBroadside(self, ctx):
        side = self._get_text(ctx.boardSide())
        self.state.cargo["proch"] = max(0, self.state.cargo["proch"] - 20)
        self.state.add_log(f"SALWA {side}! 💥💥", "uzbrojenie")

    def visitBroadsideLeft(self, ctx):
        self.state.cargo["proch"] = max(0, self.state.cargo["proch"] - 20)
        self.state.add_log("SALWA lewa burta! 💥💥", "uzbrojenie")

    def visitBroadsideRight(self, ctx):
        self.state.cargo["proch"] = max(0, self.state.cargo["proch"] - 20)
        self.state.add_log("SALWA prawa burta! 💥💥", "uzbrojenie")

    def visitPrepareMuskets(self, ctx):
        self.state.cannons["muszkiety"].state = CannonState.LOADED
        self.state.add_log("Przygotowano muszkiety", "uzbrojenie")

    def visitFireMuskets(self, ctx):
        self.state.cannons["muszkiety"].state = CannonState.EMPTY
        self.state.add_log("Ogień z muszkietów! 💥", "uzbrojenie")

    # ─────────────────────────────────────────────────────────────────────
    # ABORDAŻ
    # ─────────────────────────────────────────────────────────────────────

    def visitPrepareBoarding(self, ctx):
        self.state.boarding = BoardingPhase.PREPARING
        self.state.add_log("Przygotowanie do abordażu!", "abordaż")

    def visitBoard(self, ctx):
        self.state.boarding = BoardingPhase.BOARDING
        self.state.add_log("ABORDAŻ! ⚔️", "abordaż")

    def visitStorm(self, ctx):
        self.state.boarding = BoardingPhase.STORMING
        self.state.add_log("SZTURM! ⚔️⚔️", "abordaż")

    def visitRetreat(self, ctx):
        self.state.boarding = BoardingPhase.RETREATING
        self.state.add_log("Wycofanie z abordażu", "abordaż")

    def visitThrowBoardingLines(self, ctx):
        self.state.boarding = BoardingPhase.HOOKS_THROWN
        self.state.add_log("Rzucono liny abordażowe!", "abordaż")

    def visitThrowGrapplingHooksBoard(self, ctx):
        self.state.grappling_hooks = True
        self.state.boarding = BoardingPhase.HOOKS_THROWN
        self.state.add_log("Rzucono haki abordażowe! ⚓", "abordaż")

    def visitGangwayToSide(self, ctx):
        side = self._get_text(ctx.boardSide())
        self.state.add_log(f"Trap na {side}", "abordaż")

    # ─────────────────────────────────────────────────────────────────────
    # ŁADUNEK / ŁUPY
    # ─────────────────────────────────────────────────────────────────────

    def _cargo_key(self, ctx) -> str:
        text = self._get_text(ctx)
        mapping = {
            "złoto": "zloto", "zloto": "zloto",
            "srebro": "srebro", "łupy": "lupy", "lupy": "lupy",
            "amunicja": "amunicja", "amunicję": "amunicja",
            "prowiant": "prowiant", "rum": "rum",
            "wodapitna": "woda_pitna", "wodępitną": "woda_pitna",
            "proch": "proch", "beczki": "beczki",
            "skrzynie": "skrzynie", "skarb": "skarb",
        }
        clean = text.replace(" ", "").lower()
        return mapping.get(clean, clean)

    def visitLoadCargo(self, ctx):
        key = self._cargo_key(ctx.cargoType())
        amount = int(self._get_number(ctx.value)) if ctx.value else 10
        self.state.cargo[key] = self.state.cargo.get(key, 0) + amount
        self.state.add_log(f"Załadowano {key} x{amount}", "ładunek")

    def visitUnloadCargo(self, ctx):
        key = self._cargo_key(ctx.cargoType())
        amount = int(self._get_number(ctx.value)) if ctx.value else 10
        self.state.cargo[key] = max(0, self.state.cargo.get(key, 0) - amount)
        self.state.add_log(f"Rozładowano {key} x{amount}", "ładunek")

    def visitTransferCargo(self, ctx):
        key = self._cargo_key(ctx.cargoType())
        self.state.add_log(f"Przeładowano {key}", "ładunek")

    def visitBuryTreasure(self, ctx):
        location = self._get_string(ctx.point)
        self.state.buried_treasures.append(location)
        self.state.cargo["skarb"] = max(0, self.state.cargo["skarb"] - 1)
        self.state.add_log(f"Zakopano skarb na wyspie: {location} 🗺️", "ładunek")

    def visitDigTreasure(self, ctx):
        location = self._get_string(ctx.point)
        self.state.cargo["skarb"] = self.state.cargo.get("skarb", 0) + 1
        self.state.add_log(f"Wykopano skarb na wyspie: {location} 💰", "ładunek")

    def visitCargoReport(self, ctx):
        self.state.add_log("Raport ładowni", "ładunek")

    def visitCargoStateReport(self, ctx):
        self.state.add_log("Raport stanu ładowni", "ładunek")

    # ─────────────────────────────────────────────────────────────────────
    # OBSERWACJA / ZWIAD
    # ─────────────────────────────────────────────────────────────────────

    def visitScanHorizon(self, ctx):
        self.state.scouting_active = True
        self.state.add_log("Obserwacja horyzontu 🔭", "obserwacja")

    def visitScanSide(self, ctx):
        side = self._get_text(ctx.boardSide())
        self.state.scouting_active = True
        self.state.add_log(f"Obserwacja {side}", "obserwacja")

    def visitScanDirection(self, ctx):
        direction = self._get_text(ctx.compassPoint())
        self.state.scouting_active = True
        self.state.add_log(f"Obserwacja kierunek: {direction}", "obserwacja")

    def visitIdentifyShip(self, ctx):
        self.state.add_log("Identyfikacja statku", "obserwacja")

    def visitIdentifyTarget(self, ctx):
        target = self._get_text(ctx.target())
        self.state.identified_targets.append(target)
        self.state.add_log(f"Zidentyfikowano: {target}", "obserwacja")

    def visitLookoutToCrowsNest(self, ctx):
        self.state.lookout_position = "bocianie gniazdo"
        self.state.scouting_active = True
        self.state.add_log("Obserwator na bocianie gniazdo! 🔭", "obserwacja")

    def visitLookoutReport(self, ctx):
        self.state.add_log("Raport obserwatora", "obserwacja")

    # ─────────────────────────────────────────────────────────────────────
    # TAKTYKA
    # ─────────────────────────────────────────────────────────────────────

    def visitChaseTarget(self, ctx):
        target = self._get_text(ctx.target())
        self.state.tactic = TacticMode.CHASING
        self.state.chase_target = target
        self.state.add_log(f"Pościg za {target}! 🏴‍☠️", "taktyka")

    def visitChaseNamed(self, ctx):
        name = self._get_string(ctx.point)
        self.state.tactic = TacticMode.CHASING
        self.state.chase_target = name
        self.state.add_log(f"Pościg za statkiem: {name}!", "taktyka")

    def visitFlee(self, ctx):
        self.state.tactic = TacticMode.FLEEING
        self.state.add_log("Uciekamy! 💨", "taktyka")

    def visitIntercept(self, ctx):
        target = self._get_text(ctx.target())
        self.state.tactic = TacticMode.INTERCEPTING
        self.state.chase_target = target
        self.state.add_log(f"Przechwyt {target}", "taktyka")

    def visitBlockTarget(self, ctx):
        target = self._get_text(ctx.target())
        self.state.tactic = TacticMode.BLOCKING
        self.state.add_log(f"Blokada {target}", "taktyka")

    def visitAmbush(self, ctx):
        self.state.tactic = TacticMode.AMBUSH
        self.state.add_log("Zasadzka! 🏴‍☠️", "taktyka")

    def visitEvadeTarget(self, ctx):
        target = self._get_text(ctx.target())
        self.state.tactic = TacticMode.EVADING
        self.state.add_log(f"Unikanie {target}", "taktyka")

    def visitRamTarget(self, ctx):
        target = self._get_text(ctx.target())
        self.state.tactic = TacticMode.RAMMING
        self.state.add_log(f"TARANOWANIE {target}! 💀", "taktyka")

    def visitDemandSurrender(self, ctx):
        self.state.tactic = TacticMode.DEMANDING_SURRENDER
        self.state.add_log("Żądanie kapitulacji! ☠️", "taktyka")

    def visitSurrender(self, ctx):
        self.state.tactic = TacticMode.SURRENDERING
        self.state.add_log("Poddajemy się... 🏳️", "taktyka")

    def visitExchangeFire(self, ctx):
        self.state.tactic = TacticMode.EXCHANGING_FIRE
        self.state.add_log("Wymiana ognia! 💥", "taktyka")

    def visitBattleStations(self, ctx):
        self.state.alert = AlertLevel.BATTLE_STATIONS
        for role in self.state.crew:
            self.state.crew[role].station = CrewStation.STATIONS
        self.state.add_log("ALARM BOJOWY! ⚔️ Wszyscy na stanowiska!", "taktyka")

    # ─────────────────────────────────────────────────────────────────────
    # ZAŁOGA
    # ─────────────────────────────────────────────────────────────────────

    def visitCrewToStations(self, ctx):
        for role in self.state.crew:
            self.state.crew[role].station = CrewStation.STATIONS
        self.state.add_log("Załoga na stanowiska!", "załoga")

    def visitManOverboard(self, ctx):
        self.state.man_overboard = True
        if ctx.boardSide():
            self.state.man_overboard_side = self._get_text(ctx.boardSide())
        self.state.add_log(f"🆘 CZŁOWIEK ZA BURTĄ! {self.state.man_overboard_side}", "załoga")

    def visitAllOnDeck(self, ctx):
        for role in self.state.crew:
            self.state.crew[role].station = CrewStation.ON_DECK
        self.state.add_log("Wszyscy na pokład!", "załoga")

    def visitWatchChange(self, ctx):
        self.state.watch = ctx.zmiana.text
        self.state.add_log(f"Zmiana wachty: {self.state.watch}", "załoga")

    def visitCrewReport(self, ctx):
        role = self._get_text(ctx.role())
        self.state.add_log(f"Raport od: {role}", "załoga")

    def visitRoleToStation(self, ctx):
        role = self._get_text(ctx.role())
        if role in self.state.crew:
            self.state.crew[role].station = CrewStation.STATIONS
        self.state.add_log(f"{role} na stanowisko!", "załoga")

    def visitCrewStateReport(self, ctx):
        self.state.add_log("Raport stanu załogi", "załoga")

    # ─────────────────────────────────────────────────────────────────────
    # FLAGI
    # ─────────────────────────────────────────────────────────────────────

    def visitRaiseJollyRoger(self, ctx):
        self.state.flags["jolly_roger"] = True
        self.state.add_log("Podniesiono Jolly Rogera! 🏴‍☠️", "flagi")

    def visitLowerJollyRoger(self, ctx):
        self.state.flags["jolly_roger"] = False
        self.state.add_log("Opuszczono Jolly Rogera", "flagi")

    def visitRaiseBanner(self, ctx):
        self.state.flags["bandera"] = True
        self.state.add_log("Podniesiono banderę", "flagi")

    def visitLowerBanner(self, ctx):
        self.state.flags["bandera"] = False
        self.state.add_log("Opuszczono banderę", "flagi")

    def visitRaiseFalseFlag(self, ctx):
        self.state.flags["falszywa_flaga"] = True
        self.state.add_log("Podniesiono fałszywą flagę! 🎭", "flagi")

    def visitLowerFalseFlag(self, ctx):
        self.state.flags["falszywa_flaga"] = False
        self.state.add_log("Opuszczono fałszywą flagę", "flagi")

    def visitRaiseMerchantFlag(self, ctx):
        self.state.flags["handlowa"] = True
        self.state.add_log("Podniesiono flagę handlową (kamuflaż!)", "flagi")

    def visitRaiseWhiteFlag(self, ctx):
        self.state.flags["biala"] = True
        self.state.add_log("Podniesiono białą flagę 🏳️", "flagi")

    def visitRaiseFlag(self, ctx):
        flag = self._get_string(ctx.flag)
        self.state.flags["custom"].append(flag)
        self.state.add_log(f"Podniesiono flagę: {flag}", "flagi")

    def visitLowerFlag(self, ctx):
        flag = self._get_string(ctx.flag)
        if flag in self.state.flags["custom"]:
            self.state.flags["custom"].remove(flag)
        self.state.add_log(f"Opuszczono flagę: {flag}", "flagi")

    def visitSignalFlags(self, ctx):
        self.state.add_log("Sygnalizacja flagowa", "flagi")

    # ─────────────────────────────────────────────────────────────────────
    # ŚWIATŁA
    # ─────────────────────────────────────────────────────────────────────

    def visitNavLights(self, ctx):
        self.state.lights["nawigacyjne"] = True
        self.state.add_log("Światła nawigacyjne ON", "światła")

    def visitAnchorLights(self, ctx):
        self.state.lights["kotwiczne"] = True
        self.state.add_log("Światła kotwiczne ON", "światła")

    def visitEmergencyLights(self, ctx):
        self.state.lights["awaryjne"] = True
        self.state.add_log("Światła awaryjne ON", "światła")

    def visitMastHeadLights(self, ctx):
        self.state.lights["topowe"] = True
        self.state.add_log("Światła topowe ON", "światła")

    def visitSternLights(self, ctx):
        self.state.lights["rufowe"] = True
        self.state.add_log("Światła rufowe ON", "światła")

    def visitLightLantern(self, ctx):
        self.state.lights["latarnia"] = True
        self.state.add_log("Zapalono latarnię 🔥", "światła")

    def visitExtinguishLantern(self, ctx):
        self.state.lights["latarnia"] = False
        self.state.add_log("Zgaszono latarnię", "światła")

    def visitLightTorches(self, ctx):
        self.state.lights["pochodnie"] = True
        self.state.add_log("Zapalono pochodnie 🔥", "światła")

    def visitExtinguishTorches(self, ctx):
        self.state.lights["pochodnie"] = False
        self.state.add_log("Zgaszono pochodnie", "światła")

    def visitLightLamps(self, ctx):
        self.state.lights["lampy"] = True
        self.state.add_log("Zapalono lampy", "światła")

    def visitExtinguishLamps(self, ctx):
        self.state.lights["lampy"] = False
        self.state.add_log("Zgaszono lampy", "światła")

    def visitDarkenShip(self, ctx):
        for key in self.state.lights:
            self.state.lights[key] = False
        self.state.add_log("Zgaszono wszystkie światła! 🌑", "światła")

    # ─────────────────────────────────────────────────────────────────────
    # NAPRAWY
    # ─────────────────────────────────────────────────────────────────────

    def _repair_key(self, ctx) -> str:
        text = self._get_text(ctx)
        mapping = {
            "kadłub": "hull", "kadlub": "hull",
            "maszt": "mast", "rej": "yards", "reje": "yards",
            "takielunek": "rigging",
        }
        return mapping.get(text, text)

    def visitRepair(self, ctx):
        key = self._repair_key(ctx.repairTarget())
        current = getattr(self.state.damage, key, 0)
        setattr(self.state.damage, key, min(100, current + 25))
        self.state.add_log(f"Naprawiono {self._get_text(ctx.repairTarget())}", "naprawy")

    def visitPatch(self, ctx):
        key = self._repair_key(ctx.repairTarget())
        current = getattr(self.state.damage, key, 0)
        setattr(self.state.damage, key, min(100, current + 15))
        self.state.add_log(f"Załatano {self._get_text(ctx.repairTarget())}", "naprawy")

    def visitSealHull(self, ctx):
        self.state.damage.hull = min(100, self.state.damage.hull + 20)
        self.state.add_log("Uszczelniono kadłub", "naprawy")

    def visitRepairMast(self, ctx):
        self.state.damage.mast = min(100, self.state.damage.mast + 25)
        self.state.add_log("Naprawiono maszt", "naprawy")

    def visitRepairRigging(self, ctx):
        self.state.damage.rigging = min(100, self.state.damage.rigging + 25)
        self.state.add_log("Naprawiono takielunek", "naprawy")

    def visitCarpenterReport(self, ctx):
        self.state.add_log(f"Raport cieśli: {self.state.damage}", "naprawy")

    # ─────────────────────────────────────────────────────────────────────
    # DZIENNIK POKŁADOWY
    # ─────────────────────────────────────────────────────────────────────

    def visitLogMessage(self, ctx):
        msg = self._get_string(ctx.message)
        self.state.add_log(msg, "dziennik")

    def visitLogPosition(self, ctx):
        self.state.add_log(f"Pozycja: {self.state.latitude}, {self.state.longitude}", "dziennik")

    def visitLogWeather(self, ctx):
        self.state.add_log("Zalogowano warunki pogodowe", "dziennik")

    def visitLogEvent(self, ctx):
        msg = self._get_string(ctx.message)
        self.state.add_log(f"Zdarzenie: {msg}", "dziennik")

    def visitLogSailState(self, ctx):
        self.state.add_log("Zalogowano stan żagli", "dziennik")

    def visitLogWeaponsState(self, ctx):
        self.state.add_log("Zalogowano stan uzbrojenia", "dziennik")

    def visitLogCargoState(self, ctx):
        self.state.add_log("Zalogowano stan ładowni", "dziennik")

    def visitLogCrewState(self, ctx):
        self.state.add_log("Zalogowano stan załogi", "dziennik")

    def visitLogShipState(self, ctx):
        self.state.add_log("Zalogowano stan jednostki", "dziennik")

    # ─────────────────────────────────────────────────────────────────────
    # AWARYJNE
    # ─────────────────────────────────────────────────────────────────────

    def visitFireAlarm(self, ctx):
        self.state.alert = AlertLevel.FIRE
        self.state.active_emergencies.append("pożar")
        self.state.add_log("🔥 ALARM POŻAROWY!", "awaria")

    def visitWaterAlarm(self, ctx):
        self.state.alert = AlertLevel.FLOODING
        self.state.active_emergencies.append("przeciek")
        self.state.add_log("💧 ALARM WODNY!", "awaria")

    def visitBattleAlarm(self, ctx):
        self.state.alert = AlertLevel.BATTLE_STATIONS
        self.state.add_log("⚔️ ALARM BOJOWY!", "awaria")

    def visitPumpBilge(self, ctx):
        self.state.add_log("Odpompowywanie wody z zęzy", "awaria")

    def visitLifeJackets(self, ctx):
        self.state.add_log("Kamizelki ratunkowe!", "awaria")

    def visitEvacuate(self, ctx):
        self.state.alert = AlertLevel.EVACUATE
        self.state.add_log("🚨 EWAKUACJA!", "awaria")

    def visitAbandonShip(self, ctx):
        self.state.alert = AlertLevel.ABANDON_SHIP
        self.state.add_log("🚨 OPUŚCIĆ JEDNOSTKĘ!", "awaria")

    def visitFireOnBoard(self, ctx):
        side = self._get_text(ctx.boardSide()) if ctx.boardSide() else ""
        self.state.active_emergencies.append(f"pożar {side}".strip())
        self.state.add_log(f"🔥 POŻAR na pokładzie! {side}", "awaria")

    def visitLeakDetected(self, ctx):
        side = self._get_text(ctx.boardSide()) if ctx.boardSide() else ""
        self.state.active_emergencies.append(f"przeciek {side}".strip())
        self.state.add_log(f"💧 PRZECIEK! {side}", "awaria")

    def visitMastBroken(self, ctx):
        self.state.damage.mast = 0.0
        self.state.active_emergencies.append("maszt złamany")
        self.state.add_log("💀 MASZT ZŁAMANY!", "awaria")

    # ─────────────────────────────────────────────────────────────────────
    # POGODA
    # ─────────────────────────────────────────────────────────────────────

    def visitReportWind(self, ctx):
        self.state.add_log("Raport: wiatr", "pogoda")

    def visitReportWave(self, ctx):
        self.state.add_log("Raport: fala", "pogoda")

    def visitReportVisibility(self, ctx):
        self.state.add_log("Raport: widoczność", "pogoda")

    def visitReportWeather(self, ctx):
        self.state.add_log("Raport: pogoda", "pogoda")

    def visitReportDepth(self, ctx):
        self.state.add_log("Raport: głębokość", "pogoda")

    def visitReportCurrent(self, ctx):
        self.state.add_log("Raport: prąd", "pogoda")

    # ─────────────────────────────────────────────────────────────────────
    # KONTROLA PRZEPŁYWU
    # ─────────────────────────────────────────────────────────────────────

    def visitRepeat(self, ctx):
        times = int(self._get_number(ctx.times))
        self.state.add_log(f"Powtarzanie {times} razy...", "kontrola")
        for i in range(times):
            for cmd in ctx.command():
                self.visit(cmd)

    def visitWhileLoop(self, ctx):
        self.state.add_log("Pętla while (max 100 iteracji)", "kontrola")
        max_iter = 100
        i = 0
        while i < max_iter and self._evaluate_condition(ctx.condition()):
            for cmd in ctx.command():
                self.visit(cmd)
            i += 1

    def visitWaitDuration(self, ctx):
        val = self._get_number(ctx.duration().value)
        unit = self._get_text(ctx.duration().timeUnit())
        self.state.add_log(f"Czekanie {val} {unit}...", "kontrola")

    def visitWaitUntil(self, ctx):
        self.state.add_log("Czekanie na warunek...", "kontrola")

    def visitDefineManeuver(self, ctx):
        name = self._get_string(ctx.name)
        self.state.maneuvers[name] = ctx.command()
        self.state.add_log(f"Zdefiniowano manewr: {name}", "kontrola")

    def visitExecuteManeuver(self, ctx):
        name = self._get_string(ctx.name)
        if name in self.state.maneuvers:
            self.state.add_log(f"Wykonanie manewru: {name}", "kontrola")
            for cmd in self.state.maneuvers[name]:
                self.visit(cmd)
        else:
            self.state.add_log(f"Nieznany manewr: {name}!", "błąd")

    def visitDefineProcedure(self, ctx):
        name = self._get_string(ctx.name)
        self.state.procedures[name] = ctx.command()
        self.state.add_log(f"Zdefiniowano procedurę: {name}", "kontrola")

    def visitExecuteProcedure(self, ctx):
        name = self._get_string(ctx.name)
        if name in self.state.procedures:
            self.state.add_log(f"Wykonanie procedury: {name}", "kontrola")
            for cmd in self.state.procedures[name]:
                self.visit(cmd)
        else:
            self.state.add_log(f"Nieznana procedura: {name}!", "błąd")

    # ─────────────────────────────────────────────────────────────────────
    # WARUNKI
    # ─────────────────────────────────────────────────────────────────────

    def _evaluate_condition(self, ctx) -> bool:
        """Ewaluuje warunek — uproszczona symulacja."""
        return True

    def visitIfCondition(self, ctx):
        if self._evaluate_condition(ctx.condition()):
            self.state.add_log("Warunek spełniony — wykonuję", "kontrola")
            self.visit(ctx.command(0))
        elif len(ctx.command()) > 1:
            self.state.add_log("Warunek niespełniony — alternatywa", "kontrola")
            self.visit(ctx.command(1))

    def visitIfConditionBlock(self, ctx):
        if self._evaluate_condition(ctx.condition()):
            self.state.add_log("Warunek blokowy spełniony", "kontrola")
            for cmd in ctx.command():
                self.visit(cmd)