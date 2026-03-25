import type {
  ExecuteRequest,
  ExecuteResponse,
  ExampleCommand,
  HealthResponse,
  ShipState,
  LogEntry,
} from "../types/ship";

const API_BASE = "/api";

class ApiError extends Error {
  status: number;
  constructor(message: string, status: number) {
    super(message);
    this.name = "ApiError";
    this.status = status;
  }
}

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });

  if (!response.ok) {
    const body = await response.json().catch(() => ({}));
    throw new ApiError(
      body.detail || `Błąd serwera (${response.status})`,
      response.status
    );
  }

  return response.json() as Promise<T>;
}

// ── Endpointy ──

export async function healthCheck(): Promise<HealthResponse> {
  return request<HealthResponse>("/health");
}

export async function executeCommands(
  commands: string,
  reset: boolean = true
): Promise<ExecuteResponse> {
  return request<ExecuteResponse>("/execute", {
    method: "POST",
    body: JSON.stringify({ commands, reset } satisfies ExecuteRequest),
  });
}

export async function getState(): Promise<{
  state: ShipState;
  log: LogEntry[];
}> {
  return request("/state");
}

export async function resetState(): Promise<{
  success: boolean;
  message: string;
}> {
  return request("/reset", { method: "POST" });
}

export async function getExamples(): Promise<{ examples: ExampleCommand[] }> {
  return request("/examples");
}
