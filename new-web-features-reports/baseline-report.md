# Baseline — What Google Shipped

A single shared definition of "this web feature is safe to use".

**Last checked:** 2026-11-26
**Method:** `web.dev/baseline` (hub), `web.dev/blog/baseline-alerts` (2026-06-25), `web.dev/articles/how-to-choose-your-baseline-target`, `web.dev/articles/use-baseline-with-browserslist`, `web.dev/blog/show-baseline-status`, plus `web-platform-dx/web-features` and `webstatus.dev`.

---

## 1. What it is

Baseline is not a technology. It is a **shared vocabulary** for browser support, replacing per-browser version tables with two states.

Before Baseline, "can I use this?" had no stable answer: Can I Use gave version tables, MDN gave compatibility tables, and every team invented a policy. Baseline collapses that into one signal that MDN, Can I Use, web.dev, and your build tooling all read from the same source.

| Status | Definition | Practical meaning |
|---|---|---|
| **Limited availability** | Not yet in all core browsers | Don't ship without a fallback |
| **Newly available** | Supported in **all** core browsers | Interoperable — but recent; consider fallbacks |
| **Widely available** | Newly available **≥ 30 months** ago | Safe default for most sites |

**Core browser set:** Chrome, Edge, Firefox, Safari — desktop and mobile. Other Chromium browsers are *downstream* and must be opted into explicitly.

**Governance:** the **W3C WebDX Community Group**. Data lives in the `web-features` repository; every other surface is a reader of it.

**At a glance**

| Dimension | Detail |
|---|---|
| Introduced | 2023, by the WebDX CG |
| Maintainers | Multi-vendor community group; Chrome builds much of the tooling |
| Data source | `web-platform-dx/web-features` |
| Surfaces | MDN, Can I Use, webstatus.dev, web.dev, your toolchain |
| Enforcement | Browserslist queries consumed by Babel, postcss, Autoprefixer, stylelint, webpack |

---

## 2. What the features are

### 2.1 Targets — the feature sets you choose between

**Moving targets** evolve as browsers ship:

- `baseline widely available` — everything ≥ 30 months interoperable
- `baseline newly available` — everything interoperable today

**Fixed targets** are frozen calendar snapshots:

- `baseline 2023`, `baseline 2024`, … — features that became Newly available during that year
- Never change, which is the point (and why they go stale)

Guidance: **Widely available is the right default**; drop to a fixed year only when analytics say your users are behind; raise to Newly available when you control both ends of the deployment.

### 2.2 Integration surfaces

| Surface | What you get |
|---|---|
| **MDN** | Baseline badge on every reference page |
| **Can I Use** | Baseline status beside the version table |
| **webstatus.dev** | Searchable dashboard, per-feature pages, **Baseline Alerts** (2026) |
| **web.dev** | `<baseline-status>` component, annual targets |
| **Your toolchain** | Browserslist queries → compiler, linter, bundler |
| **Your analytics** | `baseline-browser-mapping` joins your RUM data to Baseline |

### 2.3 Baseline Alerts (June 2026)

Subscribe on webstatus.dev to a feature, a saved search, or the whole catalogue. Triggers:

- Becomes **Widely available**
- Becomes **Newly available**
- Gets a **new browser implementation**
- **Regresses** to limited availability

Delivery: email, RSS, or Slack webhook; frequency monthly, weekly, or every change. Requires a GitHub sign-in.

---

## 3. How developers use it

### 3.1 Declare a target once

Because Browserslist is the shared config point for the front-end toolchain, one line propagates everywhere:

```json
{
  "browserslist": [
    "baseline widely available"
  ]
}
```

Other valid queries:

```jsonc
"browserslist": "baseline newly available"
"browserslist": "baseline 2024"                              // fixed year
"browserslist": "baseline widely available with downstream"  // incl. Chromium derivatives
```

Years from `baseline 2015` through the current year are accepted.

### 3.2 It changes your build output

```json
{
  "presets": [
    ["@babel/preset-env", { "targets": { "browsers": "baseline widely available" } }]
  ]
}
```

With `@babel/preset-env` defaults, modern syntax is downleveled for ancient browsers. web.dev's own example drops from **12 KB to 1.5 KB** on the same source when targeting `baseline 2020`.

### 3.3 Catch unsupported CSS at lint time

```js
module.exports = {
  plugins: ["stylelint-browser-compat"],
  rules: {
    "plugin/browser-compat": [
      true,
      { browserslist: ["baseline widely available"] },
    ],
  },
};
```

A dedicated `stylelint-plugin-use-baseline` also exists if you prefer setting Baseline rules directly.

### 3.4 Join Baseline to your own traffic

```js
import { getAllVersions } from "baseline-browser-mapping";

const versions = getAllVersions(); // arrays, keyed objects, or CSV
// each entry carries `supports`: "widely" | "newly" | ""
```

Google's [GA Baseline Checker](https://github.com/GoogleChromeLabs/baseline-demos) is a working example of this join.

### 3.5 Publish status wherever you write

```html
<baseline-status featureId="font-size-adjust"></baseline-status>
```

`featureId` is the feature's name in `web-features`. The component updates itself as the feature moves Limited → Newly → Widely, so an article written in 2024 stays accurate.

### 3.6 Never ship blind

```js
// Baseline is a planning tool, not a polyfill.
if (CSS.supports("font-size-adjust", "0.5")) {
  // enhanced path
} else {
  // fallback
}
```

---

## 4. What value it brings

### To web users

- **Fewer "works in Chrome only" pages** — the 30-month rule pushes sites toward features that already work everywhere.
- **Faster sites** — fewer transpilation polyfills means smaller bundles.
- **Predictable behaviour** — Newly available means four independent engines agree, not one vendor's implementation.
- **Progressive enhancement as the default**, rather than a discipline few teams sustain.

### To developers

- **One word replaces a spreadsheet.** "Is this Baseline?" instead of arguing about Safari versions.
- **A vocabulary non-engineers can use** — product managers can reason about Newly vs Widely without reading compat tables.
- **Enforcement, not advice.** The same query drives Babel, postcss, Autoprefixer, stylelint, and webpack, so the target cannot silently drift.
- **Justifiable upgrade pressure.** "This is Baseline Widely available now" beats "Safari 16.4 supports it".
- **Validation against reality** — `baseline-browser-mapping` checks the target against your actual traffic.
- **Content that doesn't rot** — embeddable status components keep documentation current.

### What it costs

- **30 months is a policy, not a guarantee.** It is tuned for consumer traffic; enterprise, kiosks, regulated environments, and slow device-refresh markets can sit outside it.
- **"Widely available" describes core browsers, not your users.** Only your RUM data answers that.
- **Silent on quality.** Baseline says nothing about performance, accessibility, security, or DX.
- **Feature granularity is fuzzy.** A bundled "feature" may have uneven sub-feature support; partial and prefixed behaviour still differ.
- **Downstream browsers are opt-in.** Samsung Internet, Opera, and embedded webviews are excluded unless you add `with downstream` — and webviews are where many mobile users are.
- **It does not replace testing.** Interoperable specs still produce divergent bugs.
- **Year targets drift.** `baseline 2024` never grows; teams that set it and forget it fall behind.
- **Not everything can be polyfilled.** Baseline tells you when you *can* use something, not whether a fallback is feasible.

---

## Sources

- [Baseline — hub](https://web.dev/baseline) · [Introducing Baseline Alerts](https://web.dev/blog/baseline-alerts) · [How to choose your Baseline target](https://web.dev/articles/how-to-choose-your-baseline-target) · [Use Baseline with Browserslist](https://web.dev/articles/use-baseline-with-browserslist) · [Show Baseline status on your site](https://web.dev/blog/show-baseline-status)
- [web-features (WebDX CG)](https://github.com/web-platform-dx/web-features) · [baseline-status component](https://github.com/web-platform-dx/baseline-status) · [baseline-browser-mapping](https://github.com/web-platform-dx/baseline-browser-mapping) · [baseline-demos](https://github.com/GoogleChromeLabs/baseline-demos)
- [Web Platform Status](https://webstatus.dev/) · [Browserslist](https://github.com/browserslist/browserslist)
