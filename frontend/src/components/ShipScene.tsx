import { useRef, useMemo, useEffect, Suspense, useState } from "react";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import { OrbitControls, useGLTF, Html } from "@react-three/drei";
import * as THREE from "three";
import React from "react";
import type { ShipState } from "../types/ship";

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
}

function CompassOverlay({ heading }: CompassOverlayProps) {
    const directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"];

    // Wyznacz nazwę kierunku
    const dirIndex = Math.round(((heading % 360) + 360) % 360 / 45) % 8;
    const dirName = directions[dirIndex];

    return (
        <div style={{
            position: "absolute",
            top: 16,
            right: 16,
            zIndex: 10,
            pointerEvents: "none",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 4,
        }}>
            {/* Kompas kółko */}
            <div style={{
                width: 90,
                height: 90,
                borderRadius: "50%",
                background: "rgba(0,0,0,0.65)",
                border: "2px solid rgba(240,192,64,0.5)",
                position: "relative",
                backdropFilter: "blur(4px)",
            }}>
                {/* Literki N/E/S/W — nieruchome */}
                {(["N", "E", "S", "W"] as const).map((dir, i) => {
                    const angle = i * 90;
                    const rad = (angle * Math.PI) / 180;
                    const r = 34;
                    const x = 45 + Math.sin(rad) * r;
                    const y = 45 - Math.cos(rad) * r;
                    return (
                        <span
                            key={dir}
                            style={{
                                position: "absolute",
                                left: x,
                                top: y,
                                transform: "translate(-50%, -50%)",
                                fontSize: 10,
                                fontWeight: dir === "N" ? 800 : 600,
                                fontFamily: "JetBrains Mono, monospace",
                                color: dir === "N" ? "#f05050" : "rgba(255,255,255,0.5)",
                            }}
                        >
              {dir}
            </span>
                    );
                })}

                {/* Strzałka — obraca się z headingiem */}
                <div style={{
                    position: "absolute",
                    top: "50%",
                    left: "50%",
                    width: 0,
                    height: 0,
                    transform: `translate(-50%, -50%) rotate(${heading}deg)`,
                    transition: "transform 0.4s ease-out",
                }}>
                    {/* Trójkąt N (czerwony) */}
                    <div style={{
                        position: "absolute",
                        left: -5,
                        top: -28,
                        width: 0,
                        height: 0,
                        borderLeft: "5px solid transparent",
                        borderRight: "5px solid transparent",
                        borderBottom: "28px solid #f05050",
                    }} />
                    {/* Trójkąt S (biały) */}
                    <div style={{
                        position: "absolute",
                        left: -5,
                        top: 0,
                        width: 0,
                        height: 0,
                        borderLeft: "5px solid transparent",
                        borderRight: "5px solid transparent",
                        borderTop: "28px solid rgba(255,255,255,0.4)",
                    }} />
                    {/* Punkt środkowy */}
                    <div style={{
                        position: "absolute",
                        left: -3,
                        top: -3,
                        width: 6,
                        height: 6,
                        borderRadius: "50%",
                        background: "#f0c040",
                    }} />
                </div>
            </div>

            {/* Wartość liczbowa pod kompasem */}
            <div style={{
                background: "rgba(0,0,0,0.65)",
                color: "#f0c040",
                padding: "3px 12px",
                borderRadius: 6,
                fontFamily: "JetBrains Mono, monospace",
                fontSize: 13,
                fontWeight: 700,
                border: "1px solid rgba(240,192,64,0.3)",
                backdropFilter: "blur(4px)",
                letterSpacing: 0.5,
            }}>
                {heading.toFixed(0)}° {dirName}
            </div>
        </div>
    );
}

// ─────────────────────────────────────────────────────────────────
// WODA — animowana płaszczyzna
// ─────────────────────────────────────────────────────────────────

function Water() {
    const meshRef = useRef<THREE.Mesh>(null);
    const geometry = useMemo(
        () => new THREE.PlaneGeometry(300, 300, 64, 64),
        []
    );

    useFrame(({ clock }) => {
        if (!meshRef.current) return;
        const positions = meshRef.current.geometry.attributes
            .position as THREE.BufferAttribute;
        const time = clock.getElapsedTime();

        for (let i = 0; i < positions.count; i++) {
            const x = positions.getX(i);
            const y = positions.getY(i);
            const z =
                Math.sin(x * 0.08 + time * 0.7) * 0.3 +
                Math.sin(y * 0.12 + time * 0.5) * 0.2;
            positions.setZ(i, z);
        }
        positions.needsUpdate = true;
    });

    return (
        <mesh ref={meshRef} rotation={[-Math.PI / 2, 0, 0]} position={[0, -0.5, 0]}>
            <primitive object={geometry} />
            <meshStandardMaterial
                color="#0a4a7a"
                transparent
                opacity={0.85}
                side={THREE.DoubleSide}
                roughness={0.3}
                metalness={0.1}
            />
        </mesh>
    );
}

// ─────────────────────────────────────────────────────────────────
// FLAGA JOLLY ROGER
// ─────────────────────────────────────────────────────────────────

function JollyRogerFlag({ visible }: { visible: boolean }) {
    const ref = useRef<THREE.Group>(null);

    useFrame(({ clock }) => {
        if (ref.current && visible) {
            ref.current.rotation.y = Math.sin(clock.getElapsedTime() * 2) * 0.1;
        }
    });

    if (!visible) return null;

    return (
        <group ref={ref} position={[0, 6.5, 0]}>
            <mesh position={[0, 0.5, 0]}>
                <cylinderGeometry args={[0.02, 0.02, 1.5]} />
                <meshStandardMaterial color="#4a3728" />
            </mesh>
            <mesh position={[0.4, 0.8, 0]}>
                <planeGeometry args={[0.8, 0.5]} />
                <meshStandardMaterial color="#111" side={THREE.DoubleSide} />
            </mesh>
            <mesh position={[0.4, 0.8, 0.01]}>
                <circleGeometry args={[0.1, 16]} />
                <meshStandardMaterial color="#fff" />
            </mesh>
        </group>
    );
}

// ─────────────────────────────────────────────────────────────────
// MODEL GLB — ustawia widoczność rekurencyjnie na wszystkich mesh
// ─────────────────────────────────────────────────────────────────

function GLBModel({ url, visible }: { url: string; visible: boolean }) {
    const { scene } = useGLTF(url);
    const cloned = useMemo(() => scene.clone(true), [scene]);
    const groupRef = useRef<THREE.Group>(null);

    // Rekurencyjnie ustaw visible na WSZYSTKICH obiektach w scenie
    useEffect(() => {
        cloned.traverse((child) => {
            child.visible = visible;
        });
    }, [visible, cloned]);

    return <primitive ref={groupRef} object={cloned} visible={visible} scale={1} />;
}

// ─────────────────────────────────────────────────────────────────
// FALLBACK — prosty statek z prymitywów (gdy brak GLB)
// ─────────────────────────────────────────────────────────────────

function FallbackShip({ hasSailsSet }: FallbackShipProps) {
    const sailColor = "#f5f0e0";
    const sailMat = (
        <meshStandardMaterial
            color={sailColor}
            side={THREE.DoubleSide}
            transparent
            opacity={0.92}
        />
    );

    return (
        <group>
            {/* ── KADŁUB ── */}
            <mesh position={[0, 0, 0]}>
                <boxGeometry args={[2.4, 1, 8]} />
                <meshStandardMaterial color="#6B3A2A" />
            </mesh>
            <mesh position={[0, 0, 4.5]} rotation={[0, 0, Math.PI / 4]}>
                <boxGeometry args={[1.2, 0.7, 1.5]} />
                <meshStandardMaterial color="#6B3A2A" />
            </mesh>
            <mesh position={[0, 0.6, 6]} rotation={[Math.PI / 6, 0, 0]}>
                <cylinderGeometry args={[0.04, 0.06, 3.5]} />
                <meshStandardMaterial color="#4a3728" />
            </mesh>
            <mesh position={[0, 0.2, -4.2]} rotation={[0, 0, Math.PI / 4]}>
                <boxGeometry args={[1, 0.5, 0.8]} />
                <meshStandardMaterial color="#6B3A2A" />
            </mesh>
            <mesh position={[0, 0.55, 0]}>
                <boxGeometry args={[2.2, 0.08, 7.5]} />
                <meshStandardMaterial color="#A0522D" />
            </mesh>
            <mesh position={[0, 1.1, -2.8]}>
                <boxGeometry args={[2.2, 0.8, 2.5]} />
                <meshStandardMaterial color="#5C3317" />
            </mesh>
            <mesh position={[0, 1.55, -2.8]}>
                <boxGeometry args={[2.3, 0.06, 2.6]} />
                <meshStandardMaterial color="#4a2a14" />
            </mesh>
            <mesh position={[1.15, 0.8, 0]}>
                <boxGeometry args={[0.06, 0.5, 7.5]} />
                <meshStandardMaterial color="#5C3317" />
            </mesh>
            <mesh position={[-1.15, 0.8, 0]}>
                <boxGeometry args={[0.06, 0.5, 7.5]} />
                <meshStandardMaterial color="#5C3317" />
            </mesh>

            {/* ── MASZTY ── */}
            <mesh position={[0, 3.8, 0]}>
                <cylinderGeometry args={[0.07, 0.1, 7]} />
                <meshStandardMaterial color="#4a3728" />
            </mesh>
            <mesh position={[0, 3.5, 0]} rotation={[0, 0, Math.PI / 2]}>
                <cylinderGeometry args={[0.03, 0.04, 3.5]} />
                <meshStandardMaterial color="#4a3728" />
            </mesh>
            <mesh position={[0, 5.5, 0]} rotation={[0, 0, Math.PI / 2]}>
                <cylinderGeometry args={[0.025, 0.035, 2.8]} />
                <meshStandardMaterial color="#4a3728" />
            </mesh>
            <mesh position={[0, 6.8, 0]} rotation={[0, 0, Math.PI / 2]}>
                <cylinderGeometry args={[0.02, 0.03, 2]} />
                <meshStandardMaterial color="#4a3728" />
            </mesh>
            <mesh position={[0, 3.2, 2.8]}>
                <cylinderGeometry args={[0.06, 0.09, 6]} />
                <meshStandardMaterial color="#4a3728" />
            </mesh>
            <mesh position={[0, 2.8, 2.8]} rotation={[0, 0, Math.PI / 2]}>
                <cylinderGeometry args={[0.03, 0.04, 3]} />
                <meshStandardMaterial color="#4a3728" />
            </mesh>
            <mesh position={[0, 4.5, 2.8]} rotation={[0, 0, Math.PI / 2]}>
                <cylinderGeometry args={[0.025, 0.035, 2.4]} />
                <meshStandardMaterial color="#4a3728" />
            </mesh>
            <mesh position={[0, 3, -2.5]}>
                <cylinderGeometry args={[0.05, 0.08, 5.2]} />
                <meshStandardMaterial color="#4a3728" />
            </mesh>
            <mesh position={[0, 2.5, -2.5]} rotation={[0, 0, Math.PI / 2]}>
                <cylinderGeometry args={[0.025, 0.035, 2.5]} />
                <meshStandardMaterial color="#4a3728" />
            </mesh>
            <mesh position={[0, 6.5, 0]}>
                <cylinderGeometry args={[0.3, 0.25, 0.3, 8, 1, true]} />
                <meshStandardMaterial color="#4a3728" side={THREE.DoubleSide} />
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
                            opacity={0.8}
                        />
                    </mesh>
                </>
            )}
        </group>
    );
}

// ─────────────────────────────────────────────────────────────────
// MODEL STATKU — rotacja + wybór GLB/fallback
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

    useFrame((_, delta) => {
        if (!groupRef.current) return;
        const current = groupRef.current.rotation.y;
        const target = targetRotation.current;
        const diff = target - current;
        const shortDiff = ((diff + Math.PI) % (Math.PI * 2)) - Math.PI;
        groupRef.current.rotation.y += shortDiff * Math.min(delta * 2, 1);
    });

    const hasSailsSet = shipState
        ? Object.values(shipState.sails).some((s) => s.state === "postawiony")
        : false;

    const jollyRoger = shipState?.flags?.jolly_roger ?? false;

    return (
        <group ref={groupRef}>
            <JollyRogerFlag visible={jollyRoger} />

            {hasGLB ? (
                <ErrorBoundaryFallback onError={() => setHasGLB(false)}>
                    <Suspense fallback={<FallbackShip hasSailsSet={hasSailsSet} />}>
                        <GLBModel
                            url="/models/ship_sails_up.glb"
                            visible={hasSailsSet}
                        />
                        <GLBModel
                            url="/models/ship_sails_down.glb"
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

class ErrorBoundaryFallback extends React.Component<
    ErrorBoundaryProps,
    ErrorBoundaryState
> {
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
// SCENA GŁÓWNA (eksport)
// ─────────────────────────────────────────────────────────────────

export default function ShipScene({ shipState }: ShipSceneProps) {
    const heading = shipState?.heading ?? 0;

    return (
        <div style={{ width: "100%", height: "100%", position: "relative" }}>
            {/* Kompas — HTML overlay poza Canvas */}
            <CompassOverlay heading={heading} />

            <Canvas
                camera={{ position: [30, 14, 35], fov: 35 }}
                style={{ background: "linear-gradient(180deg, #0d1f3c 0%, #0a1628 100%)" }}
            >
                <ambientLight intensity={0.5} />
                <directionalLight position={[10, 15, 5]} intensity={1.3} castShadow />
                <directionalLight
                    position={[-5, 8, -10]}
                    intensity={0.3}
                    color="#4488ff"
                />
                <hemisphereLight groundColor="#0a4a7a" intensity={0.35} />

                <fog attach="fog" args={["#0a1628", 60, 160]} />

                <Suspense fallback={null}>
                    <ShipModel shipState={shipState} />
                    <Water />
                    <OrbitControls
                        target={[0, 3, 0]}
                        minDistance={8}
                        maxDistance={120}
                        maxPolarAngle={Math.PI / 2.2}
                        minPolarAngle={0.2}
                        enableDamping
                        dampingFactor={0.08}
                    />
                </Suspense>
            </Canvas>
        </div>
    );
}
