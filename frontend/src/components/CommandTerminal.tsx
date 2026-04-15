import {
  useState,
  useRef,
  useEffect,
  useCallback,
  type KeyboardEvent,
  type ChangeEvent,
  type ReactNode,
} from "react";
import type { ExampleCommand } from "../types/ship";

interface CommandTerminalProps {
  onExecute: (commands: string, reset: boolean) => Promise<void>;
  onReset: () => Promise<void>;
  loading: boolean;
  errors: string[];
  examples: ExampleCommand[];
  connected: boolean;
}

// -----------------------------------------------------------------
// SYNTAX HIGHLIGHTING
// -----------------------------------------------------------------

const COMMANDS = new Set([
  "postaw", "zwin", "zwiń", "refuj", "ustaw", "wybierz", "luzuj",
  "ster", "zwrot", "odpadaj", "ostrzej", "kurs",
  "rzuć", "rzuc", "podnieś", "podnies", "cumuj", "odcumuj",
  "wiosłuj", "wiosluj", "stop",
  "loguj", "raport", "zamelduj",
  "powtórz", "powtorz", "jeżeli", "jezeli", "jeśli", "jesli",
  "czekaj", "sygnalizuj", "opuść", "opusc",
  "napnij", "dobij",
  "cała", "cala", "naprzód", "naprzod", "wolny", "średni", "sredni",
  "wsteczny", "wstecz",
  // ★ NOWE
  "niech",
]);

const OBJECTS = new Set([
  "grot", "fok", "bezan", "mezana", "sztaksel",
  "szoty", "fały", "faly", "brasy", "talrepy",
  "kotwicę", "kotwice",
  "maszt", "takielunek",
  "wiosła", "wiosla",
  "żagle", "zagle",
  "bandera", "banderę", "bandere",
  "klubowa", "klubową",
  "gościa", "goscia",
  "protestowa", "protestową",
  "proporczyk", "proporczyka",
  "flagę", "flage", "flaga",
  "Q", "kwarantanny",
  // ★ NOWE - pola stanu (dla wiatr.sila, zagle.grot.stan itp.)
  "sila", "siła", "kierunek", "predkosc", "prędkość",
  "stan", "kat", "kąt", "ref", "szot",
]);

const MODIFIERS = new Set([
  "na", "do", "przez", "za",
  "prosto", "sztag", "rufę", "rufe",
  "baksztag", "bejdewind", "półwiatr", "polwiatr", "fordewind",
  "półbaksztag", "polbaksztag",
  "ostry",
  "północ", "polnoc", "południe", "poludnie",
  "wschód", "wschod", "zachód", "zachod",
  "wtedy", "to", "inaczej", "albo", "razy",
  "stopni", "procent", "węzłów", "wezlow", "metrów", "metrow",
  "sekund", "minut", "beaufort",
  "wiatr", "prędkość", "predkosc", "głębokość", "glebokosc",
  "pogodę", "pogode", "pozycję", "pozycje", "zdarzenie",
  "punkt",
  "lewa", "prawa", "bakburta", "sterburta",
  "wszystkie", "pełne", "pelne", "sztormowe",
  "morskich", "mil",
  "stan", "jednostki",
  "aż", "az",
  "pod", "wiatrem",
  // ★ NOWE - operatory logiczne (słowne)
  "oraz", "lub", "negacja",
]);

type TT = "cmd" | "obj" | "mod" | "str" | "num" | "cmt" | "op" | "pun" | "txt";

function tokenizeLine(line: string): Array<{ t: TT; v: string }> {
  const out: Array<{ t: TT; v: string }> = [];
  let i = 0;

  const trimmed = line.trimStart();
  if (trimmed.startsWith("//")) {
    const pre = line.substring(0, line.indexOf("//"));
    if (pre) out.push({ t: "txt", v: pre });
    out.push({ t: "cmt", v: line.substring(line.indexOf("//")) });
    return out;
  }

  while (i < line.length) {
    if (/\s/.test(line[i])) {
      let j = i;
      while (j < line.length && /\s/.test(line[j])) j++;
      out.push({ t: "txt", v: line.substring(i, j) });
      i = j;
      continue;
    }
    if (line[i] === '"') {
      let j = i + 1;
      while (j < line.length && line[j] !== '"') j++;
      j++;
      out.push({ t: "str", v: line.substring(i, j) });
      i = j;
      continue;
    }
    const two = line.substring(i, i + 2);
    if (two === ">=" || two === "<=" || two === "==" || two === "&&" || two === "||") {
      out.push({ t: "op", v: two });
      i += 2;
      continue;
    }
    // ★ NOWE - arytmetyka jako operatory
    if ("><=%+-*/!".includes(line[i])) {
      out.push({ t: "op", v: line[i] });
      i++;
      continue;
    }
    if (";{}(),.".includes(line[i])) {
      out.push({ t: "pun", v: line[i] });
      i++;
      continue;
    }
    if (/\d/.test(line[i])) {
      let j = i;
      while (j < line.length && /[\d.]/.test(line[j])) j++;
      out.push({ t: "num", v: line.substring(i, j) });
      i = j;
      continue;
    }
    if (/[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]/.test(line[i])) {
      let j = i;
      while (j < line.length && /[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ_0-9]/.test(line[j])) j++;
      const w = line.substring(i, j);
      const lo = w.toLowerCase();
      out.push({
        t: COMMANDS.has(lo)
          ? "cmd"
          : OBJECTS.has(lo) || OBJECTS.has(w)
          ? "obj"
          : MODIFIERS.has(lo)
          ? "mod"
          : "txt",
        v: w,
      });
      i = j;
      continue;
    }
    out.push({ t: "txt", v: line[i] });
    i++;
  }
  return out;
}

const CLS: Record<TT, string | null> = {
  cmd: "hl-command",
  obj: "hl-object",
  mod: "hl-modifier",
  str: "hl-string",
  num: "hl-number",
  cmt: "hl-comment",
  op: "hl-operator",
  pun: "hl-punct",
  txt: null,
};

function Highlighted({ code }: { code: string }) {
  const lines = code.split("\n");
  const els: ReactNode[] = [];
  lines.forEach((line, li) => {
    tokenizeLine(line).forEach((tok, ti) => {
      const c = CLS[tok.t];
      els.push(
        c ? (
          <span key={`${li}-${ti}`} className={c}>
            {tok.v}
          </span>
        ) : (
          tok.v
        )
      );
    });
    if (li < lines.length - 1) els.push("\n");
  });
  return <>{els}</>;
}

// -----------------------------------------------------------------
// COMPONENT
// -----------------------------------------------------------------

const DEFAULT_CODE = `// Wpisz polecenia żeglarskie. Używaj zmiennych i wyrażeń!
wiatr 270 stopni;
wiatr 14 wezlow;

niech baza_ref = 30;

jezeli wiatr.sila >= 6 {
    refuj grot do (baza_ref + 20) procent;
} inaczej {
    postaw grot;
    postaw fok;
};

kurs na polwiatr;
`;

export default function CommandTerminal({
  onExecute,
  onReset,
  loading,
  errors,
  examples,
  connected,
}: CommandTerminalProps) {
  const [commands, setCommands] = useState(DEFAULT_CODE);
  const [resetOnExecute, setResetOnExecute] = useState(true);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const highlightRef = useRef<HTMLPreElement>(null);

  useEffect(() => {
    textareaRef.current?.focus();
  }, []);

  const syncScroll = useCallback(() => {
    if (textareaRef.current && highlightRef.current) {
      highlightRef.current.scrollTop = textareaRef.current.scrollTop;
      highlightRef.current.scrollLeft = textareaRef.current.scrollLeft;
    }
  }, []);

  const handleExecute = () => {
    if (!commands.trim() || loading || !connected) return;
    onExecute(commands, resetOnExecute);
  };

  const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.ctrlKey && e.key === "Enter") {
      e.preventDefault();
      handleExecute();
    }
    if (e.key === "Tab") {
      e.preventDefault();
      const t = e.currentTarget,
        s = t.selectionStart,
        en = t.selectionEnd;
      setCommands(commands.substring(0, s) + "    " + commands.substring(en));
      setTimeout(() => {
        t.selectionStart = t.selectionEnd = s + 4;
      }, 0);
    }
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

      {examples.length > 0 && (
        <div className="examples-bar">
          <span className="examples-label">Przykłady:</span>
          {examples.map((ex, i) => (
            <button
              key={i}
              className="example-btn"
              onClick={() => setCommands(ex.commands)}
              title={ex.commands}
            >
              {ex.name}
            </button>
          ))}
        </div>
      )}

      <div className="textarea-wrapper">
        <div className="editor-container">
          <pre ref={highlightRef} className="highlight-backdrop" aria-hidden="true">
            <Highlighted code={commands} />
            {"\n"}
          </pre>
          <textarea
            ref={textareaRef}
            value={commands}
            onChange={(e: ChangeEvent<HTMLTextAreaElement>) =>
              setCommands(e.target.value)
            }
            onKeyDown={handleKeyDown}
            onScroll={syncScroll}
            placeholder="Wpisz polecenia żeglarskie..."
            spellCheck={false}
            className="command-textarea"
          />
        </div>
      </div>

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

      <div className="terminal-actions">
        <button
          className="btn btn-primary"
          onClick={handleExecute}
          disabled={loading || !connected}
        >
          {loading ? "⏳ Wykonywanie..." : "▶ Wykonaj (Ctrl+Enter)"}
        </button>
        <button className="btn btn-secondary" onClick={onReset} disabled={loading}>
          ↺ Reset
        </button>
        <button className="btn btn-ghost" onClick={() => setCommands("")}>
          ✕ Wyczyść
        </button>
      </div>
    </div>
  );
}
