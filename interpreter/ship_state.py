from dataclasses import dataclass, field
from enum import Enum
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
    """Tryb wiosłowania."""
    OFF = "wyłączone"
    FORWARD_FULL = "cała naprzód"
    FORWARD_SLOW = "wolny naprzód"
    FORWARD_MEDIUM = "średni naprzód"
    REVERSE = "wsteczny"


class PointOfSail(Enum):
    """Kurs względem wiatru (TWA - True Wind Angle)."""
    IN_IRONS = "martwy kąt"      # 0–30°
    CLOSE_HAULED = "bejdewind"    # 30–60°
    BEAM_REACH = "półwiatr"       # 60–100°
    BROAD_REACH = "baksztag"      # 100–150°
    RUNNING = "fordewind"         # 150–180°


@dataclass
class SailInfo:
    state: SailState = SailState.FURLED
    angle: float = 0.0
    reef_percent: float = 0.0
    sheet_tension: float = 50.0

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
class WindState:
    """Stan wiatru - kierunek Z którego wieje (0–360°) i prędkość."""
    direction: float = 270.0   # kierunek Z którego wieje, 0=N, 90=E, 180=S, 270=W
    speed: float = 12.0        # węzły
    beaufort: int = 4

    def __str__(self):
        return f"{self.direction:.0f}°, {self.speed:.0f} kn (B{self.beaufort})"

    def to_dict(self):
        return {
            "direction": self.direction,
            "speed": self.speed,
            "beaufort": self.beaufort,
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
    """Pełny stan żaglowca."""

    # -- Żagle --
    sails: dict = field(default_factory=lambda: {
        "grot": SailInfo(),
        "fok": SailInfo(),
        "bezan": SailInfo(),
        "sztaksel": SailInfo(),
    })

    # -- Olinowanie --
    rigging_tension: dict = field(default_factory=lambda: {
        "faly": 50.0,
        "brasy": 50.0,
        "talrepy": 50.0,
        "szoty": 50.0,
    })

    # -- Ster i kurs --
    heading: float = 0.0
    target_heading: float = 0.0
    wind_course: str = ""        # nazwa point of sail (bejdewind, etc.)
    point_of_sail: str = ""      # aktualny point of sail obliczony z heading vs wiatru
    rudder_angle: float = 0.0

    # -- Kotwica i cumowanie --
    anchor: AnchorState = AnchorState.RAISED
    mooring: MooringState = MooringState.FREE

    # -- Prędkość / Wiosła --
    speed: float = 0.0
    rowing: EngineMode = EngineMode.OFF

    # -- Wiatr --
    wind: WindState = field(default_factory=WindState)

    # -- Flagi żeglarskie (nie pirackie) --
    flags: dict = field(default_factory=lambda: {
        "bandera": True,        # bandera narodowa - zwykle zawsze podniesiona
        "klubowa": False,       # flaga klubu żeglarskiego
        "goscia": False,        # flaga gościa - kraju na którego wodach pływamy
        "q": False,             # flaga Q - żółta, prośba o odprawę / kwarantanna
        "protestowa": False,    # flaga protestowa (regaty)
        "proporczyk": False,    # proporczyk
        "custom": [],           # flagi sygnalizacyjne / inne
    })

    # -- Dziennik pokładowy --
    log: list = field(default_factory=list)

    # -- Pozycja --
    latitude: float = 0.0
    longitude: float = 0.0

    # -------------------------------------------------------------
    # LOG
    # -------------------------------------------------------------
    def add_log(self, message: str, category: str = "ogólny"):
        ts = time.strftime("%H:%M:%S")
        entry = LogEntry(timestamp=ts, message=message, category=category)
        self.log.append(entry)
        print(f"  📜 {entry}")

    # -------------------------------------------------------------
    # NORMALIZACJA NAZW
    # -------------------------------------------------------------
    def normalize_sail_key(self, name: str) -> str:
        mapping = {
            "grot": "grot", "fok": "fok", "bezan": "bezan",
            "mezana": "bezan", "sztaksel": "sztaksel",
        }
        return mapping.get(name, name)

    # -------------------------------------------------------------
    # LOGIKA WIATRU
    # -------------------------------------------------------------
    def true_wind_angle(self) -> float:
        """Kąt między dziobem a kierunkiem Z którego wieje wiatr (0–180°)."""
        delta = (self.heading - self.wind.direction) % 360
        if delta > 180:
            delta = 360 - delta
        return delta

    def compute_point_of_sail(self) -> PointOfSail:
        twa = self.true_wind_angle()
        if twa < 30:
            return PointOfSail.IN_IRONS
        if twa < 60:
            return PointOfSail.CLOSE_HAULED
        if twa < 100:
            return PointOfSail.BEAM_REACH
        if twa < 150:
            return PointOfSail.BROAD_REACH
        return PointOfSail.RUNNING

    def sail_efficiency(self) -> float:
        """Wydajność żagli 0..1 zależna od kursu względem wiatru."""
        twa = self.true_wind_angle()
        if twa < 30:
            return 0.0                      # martwy kąt
        if twa < 60:
            return (twa - 30) / 30 * 0.7    # ostry, rośnie do 0.7
        if twa < 100:
            return 1.0                      # półwiatr - max
        if twa < 150:
            return 0.9                      # baksztag
        return 0.75                         # fordewind

    def active_sail_area(self) -> float:
        """Suma „aktywnej" powierzchni żagli - 0..1 (średnia z wszystkich)."""
        total = 0.0
        for info in self.sails.values():
            if info.state == SailState.SET:
                total += 1.0
            elif info.state == SailState.REEFED:
                total += max(0.0, 1.0 - info.reef_percent / 100.0)
        return total / max(1, len(self.sails))

    def recompute_sailing_speed(self):
        """Przelicza prędkość statku na podstawie wiatru, żagli i stanu."""
        # Zacumowany / zakotwiczony - stop
        if self.anchor == AnchorState.DROPPED or self.mooring == MooringState.MOORED:
            self.speed = 0.0
            self.point_of_sail = ""
            return

        # Wiosła dominują - nie ruszamy prędkości wyliczonej przez komendy wiosłowe
        if self.rowing != EngineMode.OFF:
            self.point_of_sail = ""
            return

        area = self.active_sail_area()
        if area <= 0:
            self.speed = 0.0
            self.point_of_sail = ""
            return

        pos = self.compute_point_of_sail()
        self.point_of_sail = pos.value
        eff = self.sail_efficiency()
        # Teoretyczna prędkość max ~ 80% prędkości wiatru
        max_speed = self.wind.speed * 0.8
        self.speed = round(max_speed * eff * area, 1)

    # -------------------------------------------------------------
    # SERIALIZACJA
    # -------------------------------------------------------------
    def to_dict(self) -> dict:
        return {
            "sails": {k: v.to_dict() for k, v in self.sails.items()},
            "rigging_tension": dict(self.rigging_tension),
            "heading": self.heading,
            "target_heading": self.target_heading,
            "wind_course": self.wind_course,
            "point_of_sail": self.point_of_sail,
            "rudder_angle": self.rudder_angle,
            "anchor": self.anchor.value,
            "mooring": self.mooring.value,
            "speed": self.speed,
            "rowing": self.rowing.value,
            "wind": self.wind.to_dict(),
            "flags": {
                k: (list(v) if isinstance(v, list) else v)
                for k, v in self.flags.items()
            },
            "log": [e.to_dict() for e in self.log],
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    def summary(self) -> str:
        lines = []
        lines.append("=" * 60)
        lines.append("⛵ STAN ŻAGLOWCA")
        lines.append("=" * 60)

        lines.append("\n⛵ ŻAGLE:")
        active = [(n, s) for n, s in self.sails.items() if s.state != SailState.FURLED]
        if not active:
            lines.append("  (wszystkie zwinięte)")
        for name, info in active:
            lines.append(f"  {name:12s} → {info}")

        lines.append(f"\n🧭 KURS: {self.heading:.0f}°")
        if self.point_of_sail:
            lines.append(f"   Point of sail: {self.point_of_sail}")
        lines.append(f"   Ster: {self.rudder_angle}°")

        lines.append(f"\n💨 PRĘDKOŚĆ: {self.speed} kn")
        if self.rowing != EngineMode.OFF:
            lines.append(f"   Wiosła: {self.rowing.value}")

        lines.append(f"\n🌬️  WIATR: {self.wind}")

        lines.append(f"\n⚓ KOTWICA: {self.anchor.value}")
        lines.append(f"   Cumowanie: {self.mooring.value}")

        active_flags = [k for k, v in self.flags.items()
                        if v is True or (isinstance(v, list) and v)]
        if active_flags:
            lines.append(f"\n🏳️  FLAGI: {', '.join(active_flags)}")

        lines.append("\n" + "=" * 60)
        return "\n".join(lines)