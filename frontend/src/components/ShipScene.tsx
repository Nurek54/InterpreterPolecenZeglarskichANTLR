import { useRef, useMemo, useEffect, Suspense, useState } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls, useGLTF, Html } from "@react-three/drei";
import * as THREE from "three";
import type { ShipState } from "../types/ship";

// ─────────────────────────────────────────────────────────────────
// PROPS
// ─────────────────────────────────────────────────────────────────

interface ShipSceneProps {
  shipState: ShipState | null;
}

interface ShipModelProps {
  shipState: ShipState | null;
}

interface CompassHUDProps {
  heading: number;
}

interface JollyRogerFlagProps {
  visible: boolean;
}

interface FallbackShipProps {
  hasSailsSet: boolean;
}

interface GLBModelProps {
  url: string;
  visible: boolean;
}

// ─────────────────────────────────────────────────────────────────
// WODA — animowana płaszczyzna
// ─────────────────────────────────────────────────────────────────

function Water() {
  const meshRef = useRef<THREE.Mesh>(null);
  const geometry = useMemo(
    () => new THREE.PlaneGeometry(200, 200, 64, 64),
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
        Math.sin(x * 0.1 + time * 0.8) * 0.3 +
        Math.sin(y * 0.15 + time * 0.6) * 0.2;
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
// KOMPAS HUD
// ─────────────────────────────────────────────────────────────────

function CompassHUD({ heading }: CompassHUDProps) {
  return (
    <Html position={[0, 8, 0]} center style={{ pointerEvents: "none" }}>
      <div
        style={{
          background: "rgba(0,0,0,0.7)",
          color: "#ffd700",
          padding: "6px 14px",
          borderRadius: "8px",
          fontFamily: "JetBrains Mono, monospace",
          fontSize: "14px",
          fontWeight: "bold",
          border: "1px solid #ffd700",
          whiteSpace: "nowrap",
        }}
      >
        🧭 {heading.toFixed(0)}°
      </div>
    </Html>
  );
}

// ─────────────────────────────────────────────────────────────────
// FLAGA JOLLY ROGER
// ─────────────────────────────────────────────────────────────────

function JollyRogerFlag({ visible }: JollyRogerFlagProps) {
  const ref = useRef<THREE.Group>(null);

  useFrame(({ clock }) => {
    if (ref.current && visible) {
      ref.current.rotation.y = Math.sin(clock.getElapsedTime() * 2) * 0.1;
    }
  });

  if (!visible) return null;

  return (
    <group ref={ref} position={[0, 6.5, 0]}>
      {/* Drzewce */}
      <mesh position={[0, 0.5, 0]}>
        <cylinderGeometry args={[0.02, 0.02, 1.5]} />
        <meshStandardMaterial color="#4a3728" />
      </mesh>
      {/* Flaga */}
      <mesh position={[0.4, 0.8, 0]}>
        <planeGeometry args={[0.8, 0.5]} />
        <meshStandardMaterial color="#111" side={THREE.DoubleSide} />
      </mesh>
      {/* Czaszka */}
      <mesh position={[0.4, 0.8, 0.01]}>
        <circleGeometry args={[0.1, 16]} />
        <meshStandardMaterial color="#fff" />
      </mesh>
    </group>
  );
}

// ─────────────────────────────────────────────────────────────────
// ŁADOWANIE MODELU GLB (osobny komponent — łapie błędy)
// ─────────────────────────────────────────────────────────────────

function GLBModel({ url, visible }: GLBModelProps) {
  const { scene } = useGLTF(url);
  const cloned = useMemo(() => scene.clone(), [scene]);

  return <primitive object={cloned} visible={visible} scale={1} />;
}

// ─────────────────────────────────────────────────────────────────
// FALLBACK — prosty statek z prymitywów (gdy brak GLB)
// ─────────────────────────────────────────────────────────────────

function FallbackShip({ hasSailsSet }: FallbackShipProps) {
  return (
    <group>
      {/* Kadłub */}
      <mesh position={[0, 0, 0]}>
        <boxGeometry args={[2, 0.8, 6]} />
        <meshStandardMaterial color="#8B4513" />
      </mesh>
      {/* Dziób */}
      <mesh position={[0, 0, 3.5]} rotation={[0, 0, Math.PI / 4]}>
        <boxGeometry args={[1, 0.6, 1]} />
        <meshStandardMaterial color="#8B4513" />
      </mesh>
      {/* Pokład */}
      <mesh position={[0, 0.45, 0]}>
        <boxGeometry args={[1.8, 0.1, 5.5]} />
        <meshStandardMaterial color="#A0522D" />
      </mesh>
      {/* Maszt główny */}
      <mesh position={[0, 3, 0]}>
        <cylinderGeometry args={[0.06, 0.08, 5.5]} />
        <meshStandardMaterial color="#654321" />
      </mesh>
      {/* Maszt przedni */}
      <mesh position={[0, 2.5, 2]}>
        <cylinderGeometry args={[0.05, 0.07, 4.5]} />
        <meshStandardMaterial color="#654321" />
      </mesh>

      {/* Żagle — widoczne tylko gdy postawione */}
      {hasSailsSet && (
        <>
          {/* Grot */}
          <mesh position={[0.5, 3.5, 0]}>
            <planeGeometry args={[2, 3]} />
            <meshStandardMaterial
              color="#f5f0e0"
              side={THREE.DoubleSide}
              transparent
              opacity={0.9}
            />
          </mesh>
          {/* Fok */}
          <mesh position={[0.4, 3, 2]}>
            <planeGeometry args={[1.5, 2.5]} />
            <meshStandardMaterial
              color="#f5f0e0"
              side={THREE.DoubleSide}
              transparent
              opacity={0.9}
            />
          </mesh>
        </>
      )}

      {/* Nadbudówka rufowa */}
      <mesh position={[0, 0.9, -2]}>
        <boxGeometry args={[1.6, 0.8, 1.5]} />
        <meshStandardMaterial color="#6B3A2A" />
      </mesh>
    </group>
  );
}

// ─────────────────────────────────────────────────────────────────
// MODEL STATKU — rotacja + wybór modelu
// ─────────────────────────────────────────────────────────────────

function ShipModel({ shipState }: ShipModelProps) {
  const groupRef = useRef<THREE.Group>(null);
  const targetRotation = useRef(0);
  const [hasGLB, setHasGLB] = useState(true);

  // Docelowa rotacja z heading
  useEffect(() => {
    if (shipState) {
      targetRotation.current = -(shipState.heading * Math.PI) / 180;
    }
  }, [shipState?.heading]);

  // Płynna animacja obrotu (lerp)
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
  const heading = shipState?.heading ?? 0;

  return (
    <group ref={groupRef}>
      <CompassHUD heading={heading} />
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
// ERROR BOUNDARY — łapie błędy ładowania GLB
// ─────────────────────────────────────────────────────────────────

import React from "react";

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
  return (
    <Canvas
      camera={{ position: [8, 6, 12], fov: 50 }}
      style={{ background: "#0a1628" }}
    >
      <ambientLight intensity={0.4} />
      <directionalLight position={[10, 15, 5]} intensity={1.2} castShadow />
      <directionalLight
        position={[-5, 8, -10]}
        intensity={0.3}
        color="#4488ff"
      />
      <hemisphereLight
        groundColor="#0a4a7a"
        intensity={0.3}
      />

      <fog attach="fog" args={["#0a1628", 30, 80]} />

      <Suspense fallback={null}>
        <ShipModel shipState={shipState} />
        <Water />
        <OrbitControls
          target={[0, 2, 0]}
          minDistance={5}
          maxDistance={40}
          maxPolarAngle={Math.PI / 2.1}
        />
      </Suspense>
    </Canvas>
  );
}
