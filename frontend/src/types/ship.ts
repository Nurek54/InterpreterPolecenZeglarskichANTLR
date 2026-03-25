// ─────────────────────────────────────────────────────────────────
// types/ship.ts — Typy stanu statku (mapowanie 1:1 z Python backend)
// ─────────────────────────────────────────────────────────────────

export interface SailInfo {
  state: "zwinięty" | "postawiony" | "zrefowany";
  angle: number;
  reef_percent: number;
  sheet_tension: number;
}

export interface CannonGroupInfo {
  state: "pusty" | "załadowany" | "wycelowany";
  ammo: string;
  target: string;
  aim_angle: number;
}

export interface CrewMember {
  role: string;
  station: "wolny" | "na stanowisku" | "na pokładzie";
}

export interface DamageReport {
  hull: number;
  mast: number;
  rigging: number;
  yards: number;
}

export interface LogEntry {
  timestamp: string;
  message: string;
  category: string;
}

export interface ShipFlags {
  jolly_roger: boolean;
  bandera: boolean;
  falszywa_flaga: boolean;
  handlowa: boolean;
  biala: boolean;
  custom: string[];
}

export interface ShipLights {
  nawigacyjne: boolean;
  kotwiczne: boolean;
  awaryjne: boolean;
  topowe: boolean;
  rufowe: boolean;
  latarnia: boolean;
  pochodnie: boolean;
  lampy: boolean;
}

export interface ShipState {
  // Żagle
  sails: Record<string, SailInfo>;
  rigging_tension: Record<string, number>;

  // Nawigacja
  heading: number;
  target_heading: number;
  wind_course: string;
  rudder_angle: number;

  // Kotwica / Cumowanie
  anchor: "podniesiona" | "rzucona";
  chain_length: number;
  mooring: "wolny" | "zacumowany";
  grappling_hooks: boolean;

  // Prędkość
  speed: number;
  rowing: string;

  // Uzbrojenie
  cannons: Record<string, CannonGroupInfo>;

  // Abordaż
  boarding: string;

  // Ładunek
  cargo: Record<string, number>;
  buried_treasures: string[];

  // Załoga
  crew: Record<string, CrewMember>;
  watch: string;
  man_overboard: boolean;
  man_overboard_side: string;

  // Taktyka
  tactic: string;
  chase_target: string;

  // Flagi
  flags: ShipFlags;

  // Światła
  lights: ShipLights;

  // Uszkodzenia
  damage: DamageReport;

  // Alarmy
  alert: string;
  active_emergencies: string[];

  // Log
  log: LogEntry[];

  // Pozycja
  latitude: number;
  longitude: number;

  // Obserwacja
  scouting_active: boolean;
  lookout_position: string;
  identified_targets: string[];
}

// ─────────────────────────────────────────────────────────────────
// Typy API
// ─────────────────────────────────────────────────────────────────

export interface ExecuteRequest {
  commands: string;
  reset: boolean;
}

export interface ExecuteResponse {
  success: boolean;
  state: ShipState;
  log: LogEntry[];
  errors: string[];
}

export interface ExampleCommand {
  name: string;
  commands: string;
}

export interface HealthResponse {
  status: string;
  message: string;
}
