import sys
import copy
sys.path.insert(0, "gen")

from gen.SailingParser import SailingParser
from gen.SailingParserVisitor import SailingParserVisitor
from .ship_state import (
    ShipState, SailState, SailInfo, AnchorState, MooringState,
    EngineMode, CannonState, AlertLevel, CrewStation
)

class SailingCommandVisitor(SailingParserVisitor):

    def __init__(self, state: ShipState = None):
        self.state = state or ShipState()
        self.snapshots: list[dict] = []

    def _get_sail_name(self, ctx) -> str:
        return ctx.getText()

    def _get_text(self, ctx) -> str:
        if ctx is None:
            return ""
        return ctx.getText()

    def _get_number(self, token) -> float:
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
        self.state.sails["fok"].state = SailState.SET
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

    def visitTurnThroughSide(self, ctx):
        side = self._get_text(ctx.boardSide())
        if "lewa" in side or "bak" in side:
            self.state.heading = (self.state.heading - 90) % 360
            self.state.rudder_angle = -30
        else:
            self.state.heading = (self.state.heading + 90) % 360
            self.state.rudder_angle = 30
        self.state.add_log(f"Zwrot przez {side}! Nowy kurs: {self.state.heading}°", "ster")

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
        self.state.add_log("Podniesiono kotwicę", "kotwica")

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

    # ─────────────────────────────────────────────────────────────────────
    # KURS KOMPASOWY
    # ─────────────────────────────────────────────────────────────────────

    def _compass_to_degrees(self, text: str) -> float:
        mapping = {
            "polnoc": 0, "północ": 0,
            "poludnie": 180, "południe": 180,
            "wschod": 90, "wschód": 90,
            "zachod": 270, "zachód": 270,
            "NE": 45, "polnocnywschod": 45,
            "NW": 315, "polnocnyzachod": 315,
            "SE": 135, "poludniowywschod": 135,
            "SW": 225, "poludniowyzachod": 225,
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

    # ─────────────────────────────────────────────────────────────────────
    # UZBROJENIE (ładowanie + salwa)
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

    def visitFireCannons(self, ctx):
        name = self._get_text(ctx.cannonGroup())
        key = self.state.normalize_cannon_key(name)
        self.state.cannons[key].state = CannonState.EMPTY
        self.state.cannons[key].ammo = ""
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
    # ZAŁOGA (uproszczona)
    # ─────────────────────────────────────────────────────────────────────

    def visitCrewToStations(self, ctx):
        self.state.crew_station = CrewStation.STATIONS
        self.state.add_log("Załoga na stanowiska!", "załoga")

    def visitManOverboard(self, ctx):
        self.state.man_overboard = True
        if ctx.boardSide():
            self.state.man_overboard_side = self._get_text(ctx.boardSide())
        self.state.add_log(f"🆘 CZŁOWIEK ZA BURTĄ! {self.state.man_overboard_side}", "załoga")

    def visitAllOnDeck(self, ctx):
        self.state.crew_station = CrewStation.ON_DECK
        self.state.add_log("Wszyscy na pokład!", "załoga")

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
    # NAPRAWY (uproszczone)
    # ─────────────────────────────────────────────────────────────────────

    def _repair_key(self, ctx) -> str:
        text = self._get_text(ctx)
        mapping = {
            "kadłub": "hull", "kadlub": "hull",
            "maszt": "mast",
            "takielunek": "rigging",
        }
        return mapping.get(text, text)

    def visitRepair(self, ctx):
        key = self._repair_key(ctx.repairTarget())
        current = getattr(self.state.damage, key, 0)
        setattr(self.state.damage, key, min(100, current + 25))
        self.state.add_log(f"Naprawiono {self._get_text(ctx.repairTarget())}", "naprawy")

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

    def visitLogCargoState(self, ctx):
        self.state.add_log("Zalogowano stan ładowni", "dziennik")

    def visitLogShipState(self, ctx):
        self.state.add_log("Zalogowano stan jednostki", "dziennik")

    # ─────────────────────────────────────────────────────────────────────
    # ALARMY (uproszczone)
    # ─────────────────────────────────────────────────────────────────────

    def visitBattleAlarm(self, ctx):
        self.state.alert = AlertLevel.BATTLE_STATIONS
        self.state.crew_station = CrewStation.STATIONS
        self.state.add_log("⚔️ ALARM BOJOWY!", "awaria")

    # ─────────────────────────────────────────────────────────────────────
    # POGODA
    # ─────────────────────────────────────────────────────────────────────

    def visitReportWind(self, ctx):
        self.state.add_log("Raport: wiatr", "pogoda")

    def visitReportWeather(self, ctx):
        self.state.add_log("Raport: pogoda", "pogoda")

    def visitReportDepth(self, ctx):
        self.state.add_log("Raport: głębokość", "pogoda")

    # ─────────────────────────────────────────────────────────────────────
    # KONTROLA PRZEPŁYWU
    # ─────────────────────────────────────────────────────────────────────

    def visitRepeat(self, ctx):
        times = min(int(self._get_number(ctx.times)), 1000)
        if times > 1000:
            self.state.add_log("Ograniczono powtórzenia do 1000!", "kontrola")
        self.state.add_log(f"Powtarzanie {times} razy...", "kontrola")
        for i in range(times):
            for cmd in ctx.command():
                self.visit(cmd)
            # Snapshot after each iteration for animated playback
            self.snapshots.append({
                "state": self.state.to_dict(),
                "log": [entry.to_dict() for entry in self.state.log],
            })

    def visitWaitDuration(self, ctx):
        val = self._get_number(ctx.duration().value)
        unit = self._get_text(ctx.duration().timeUnit())
        self.state.add_log(f"Czekanie {val} {unit}...", "kontrola")

    def visitWaitUntil(self, ctx):
        self.state.add_log("Czekanie na warunek...", "kontrola")

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

