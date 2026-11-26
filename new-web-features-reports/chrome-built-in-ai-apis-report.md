# Chrome Built-in AI APIs — What Google Shipped

On-device models behind browser APIs: summarize, translate, proofread, prompt, and embed without an API key.

**Last checked:** 2026-11-26
**Method:** Primary sources only — `developer.chrome.com/docs/ai/*`, the Chrome AI Dev Preview Google Group, `chromestatus.com`, and WICG/explainer repos where no docs page exists. Where the docs contradict the EPP group, both readings are recorded.

---

## 1. What it is

Chrome ships a small language model **inside the browser**. A page calls a JavaScript API; inference runs on the user's device; nothing is uploaded and no API key is needed.

The model stack in 2026:

| Layer | Model | Status |
|---|---|---|
| Default | **Gemini Nano** | Stable |
| Experimental | **Gemma 4** | Dev Trial since 2026-08-25 — up to **+70% tok/s** |
| Task-specialised | Expert models for Summarizer and Proofreader | Developer preview since 2026-06-04 |
| Embedding | `embeddinggemma-300m` | Dev Trial since 2026-07-16 |

**Why it matters architecturally:** the privacy story is structural, not a policy promise — the text never leaves the device. The cost story is the same: no per-token billing.

**Why it is hard:** model download is hundreds of MB, capability depends on hardware, and the API surface has changed repeatedly. Every API is gated behind availability checks and quotas.

**At a glance**

| API | What it does | Status |
|---|---|---|
| **Prompt** | General-purpose `LanguageModel` session | **Stable — Chrome 148** (I/O 2026) |
| **Summarizer** | Condense long text | Stable |
| **Translator** | On-device translation | Stable |
| **Language Detector** | Identify source language | Stable |
| **Proofreader** | Grammar and spelling correction | Developer trial |
| **Embedding** | Text vectors for semantic search | Dev Trial (2026-07-16) |
| **Writer / Rewriter** | Tone and length rewriting | **Deprecated** |
| **Decisions** | Classify into pre-set labels | Intent to Prototype |
| **MTP** | Faster decode for Gemma 4 | Flag — not an API |

---

## 2. What the features are

### 2.1 Prompt API — the general model

`LanguageModel` is the base capability; every other text API is effectively a constrained wrapper around the same session model.

- **Availability-aware** — `LanguageModel.availability()` returns whether the model is ready, downloadable, or unavailable.
- **Sessions** — `create()` with `initialPrompts` (system role), `expectedInputs`/`expectedOutputs` for language hints, and `monitor` for download progress.
- **Streaming** — `promptStreaming()` yields chunks, so UI starts rendering before the answer finishes.
- **Multimodal input** — text plus images (and audio, where available).
- **Quotas** — per-session token limits, with a `contextoverflow` path when you exceed them.

**Sampling changed.** `params()`, `topK`, and `temperature` were **deprecated 2026-02-17** and moved to an origin trial; named presets are proposed (2026-06-11). Code written against the old surface will break.

### 2.2 Summarizer

- **Types:** `key-points`, `tl;dr`, `teaser`, `headline`.
- **Lengths:** `short`, `medium`, `long`.
- **Formats:** plain text, Markdown.
- **Context:** `context` (this document) plus `sharedContext` (background that persists across calls).
- **Streaming** — `summarizeStreaming()`.
- **Expert models** — a specialist summarizer available as a developer preview, plus `preference: 'speed'` (2026-06-04) to trade quality for latency.

### 2.3 Translator

- **Language pairs** declared at creation; `Translator.availability({ sourceLanguage, targetLanguage })` tells you if the pair is downloadable.
- **Streaming** translation for long text.
- Download is substantial — show progress, don't assume instant readiness.

### 2.4 Proofreader

- Returns `correctedInput` plus a `corrections` array.
- **`correctionExplanation`** — per-correction rationale, which is what makes it usable in an editor rather than as a black-box rewrite.
- An expert proofreader model is in developer preview.

### 2.5 Embedding

Turns text into vectors for semantic search, clustering, and deduplication — on device, with no vector service.

- Model: `embeddinggemma-300m`.
- Requires Canary > 152 and `chrome://flags/#semantic-embedder-api`.
- **Note:** `chromestatus` still says "Proposed" and `/docs/ai/embedding-api` still 404s. The Dev Trial post is the current source of truth.

### 2.6 Decisions — "Semantic If"

`DecisionModel.create({ context, questions })` plus `decide(text)` returns `{ label, confidence }` per question.

- **Does not generate text** — it scores pre-defined options, so it structurally cannot emit a label you did not define.
- **Latency** is tens to ~200 ms: a single forward pass, no token generation.
- Fits the gap between "an LLM is too heavy" and "regex is too brittle".

### 2.7 Writer and Rewriter — deprecated

The EPP group announced retirement on **2026-09-23**: least-used APIs, and tone is too subjective to express well in WebIDL. The consultation on migration blockers closed **2026-10-23**, after which the code is removed. Migrate to `window.LanguageModel` with userland prompt templates.

### 2.8 MTP — not an API

Multi-Token Prediction pairs Gemma 4 with a lightweight drafter model that proposes tokens in parallel for parallel verification, bypassing serial decode.

- **+20–30% warm decode throughput**: +20% on discrete GPUs, +30% on integrated.
- Largest gain on **JSON structured output**.
- Canary only; `chrome://flags/#on-device-model-speculative-decoding`.
- **Greedy decoding only** — Summarizer sessions qualify automatically; Prompt requires `samplingMode: 'most-predictable'`.
- Trade-off: reduced output diversity.

---

## 3. How developers use it

### 3.1 Always check availability first

```js
const availability = await LanguageModel.availability();
// "unavailable" | "downloadable" | "downloading" | "available"
if (availability === "unavailable") {
  return fallbackToServer();
}
```

### 3.2 Prompt with streaming

```js
const session = await LanguageModel.create({
  initialPrompts: [
    { role: "system", content: "You are a concise accessibility reviewer." },
  ],
  expectedInputs: [{ type: "text", languages: ["en"] }],
  expectedOutputs: [{ type: "text", languages: ["en"] }],
});

for await (const chunk of session.promptStreaming("Audit this markup: …")) {
  output.textContent += chunk;
}

await session.destroy();
```

### 3.3 Summarize a document

```js
const summarizer = await Summarizer.create({
  type: "key-points",
  length: "short",
  format: "markdown",
  sharedContext: "Release notes for a web framework.",
});

const summary = await summarizer.summarize(longText, {
  context: "Summarize for a developer audience.",
});
```

### 3.4 Translate with progress

```js
const pair = { sourceLanguage: "en", targetLanguage: "zh" };
const status = await Translator.availability(pair);

if (status !== "available") {
  const translator = await Translator.create({
    ...pair,
    monitor(m) {
      m.addEventListener("downloadprogress", (e) => {
        progress.value = e.loaded;   // 0 → 1
      });
    },
  });
}

const translator = await Translator.create(pair);
for await (const chunk of translator.translateStreaming(text)) {
  output.textContent += chunk;
}
```

### 3.5 Proofread with explanations

```js
const proofreader = await Proofreader.create({
  expectedInputLanguages: ["en"],
  includeCorrectionExplanation: true,
});

const { correctedInput, corrections } = await proofreader.proofread(input.value);
for (const c of corrections) {
  console.log(`${c.startIndex}-${c.endIndex}: ${c.correction} — ${c.explanation}`);
}
```

### 3.6 Embed and rank

```js
// API shape is still in Dev Trial — verify against the flag before shipping.
const embedder = await ai.embedder.create({ model: "embeddinggemma-300m" });
const [query, ...docs] = await embedder.embed([q, ...corpus]);

const cosine = (a, b) => a.reduce((s, v, i) => s + v * b[i], 0);
const ranked = docs
  .map((v, i) => ({ i, score: cosine(query, v) }))
  .sort((x, y) => y.score - x.score);
```

### 3.7 Classify without generating

```js
const decision = await DecisionModel.create({
  context: "You triage an e-commerce support inbox.",
  questions: [
    { question: "Is this a refund request?", options: ["yes", "no"] },
  ],
});

const [{ label, confidence }] = await decision.decide(emailBody);
if (label === "yes" && confidence > 0.8) routeToRefunds();
```

### 3.8 Opt into speculative decoding

```js
// Summarizer: automatic.
// Prompt API: greedy decoding is required for MTP to apply.
const session = await LanguageModel.create({ samplingMode: "most-predictable" });
```

---

## 4. What value it brings

### To web users

- **Their text never leaves the device** — a structural privacy guarantee, not a policy.
- **Works offline** once the model is downloaded.
- **Zero latency to a server** — no round trip, no region routing.
- **Free features** — summarise, translate, and proofread without a subscription or a metered API.
- **Text they can read at their reading level** — summarisation and translation become ambient.

### To developers

- **No API key, no billing, no backend** — the biggest adoption barrier for AI features disappears.
- **One model, many constrained APIs** — Summarizer and Proofreader encode the prompts so you don't have to.
- **Streaming everywhere**, so UI feels instant.
- **A standards effort, not a vendor SDK** — the same APIs are discussed in W3C/WICG, and other browsers have implementations.
- **Predictable classification** via Decisions, without prompt-engineering a parser.

### What it costs

- **Availability is conditional.** Hardware, disk, and download state all gate the API; every call path needs a fallback.
- **The surface is unstable.** Sampling parameters were deprecated in February and moved to an origin trial; Writer and Rewriter are being **removed**; Embedding and Decisions are still pre-stable.
- **Docs lag the reality by up to 14 months** in places — Embedding is testable in Canary while `chromestatus` and the docs index still describe it as proposed.
- **Quotas are small** compared with server models; long documents need chunking.
- **Download size** is a real UX cost on metered connections.
- **Output quality is model-bound** to Gemini Nano/Gemma 4 on-device — good enough for summarising and classification, not for open-ended reasoning.
- **`params()`, `topK`, and `temperature` no longer work** as documented in most tutorials still online.

---

## Sources

- [Built-in AI APIs — status table](https://developer.chrome.com/docs/ai/built-in-apis) · [Prompt API](https://developer.chrome.com/docs/ai/prompt-api) · [Summarizer API](https://developer.chrome.com/docs/ai/summarizer-api) · [Translator API](https://developer.chrome.com/docs/ai/translator-api) · [Proofreader API](https://developer.chrome.com/docs/ai/proofreader-api)
- EPP: [Prompt API ships to Stable (I/O 2026)](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview/c/J3gcIdxjvxs) · [Embedding API Dev Trial](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview/c/LYsU9EtJxsA) · [Gemma 4](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview/c/n_on_1E2_aA) · [Expert models](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview/c/AYX1UIHYjec) · [Writer/Rewriter deprecation](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview/c/5eJGK6nxGdc) · [Sampling → presets](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview/c/fbJsJjPM4hE) · [MTP](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview/c/M4Ozq6VtB_Y) · [Decisions API](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview/c/8zr8ILiTKEc)
- [chrome-status entries](https://chromestatus.com/features) · [Built-in AI: Do and Don't](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview/c/9aiMP5U4TU4)
