# WebGPU — What Google Shipped

A modern GPU API for the web: compute shaders and rendering, with near-native performance.

**Last checked:** 2026-11-26
**Method:** Chrome's `What's New in WebGPU` changelog series (latest edition: Chrome 155–156, 2026-10-15) and the linked `Intent to Ship` threads. Note that `/docs/web-platform/webgpu` renders an empty index — the changelog is the authoritative source.

---

## 1. What it is

WebGPU is a JavaScript API plus the **WGSL** shading language that expose the GPU directly — compute and rendering — through an explicit object model instead of WebGL's global state machine.

| | WebGL 2 | WebGPU |
|---|---|---|
| Model | Global state machine | Explicit: adapter → device → pipelines → command buffers |
| Shaders | GLSL ES 3.0 | **WGSL** — statically typed, validated, better errors |
| Compute | None (transform-feedback hacks) | **First-class compute shaders** |
| Backend | OpenGL / ES | Vulkan, Metal, D3D12 (via **Dawn**) |
| Threading | Main thread only | Command encoding off the main thread |
| Validation | Loose | Strict, ahead-of-time pipeline validation |

**Dawn** is Chrome's cross-platform implementation (Vulkan / Metal / D3D12 / OpenGL ES). Its change log is the real record of what landed when — which is why every changelog edition ends with "Dawn updates".

**Compatibility mode** is the reach feature: a deliberately reduced feature level that runs on **OpenGL ES 3.1**-class hardware, opted into per device. It is how WebGPU gets to older phones without forking the API.

**At a glance**

| Platform | Available from |
|---|---|
| Windows, macOS, ChromeOS | Chrome 113 (2023) |
| Android 12+ | Chrome 121 |
| Linux | Chrome 144 |
| Linux + NVIDIA proprietary drivers | Chrome 147–148 |

Feature availability is **adapter-dependent** by design: `shader-f16`, subgroups, and compressed formats are all optional and must be feature-detected.

---

## 2. What the features are

### 2.1 Core capability

- **Compute.** Real GPGPU — image processing, physics, particle systems, ML preprocessing — without WebGL gymnastics.
- **Render pipelines.** Vertex/fragment stages, explicit bind groups, render passes with `loadOp`/`storeOp`.
- **Async pipeline compilation.** `createComputePipelineAsync` / `createRenderPipelineAsync` compile off the main thread.
- **Queryable limits and features.** `adapter.features`, `adapter.limits`, and per-device requests.
- **Useful shader diagnostics.** `shader.getCompilationInfo()` returns typed messages with line and column.
- **Device loss handling.** `device.lost` is a promise — driver updates, backgrounding, and GPU resets all trigger it.

### 2.2 Feature trajectory, 2025 → 2026

| Chrome | Highlights |
|---|---|
| **155–156** | WGSL `fragment_depth` (early-Z with custom depth); `texture-compression-unaligned`; `srgb-linear` + `display-p3-linear`; `snorm10-10-10-2`; `shader-f16` on Linux NVIDIA |
| **153–154** | WGSL `buffer_view` (safe type-punning); `swizzle_assignment` |
| **151–152** | **Subgroup size control** (`@subgroup_size`) for compute — aimed at AI workloads |
| **149–150** | **Immediates** (push-constant-style small data) |
| **147–148** | WGSL `linear_indexing`; **WebGPU on Linux NVIDIA** |
| **146** | **Compatibility mode on OpenGL ES 3.1**; transient attachments |
| **145** | `subgroup_uniformity`; experimental synchronous buffer mapping in workers |
| **144** | **WebGPU on Linux**; `subgroup_id`; `uniform_buffer_standard_layout` |
| **143** | Texture component swizzle; `bgra8unorm` read-only storage removed (breaking) |
| **142** | Extended texture formats; primitive index in WGSL |
| **141** | Tint IR completed; integer range analysis; SPIR-V 1.4 |
| **140** | Device requests **consume** the adapter (breaking); `isFallbackAdapter` removed (breaking) |
| **139** | Compatibility-mode origin trial; `core-features-and-limits`; 3D BC/ASTC textures |

**Three themes:** compute maturity for on-device ML (subgroups, immediates), WGSL ergonomics (`buffer_view`, `swizzle_assignment`, `linear_indexing`, `fragment_depth`), and reach (Linux, NVIDIA, compatibility mode).

### 2.3 The core model

Five steps, every time:

1. `navigator.gpu.requestAdapter()` — pick a GPU.
2. `adapter.requestDevice()` — get a device; request features and limits here.
3. Create resources — buffers, textures, shader modules, pipelines, bind groups.
4. Encode — `createCommandEncoder()`, passes, `finish()`.
5. Submit — `device.queue.submit([commandBuffer])`.

Two rules that trip people up: **pipeline creation is async** (use the async variants in production), and **bind groups are explicit** — you lay out `@group(n) @binding(m)` and build the matching `GPUBindGroup` yourself.

---

## 3. How developers use it

### 3.1 Initialise with feature detection

```js
if (!navigator.gpu) throw new Error("WebGPU is not supported.");

const adapter = await navigator.gpu.requestAdapter();
if (!adapter) throw new Error("No suitable GPU adapter found.");

const requiredFeatures = [];
if (adapter.features.has("shader-f16")) requiredFeatures.push("shader-f16");
if (adapter.features.has("texture-compression-unaligned")) {
  requiredFeatures.push("texture-compression-unaligned");
}

const device = await adapter.requestDevice({ requiredFeatures });

device.lost.then((info) => {
  console.error(`GPU device lost: ${info.reason} — ${info.message}`);
});
```

### 3.2 A compute shader, end to end

```js
const shader = device.createShaderModule({
  code: /* wgsl */ `
    @group(0) @binding(0) var<storage, read>       input  : array<f32>;
    @group(0) @binding(1) var<storage, read_write> output : array<f32>;

    @compute @workgroup_size(64)
    fn main(@builtin(global_invocation_id) id : vec3u) {
      let i = id.x;
      if (i >= arrayLength(&input)) { return; }
      output[i] = input[i] * 2.0;
    }
  `,
});

const N = 1024, byteSize = N * 4;

const inputBuffer = device.createBuffer({
  size: byteSize,
  usage: GPUBufferUsage.STORAGE | GPUBufferUsage.COPY_DST,
});
const outputBuffer = device.createBuffer({
  size: byteSize,
  usage: GPUBufferUsage.STORAGE | GPUBufferUsage.COPY_SRC,
});
const readback = device.createBuffer({
  size: byteSize,
  usage: GPUBufferUsage.COPY_DST | GPUBufferUsage.MAP_READ,
});

device.queue.writeBuffer(inputBuffer, 0, new Float32Array(N).fill(1.5));

const pipeline = await device.createComputePipelineAsync({
  layout: "auto",
  compute: { module: shader, entryPoint: "main" },
});

const bindGroup = device.createBindGroup({
  layout: pipeline.getBindGroupLayout(0),
  entries: [
    { binding: 0, resource: { buffer: inputBuffer } },
    { binding: 1, resource: { buffer: outputBuffer } },
  ],
});

const encoder = device.createCommandEncoder();
const pass = encoder.beginComputePass();
pass.setPipeline(pipeline);
pass.setBindGroup(0, bindGroup);
pass.dispatchWorkgroups(Math.ceil(N / 64));
pass.end();
encoder.copyBufferToBuffer(outputBuffer, 0, readback, 0, byteSize);
device.queue.submit([encoder.finish()]);

await readback.mapAsync(GPUMapMode.READ);
console.log(new Float32Array(readback.getMappedRange())[0]); // 3
readback.unmap();
```

### 3.3 The render path

```js
const context = canvas.getContext("webgpu");
const format = navigator.gpu.getPreferredCanvasFormat();
context.configure({ device, format, alphaMode: "premultiplied" });

const renderPipeline = await device.createRenderPipelineAsync({
  layout: "auto",
  vertex:   { module: shader, entryPoint: "vs" },
  fragment: { module: shader, entryPoint: "fs", targets: [{ format }] },
  primitive: { topology: "triangle-list" },
});

function frame() {
  const encoder = device.createCommandEncoder();
  const pass = encoder.beginRenderPass({
    colorAttachments: [{
      view: context.getCurrentTexture().createView(),
      clearValue: { r: 0, g: 0, b: 0, a: 1 },
      loadOp: "clear",
      storeOp: "store",
    }],
  });
  pass.setPipeline(renderPipeline);
  pass.draw(3);
  pass.end();
  device.queue.submit([encoder.finish()]);
  requestAnimationFrame(frame);
}
frame();
```

### 3.4 Wide gamut and older hardware

```js
// Linear wide-gamut output (Chrome 155–156)
context.configure({
  device,
  format: "rgba16float",
  colorSpace: "display-p3-linear",
});

// Compatibility mode: the OpenGL ES 3.1-class feature level
const compatAdapter = await navigator.gpu.requestAdapter({
  featureLevel: "compatibility",
});
```

### 3.5 Debug shaders

```js
const info = await shader.getCompilationInfo();
for (const msg of info.messages) {
  console.log(`${msg.type} at ${msg.lineNum}:${msg.linePos} — ${msg.message}`);
}
```

---

## 4. What value it brings

### To web users

- **Desktop-class graphics in a tab** — games, CAD, video editors, 3D configurators without an install.
- **On-device AI that doesn't upload data** — compute shaders plus subgroup control make local inference practical.
- **Better battery behaviour than a naive WebGL fallback**, because the API exposes real capabilities instead of hiding them.
- **Reaches older phones** — compatibility mode means "WebGPU app" no longer implies "recent flagship".
- **HDR and wide-gamut output** that matches modern displays.

### To developers

- **One API across Vulkan, Metal, and D3D12** — Dawn handles the platform differences.
- **Genuine GPGPU** — compute without WebGL workarounds.
- **Predictable performance** — explicit pipelines, bind groups, and synchronisation; no driver guesswork.
- **Debuggable shaders** — strict validation and `getCompilationInfo()` beat debugging GLSL blind.
- **Threading** — command encoding can leave the main thread, so heavy scenes don't jank the page.
- **Real ecosystem** — Babylon.js, Three.js `WebGPURenderer`, PlayCanvas, TensorFlow.js.

### What it costs

- **Nearly every interesting feature is optional.** `shader-f16`, subgroups, and compressed formats are adapter capabilities; there is no guaranteed baseline. Feature-detect or fall back.
- **The API still breaks.** Chrome 140 made device requests **consume** the adapter, breaking code that reused one, and removed `GPUAdapter.isFallbackAdapter`.
- **Compatibility mode is a subset.** The heaviest ML workloads generally need the full feature level.
- **WebGL is not going away** — compatibility mode exists precisely because full WebGPU is unreachable for a slice of devices.
- **Docs are fragmented.** The docs hub is empty; content lives in the changelog series and `webgpu-samples`. Blog version numbers are Chrome milestones, not WebGPU spec versions.
- **`device.lost` is normal**, not exceptional — handle it as a first-class state.

---

## Sources

- [What's New in WebGPU (Chrome 155–156)](https://developer.chrome.com/blog/new-in-webgpu-155-156) · [153–154](https://developer.chrome.com/blog/new-in-webgpu-153-154) · [151–152](https://developer.chrome.com/blog/new-in-webgpu-151-152) · [149–150](https://developer.chrome.com/blog/new-in-webgpu-149-150)
- [Series index](https://developer.chrome.com/docs/web-platform/webgpu/news) · [WebGPU samples](https://github.com/webgpu/webgpu-samples) · [Dawn](https://dawn.googlesource.com/dawn)
- [Intent to Ship: WGSL fragment_depth](https://groups.google.com/a/chromium.org/g/blink-dev/c/sS8f4X1SEkk/m/v7fWPbr-DgAJ) · [texture-compression-unaligned](https://groups.google.com/a/chromium.org/g/blink-dev/c/Hp-KNpz1iK4) · [srgb-linear / display-p3-linear](https://groups.google.com/a/chromium.org/g/blink-dev/c/MoKhf3DLhQM/m/41Asvc44CQAJ)
