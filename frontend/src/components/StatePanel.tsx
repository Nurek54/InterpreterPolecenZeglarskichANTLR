import { useState, type ReactNode } from "react";
import type { ShipState } from "../types/ship";

interface StatePanelProps {
  shipState: ShipState | null;
}

interface SectionProps {
  title: string;
  icon: string;
  children: ReactNode;
  defaultOpen?: boolean;
}

interface StateRowProps {
  label: string;
  value: string | number;
  color?: string;
}

function Section({ title, icon, children, defaultOpen = true }: SectionProps) {
  const [open, setOpen] = useState(defaultOpen);
  return (
    <div className="state-section">
      <div className="section-header" onClick={() => setOpen(!open)}>
        <span>
          {icon} {title}
        </span>
        <span className="toggle">{open ? "▾" : "▸"}</span>
      </div>
      {open && <div className="section-body">{children}</div>}
    </div>
  );
}

function StateRow({ label, value, color }: StateRowProps) {
  return (
    <div className="state-row">
      <span className="state-label">{label}</span>
      <span className="state-value" style={color ? { color } : undefined}>
        {value}
      </span>
    </div>
  );
}

const FLAG_LABELS: Record<string, string> = {
  bandera: "bandera",
  klubowa: "klubowa",
  goscia: "gościa",
  q: "Q (kwarantanna)",
  protestowa: "protestowa",
  proporczyk: "proporczyk",
};

export default function StatePanel({ shipState }: StatePanelProps) {
  if (!shipState) {
    return (
      <div className="state-panel">
        <div className="panel-header">
          <h2>📊 Stan statku</h2>
        </div>
        <div className="state-empty">
          Wykonaj polecenia, aby zobaczyć stan statku
        </div>
      </div>
    );
  }

  const s = shipState;

  const activeSails = Object.entries(s.sails).filter(
    ([, sail]) => sail.state !== "zwinięty"
  );
  const totalSails = Object.keys(s.sails).length;

  const activeFlags = Object.entries(s.flags)
    .filter(([k, v]) => {
      if (k === "custom") return Array.isArray(v) && v.length > 0;
      return v === true;
    })
    .map(([k, v]) =>
      k === "custom" ? (v as string[]).join(", ") : FLAG_LABELS[k] ?? k
    );

  return (
    <div className="state-panel">
      <div className="panel-header">
        <h2>📊 Stan statku</h2>
      </div>
      <div className="state-scroll">
        {/* Nawigacja */}
        <Section title="Nawigacja" icon="🧭">
          <StateRow label="Kurs" value={`${s.heading.toFixed(0)}°`} />
          <StateRow
            label="Prędkość"
            value={`${s.speed} kn`}
            color={s.speed > 0 ? "#4ade80" : undefined}
          />
          <StateRow label="Ster" value={`${s.rudder_angle}°`} />
          {s.point_of_sail && (
            <StateRow
              label="Point of sail"
              value={s.point_of_sail}
              color="#a78bfa"
            />
          )}
          <StateRow
            label="Kotwica"
            value={s.anchor}
            color={s.anchor === "rzucona" ? "#fbbf24" : undefined}
          />
          <StateRow label="Cumowanie" value={s.mooring} />
          {s.rowing !== "wyłączone" && (
            <StateRow label="Wiosła" value={s.rowing} color="#22d3ee" />
          )}
        </Section>

        {/* Wiatr */}
        <Section title="Wiatr" icon="🌬️">
          <StateRow
            label="Kierunek (z)"
            value={`${s.wind.direction.toFixed(0)}°`}
          />
          <StateRow
            label="Prędkość"
            value={`${s.wind.speed.toFixed(0)} kn`}
            color="#38bdf8"
          />
          <StateRow label="Siła" value={`${s.wind.beaufort} B`} />
        </Section>

        {/* Żagle */}
        <Section
          title={`Żagle (${activeSails.length}/${totalSails})`}
          icon="⛵"
        >
          {activeSails.length === 0 ? (
            <div className="state-muted">Wszystkie zwinięte</div>
          ) : (
            activeSails.map(([name, sail]) => (
              <StateRow
                key={name}
                label={name}
                value={
                  sail.state === "zrefowany"
                    ? `${sail.state} (${sail.reef_percent}%)`
                    : sail.state
                }
                color={sail.state === "postawiony" ? "#4ade80" : "#fbbf24"}
              />
            ))
          )}
        </Section>

        {/* Olinowanie */}
        <Section title="Olinowanie" icon="🪢" defaultOpen={false}>
          {Object.entries(s.rigging_tension).map(([name, val]) => (
            <StateRow key={name} label={name} value={`${val}%`} />
          ))}
        </Section>

        {/* Flagi */}
        {activeFlags.length > 0 && (
          <Section title="Flagi" icon="🏳️">
            <StateRow label="Podniesione" value={activeFlags.join(", ")} />
          </Section>
        )}
      </div>
    </div>
  );
}