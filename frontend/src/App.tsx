import { useState, useCallback, useEffect } from "react";
import type { ShipState, LogEntry, ExampleCommand } from "./types/ship";
import {
  healthCheck,
  executeCommands as apiExecute,
  resetState as apiReset,
  getExamples,
} from "./api/client";
import ShipScene from "./components/ShipScene";
import CommandTerminal from "./components/CommandTerminal";
import StatePanel from "./components/StatePanel";
import LogPanel from "./components/LogPanel";

export default function App() {
  const [shipState, setShipState] = useState<ShipState | null>(null);
  const [log, setLog] = useState<LogEntry[]>([]);
  const [errors, setErrors] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [examples, setExamples] = useState<ExampleCommand[]>([]);
  const [connected, setConnected] = useState(false);

  // ── Sprawdź połączenie z backendem ──
  useEffect(() => {
    healthCheck()
      .then(() => setConnected(true))
      .catch(() => setConnected(false));
  }, []);

  // ── Pobierz przykłady ──
  useEffect(() => {
    getExamples()
      .then((data) => setExamples(data.examples))
      .catch(() => {});
  }, []);

  // ── Wykonaj polecenia ──
  const executeCommands = useCallback(
    async (commands: string, reset: boolean = true) => {
      setLoading(true);
      setErrors([]);
      try {
        const data = await apiExecute(commands, reset);
        setShipState(data.state);
        setLog(data.log);
        if (data.errors.length > 0) {
          setErrors(data.errors);
        }
      } catch (err) {
        setErrors([(err as Error).message]);
      } finally {
        setLoading(false);
      }
    },
    []
  );

  // ── Reset stanu ──
  const resetState = useCallback(async () => {
    try {
      await apiReset();
      setShipState(null);
      setLog([]);
      setErrors([]);
    } catch (err) {
      setErrors([(err as Error).message]);
    }
  }, []);

  return (
    <div className="app">
      {/* ── HEADER ── */}
      <header className="app-header">
        <div className="header-left">
          <h1>🏴‍☠️ Pirate Ship Commander</h1>
          <span className="subtitle">Interpreter poleceń żeglarskich</span>
        </div>
        <div className="header-right">
          <span
            className={`status-dot ${connected ? "connected" : "disconnected"}`}
          />
          <span className="status-text">
            {connected
              ? "Backend połączony"
              : "Brak połączenia z backendem"}
          </span>
        </div>
      </header>

      {/* ── MAIN LAYOUT ── */}
      <div className="app-body">
        {/* LEWA KOLUMNA: 3D + State */}
        <div className="left-column">
          <div className="scene-container">
            <ShipScene shipState={shipState} />
          </div>
          <StatePanel shipState={shipState} />
        </div>

        {/* PRAWA KOLUMNA: Terminal + Log */}
        <div className="right-column">
          <CommandTerminal
            onExecute={executeCommands}
            onReset={resetState}
            loading={loading}
            errors={errors}
            examples={examples}
            connected={connected}
          />
          <LogPanel log={log} />
        </div>
      </div>
    </div>
  );
}
