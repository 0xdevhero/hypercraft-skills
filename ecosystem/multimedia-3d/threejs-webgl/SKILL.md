---
name: threejs-webgl
description: Three.js and React Three Fiber patterns for 3D web experiences — scenes, lighting, shaders, particles, post-processing, and immersive WebGL. Use when building 3D websites, particle effects, shader animations, or immersive web experiences.

metadata:
  author: HyperCraft Core Team
  license: Apache-2.0
---

# Three.js & React Three Fiber

## When to Activate
- User wants 3D elements on a website
- User mentions Three.js, R3F, WebGL, shaders
- User wants particle effects, 3D backgrounds, or immersive scenes
- User wants creative/Awwwards-style 3D experiences

## Installation
```bash
npm install three @react-three/fiber @react-three/drei @react-three/postprocessing
```

## React Three Fiber Patterns

### 1. Basic Scene
```tsx
"use client";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Environment } from "@react-three/drei";

export function Scene3D() {
  return (
    <Canvas
      camera={{ position: [0, 0, 5], fov: 45 }}
      dpr={[1, 2]}
      gl={{ antialias: true, alpha: true }}
    >
      <ambientLight intensity={0.5} />
      <directionalLight position={[10, 10, 5]} intensity={1} />
      <mesh>
        <sphereGeometry args={[1, 64, 64]} />
        <meshStandardMaterial color="#6366f1" roughness={0.2} metalness={0.8} />
      </mesh>
      <OrbitControls enableZoom={false} autoRotate autoRotateSpeed={0.5} />
      <Environment preset="city" />
    </Canvas>
  );
}
```

### 2. Floating Particles Background
```tsx
import { useRef, useMemo } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";

function Particles({ count = 5000 }) {
  const mesh = useRef<THREE.Points>(null);
  const particles = useMemo(() => {
    const positions = new Float32Array(count * 3);
    for (let i = 0; i < count; i++) {
      positions[i * 3] = (Math.random() - 0.5) * 20;
      positions[i * 3 + 1] = (Math.random() - 0.5) * 20;
      positions[i * 3 + 2] = (Math.random() - 0.5) * 20;
    }
    return { positions };
  }, [count]);

  useFrame((state) => {
    if (!mesh.current) return;
    mesh.current.rotation.y = state.clock.elapsedTime * 0.05;
    mesh.current.rotation.x = state.clock.elapsedTime * 0.02;
  });

  return (
    <points ref={mesh}>
      <bufferGeometry>
        <bufferAttribute attach="attributes-position" array={particles.positions} count={count} itemSize={3} />
      </bufferGeometry>
      <pointsMaterial size={0.02} color="#6366f1" transparent opacity={0.6} sizeAttenuation depthWrite={false} />
    </points>
  );
}
```

### 3. Gradient Sphere with Custom Shader
```tsx
import { shaderMaterial } from "@react-three/drei";
import { extend } from "@react-three/fiber";

const GradientMaterial = shaderMaterial(
  { uTime: 0, uColor1: new THREE.Color("#6366f1"), uColor2: new THREE.Color("#ec4899") },
  `varying vec2 vUv;
   uniform float uTime;
   void main() {
     vUv = uv;
     vec3 pos = position + normal * sin(position.y * 4.0 + uTime) * 0.05;
     gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
   }`,
  `uniform vec3 uColor1;
   uniform vec3 uColor2;
   uniform float uTime;
   varying vec2 vUv;
   void main() {
     vec3 color = mix(uColor1, uColor2, vUv.y + sin(uTime * 0.5) * 0.2);
     gl_FragColor = vec4(color, 1.0);
   }`
);
extend({ GradientMaterial });
```

### 4. Post-Processing
```tsx
import { EffectComposer, Bloom, Noise, Vignette } from "@react-three/postprocessing";

<Canvas>
  <EffectComposer>
    <Bloom intensity={1.5} luminanceThreshold={0.2} luminanceSmoothing={0.9} />
    <Noise opacity={0.02} />
    <Vignette eskil={false} offset={0.1} darkness={0.5} />
  </EffectComposer>
</Canvas>
```

### 5. 3D Text
```tsx
import { Text3D, Center } from "@react-three/drei";

<Center>
  <Text3D font="/fonts/Inter_Bold.json" size={1.5} height={0.2} bevelEnabled bevelThickness={0.02} bevelSize={0.02}>
    HELLO
    <meshStandardMaterial color="#6366f1" metalness={0.8} roughness={0.2} />
  </Text3D>
</Center>
```

### 6. Drei Helpers
```tsx
import { Float, MeshDistortMaterial, Sparkles, Stars, ScrollControls } from "@react-three/drei";

<Float speed={1.5} rotationIntensity={0.5} floatIntensity={1}>
  <mesh>
    <torusGeometry args={[1, 0.4, 32, 64]} />
    <MeshDistortMaterial color="#6366f1" distort={0.3} speed={2} />
  </mesh>
</Float>
```

## Next.js Integration
```tsx
"use client";
import dynamic from "next/dynamic";

const Scene3D = dynamic(() => import("./Scene3D"), {
  ssr: false,
  loading: () => <div className="h-screen bg-black" />,
});
```

## Performance Rules
1. Use `dpr={[1, 2]}` — adaptive pixel ratio
2. Dispose geometries and materials on unmount
3. Use instanced meshes for repeated objects
4. Keep poly count low
5. Lazy load 3D scenes with `next/dynamic` (ssr: false)

