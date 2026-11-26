# Modern Web Guidance — What Google Shipped

A skill you install into your coding agent so it writes 2026 web code instead of 2019 web code.

**Last checked:** 2026-11-26
**Method:** `developer.chrome.com/docs/modern-web-guidance` (hub), `blog/modern-web-guidance-v1` (1.0, 2026-11-10, Philip Walton), `blog/mwg-technical-deep-dive` (2026-11-12, Paul Irish). Source: `GoogleChrome/modern-web-guidance-src`.

---

## 1. What it is

An agent asked to "build an accessible dialog" will usually succeed — with a hand-rolled `div`, manual focus trapping, and a `keydown` listener. It works, and it is worse than `<dialog closedby="any">`.

Modern Web Guidance packages the review comments a senior web engineer would give you into skills a coding agent loads on demand.

> Modern Web Guidance is a set of skills that embed web platform expertise, best practices, and browser compatibility data directly into your coding agents.

**This is not a browser API.** It has no runtime presence on a page. It is a skill — a `SKILL.md` with a trigger description, plus resources loaded progressively.

Three properties make it more than a prompt pack:

| Property | Why it matters |
|---|---|
| **Curated, not scraped** | 1.7 MB of Markdown written by browser engineers and a11y specialists |
| **Baseline-aware** | Recommendations are filtered by your browser-support target |
| **Evaluated** | A public dashboard measures agent output with vs. without it |

**At a glance**

| Dimension | Detail |
|---|---|
| Version | **1.0**, 2026-11-10 (preview at I/O, May 2026) |
| Scope | 200+ guides across HTML, CSS, and Web APIs |
| Owners | Chrome **+ Firefox + Edge** (cross-browser since 1.0) |
| Distribution | npm package, installed via CLI |
| Works with | Claude Code, Codex CLI, Gemini CLI, and other agent runtimes |
| Evaluation | `goo.gle/mwg-evals` |
| Production users cited | Policybazaar, MetaMask, WeTV, note inc. |

Cross-browser ownership matters because a recommendation is only useful if it is interoperable. Built on Baseline and reviewed by three vendors, it is positioned as a *web* practice layer, not a Chrome one.

---

## 2. What the features are

### 2.1 The guide library

200+ guides covering where models measurably fail:

| Area | Where models fall short |
|---|---|
| **Accessibility** | Focus and inert management, reduced-motion, accessible validation. Bad ARIA can make a page *less* accessible than none |
| **UX** | Swipe and touch gestures, dialog and popover transitions, light/dark theming |
| **Performance** | Main-thread scheduling, offscreen rendering isolation, layout-shift prevention |
| **Security** | Sanitization, strict CSP, passkey/WebAuthn management |
| **Right platform feature** | Popover and dialog animation, scroll/swipe interactions, view transitions — instead of 200 lines of JS |
| **Conversion flows** | Passkeys for login; Autofill for checkout, where custom JS controls routinely break mobile autofill |

The recurring theme: **models default to JavaScript when HTML or CSS already does the job.**

### 2.2 Progressive disclosure

The design constraint is that 1.7 MB cannot enter a context window. Three steps:

| Stage | What the agent sees | Cost |
|---|---|---|
| At rest | Only the skill `description` | ~205 tokens |
| Frontend task | `search "<intent>"` → 10 matches | ~530 tokens |
| After choosing | `retrieve <guide-id>` → full guide | ~800 tokens |

A typical interaction stays under ~2 K tokens, almost all of it the guide actually needed.

### 2.3 Why a CLI rather than MCP or web search

- **MCP servers** either waste tokens or trigger unreliably because of dynamic tool discovery.
- **Web search** surfaces 2015 Stack Overflow answers, takes seconds, and fails offline.
- **A local CLI** runs on CPU in milliseconds, works offline, and returns curated DO / DO NOT patterns.

### 2.4 Modernization workflow (new in 1.0)

Scans existing HTML, CSS, JS, and `package.json` for safe upgrade opportunities — legacy workarounds, unnecessary dependencies, dead polyfills. Scope is honest: **static analysis over a limited pattern set**, chosen for predictable results. Agentic audits are planned.

### 2.5 The retrieval engine

Rebuilt three times in six months, and the numbers are the feature:

| Metric | Gen 1 (native ONNX) | Gen 2 (TF.js) | Gen 3 (static Int8 + BM25) |
|---|---|---|---|
| Package | 507 MB | 23.4 MB | **7.1 MB** |
| Search bundle | ~6.0 MB | 423.6 KB | **5.7 KB** |
| Cold CLI latency | ~35 ms | 770 ms | **185 ms** |
| Warm embed | ~34 ms | ~227 ms | **30 µs** |
| Search hit rate (Hit@K) | — | 80.6% | **95.4%** |

Gen 2's `all-MiniLM-L6-v2` was trained on 2018–2020 text, so its vocabulary **did not contain post-2020 APIs** — `fetchpriority` became `fetch · ##pr · ##ior · ##ity`. With a `0.38` similarity cutoff, "confirm destructive action" returned nothing, and the fallback dumped ~1,500 tokens of guide titles into context.

The fix was hybrid **BM25 + semantic** search, compact result objects, and pre-baked `gemini-embedding-001` guide vectors matched against an offline 29,165-word Int8 lookup table summed in a 7-line loop.

---

## 3. How developers use it

### 3.1 Install

```bash
npx modern-web-guidance@latest install
npx modern-web-guidance@latest update   # upgrade from an earlier version
```

### 3.2 What the agent runs

```bash
# Semantic + keyword search — 10 compact results
npx modern-web-guidance search "animate height auto"

# Pull the full guide by id
npx modern-web-guidance retrieve animate-to-intrinsic-sizes

# Optional: list all ids (costly — ~200 descriptions)
npx modern-web-guidance list
```

Results are deliberately compact after the 1.0 tuning:

```json
{"id":"dialog","description":"Build accessible modal and non-modal dialogs with native <dialog>, showModal(), and closedby."}
```

Same 530-token budget gives **10 results instead of 5**, because fields the agent was told to ignore (`similarity`, `tokenCount`, `featuresUsed`) were removed.

### 3.3 Modernize an existing codebase

```
/modern-web-guidance Modernize the code in this directory
```

### 3.4 Pair it with DevTools for agents

```
Modern Web Guidance   →  write it correctly
DevTools for agents   →  verify it in a live browser
```

Concrete example: MWG teaches how to break long tasks, but only a performance trace on a simulated low-end CPU tells you whether you got under **50 ms** — the INP-relevant threshold. Same for verifying `prefers-reduced-motion` and judging whether an animation actually looks right.

---

## 4. What value it brings

### To web users

- **Accessible by default.** The failure modes MWG targets — broken focus management, missing reduced-motion, inaccessible validation — are invisible to mouse users and blocking to everyone else.
- **Faster pages** — recommendations favour platform features over JS, so less main-thread work and fewer layout shifts.
- **Checkout and login that work on mobile**, because Autofill and passkeys are the two flows most often broken by custom JS controls.
- **Fewer legacy workarounds carried forward** — the modernization pass removes polyfills that stopped being necessary years ago.

### To developers

- **Your agent stops writing 2019 code** — the immediate, measurable effect.
- **A readable second opinion.** The guides are useful to humans too; teams use them as a learning resource, not only as agent input.
- **Token-cheap** — under ~2 K tokens per lookup versus dumping a docs index.
- **Offline and dependency-free** — no API key, no network, 30 µs warm embedding.
- **Shared vocabulary with Baseline**, so recommendations respect your support target.
- **Cross-vendor review** — Chrome, Firefox, and Edge own the same guides.

### What it costs

- **It guides, it does not verify.** Nothing proves the generated code works, is accessible in practice, or meets a performance budget. The DevTools pairing is not optional if outcomes matter.
- **Modernization is pattern-based in 1.0** and will miss things by design.
- **Quality is bounded by the agent.** Evals cover Claude Code, Codex CLI, and Gemini CLI; skill triggering is heuristic, not guaranteed.
- **Coverage is finite.** 200+ guides is not the platform — absence of a guide is not permission to write legacy code.
- **Benchmarks are self-reported.** Open and reproducible, but they measure *retrieval*, not code quality.
- **Telemetry is on by default** (opt out with `DISABLE_TELEMETRY=1`); it logs only the 2–5 word search argument, never prompts or repo code.
- **It is a moving target too** — pinning goes stale, not pinning changes behaviour between runs.
- **Not a substitute for expertise.** The announcement says so: there is still value in learning the platform.

---

## Sources

- [Modern Web Guidance — docs](https://developer.chrome.com/docs/modern-web-guidance) · [1.0 announcement](https://developer.chrome.com/blog/modern-web-guidance-v1) · [Local vector search: 507 MB → a 7-line loop](https://developer.chrome.com/blog/mwg-technical-deep-dive) · [Beyond code generation](https://developer.chrome.com/blog/beyond-code-generation)
- [Top 10 things AI gets wrong in web development](https://developer.chrome.com/blog/top-10-things-ai-gets-wrong-in-web-dev) · [Modernization workflow](https://developer.chrome.com/docs/modern-web-guidance/modernization-workflow) · [Guide index](https://developer.chrome.com/docs/modern-web-guidance/guides)
- [Source code](https://github.com/GoogleChrome/modern-web-guidance-src) · [Search quality dashboard](https://googlechrome.github.io/modern-web-guidance-src/search/) · [Eval dashboard](https://goo.gle/mwg-evals) · [DevTools for agents](https://developer.chrome.com/docs/devtools/agents) · [Baseline](https://web.dev/baseline)
