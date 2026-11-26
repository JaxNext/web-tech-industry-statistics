# New Web UI Features — What Google Shipped (2024–2026)

Google's HTML, CSS, and JavaScript work that makes pages more capable and more expressive.

**Last checked:** 2026-11-26
**Method:** Chrome's *What's New in Web UI* I/O 2026 roundup (2026-07-01) as the feature inventory; State of CSS / HTML / JS 2025 for demand evidence; MDN and Chrome release notes for status.
**Status labels:** **Shipped** (stable Chrome) · **Chrome N** (named milestone) · **Origin trial** · **Flag** · **Proposed**

---

## 1. What it is

"Web UI" here means the platform features that change how a page *behaves* and *reads* — not rendering engines or tooling. Google's 2024–2026 work in this area follows one thesis: **move common UI work out of JavaScript and into HTML and CSS.**

At I/O 2026 the Chrome team presented roughly 35 features organized under five UX principles:

| Principle | Google's interpretation |
|---|---|
| Respect user preferences | Follow OS settings (contrast, colour scheme, text size) instead of overriding them |
| Implement natural interactions | Physical motion and gestures without a motion library |
| Provide guided navigation | Preserve context across state changes and page loads |
| Maximize content, reduce noise | Remove chrome, borders, and overlays that block content |
| Adapt to the form factor | Respond to input method, viewport, and canvas |

**At a glance**

| Dimension | Detail |
|---|---|
| Scale | ~35 features across HTML, CSS, and JS |
| Maturity mix | Majority shipped; 4 experimental; 1 origin trial; 1 proposed |
| Compatibility model | All are Baseline-tracked; several are Newly available, not Widely available |
| Who leads | Chrome-led for most; spec review multi-vendor |

---

## 2. What the features are

### 2.1 HTML

Features that add declarative behaviour, removing JavaScript.

| Feature | What it replaces | Status |
|---|---|---|
| `<meta name="text-scale">` | Manual font-size scaling / ignoring OS text size | Shipped |
| `closedby` on `<dialog>` | ~40 lines of outside-click + Esc handling | Shipped |
| `layoutsubtree` (HTML-in-Canvas) | Screenshotting DOM into a canvas | Origin trial |
| `overscrollcontainer` + command invokers | Touch-event swipe implementations | Proposed |

```html
<meta name="text-scale" value="scale">

<dialog closedby="any">
  <p>Click outside or press Esc to close.</p>
</dialog>
```

### 2.2 CSS

**Theming and adaptation**

| Feature | What it replaces | Status |
|---|---|---|
| `contrast-color()` | Hand-maintained text/background pairs | Shipped |
| `light-dark()` (now accepts images) | Duplicated theme blocks | Chrome 150 |
| `@function` | Sass functions / preprocessor mixins | Shipped |
| Container style queries | Prop-drilling or class variants for theming | Shipped |
| `if()` | Media-query sprawl for value switching | Shipped |
| `@supports at-rule()` | Hacky at-rule detection | Shipped |

**Motion**

| Feature | What it replaces | Status |
|---|---|---|
| `linear()` | JS spring libraries | Shipped |
| `@starting-style` | Entry-animation JS shims | Shipped |
| `transition-behavior: allow-discrete` | Exit-animation workarounds | Shipped |
| `sibling-index()` / `sibling-count()` | JS index loops for stagger | Shipped |
| `corner-shape` | SVG masks / clip-path for notched corners | Experimental |

**Navigation and scrolling**

| Feature | What it replaces | Status |
|---|---|---|
| Same-document view transitions | SPA animation libraries | Shipped |
| Cross-document view transitions | Client-side routers for page transitions | Shipped |
| Element-scoped view transitions | Manual scoping of transition names | Chrome 147 |
| Two-phase view transitions | Skeleton-screen orchestration | Experimental |
| Scroll-driven animations | Scroll listeners + `requestAnimationFrame` | Shipped |
| Scroll-triggered animations | `IntersectionObserver` reveal logic | Shipped |
| `scroll-target-group: auto` | Scroll-spy JavaScript | Shipped |
| `scrollIntoView({ container })` | Manual scroll container maths | Shipped |
| Awaitable scroll methods | Timeout-guessing after smooth scroll | Shipped |

**Layout, density, typography**

| Feature | What it replaces | Status |
|---|---|---|
| Scroll-state queries | Scroll-position JS for sticky headers | Shipped |
| Anchored container queries | Manual tooltip arrow positioning | Shipped |
| `border-shape` | Clip-path with mismatched borders | Shipped |
| `shape()` | SVG paths for clip/shape-outside | Shipped |
| Sticky per axis | Wrapper-div workarounds in tables | Flag (148) |
| `text-box-trim` | Negative-margin vertical centring | Shipped |
| `text-fit` | JS fit-to-width text | Experimental |
| Gap decorations | Border/pseudo-element gutters | Shipped |
| Scrollbar-aware `vw`/`vh` | `calc(100vw - scrollbar)` hacks | Shipped |

### 2.3 JavaScript

| API | What it replaces | Status |
|---|---|---|
| `Element.moveBefore()` | Re-append workarounds that destroy state | Shipped |
| `Element.pseudo()` → `CSSPseudoElement` | Reading computed styles to infer pseudo-element state | Shipped |
| `Event.pseudoTarget` | Guessing the event origin | Shipped |
| `element.startViewTransition()` | Whole-page transitions for local changes | Chrome 147 |

### 2.4 Demand evidence

These are the features developers actually use and rate highest, per State of CSS / HTML / JS 2025 — the basis for the ordering above.

| Signal | Result |
|---|---|
| Most-used **and** most-loved CSS feature | `:has()` — 80.4% used |
| Largest YoY usage increase | `text-wrap: pretty` |
| Largest YoY awareness increase | `light-dark()` |
| Most-used HTML interactivity features | `<details>` 65.5%, `<dialog>` 52.8% |
| Least-aware, high-satisfaction | `moveBefore()` 6.3% used / 74.5% never heard; `commandfor` 3.7% |
| #1 HTML pain point | Browser support (202 answers), ahead of DOM APIs and accessibility |
| JS contrast | Set methods: "None" is the top answer (7,328 of 10,913) |

The pattern: **the demand is for declarative primitives, and it is concentrated in HTML/CSS rather than in the language.**

---

## 3. How developers use it

### 3.1 A dialog that opens, animates, and light-dismisses — no JS

```html
<dialog closedby="any" id="confirm">…</dialog>
<button commandfor="confirm" command="show-modal">Delete</button>
```

```css
dialog {
  opacity: 0;
  transform: translateY(8px);
  transition: opacity .2s, transform .2s, overlay .2s allow-discrete;
}
dialog[open] { opacity: 1; transform: none; }

@starting-style {
  dialog[open] { opacity: 0; transform: translateY(8px); }
}
```

Three features cooperate: `commandfor` (no click handler), `closedby` (no outside-click handler), `@starting-style` + `allow-discrete` (no animation library).

### 3.2 Parent-aware styling

```css
/* Style a form only when it has an invalid field */
form:has(input:invalid) .submit-hint { display: block; }

/* Style a card when its checkbox is checked — no JS class toggle */
.card:has(input:checked) { outline: 2px solid; }
```

### 3.3 Theming that follows the OS

```css
:root { color-scheme: light dark; }

.card {
  background: light-dark(#fff, #1e1e1e);
  color: contrast-color(var(--card-bg));
  background-image: light-dark(url(a-light.png), url(a-dark.png));
}
```

### 3.4 View transitions — full page and scoped

```js
// Same-document
document.startViewTransition(() => render(newState));

// Element-scoped (Chrome 147): only this list animates, rest stays interactive
list.startViewTransition(() => reorder());
```

```css
@view-transition { navigation: auto; }  /* cross-document, MPA */
```

### 3.5 Scroll work without listeners

```css
@keyframes reveal { from { opacity: 0 } to { opacity: 1 } }

.card {
  animation: reveal linear both;
  animation-timeline: view();          /* driven by scroll position */
  animation-range: entry 25% cover 50%;
}

.container { container-type: scroll-state; }
@container scroll-state(scrolled: bottom) {
  .header { translate: 0 -100%; }      /* hidey bar */
}
```

### 3.6 Staggered content with no JS counter

```css
dialog[open] > * {
  animation: entry .6s var(--spring) forwards;
  animation-delay: calc(sibling-index() * 0.05s + 0.2s);
}
```

### 3.7 Reparent without losing state

```js
// Video restarts, focus is lost, iframe reloads:
newParent.appendChild(video);

// Playback, focus, and iframe state survive:
newParent.moveBefore(video, null);
```

### 3.8 Sequential logic after a smooth scroll

```js
await el.scrollIntoView({ behavior: 'smooth', container: 'nearest' });
el.classList.add('highlight');
```

---

## 4. What value it brings

### To web users

- **Text respects their OS setting** — one meta tag replaces a decade of ignoring user preference.
- **Fewer broken modals and tooltips**, the most common interactive failure on the web; native `<dialog>` and popover inherit browser focus management and top-layer behaviour.
- **Less jank** — scroll-driven animations and view transitions run off the main thread.
- **Faster pages** — every feature in the top of the demand list removes shipped JavaScript.
- **Correct contrast and theming** computed by the browser rather than hand-tuned per theme.

### To developers

- **Less code for the same UI.** Light dismiss, scroll-spy, stagger, scroll-triggered reveal, and theming all became declarative.
- **No preprocessor for logic.** `@function` + `if()` + style queries cover the patterns people built in Sass.
- **Fewer dependencies.** `moveBefore()` alone removes a category of DOM helpers.
- **Cheaper motion authoring** — four view-transition scopes cover most product asks without a motion library.
- **Graceful degradation by default** — additive CSS and HTML attributes; unsupported browsers render the plain version.

### What it costs

- **Chrome-first is not "available".** The top-ranked features shipped in Chrome first; the #1 developer pain point is browser support, not missing capability. Check Baseline per feature before deleting a fallback.
- **Awareness lags support by 12–24 months.** `moveBefore()` is shipped and 74.5% of surveyed developers have never heard of it — education is part of adoption.
- **"No JS" degrades to nothing.** Declarative light dismiss and native scroll-spy have no fallback behaviour; older browsers simply lose the feature.
- **Four items are experimental** (`corner-shape`, `text-fit`, two-phase transitions, sticky-per-axis) and can change shape.
- **`@supports at-rule()` is shallow** — it detects the at-rule, not descriptors or preludes.

---

## Sources

- [What's new in web UI (Google I/O 2026)](https://developer.chrome.com/blog/new-in-web-ui-io26)
- [State of CSS 2025](https://2025.stateofcss.com/en-US/features/) · [State of HTML 2025 — Interactivity](https://2025.stateofhtml.com/en-US/features/interactivity/) · [State of JS 2025](https://2025.stateofjs.com/en-US/features/)
- [Style queries](https://developer.chrome.com/docs/css-ui/style-queries) · [Scroll-driven animations](https://developer.chrome.com/docs/css-ui/scroll-driven-animations) · [Element-scoped view transitions](https://developer.chrome.com/docs/css-ui/view-transitions/element-scoped-view-transitions)
- [Scroll-triggered animations](https://developer.chrome.com/blog/scroll-triggered-animations) · [Scroll-state queries](https://developer.chrome.com/blog/css-scroll-state-queries) · [CSS shapes](https://developer.chrome.com/blog/css-shape) · [HTML-in-Canvas](https://developer.chrome.com/blog/html-in-canvas-origin-trial)
- [MDN: `:has()`](https://developer.mozilla.org/docs/Web/CSS/:has) · [`light-dark()`](https://developer.mozilla.org/docs/Web/CSS/light-dark) · [`text-box`](https://developer.mozilla.org/docs/Web/CSS/text-box) · [`Element.moveBefore()`](https://developer.mozilla.org/docs/Web/API/Element/moveBefore) · [`closedby`](https://developer.mozilla.org/docs/Web/API/HTMLDialogElement/closedBy)
- [Baseline](https://web.dev/baseline)
