// ─────────────────────────────────────────────────────────────────
// types/ship.ts — Typy stanu statku (mapowanie 1:1 z Python backend)
// ─────────────────────────────────────────────────────────────────

export interface SailInfo {
  state: "zwinięty" | "postawiony" | "zrefowany";
  angle: number;
  reef_percent: number;
  sheet_tension: number;
}

export interface WindState {
  direction: number;   // 0–360°, kierunek Z którego wieje
  speed: number;       // węzły
  beaufort: number;    // stopnie Beauforta
}

export interface LogEntry {
  timestamp: string;
  message: string;
  category: string;
}

export interface ShipFlags {
  bandera: boolean;
  klubowa: boolean;
  goscia: boolean;
  q: boolean;
  protestowa: boolean;
  proporczyk: boolean;
  custom: string[];
}

export interface ShipState {
  sails: Record<string, SailInfo>;
  rigging_tension: Record<string, number>;
  heading: number;
  target_heading: number;
  wind_course: string;
  point_of_sail: string;
  rudder_angle: number;
  anchor: "podniesiona" | "rzucona";
  mooring: "wolny" | "zacumowany";
  speed: number;
  rowing: string;
  wind: WindState;
  flags: ShipFlags;
  log: LogEntry[];
  latitude: number;
  longitude: number;
}

export interface ExecuteRequest {
  commands: string;
  reset: boolean;
}

export interface StateSnapshot {
  state: ShipState;
  log: LogEntry[];
}

export interface ExecuteResponse {
  success: boolean;
  state: ShipState;
  log: LogEntry[];
  errors: string[];
  snapshots: StateSnapshot[];
}

export interface ExampleCommand {
  name: string;
  commands: string;
}

export interface HealthResponse {
  status: string;
  message: string;
}