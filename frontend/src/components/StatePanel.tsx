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
  const activeCargo = Object.entries(s.cargo).filter(([, qty]) => qty > 0);
  const activeFlags = Object.entries(s.flags)
    .filter(([, v]) => v === true || (Array.isArray(v) && v.length > 0))
    .map(([k]) => k);

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
          {s.wind_course && (
            <StateRow label="Kurs wiatrowy" value={s.wind_course} />
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

        {/* Żagle */}
        <Section title={`Żagle (${activeSails.length}/${totalSails})`} icon="⛵">
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

        {/* Uzbrojenie */}
        <Section title="Uzbrojenie" icon="💣" defaultOpen={false}>
          {Object.entries(s.cannons).map(([name, info]) => (
            <StateRow
              key={name}
              label={name}
              value={`${info.state}${info.ammo ? " (" + info.ammo + ")" : ""}`}
              color={info.state === "załadowany" ? "#f97316" : undefined}
            />
          ))}
        </Section>

        {/* Ładunek */}
        <Section title="Ładownia" icon="📦" defaultOpen={false}>
          {activeCargo.length === 0 ? (
            <div className="state-muted">Pusto</div>
          ) : (
            activeCargo.map(([item, qty]) => (
              <StateRow key={item} label={item} value={qty} />
            ))
          )}
        </Section>

        {/* Uszkodzenia */}
        <Section title="Uszkodzenia" icon="🔧" defaultOpen={false}>
          <StateRow
            label="Kadłub"
            value={`${s.damage.hull}%`}
            color={s.damage.hull < 50 ? "#ef4444" : "#4ade80"}
          />
          <StateRow
            label="Maszt"
            value={`${s.damage.mast}%`}
            color={s.damage.mast < 50 ? "#ef4444" : "#4ade80"}
          />
          <StateRow
            label="Takielunek"
            value={`${s.damage.rigging}%`}
            color={s.damage.rigging < 50 ? "#ef4444" : "#4ade80"}
          />
        </Section>

        {/* Status */}
        {(s.alert !== "brak" ||
          activeFlags.length > 0 ||
          s.man_overboard) && (
          <Section title="Status" icon="🏴‍☠️">
            {s.alert !== "brak" && (
              <StateRow label="Alarm" value={s.alert} color="#ef4444" />
            )}
            {activeFlags.length > 0 && (
              <StateRow label="Flagi" value={activeFlags.join(", ")} />
            )}
            {s.man_overboard && (
              <StateRow
                label="Człowiek za burtą"
                value={s.man_overboard_side || "TAK"}
                color="#ef4444"
              />
            )}
            <StateRow label="Załoga" value={s.crew_station} />
          </Section>
        )}
      </div>
    </div>
  );
}

