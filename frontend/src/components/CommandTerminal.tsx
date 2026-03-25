import { useState, useRef, useEffect, type KeyboardEvent, type ChangeEvent } from "react";
import type { ExampleCommand } from "../types/ship";

// ─────────────────────────────────────────────────────────────────
// PROPS
// ─────────────────────────────────────────────────────────────────

interface CommandTerminalProps {
  onExecute: (commands: string, reset: boolean) => Promise<void>;
  onReset: () => Promise<void>;
  loading: boolean;
  errors: string[];
  examples: ExampleCommand[];
  connected: boolean;
}

// ─────────────────────────────────────────────────────────────────
// COMPONENT
// ─────────────────────────────────────────────────────────────────

export default function CommandTerminal({
  onExecute,
  onReset,
  loading,
  errors,
  examples,
  connected,
}: CommandTerminalProps) {
  const [commands, setCommands] = useState(
    "// Wpisz polecenia pirackie poniżej\npostaw grot;\npostaw fok;\nkurs 185;\n"
  );
  const [resetOnExecute, setResetOnExecute] = useState(true);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    textareaRef.current?.focus();
  }, []);

  const handleExecute = (): void => {
    if (!commands.trim() || loading || !connected) return;
    onExecute(commands, resetOnExecute);
  };

  const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>): void => {
    // Ctrl+Enter = wykonaj
    if (e.ctrlKey && e.key === "Enter") {
      e.preventDefault();
      handleExecute();
    }
    // Tab = wstaw 4 spacje
    if (e.key === "Tab") {
      e.preventDefault();
      const target = e.currentTarget;
      const start = target.selectionStart;
      const end = target.selectionEnd;
      const newValue =
        commands.substring(0, start) + "    " + commands.substring(end);
      setCommands(newValue);
      setTimeout(() => {
        target.selectionStart = target.selectionEnd = start + 4;
      }, 0);
    }
  };

  const loadExample = (example: ExampleCommand): void => {
    setCommands(example.commands);
  };

  return (
    <div className="terminal-panel">
      <div className="panel-header">
        <h2>⌨️ Terminal poleceń</h2>
        <div className="header-actions">
          <label className="checkbox-label">
            <input
              type="checkbox"
              checked={resetOnExecute}
              onChange={(e: ChangeEvent<HTMLInputElement>) =>
                setResetOnExecute(e.target.checked)
              }
            />
            Reset przed wykonaniem
          </label>
        </div>
      </div>

      {/* Dropdown z przykładami */}
      {examples.length > 0 && (
        <div className="examples-bar">
          <span className="examples-label">Przykłady:</span>
          {examples.map((ex, i) => (
            <button
              key={i}
              className="example-btn"
              onClick={() => loadExample(ex)}
              title={ex.commands}
            >
              {ex.name}
            </button>
          ))}
        </div>
      )}

      {/* Textarea */}
      <div className="textarea-wrapper">
        <textarea
          ref={textareaRef}
          value={commands}
          onChange={(e: ChangeEvent<HTMLTextAreaElement>) =>
            setCommands(e.target.value)
          }
          onKeyDown={handleKeyDown}
          placeholder="Wpisz polecenia pirackie... np. postaw grot;"
          spellCheck={false}
          className="command-textarea"
        />
      </div>

      {/* Błędy */}
      {errors.length > 0 && (
        <div className="error-box">
          <strong>⚠️ Błędy:</strong>
          {errors.map((err, i) => (
            <div key={i} className="error-item">
              {err}
            </div>
          ))}
        </div>
      )}

      {/* Przyciski */}
      <div className="terminal-actions">
        <button
          className="btn btn-primary"
          onClick={handleExecute}
          disabled={loading || !connected}
        >
          {loading ? "⏳ Wykonywanie..." : "▶️ Wykonaj (Ctrl+Enter)"}
        </button>
        <button
          className="btn btn-secondary"
          onClick={onReset}
          disabled={loading}
        >
          🔄 Reset
        </button>
        <button className="btn btn-ghost" onClick={() => setCommands("")}>
          🗑️ Wyczyść
        </button>
      </div>
    </div>
  );
}
