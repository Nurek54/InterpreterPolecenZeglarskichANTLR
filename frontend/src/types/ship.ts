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
  state: "pusty" | "załadowany";
  ammo: string;
}

export interface DamageReport {
  hull: number;
  mast: number;
  rigging: number;
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

export interface ShipState {
  sails: Record<string, SailInfo>;
  rigging_tension: Record<string, number>;
  heading: number;
  target_heading: number;
  wind_course: string;
  rudder_angle: number;
  anchor: "podniesiona" | "rzucona";
  mooring: "wolny" | "zacumowany";
  speed: number;
  rowing: string;
  cannons: Record<string, CannonGroupInfo>;
  cargo: Record<string, number>;
  buried_treasures: string[];
  crew_station: string;
  man_overboard: boolean;
  man_overboard_side: string;
  flags: ShipFlags;
  damage: DamageReport;
  alert: string;
  log: LogEntry[];
  latitude: number;
  longitude: number;
}

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
