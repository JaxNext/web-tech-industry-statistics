# WebMCP — What Google Shipped

A proposed web standard that lets a page declare its features as tools an AI agent can call.

**Last checked:** 2026-11-26
**Method:** `developer.chrome.com/docs/ai/webmcp/*` (updated Sep–Nov 2026), the Chrome AI Dev Preview EPP group (19 WebMCP threads), `chromestatus.com`. Where docs lag the EPP announcements, the EPP thread wins.

---

## 1. What it is

WebMCP (**Web** **M**odel **C**ontext **P**rotocol) lets a website publish structured tools — name, description, JSON Schema, execution handler — so an AI agent calls `checkout` instead of scraping the DOM to guess which button is "checkout".

The problem is **actuation reliability**. An agent trying to "book me a flight" must read the DOM, infer a button's purpose, click it, and interpret what happened — every step open to misreading. WebMCP flips the direction: **the page declares its capabilities**, and the agent uses them as intended.

Three pillars:

| Pillar | What an agent gets |
|---|---|
| **Discovery** | A standard way to list what the page can do, right now |
| **JSON Schemas** | Typed inputs and outputs, reducing hallucinated arguments |
| **Shared state** | An explicit notion of what the current page can act on |

**Not MCP.** MCP connects an agent to remote servers; WebMCP connects an agent to **the page the user is already on**, with the user watching.

**Progressive enhancement.** Nothing is required. Agents that don't understand WebMCP fall back to DOM actuation; pages without WebMCP behave exactly as before.

**At a glance**

| Dimension | Detail |
|---|---|
| Standard body | WICG / WebML Community Group draft |
| Chrome status | **Origin trial from Chrome 149**; `Intent to Experiment` filed |
| Local testing | `chrome://flags/#enable-webmcp-testing` → relaunch |
| Next breaking change | **Chrome 160.0.8173.0** — `Tool` interface replaces `RegisteredTool` |
| Ship target | **Early 2027** (Chrome 160 stable expected 2027-01-05) |
| Tooling | DevTools **Application → WebMCP** panel; `webmcp-types`; `webmcp-extension` |

---

## 2. What the features are

### 2.1 Imperative registration

`document.modelContext.registerTool()` accepts a tool object with three required parts — `name`, `description`, `inputSchema` — plus `execute`.

- **`description` is prompt text.** It is what the model reads when deciding whether to call the tool, so it deserves as much care as a UI label.
- **`inputSchema`** is standard JSON Schema: types, enums, `required`.
- **`outputSchema`** (Chrome 159+) lets the client validate results and return a structured tool error instead of feeding malformed data back to the model. Chrome's guidance: add it to consolidated read/search tools and to tools returning IDs for chaining; skip it on narrow reads, mutations, and navigation, because every schema costs prompt tokens.

### 2.2 Safety annotations

| Annotation | Default | Meaning | Who acts on it |
|---|---|---|---|
| `readOnlyHint` | `false` | No state change | Agent decides whether to ask first |
| `untrustedContentHint` | `false` | Output contains user or external content | Client sanitises — defends indirect prompt injection |
| `consequentialHint` | `false` | Hard-to-reverse real-world action | Browser/agent enforces confirmation |
| `debugging` | `false` | Tooling-only, not for end users (Chrome 156+) | End-user agents filter it out |

### 2.3 Lifecycle

- **Unregister** by aborting an `AbortController` passed as `{ signal }` — replaced `unregisterTool()` in Chrome 153.
- **Cancel a run** with the `AbortSignal` passed as the second `execute` argument, so cancellation reaches real work.
- **`toolchange`** fires on `document.modelContext` when the available tools change.

### 2.4 Declarative registration

Forms become tools through attributes, so the schema cannot drift from the markup.

| Attribute | On | Purpose |
|---|---|---|
| `toolname` | `<form>` | Tool name; removing it unregisters the tool |
| `tooldescription` | `<form>` | What the tool does (required) |
| `toolparamdescription` | field | Overrides label/`aria-description` as the property description |
| `toolautosubmit` | `<form>` | Agent invocation submits and navigates automatically |

Supporting behaviour:

- **`SubmitEvent.agentInvoked`** — `true` when an agent triggered the submit, so you can branch behaviour.
- **`SubmitEvent.respondWith(promise)`** — resolve with the result; the browser serialises it as the tool output (requires `preventDefault()`).
- **`toolactivated` / `toolcancel`** events on `document.modelContext`, each carrying `toolName`.
- **`:tool-form-active`** and **`:tool-submit-active`** CSS pseudo-classes, so the user can see the agent acting on their page.

### 2.5 Discovery and execution

- `getTools()` returns same-origin tools by default; `getTools({ fromOrigins: [...] })` opts into cross-origin tools.
- `executeTool(tool, args, { signal })` runs a tool; returns `null` when the call triggers a navigation.
- Results are alphabetically ordered and scoped to what the calling document may access.

### 2.6 Cross-origin requires three opt-ins

| Layer | Mechanism |
|---|---|
| Embedder delegates | `<iframe allow="tools">` |
| Tool declares audience | `registerTool(tool, { exposedTo: ['https://example.com'] })` |
| Reader requests origins | `getTools({ fromOrigins: [...] })` |

All lists accept secure origins only. Any one alone does nothing.

### 2.7 Framework hooks (experimental)

| Framework | Entry point |
|---|---|
| React | `use-webmcp-tool` → `useWebMCP` |
| Vue | `useWebMCP` from `@vueuse/core` |
| Angular | `angular.dev/ai/webmcp` |

They tie registration to component lifecycle, which solves the real pain: a tool outliving its component calls into a dead UI.

---

## 3. How developers use it

### 3.1 Minimal imperative tool

```js
await document.modelContext.registerTool({
  name: 'toggle_layer',
  description: 'Control pizza layers (sauce, cheese). Use "add", "remove", or "toggle".',
  inputSchema: {
    type: 'object',
    properties: {
      layer: { type: 'string', enum: ['sauce-layer', 'cheese-layer'] },
      action: { type: 'string', enum: ['add', 'remove', 'toggle'] },
    },
    required: ['layer'],
  },
  execute: async ({ layer, action }) => {
    await toggleLayer(layer, action);
    return `Performed ${action || 'toggle'} on layer: ${layer}`;
  },
});
```

### 3.2 Output schema and annotations

```js
await document.modelContext.registerTool({
  name: 'book_flight',
  description: 'Book a flight for the user with confirmed flight details.',
  inputSchema: {
    type: 'object',
    properties: {
      flightId: { type: 'string', description: 'ID of the flight to book' },
      passengers: { type: 'number', description: 'Number of tickets to purchase' },
    },
    required: ['flightId', 'passengers'],
  },
  outputSchema: {
    type: 'object',
    properties: { confirmation: { type: 'string' }, total: { type: 'number' } },
    required: ['confirmation'],
  },
  annotations: {
    readOnlyHint: false,
    consequentialHint: true,
    untrustedContentHint: false,
  },
  execute: async ({ flightId, passengers }, { signal }) => {
    return bookFlight({ flightId, passengers, signal });
  },
});
```

### 3.3 Unregister and cancel

```js
const controller = new AbortController();
await document.modelContext.registerTool(addTodoTool, { signal: controller.signal });

// Unregister without killing in-flight executions
controller.abort();

// Cancel a specific run
const run = new AbortController();
document.modelContext.executeTool(tool, { text: 'Buy milk' }, { signal: run.signal });
run.abort();
```

### 3.4 Declarative form

```html
<form toolname="supportRequestTool"
  tooldescription="Submit a request for support."
  action="/submit">

  <label for="firstName">First Name</label>
  <input type=text name=firstName>

  <select name="select" required
    toolparamdescription="Determines what team this request is routed to.">
    <option value="Customer happiness team">Return my purchase.</option>
    <option value="Distribution team">Check where my package is.</option>
    <option value="Website support team">Get help on the website.</option>
  </select>

  <button type=submit>Submit</button>
</form>
```

The browser derives this schema from the markup:

```json
[{
  "name": "supportRequestTool",
  "description": "Submit a request for support.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "firstName": { "type": "string" },
      "lastName":  { "type": "string" },
      "select": {
        "type": "string",
        "enum": ["Customer happiness team", "Distribution team", "Website support team"],
        "anyOf": [
          { "type": "string", "const": "Customer happiness team", "title": "Return my purchase." },
          { "type": "string", "const": "Distribution team",        "title": "Check where my package is." },
          { "type": "string", "const": "Website support team",     "title": "Get help on the website." }
        ],
        "description": "Determines what team this request is routed to."
      }
    },
    "required": ["select"]
  }
}]
```

### 3.5 Agent-aware submission

```html
<form toolautosubmit toolname="search_tool"
  tooldescription="Search the web" action="/search">
  <input type=text name=query>
</form>
<script>
  document.querySelector("form").addEventListener("submit", (e) => {
    e.preventDefault();
    if (!myFormIsValid()) {
      if (e.agentInvoked) e.respondWith(myFormValidationErrorPromise);
      return;
    }
    if (e.agentInvoked) e.respondWith(Promise.resolve("Search is done!"));
  });
</script>
```

### 3.6 Show the user what is happening

```js
document.modelContext.addEventListener('toolactivated', ({ toolName }) => {
  banner.textContent = `Agent is running "${toolName}"…`;
});
document.modelContext.addEventListener('toolcancel', () => {
  banner.textContent = '';
});
```

```css
form:tool-form-active { outline: light-dark(blue, cyan) dashed 1px; outline-offset: -1px; }
input:tool-submit-active { outline: light-dark(red, pink) dashed 1px; outline-offset: -1px; }
```

### 3.7 Discover and run tools

```js
const tools = await document.modelContext.getTools({
  fromOrigins: ['https://partner.org'],
});

const result = await document.modelContext.executeTool(tools[0], { text: 'Buy milk' });

// Cross-origin exposure, on the tool's side
await document.modelContext.registerTool(sharedTool, {
  exposedTo: ['https://example.com'],
});
```

### 3.8 Read tools defensively (Chrome 160+)

```js
const tools = await document.modelContext.getTools();
for (const tool of tools) {
  // TODO: drop `tool.window` once Chrome 160 is Stable (2027-01-05)
  const source = tool.source ?? tool.window;
  const { name, description, origin } = tool; // read explicitly — no spread, no JSON.stringify
}
```

---

## 4. What value it brings

### To web users

- **Visible automation.** Tools run on the page, with the form focused and fields filled — not in a hidden headless session.
- **Fewer wrong actions.** A typed `checkout` tool is far harder to mis-click than a button an agent guessed at.
- **Confirmation on high-stakes calls.** `consequentialHint` is what lets a browser force "are you sure?" before a purchase.
- **The site's own UI stays in charge** — the agent doesn't re-render the product into a chat transcript.
- **Privacy stays local.** In-page tools run in the browser; nothing is uploaded to an automation server.

### To developers

- **More reliable, cheaper agents.** One tool list beats a full DOM tree on both accuracy and tokens.
- **Progressive enhancement by construction** — no support, no change in behaviour.
- **The declarative path is nearly free** — two attributes on an existing form.
- **Testable without an LLM.** `getTools()` + `executeTool()` work in ordinary unit tests.
- **Ecosystem exists already**: `webmcp-types`, `webmcp-extension`, `webmcp-skills`, DevTools panel, `@w3c/webmcp-polyfill`.

### What it costs

- **The API is still moving.** ~12 breaking changes in 2026 alone: `navigator.modelContext` → `document.modelContext` (Jul), `registerTool()` returning a Promise (Jun), `AbortSignal` in `execute` (Aug), `consequentialHint` (Sep), `outputSchema` (Nov), `Tool` replacing `RegisteredTool` (Nov, Chrome 160). Build against the polyfill and expect churn until the early-2027 ship target.
- **Annotations are hints, not enforcement.** `consequentialHint` only works if the *client* honours it; the browser cannot force a third-party agent to show a dialog.
- **Cross-origin needs all three opt-ins** — `allow="tools"`, `exposedTo`, and `fromOrigins`.
- **No registry, by design.** Discovery is per-visit; a client must know the site to find its tools.
- **Complex UIs still need work.** Highly dynamic interfaces may need refactoring to keep tool state consistent; headless browsing is explicitly not the target.
- **Tool objects are not serialisable.** `JSON.stringify(tool)` returns `"{}"`, spread copies nothing, `structuredClone` throws.

---

## Sources

- [WebMCP — get started](https://developer.chrome.com/docs/ai/webmcp) · [Imperative API](https://developer.chrome.com/docs/ai/webmcp/imperative-api) · [Declarative API](https://developer.chrome.com/docs/ai/webmcp/declarative-api) · [Security](https://developer.chrome.com/docs/ai/webmcp/secure-tools) · [Best practices](https://developer.chrome.com/docs/ai/webmcp/best-practices)
- [DevTools: WebMCP panel](https://developer.chrome.com/docs/devtools/application/webmcp) · [Chrome Status](https://chromestatus.com/feature/5117755740913664) · [Explainer](https://github.com/webmachinelearning/webmcp)
- EPP: [Tool interface replaces RegisteredTool — 2026-11-23](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview/c/QNhbT1W2Qu0) · [Polyfill — 2026-11-18](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview/c/XfN73lpVgfQ) · [outputSchema — 2026-11-06](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview/c/aHZfIhWWzmM) · [Developer tools — 2026-10-15](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview/c/rYP4Gp51KVM)
