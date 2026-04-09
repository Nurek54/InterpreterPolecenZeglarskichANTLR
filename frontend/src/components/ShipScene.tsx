import { useRef, useMemo, useEffect, Suspense, useState } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls, useGLTF } from "@react-three/drei";
import * as THREE from "three";
import React from "react";
import type { ShipState, WindState } from "../types/ship";

interface ShipSceneProps {
    shipState: ShipState | null;
}

interface ShipModelProps {
    shipState: ShipState | null;
}

interface FallbackShipProps {
    hasSailsSet: boolean;
}

interface CompassOverlayProps {
    heading: number;
    speed: number;
    anchor: string;
    pointOfSail: string;
}

// ─────────────────────────────────────────────────────────────────
// KOMPAS + INFO OVERLAY (top-right)
// ─────────────────────────────────────────────────────────────────

function CompassOverlay({ heading, speed, anchor, pointOfSail }: CompassOverlayProps) {
    const directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"];
    const dirIndex = Math.round(((heading % 360) + 360) % 360 / 45) % 8;
    const dirName = directions[dirIndex];

    const compassBg = "rgba(6, 13, 20, 0.82)";
    const ringColor = "rgba(212, 168, 67, 0.45)";
    const goldText = "#d4a843";
    const font = "'IBM Plex Mono', 'Menlo', monospace";

    return (
        <div style={{
            position: "absolute",
            top: 14,
            right: 14,
            zIndex: 10,
            pointerEvents: "none",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 6,
        }}>
            {/* Kompas */}
            <div style={{
                width: 86,
                height: 86,
                borderRadius: "50%",
                background: compassBg,
                border: `2px solid ${ringColor}`,
                position: "relative",
                backdropFilter: "blur(8px)",
                boxShadow: "0 4px 20px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.03)",
            }}>
                {(["N", "E", "S", "W"] as const).map((dir, i) => {
                    const angle = i * 90;
                    const rad = (angle * Math.PI) / 180;
                    const r = 32;
                    const x = 43 + Math.sin(rad) * r;
                    const y = 43 - Math.cos(rad) * r;
                    return (
                        <span
                            key={dir}
                            style={{
                                position: "absolute",
                                left: x,
                                top: y,
                                transform: "translate(-50%, -50%)",
                                fontSize: 9,
                                fontWeight: dir === "N" ? 800 : 500,
                                fontFamily: font,
                                color: dir === "N" ? "#d45050" : "rgba(213, 221, 229, 0.4)",
                                letterSpacing: 0.5,
                            }}
                        >
                            {dir}
                        </span>
                    );
                })}

                {/* Strzałka */}
                <div style={{
                    position: "absolute",
                    top: "50%",
                    left: "50%",
                    width: 0,
                    height: 0,
                    transform: `translate(-50%, -50%) rotate(${heading}deg)`,
                    transition: "transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)",
                }}>
                    <div style={{
                        position: "absolute",
                        left: -4,
                        top: -26,
                        width: 0,
                        height: 0,
                        borderLeft: "4px solid transparent",
                        borderRight: "4px solid transparent",
                        borderBottom: "26px solid #d45050",
                        filter: "drop-shadow(0 0 3px rgba(212, 80, 80, 0.4))",
                    }} />
                    <div style={{
                        position: "absolute",
                        left: -4,
                        top: 0,
                        width: 0,
                        height: 0,
                        borderLeft: "4px solid transparent",
                        borderRight: "4px solid transparent",
                        borderTop: "26px solid rgba(213, 221, 229, 0.25)",
                    }} />
                    <div style={{
                        position: "absolute",
                        left: -2.5,
                        top: -2.5,
                        width: 5,
                        height: 5,
                        borderRadius: "50%",
                        background: goldText,
                        boxShadow: `0 0 4px ${goldText}`,
                    }} />
                </div>

                {/* Ticki co 30° */}
                {Array.from({ length: 12 }).map((_, i) => {
                    const angle = i * 30;
                    const rad = (angle * Math.PI) / 180;
                    const r1 = 38;
                    return (
                        <div
                            key={i}
                            style={{
                                position: "absolute",
                                left: 43 + Math.sin(rad) * r1,
                                top: 43 - Math.cos(rad) * r1,
                                width: 1,
                                height: i % 3 === 0 ? 5 : 3,
                                background: i % 3 === 0
                                    ? "rgba(212, 168, 67, 0.5)"
                                    : "rgba(213, 221, 229, 0.15)",
                                transform: `translate(-50%, -50%) rotate(${angle}deg)`,
                                borderRadius: 1,
                            }}
                        />
                    );
                })}
            </div>

            {/* Kurs */}
            <div style={{
                background: compassBg,
                color: goldText,
                padding: "3px 12px",
                borderRadius: 5,
                fontFamily: font,
                fontSize: 12,
                fontWeight: 600,
                border: `1px solid ${ringColor}`,
                backdropFilter: "blur(8px)",
                letterSpacing: 0.5,
                boxShadow: "0 2px 10px rgba(0,0,0,0.4)",
            }}>
                {heading.toFixed(0)}° {dirName}
            </div>

            {/* Prędkość + kotwica */}
            <div style={{
                background: compassBg,
                padding: "3px 10px",
                borderRadius: 5,
                fontFamily: font,
                fontSize: 10,
                fontWeight: 500,
                border: `1px solid rgba(22, 38, 56, 0.6)`,
                backdropFilter: "blur(8px)",
                color: speed > 0 ? "#38c8a8" : "rgba(122, 146, 168, 0.6)",
                boxShadow: "0 2px 10px rgba(0,0,0,0.3)",
                display: "flex",
                gap: 8,
                alignItems: "center",
            }}>
                <span>{speed.toFixed(1)} kn</span>
                {anchor === "rzucona" && (
                    <span style={{ color: "#d4a843", fontSize: 11 }}>⚓</span>
                )}
            </div>

            {/* Point of sail */}
            {pointOfSail && (
                <div style={{
                    background: compassBg,
                    padding: "3px 10px",
                    borderRadius: 5,
                    fontFamily: font,
                    fontSize: 10,
                    color: "#a78bfa",
                    border: `1px solid rgba(167, 139, 250, 0.3)`,
                    backdropFilter: "blur(8px)",
                }}>
                    {pointOfSail}
                </div>
            )}
        </div>
    );
}

// ─────────────────────────────────────────────────────────────────
// WSKAŹNIK WIATRU (top-left)
// ─────────────────────────────────────────────────────────────────

function WindIndicator({ wind }: { wind: WindState }) {
    const bg = "rgba(6, 13, 20, 0.82)";
    const ring = "rgba(56, 189, 248, 0.45)";
    const blue = "#38bdf8";
    const font = "'IBM Plex Mono', 'Menlo', monospace";

    // Strzałka pokazuje kierunek W którym wiatr WIEJE (z direction + 180°)
    const arrowRotation = (wind.direction + 180) % 360;

    // Intensywność zależna od siły
    const intensity = Math.min(1, wind.beaufort / 10);
    const arrowColor = `rgba(56, 189, 248, ${0.5 + intensity * 0.5})`;

    return (
        <div style={{
            position: "absolute",
            top: 14,
            left: 14,
            zIndex: 10,
            pointerEvents: "none",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 6,
        }}>
            {/* Koło z różą wiatrów */}
            <div style={{
                width: 86,
                height: 86,
                borderRadius: "50%",
                background: bg,
                border: `2px solid ${ring}`,
                position: "relative",
                backdropFilter: "blur(8px)",
                boxShadow: "0 4px 20px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.03)",
            }}>
                {/* Podziałka co 45° */}
                {Array.from({ length: 8 }).map((_, i) => {
                    const angle = i * 45;
                    const rad = (angle * Math.PI) / 180;
                    return (
                        <div
                            key={i}
                            style={{
                                position: "absolute",
                                left: 43 + Math.sin(rad) * 38,
                                top: 43 - Math.cos(rad) * 38,
                                width: 1,
                                height: i % 2 === 0 ? 6 : 3,
                                background: i % 2 === 0
                                    ? "rgba(56, 189, 248, 0.5)"
                                    : "rgba(213, 221, 229, 0.2)",
                                transform: `translate(-50%, -50%) rotate(${angle}deg)`,
                            }}
                        />
                    );
                })}

                {/* Etykieta N */}
                <span style={{
                    position: "absolute",
                    left: 43,
                    top: 10,
                    transform: "translate(-50%, -50%)",
                    fontSize: 9,
                    fontWeight: 700,
                    fontFamily: font,
                    color: "rgba(213, 221, 229, 0.5)",
                }}>
                    N
                </span>

                {/* Strzałka wiatru */}
                <div style={{
                    position: "absolute",
                    top: "50%",
                    left: "50%",
                    width: 0,
                    height: 0,
                    transform: `translate(-50%, -50%) rotate(${arrowRotation}deg)`,
                    transition: "transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94)",
                }}>
                    {/* Grot strzałki */}
                    <div style={{
                        position: "absolute",
                        left: -6,
                        top: -28,
                        width: 0,
                        height: 0,
                        borderLeft: "6px solid transparent",
                        borderRight: "6px solid transparent",
                        borderBottom: `22px solid ${arrowColor}`,
                        filter: `drop-shadow(0 0 4px ${arrowColor})`,
                    }} />
                    {/* Trzon strzałki */}
                    <div style={{
                        position: "absolute",
                        left: -1.5,
                        top: -6,
                        width: 3,
                        height: 32,
                        background: arrowColor,
                        borderRadius: 2,
                    }} />
                </div>

                {/* Środek */}
                <div style={{
                    position: "absolute",
                    top: "50%",
                    left: "50%",
                    transform: "translate(-50%, -50%)",
                    width: 6,
                    height: 6,
                    borderRadius: "50%",
                    background: blue,
                    boxShadow: `0 0 6px ${blue}`,
                }} />
            </div>

            {/* Nagłówek */}
            <div style={{
                background: bg,
                color: blue,
                padding: "3px 10px",
                borderRadius: 5,
                fontFamily: font,
                fontSize: 10,
                fontWeight: 600,
                border: `1px solid ${ring}`,
                backdropFilter: "blur(8px)",
                letterSpacing: 0.5,
                textTransform: "uppercase",
            }}>
                🌬️ Wiatr
            </div>

            {/* Prędkość + Beaufort */}
            <div style={{
                background: bg,
                color: "#e8f4fb",
                padding: "3px 10px",
                borderRadius: 5,
                fontFamily: font,
                fontSize: 11,
                fontWeight: 600,
                border: `1px solid rgba(22, 38, 56, 0.6)`,
                backdropFilter: "blur(8px)",
                boxShadow: "0 2px 10px rgba(0,0,0,0.3)",
            }}>
                {wind.speed.toFixed(0)} kn · B{wind.beaufort}
            </div>

            {/* Kierunek */}
            <div style={{
                background: bg,
                color: "rgba(213, 221, 229, 0.6)",
                padding: "2px 9px",
                borderRadius: 5,
                fontFamily: font,
                fontSize: 9,
                border: `1px solid rgba(22, 38, 56, 0.6)`,
                backdropFilter: "blur(8px)",
            }}>
                z {wind.direction.toFixed(0)}°
            </div>
        </div>
    );
}

// ─────────────────────────────────────────────────────────────────
// ANIMOWANE SMUGI WIATRU (cząstki)
// ─────────────────────────────────────────────────────────────────

interface Particle {
    x: number;
    y: number;
    z: number;
    life: number;
}

function WindStreaks({ wind }: { wind: WindState }) {
    const groupRef = useRef<THREE.Group>(null);
    const COUNT = 60;

    const particles = useMemo<Particle[]>(
        () =>
            Array.from({ length: COUNT }).map(() => ({
                x: (Math.random() - 0.5) * 120,
                z: (Math.random() - 0.5) * 120,
                y: 0.5 + Math.random() * 4,
                life: Math.random(),
            })),
        []
    );

    useFrame((_, delta) => {
        if (!groupRef.current) return;

        // Kierunek W który wieje wiatr (direction + 180°)
        const blowRad = ((wind.direction + 180) * Math.PI) / 180;
        const windFactor = Math.max(0.3, wind.speed / 20);
        const vx = Math.sin(blowRad) * wind.speed * 0.4 * windFactor;
        const vz = -Math.cos(blowRad) * wind.speed * 0.4 * windFactor;

        groupRef.current.children.forEach((child, i) => {
            const p = particles[i];
            if (!p) return;

            p.x += vx * delta;
            p.z += vz * delta;
            p.life -= delta * 0.25;

            if (p.life <= 0 || Math.abs(p.x) > 70 || Math.abs(p.z) > 70) {
                p.x = (Math.random() - 0.5) * 140;
                p.z = (Math.random() - 0.5) * 140;
                p.y = 0.5 + Math.random() * 4;
                p.life = 0.6 + Math.random() * 0.6;
            }

            child.position.set(p.x, p.y, p.z);
            child.rotation.y = blowRad;

            const mat = (child as THREE.Mesh).material as THREE.MeshBasicMaterial;
            if (mat) {
                mat.opacity = Math.min(0.45, p.life * 0.45) * windFactor;
            }
        });
    });

    return (
        <group ref={groupRef}>
            {particles.map((_, i) => (
                <mesh key={i}>
                    <boxGeometry args={[2.2, 0.025, 0.025]} />
                    <meshBasicMaterial color="#c9e8ff" transparent opacity={0.3} />
                </mesh>
            ))}
        </group>
    );
}

// ─────────────────────────────────────────────────────────────────
// WODA — animowana, reagująca na wiatr
// ─────────────────────────────────────────────────────────────────

function Water({ windSpeed }: { windSpeed: number }) {
    const meshRef = useRef<THREE.Mesh>(null);
    const geometry = useMemo(
        () => new THREE.PlaneGeometry(400, 400, 80, 80),
        []
    );

    useFrame(({ clock }) => {
        if (!meshRef.current) return;
        const positions = meshRef.current.geometry.attributes
            .position as THREE.BufferAttribute;
        const time = clock.getElapsedTime();
        const amp = 0.4 + Math.min(1.5, windSpeed / 20);

        for (let i = 0; i < positions.count; i++) {
            const x = positions.getX(i);
            const y = positions.getY(i);
            const z =
                Math.sin(x * 0.06 + time * 0.6) * 0.35 * amp +
                Math.sin(y * 0.09 + time * 0.4) * 0.25 * amp +
                Math.sin((x + y) * 0.04 + time * 0.3) * 0.15 * amp;
            positions.setZ(i, z);
        }
        positions.needsUpdate = true;
    });

    return (
        <mesh ref={meshRef} rotation={[-Math.PI / 2, 0, 0]} position={[0, -0.5, 0]}>
            <primitive object={geometry} />
            <meshStandardMaterial
                color="#082840"
                transparent
                opacity={0.88}
                side={THREE.DoubleSide}
                roughness={0.25}
                metalness={0.15}
            />
        </mesh>
    );
}

// ─────────────────────────────────────────────────────────────────
// OŚWIETLENIE
// ─────────────────────────────────────────────────────────────────

function SceneLighting() {
    return (
        <>
            <ambientLight intensity={0.45} color="#8899bb" />
            <directionalLight
                position={[12, 18, 8]}
                intensity={1.4}
                castShadow
                color="#ffe8c0"
                shadow-mapSize-width={1024}
                shadow-mapSize-height={1024}
            />
            <directionalLight
                position={[-8, 10, -12]}
                intensity={0.25}
                color="#3366aa"
            />
            <pointLight
                position={[0, 8, 0]}
                intensity={0.2}
                color="#ffd080"
                distance={30}
                decay={2}
            />
            <hemisphereLight
                color="#1a2a44"
                groundColor="#061018"
                intensity={0.4}
            />
        </>
    );
}

// ─────────────────────────────────────────────────────────────────
// BANDERA — powiewa zgodnie z wiatrem
// ─────────────────────────────────────────────────────────────────

function Ensign({
    visible,
    shipHeading,
    windDirection,
}: {
    visible: boolean;
    shipHeading: number;
    windDirection: number;
}) {
    const flagRef = useRef<THREE.Mesh>(null);

    // Bandera ma być w świecie skierowana zgodnie z kierunkiem wiania (windDir + 180).
    // Statek-grupa jest obracana o -heading*PI/180, więc kompensujemy lokalnie.
    const localRotation = useMemo(() => {
        const worldBlow = -((windDirection + 180) * Math.PI) / 180;
        const shipRot = -(shipHeading * Math.PI) / 180;
        return worldBlow - shipRot;
    }, [windDirection, shipHeading]);

    useFrame(({ clock }) => {
        if (!flagRef.current) return;
        const t = clock.getElapsedTime();
        flagRef.current.scale.x = 1 + Math.sin(t * 4) * 0.06;
    });

    if (!visible) return null;

    return (
        <group position={[0, 4.8, -2.5]} rotation={[0, localRotation, 0]}>
            {/* Drzewiec */}
            <mesh position={[0, 0, 0]}>
                <cylinderGeometry args={[0.015, 0.015, 1.2]} />
                <meshStandardMaterial color="#3d2c1e" />
            </mesh>
            {/* Płat flagi */}
            <mesh ref={flagRef} position={[0.4, 0.35, 0]}>
                <planeGeometry args={[0.8, 0.45]} />
                <meshStandardMaterial
                    color="#d45050"
                    side={THREE.DoubleSide}
                    roughness={0.8}
                />
            </mesh>
            {/* Biały pasek */}
            <mesh position={[0.4, 0.42, 0.005]}>
                <planeGeometry args={[0.8, 0.15]} />
                <meshStandardMaterial
                    color="#f0f0f0"
                    side={THREE.DoubleSide}
                    roughness={0.8}
                />
            </mesh>
        </group>
    );
}

// ─────────────────────────────────────────────────────────────────
// MODEL GLB
// ─────────────────────────────────────────────────────────────────

function GLBModel({ url, visible }: { url: string; visible: boolean }) {
    const { scene } = useGLTF(url);
    const cloned = useMemo(() => scene.clone(true), [scene]);
    const groupRef = useRef<THREE.Group>(null);

    useEffect(() => {
        cloned.traverse((child) => {
            child.visible = visible;
        });
    }, [visible, cloned]);

    return <primitive ref={groupRef} object={cloned} visible={visible} scale={1} />;
}

// ─────────────────────────────────────────────────────────────────
// FALLBACK — prosty statek z prymitywów
// ─────────────────────────────────────────────────────────────────

function FallbackShip({ hasSailsSet }: FallbackShipProps) {
    const sailColor = "#e8e0d0";
    const hullDark = "#5a2e1c";
    const hullMid = "#7a4a30";
    const mastColor = "#3d2c1e";
    const deckColor = "#906840";
    const trimColor = "#4a2a14";

    const sailMat = (
        <meshStandardMaterial
            color={sailColor}
            side={THREE.DoubleSide}
            transparent
            opacity={0.9}
            roughness={0.7}
        />
    );

    return (
        <group>
            {/* ── KADŁUB ── */}
            <mesh position={[0, 0, 0]}>
                <boxGeometry args={[2.4, 1, 8]} />
                <meshStandardMaterial color={hullDark} roughness={0.8} />
            </mesh>
            <mesh position={[0, 0, 4.5]} rotation={[0, 0, Math.PI / 4]}>
                <boxGeometry args={[1.2, 0.7, 1.5]} />
                <meshStandardMaterial color={hullDark} roughness={0.8} />
            </mesh>
            <mesh position={[0, 0.6, 6]} rotation={[Math.PI / 6, 0, 0]}>
                <cylinderGeometry args={[0.04, 0.06, 3.5]} />
                <meshStandardMaterial color={mastColor} />
            </mesh>
            <mesh position={[0, 0.2, -4.2]} rotation={[0, 0, Math.PI / 4]}>
                <boxGeometry args={[1, 0.5, 0.8]} />
                <meshStandardMaterial color={hullDark} roughness={0.8} />
            </mesh>
            <mesh position={[0, 0.55, 0]}>
                <boxGeometry args={[2.2, 0.08, 7.5]} />
                <meshStandardMaterial color={deckColor} roughness={0.9} />
            </mesh>
            <mesh position={[0, 1.1, -2.8]}>
                <boxGeometry args={[2.2, 0.8, 2.5]} />
                <meshStandardMaterial color={hullMid} roughness={0.8} />
            </mesh>
            <mesh position={[0, 1.55, -2.8]}>
                <boxGeometry args={[2.3, 0.06, 2.6]} />
                <meshStandardMaterial color={trimColor} />
            </mesh>
            <mesh position={[1.15, 0.8, 0]}>
                <boxGeometry args={[0.06, 0.5, 7.5]} />
                <meshStandardMaterial color={hullMid} roughness={0.8} />
            </mesh>
            <mesh position={[-1.15, 0.8, 0]}>
                <boxGeometry args={[0.06, 0.5, 7.5]} />
                <meshStandardMaterial color={hullMid} roughness={0.8} />
            </mesh>
            <mesh position={[0, -0.1, 0]}>
                <boxGeometry args={[2.5, 0.06, 8.1]} />
                <meshStandardMaterial color="#8a6830" metalness={0.3} roughness={0.5} />
            </mesh>

            {/* ── MASZTY ── */}
            <mesh position={[0, 3.8, 0]}>
                <cylinderGeometry args={[0.07, 0.1, 7]} />
                <meshStandardMaterial color={mastColor} />
            </mesh>
            <mesh position={[0, 3.5, 0]} rotation={[0, 0, Math.PI / 2]}>
                <cylinderGeometry args={[0.03, 0.04, 3.5]} />
                <meshStandardMaterial color={mastColor} />
            </mesh>
            <mesh position={[0, 5.5, 0]} rotation={[0, 0, Math.PI / 2]}>
                <cylinderGeometry args={[0.025, 0.035, 2.8]} />
                <meshStandardMaterial color={mastColor} />
            </mesh>
            <mesh position={[0, 6.8, 0]} rotation={[0, 0, Math.PI / 2]}>
                <cylinderGeometry args={[0.02, 0.03, 2]} />
                <meshStandardMaterial color={mastColor} />
            </mesh>
            <mesh position={[0, 3.2, 2.8]}>
                <cylinderGeometry args={[0.06, 0.09, 6]} />
                <meshStandardMaterial color={mastColor} />
            </mesh>
            <mesh position={[0, 2.8, 2.8]} rotation={[0, 0, Math.PI / 2]}>
                <cylinderGeometry args={[0.03, 0.04, 3]} />
                <meshStandardMaterial color={mastColor} />
            </mesh>
            <mesh position={[0, 4.5, 2.8]} rotation={[0, 0, Math.PI / 2]}>
                <cylinderGeometry args={[0.025, 0.035, 2.4]} />
                <meshStandardMaterial color={mastColor} />
            </mesh>
            <mesh position={[0, 3, -2.5]}>
                <cylinderGeometry args={[0.05, 0.08, 5.2]} />
                <meshStandardMaterial color={mastColor} />
            </mesh>
            <mesh position={[0, 2.5, -2.5]} rotation={[0, 0, Math.PI / 2]}>
                <cylinderGeometry args={[0.025, 0.035, 2.5]} />
                <meshStandardMaterial color={mastColor} />
            </mesh>
            <mesh position={[0, 6.5, 0]}>
                <cylinderGeometry args={[0.3, 0.25, 0.3, 8, 1, true]} />
                <meshStandardMaterial color={mastColor} side={THREE.DoubleSide} />
            </mesh>

            {/* ═══ ŻAGLE ═══ */}
            {hasSailsSet && (
                <>
                    <mesh position={[0, 3.5, 0.05]}>
                        <planeGeometry args={[3.2, 2.5]} />
                        {sailMat}
                    </mesh>
                    <mesh position={[0, 5.5, 0.05]}>
                        <planeGeometry args={[2.5, 1.8]} />
                        {sailMat}
                    </mesh>
                    <mesh position={[0, 6.8, 0.05]}>
                        <planeGeometry args={[1.8, 1.2]} />
                        {sailMat}
                    </mesh>
                    <mesh position={[0, 2.8, 2.85]}>
                        <planeGeometry args={[2.8, 2.2]} />
                        {sailMat}
                    </mesh>
                    <mesh position={[0, 4.5, 2.85]}>
                        <planeGeometry args={[2.2, 1.5]} />
                        {sailMat}
                    </mesh>
                    <mesh position={[0, 2.5, -2.45]}>
                        <planeGeometry args={[2.2, 1.8]} />
                        {sailMat}
                    </mesh>
                    <mesh position={[-0.3, 3.2, 4.2]} rotation={[0.5, 0.2, 0.1]}>
                        <planeGeometry args={[1.5, 2.5]} />
                        <meshStandardMaterial
                            color={sailColor}
                            side={THREE.DoubleSide}
                            transparent
                            opacity={0.75}
                            roughness={0.7}
                        />
                    </mesh>
                </>
            )}
        </group>
    );
}

// ─────────────────────────────────────────────────────────────────
// MODEL STATKU — rotacja + kołysanie
// ─────────────────────────────────────────────────────────────────

function ShipModel({ shipState }: ShipModelProps) {
    const groupRef = useRef<THREE.Group>(null);
    const targetRotation = useRef(0);
    const [hasGLB, setHasGLB] = useState(true);

    useEffect(() => {
        if (shipState) {
            targetRotation.current = -(shipState.heading * Math.PI) / 180;
        }
    }, [shipState?.heading]);

    useFrame(({ clock }, delta) => {
        if (!groupRef.current) return;
        const current = groupRef.current.rotation.y;
        const target = targetRotation.current;
        const diff = target - current;
        const shortDiff = ((diff + Math.PI) % (Math.PI * 2)) - Math.PI;
        groupRef.current.rotation.y += shortDiff * Math.min(delta * 2, 1);

        // Kołysanie na falach
        const t = clock.getElapsedTime();
        groupRef.current.rotation.x = Math.sin(t * 0.5) * 0.015;
        groupRef.current.rotation.z = Math.sin(t * 0.3 + 1) * 0.01;
        groupRef.current.position.y = Math.sin(t * 0.6) * 0.08;
    });

    const hasSailsSet = shipState
        ? Object.values(shipState.sails).some((s) => s.state !== "zwinięty")
        : false;

    const ensignVisible = shipState?.flags?.bandera ?? true;
    const heading = shipState?.heading ?? 0;
    const windDir = shipState?.wind?.direction ?? 270;

    return (
        <group ref={groupRef}>
            <Ensign
                visible={ensignVisible}
                shipHeading={heading}
                windDirection={windDir}
            />

            {hasGLB ? (
                <ErrorBoundaryFallback onError={() => setHasGLB(false)}>
                    <Suspense fallback={<FallbackShip hasSailsSet={hasSailsSet} />}>
                        <GLBModel
                            url="/models/ship_sails_down.glb"
                            visible={hasSailsSet}
                        />
                        <GLBModel
                            url="/models/ship_sails_up.glb"
                            visible={!hasSailsSet}
                        />
                    </Suspense>
                </ErrorBoundaryFallback>
            ) : (
                <FallbackShip hasSailsSet={hasSailsSet} />
            )}
        </group>
    );
}

// ─────────────────────────────────────────────────────────────────
// ERROR BOUNDARY
// ─────────────────────────────────────────────────────────────────

interface ErrorBoundaryProps {
    children: React.ReactNode;
    onError: () => void;
}

interface ErrorBoundaryState {
    hasError: boolean;
}

class ErrorBoundaryFallback extends React.Component<ErrorBoundaryProps, ErrorBoundaryState> {
    constructor(props: ErrorBoundaryProps) {
        super(props);
        this.state = { hasError: false };
    }

    static getDerivedStateFromError(): ErrorBoundaryState {
        return { hasError: true };
    }

    componentDidCatch() {
        this.props.onError();
    }

    render() {
        if (this.state.hasError) return null;
        return this.props.children;
    }
}

// ─────────────────────────────────────────────────────────────────
// SCENA GŁÓWNA
// ─────────────────────────────────────────────────────────────────

export default function ShipScene({ shipState }: ShipSceneProps) {
    const heading = shipState?.heading ?? 0;
    const speed = shipState?.speed ?? 0;
    const anchor = shipState?.anchor ?? "podniesiona";
    const pointOfSail = shipState?.point_of_sail ?? "";
    const wind: WindState = shipState?.wind ?? {
        direction: 270,
        speed: 12,
        beaufort: 4,
    };

    return (
        <div style={{ width: "100%", height: "100%", position: "relative" }}>
            <CompassOverlay
                heading={heading}
                speed={speed}
                anchor={anchor}
                pointOfSail={pointOfSail}
            />
            <WindIndicator wind={wind} />

            <Canvas
                camera={{ position: [22, 12, 28], fov: 38 }}
                style={{
                    background:
                        "linear-gradient(180deg, #0c1a2c 0%, #060d14 60%, #040a10 100%)",
                }}
                shadows
            >
                <SceneLighting />

                <fog attach="fog" args={["#060d14", 50, 180]} />

                <Suspense fallback={null}>
                    <ShipModel shipState={shipState} />
                    <Water windSpeed={wind.speed} />
                    <WindStreaks wind={wind} />
                    <OrbitControls
                        target={[0, 2.5, 0]}
                        minDistance={10}
                        maxDistance={100}
                        maxPolarAngle={Math.PI / 2.15}
                        minPolarAngle={0.15}
                        enableDamping
                        dampingFactor={0.06}
                    />
                </Suspense>
            </Canvas>
        </div>
    );
}