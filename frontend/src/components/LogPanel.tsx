import { useRef, useEffect, useState, type ChangeEvent } from "react";
import type { LogEntry } from "../types/ship";

interface LogPanelProps {
  log: LogEntry[];
}

const CATEGORY_ICONS: Record<string, string> = {
  żagle: "⛵",
  ster: "🧭",
  nawigacja: "🗺️",
  kotwica: "⚓",
  cumowanie: "🔗",
  prędkość: "💨",
  uzbrojenie: "💣",
  abordaż: "⚔️",
  ładunek: "📦",
  obserwacja: "🔭",
  taktyka: "🏴‍☠️",
  załoga: "👥",
  flagi: "🏴",
  światła: "🔦",
  naprawy: "🔧",
  dziennik: "📜",
  awaria: "🚨",
  pogoda: "🌊",
  kontrola: "⚙️",
  takielunek: "🪢",
  błąd: "❌",
  ogólny: "📝",
};

const CATEGORY_COLORS: Record<string, string> = {
  żagle: "#4ade80",
  ster: "#60a5fa",
  nawigacja: "#a78bfa",
  kotwica: "#fbbf24",
  cumowanie: "#f97316",
  prędkość: "#22d3ee",
  uzbrojenie: "#ef4444",
  abordaż: "#f43f5e",
  ładunek: "#fb923c",
  obserwacja: "#818cf8",
  taktyka: "#e879f9",
  załoga: "#34d399",
  flagi: "#fcd34d",
  światła: "#fde68a",
  naprawy: "#a3a3a3",
  dziennik: "#d4d4d8",
  awaria: "#ff0000",
  pogoda: "#38bdf8",
  kontrola: "#94a3b8",
  takielunek: "#78716c",
  błąd: "#ff4444",
  ogólny: "#888",
};

// ─────────────────────────────────────────────────────────────────
// COMPONENT
// ─────────────────────────────────────────────────────────────────

export default function LogPanel({ log }: LogPanelProps) {
  const scrollRef = useRef<HTMLDivElement>(null);
  const [filter, setFilter] = useState("all");

  // Auto-scroll
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [log]);

  const categories = [...new Set(log.map((e) => e.category))].sort();

  const filtered =
    filter === "all" ? log : log.filter((e) => e.category === filter);

  return (
    <div className="log-panel">
      <div className="panel-header">
        <h2>📜 Dziennik pokładowy ({log.length})</h2>
        {categories.length > 1 && (
          <select
            className="log-filter"
            value={filter}
            onChange={(e: ChangeEvent<HTMLSelectElement>) =>
              setFilter(e.target.value)
            }
          >
            <option value="all">Wszystkie</option>
            {categories.map((cat) => (
              <option key={cat} value={cat}>
                {CATEGORY_ICONS[cat] ?? "📝"} {cat}
              </option>
            ))}
          </select>
        )}
      </div>

      <div className="log-scroll" ref={scrollRef}>
        {filtered.length === 0 ? (
          <div className="log-empty">
            {log.length === 0
              ? "Dziennik pusty — wykonaj polecenia"
              : "Brak wpisów w wybranej kategorii"}
          </div>
        ) : (
          filtered.map((entry, i) => {
            const icon = CATEGORY_ICONS[entry.category] ?? "📝";
            const color = CATEGORY_COLORS[entry.category] ?? "#888";
            return (
              <div key={i} className="log-entry">
                <span className="log-time">{entry.timestamp}</span>
                <span className="log-icon">{icon}</span>
                <span className="log-category" style={{ color }}>
                  [{entry.category}]
                </span>
                <span className="log-message">{entry.message}</span>
              </div>
            );
          })
        )}
      </div>
    </div>
  );
}
