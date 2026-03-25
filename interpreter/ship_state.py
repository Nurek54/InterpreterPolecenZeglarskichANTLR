from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional
import time

class SailState(Enum):
    FURLED = "zwinięty"
    SET = "postawiony"
    REEFED = "zrefowany"


class AnchorState(Enum):
    RAISED = "podniesiona"
    DROPPED = "rzucona"


class MooringState(Enum):
    FREE = "wolny"
    MOORED = "zacumowany"


class EngineMode(Enum):
    """Piracki statek — tryb wiosłowania"""
    OFF = "wyłączone"
    FORWARD_FULL = "cała naprzód"
    FORWARD_SLOW = "wolny naprzód"
    FORWARD_MEDIUM = "średni naprzód"
    REVERSE = "wsteczny"


class CannonState(Enum):
    EMPTY = "pusty"
    LOADED = "załadowany"
    AIMED = "wycelowany"


class BoardingPhase(Enum):
    NONE = "brak"
    PREPARING = "przygotowanie"
    HOOKS_THROWN = "haki rzucone"
    BOARDING = "abordaż"
    STORMING = "szturm"
    RETREATING = "wycofanie"


class TacticMode(Enum):
    NONE = "brak"
    CHASING = "pościg"
    FLEEING = "ucieczka"
    INTERCEPTING = "przechwyt"
    BLOCKING = "blokada"
    AMBUSH = "zasadzka"
    EVADING = "unikanie"
    RAMMING = "taranowanie"
    EXCHANGING_FIRE = "wymiana ognia"
    SURRENDERING = "poddanie"
    DEMANDING_SURRENDER = "żądanie kapitulacji"


class AlertLevel(Enum):
    NONE = "brak"
    BATTLE_STATIONS = "alarm bojowy"
    FIRE = "pożar"
    FLOODING = "wodny"
    EVACUATE = "ewakuacja"
    ABANDON_SHIP = "opuść jednostkę"


class CrewStation(Enum):
    IDLE = "wolny"
    STATIONS = "na stanowisku"
    ON_DECK = "na pokładzie"

@dataclass
class SailInfo:
    state: SailState = SailState.FURLED
    angle: float = 0.0
    reef_percent: float = 0.0      # 0 = brak refu, 100 = pełny ref
    sheet_tension: float = 50.0    # 0–100, napięcie szotów

    def __str__(self):
        s = f"{self.state.value}"
        if self.state == SailState.REEFED:
            s += f" ({self.reef_percent}%)"
        if self.angle != 0:
            s += f", kąt: {self.angle}°"
        return s

    def to_dict(self):
        return {
            "state": self.state.value,
            "angle": self.angle,
            "reef_percent": self.reef_percent,
            "sheet_tension": self.sheet_tension,
        }


@dataclass
class CannonGroupInfo:
    state: CannonState = CannonState.EMPTY
    ammo: str = ""
    target: str = ""
    aim_angle: float = 0.0

    def __str__(self):
        s = f"{self.state.value}"
        if self.ammo:
            s += f", amunicja: {self.ammo}"
        if self.target:
            s += f", cel: {self.target}"
        return s

    def to_dict(self):
        return {
            "state": self.state.value,
            "ammo": self.ammo,
            "target": self.target,
            "aim_angle": self.aim_angle,
        }


@dataclass
class CrewMember:
    role: str = ""
    station: CrewStation = CrewStation.IDLE

    def __str__(self):
        return f"{self.role}: {self.station.value}"

    def to_dict(self):
        return {
            "role": self.role,
            "station": self.station.value,
        }


@dataclass
class DamageReport:
    hull: float = 100.0         # 0–100 (100 = brak uszkodzeń)
    mast: float = 100.0
    rigging: float = 100.0
    yards: float = 100.0

    def __str__(self):
        return (f"kadłub: {self.hull}%, maszt: {self.mast}%, "
                f"takielunek: {self.rigging}%, reje: {self.yards}%")

    def to_dict(self):
        return {
            "hull": self.hull,
            "mast": self.mast,
            "rigging": self.rigging,
            "yards": self.yards,
        }


@dataclass
class LogEntry:
    timestamp: str
    message: str
    category: str = "ogólny"

    def __str__(self):
        return f"[{self.timestamp}] [{self.category}] {self.message}"

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "message": self.message,
            "category": self.category,
        }

@dataclass
class ShipState:
    """Pełny stan pirackiego statku."""

    # ── Żagle ──
    sails: dict = field(default_factory=lambda: {
        "grot": SailInfo(),
        "fok": SailInfo(),
        "bezan": SailInfo(),
        "sztaksel": SailInfo(),
        "topsel": SailInfo(),
        "trysel": SailInfo(),
        "sztormfok": SailInfo(),
        "bramsel": SailInfo(),
        "royal": SailInfo(),
        "latacz": SailInfo(),
    })

    # ── Olinowanie ──
    rigging_tension: dict = field(default_factory=lambda: {
        "faly": 50.0,
        "brasy": 50.0,
        "talrepy": 50.0,
        "szoty": 50.0,
    })

    # ── Ster i kurs ──
    heading: float = 0.0
    target_heading: float = 0.0
    wind_course: str = ""
    rudder_angle: float = 0.0

    # ── Kotwica i cumowanie ──
    anchor: AnchorState = AnchorState.RAISED
    chain_length: float = 0.0
    mooring: MooringState = MooringState.FREE
    grappling_hooks: bool = False

    # ── Prędkość / Wiosła ──
    speed: float = 0.0
    rowing: EngineMode = EngineMode.OFF

    # ── Uzbrojenie ──
    cannons: dict = field(default_factory=lambda: {
        "armaty": CannonGroupInfo(),
        "dziala": CannonGroupInfo(),
        "kolubryny": CannonGroupInfo(),
        "karronady": CannonGroupInfo(),
        "muszkiety": CannonGroupInfo(),
    })

    # ── Abordaż ──
    boarding: BoardingPhase = BoardingPhase.NONE

    # ── Ładunek / Łupy ──
    cargo: dict = field(default_factory=lambda: {
        "zloto": 0,
        "srebro": 0,
        "lupy": 0,
        "amunicja": 0,
        "prowiant": 100,
        "rum": 50,
        "woda_pitna": 100,
        "proch": 100,
        "beczki": 0,
        "skrzynie": 0,
        "skarb": 0,
    })
    buried_treasures: list = field(default_factory=list)

    # ── Załoga ──
    crew: dict = field(default_factory=lambda: {
        "kapitan": CrewMember(role="kapitan"),
        "bosman": CrewMember(role="bosman"),
        "nawigator": CrewMember(role="nawigator"),
        "kanonier": CrewMember(role="kanonier"),
        "ciesla": CrewMember(role="cieśla"),
        "kucharz": CrewMember(role="kucharz"),
        "chirurg": CrewMember(role="chirurg"),
        "kwatermistrz": CrewMember(role="kwatermistrz"),
        "marynarz": CrewMember(role="marynarz"),
        "obserwator": CrewMember(role="obserwator"),
        "sternik": CrewMember(role="sternik"),
    })
    watch: str = "A"
    man_overboard: bool = False
    man_overboard_side: str = ""

    # ── Taktyka ──
    tactic: TacticMode = TacticMode.NONE
    chase_target: str = ""

    # ── Flagi ──
    flags: dict = field(default_factory=lambda: {
        "jolly_roger": False,
        "bandera": False,
        "falszywa_flaga": False,
        "handlowa": False,
        "biala": False,
        "custom": [],
    })

    # ── Światła ──
    lights: dict = field(default_factory=lambda: {
        "nawigacyjne": False,
        "kotwiczne": False,
        "awaryjne": False,
        "topowe": False,
        "rufowe": False,
        "latarnia": False,
        "pochodnie": False,
        "lampy": False,
    })

    # ── Uszkodzenia ──
    damage: DamageReport = field(default_factory=DamageReport)

    # ── Alarmy ──
    alert: AlertLevel = AlertLevel.NONE
    active_emergencies: list = field(default_factory=list)

    # ── Dziennik pokładowy ──
    log: list = field(default_factory=list)

    # ── Pozycja ──
    latitude: float = 0.0
    longitude: float = 0.0

    # ── Obserwacja ──
    scouting_active: bool = False
    lookout_position: str = ""
    identified_targets: list = field(default_factory=list)

    # ── Manewry / Procedury ──
    maneuvers: dict = field(default_factory=dict)
    procedures: dict = field(default_factory=dict)

    def add_log(self, message: str, category: str = "ogólny"):
        ts = time.strftime("%H:%M:%S")
        entry = LogEntry(timestamp=ts, message=message, category=category)
        self.log.append(entry)
        print(f"  📜 {entry}")

    def get_sail(self, name: str) -> SailInfo:
        mapping = {
            "grot": "grot", "fok": "fok", "bezan": "bezan",
            "mezana": "bezan", "sztaksel": "sztaksel",
            "topsel": "topsel", "topśel": "topsel",
            "trysel": "trysel", "sztormfok": "sztormfok",
            "bramsel": "bramsel", "royal": "royal",
            "łatacz": "latacz", "latacz": "latacz",
        }
        key = mapping.get(name, name)
        return self.sails.get(key, SailInfo())

    def get_cannon_group(self, name: str) -> CannonGroupInfo:
        mapping = {
            "armaty": "armaty", "działa": "dziala", "dziala": "dziala",
            "kolubryna": "kolubryny", "kolubryny": "kolubryny",
            "karronada": "karronady", "karronady": "karronady",
            "muszkiet": "muszkiety", "muszkiety": "muszkiety",
        }
        key = mapping.get(name, name)
        return self.cannons.get(key, CannonGroupInfo())

    def normalize_sail_key(self, name: str) -> str:
        mapping = {
            "grot": "grot", "fok": "fok", "bezan": "bezan",
            "mezana": "bezan", "sztaksel": "sztaksel",
            "topsel": "topsel", "topśel": "topsel",
            "trysel": "trysel", "sztormfok": "sztormfok",
            "bramsel": "bramsel", "royal": "royal",
            "łatacz": "latacz", "latacz": "latacz",
        }
        return mapping.get(name, name)

    def normalize_cannon_key(self, name: str) -> str:
        mapping = {
            "armaty": "armaty", "działa": "dziala", "dziala": "dziala",
            "kolubryna": "kolubryny", "kolubryny": "kolubryny",
            "karronada": "karronady", "karronady": "karronady",
            "muszkiet": "muszkiety", "muszkiety": "muszkiety",
        }
        return mapping.get(name, name)

    def to_dict(self) -> dict:
        """Serializuje pełny stan statku do słownika (gotowy na JSON)."""
        return {
            "sails": {k: v.to_dict() for k, v in self.sails.items()},
            "rigging_tension": dict(self.rigging_tension),
            "heading": self.heading,
            "target_heading": self.target_heading,
            "wind_course": self.wind_course,
            "rudder_angle": self.rudder_angle,
            "anchor": self.anchor.value,
            "chain_length": self.chain_length,
            "mooring": self.mooring.value,
            "grappling_hooks": self.grappling_hooks,
            "speed": self.speed,
            "rowing": self.rowing.value,
            "cannons": {k: v.to_dict() for k, v in self.cannons.items()},
            "boarding": self.boarding.value,
            "cargo": dict(self.cargo),
            "buried_treasures": list(self.buried_treasures),
            "crew": {k: v.to_dict() for k, v in self.crew.items()},
            "watch": self.watch,
            "man_overboard": self.man_overboard,
            "man_overboard_side": self.man_overboard_side,
            "tactic": self.tactic.value,
            "chase_target": self.chase_target,
            "flags": {
                k: (list(v) if isinstance(v, list) else v)
                for k, v in self.flags.items()
            },
            "lights": dict(self.lights),
            "damage": self.damage.to_dict(),
            "alert": self.alert.value,
            "active_emergencies": list(self.active_emergencies),
            "log": [entry.to_dict() for entry in self.log],
            "latitude": self.latitude,
            "longitude": self.longitude,
            "scouting_active": self.scouting_active,
            "lookout_position": self.lookout_position,
            "identified_targets": list(self.identified_targets),
        }

    def summary(self) -> str:
        lines = []
        lines.append("=" * 60)
        lines.append("⚓ STAN PIRACKIEGO STATKU")
        lines.append("=" * 60)

        lines.append("\n⛵ ŻAGLE:")
        for name, info in self.sails.items():
            if info.state != SailState.FURLED:
                lines.append(f"  {name:12s} → {info}")
        active_sails = [n for n, s in self.sails.items() if s.state != SailState.FURLED]
        if not active_sails:
            lines.append("  (wszystkie zwinięte)")

        lines.append(f"\n🧭 KURS: {self.heading}°")
        if self.wind_course:
            lines.append(f"   Kurs wiatrowy: {self.wind_course}")
        lines.append(f"   Ster: {self.rudder_angle}°")

        lines.append(f"\n💨 PRĘDKOŚĆ: {self.speed} kn")
        if self.rowing != EngineMode.OFF:
            lines.append(f"   Wiosła: {self.rowing.value}")

        lines.append(f"\n⚓ KOTWICA: {self.anchor.value}")
        if self.anchor == AnchorState.DROPPED:
            lines.append(f"   Łańcuch: {self.chain_length} m")
        lines.append(f"   Cumowanie: {self.mooring.value}")

        lines.append("\n💣 UZBROJENIE:")
        for name, info in self.cannons.items():
            if info.state != CannonState.EMPTY:
                lines.append(f"  {name:12s} → {info}")

        if self.boarding != BoardingPhase.NONE:
            lines.append(f"\n⚔️  ABORDAŻ: {self.boarding.value}")

        if self.tactic != TacticMode.NONE:
            lines.append(f"\n🏴‍☠️ TAKTYKA: {self.tactic.value}")
            if self.chase_target:
                lines.append(f"   Cel: {self.chase_target}")

        lines.append("\n📦 ŁADOWNIA:")
        for item, qty in self.cargo.items():
            if qty > 0:
                lines.append(f"  {item:15s} → {qty}")

        if self.buried_treasures:
            lines.append("\n🗺️  ZAKOPANE SKARBY:")
            for t in self.buried_treasures:
                lines.append(f"  {t}")

        active_flags = [k for k, v in self.flags.items()
                        if v is True or (isinstance(v, list) and v)]
        if active_flags:
            lines.append(f"\n🏴 FLAGI: {', '.join(active_flags)}")

        active_lights = [k for k, v in self.lights.items() if v]
        if active_lights:
            lines.append(f"\n🔦 ŚWIATŁA: {', '.join(active_lights)}")

        lines.append(f"\n🔧 USZKODZENIA: {self.damage}")

        if self.alert != AlertLevel.NONE:
            lines.append(f"\n🚨 ALARM: {self.alert.value}")
        if self.active_emergencies:
            lines.append(f"   Aktywne: {', '.join(self.active_emergencies)}")

        if self.man_overboard:
            side = f" ({self.man_overboard_side})" if self.man_overboard_side else ""
            lines.append(f"\n🆘 CZŁOWIEK ZA BURTĄ{side}!")

        lines.append(f"\n👥 WACHTA: {self.watch}")
        active_crew = [f"{r}: {c.station.value}"
                       for r, c in self.crew.items()
                       if c.station != CrewStation.IDLE]
        if active_crew:
            lines.append("   " + ", ".join(active_crew))

        if self.scouting_active:
            lines.append(f"\n🔭 OBSERWACJA: aktywna ({self.lookout_position})")
        if self.identified_targets:
            lines.append(f"   Zidentyfikowane: {', '.join(self.identified_targets)}")

        lines.append("\n" + "=" * 60)
        return "\n".join(lines)