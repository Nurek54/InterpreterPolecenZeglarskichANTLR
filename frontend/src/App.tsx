import { useState, useCallback, useEffect, useRef } from "react";
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

const SNAPSHOT_DELAY_MS = 800;

export default function App() {
  const [shipState, setShipState] = useState<ShipState | null>(null);
  const [log, setLog] = useState<LogEntry[]>([]);
  const [errors, setErrors] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [examples, setExamples] = useState<ExampleCommand[]>([]);
  const [connected, setConnected] = useState(false);
  const snapshotTimers = useRef<number[]>([]);

  useEffect(() => {
    healthCheck()
      .then(() => setConnected(true))
      .catch(() => setConnected(false));
  }, []);

  useEffect(() => {
    getExamples()
      .then((data) => setExamples(data.examples))
      .catch(() => {});
  }, []);

  const executeCommands = useCallback(
    async (commands: string, reset: boolean = true) => {
      // Clear any pending snapshot animations
      snapshotTimers.current.forEach(clearTimeout);
      snapshotTimers.current = [];

      setLoading(true);
      setErrors([]);
      try {
        const data = await apiExecute(commands, reset);

        if (data.snapshots && data.snapshots.length > 1) {
          // Animate through snapshots with delay
          data.snapshots.forEach((snap, i) => {
            const timer = window.setTimeout(() => {
              setShipState(snap.state);
              setLog(snap.log);
              // After last snapshot, show final state and stop loading
              if (i === data.snapshots.length - 1) {
                setShipState(data.state);
                setLog(data.log);
                setLoading(false);
              }
            }, i * SNAPSHOT_DELAY_MS);
            snapshotTimers.current.push(timer);
          });
          if (data.errors.length > 0) {
            setErrors(data.errors);
          }
        } else {
          // No snapshots — apply final state immediately
          setShipState(data.state);
          setLog(data.log);
          if (data.errors.length > 0) {
            setErrors(data.errors);
          }
          setLoading(false);
        }
      } catch (err) {
        setErrors([(err as Error).message]);
        setLoading(false);
      }
    },
    []
  );

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
      <header className="app-header">
        <div className="header-left">
          <h1>🏴‍☠️ Interpreter poleceń żeglarskich</h1>
        </div>
        <div className="header-right">
          <span
            className={`status-dot ${connected ? "connected" : "disconnected"}`}
          />
          <span className="status-text">
            {connected ? "Połączono" : "Brak połączenia"}
          </span>
        </div>
      </header>

      <div className="app-body">
        <div className="left-column">
          <div className="scene-container">
            <ShipScene shipState={shipState} />
          </div>
          <StatePanel shipState={shipState} />
        </div>

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

