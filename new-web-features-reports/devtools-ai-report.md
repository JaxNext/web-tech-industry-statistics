# Chrome DevTools — MCP and AI Features — What Google Shipped

Two products that give AI access to a real browser: an MCP server for coding agents, and a Gemini assistant inside DevTools.

**Last checked:** 2026-11-26
**Method:** `developer.chrome.com/docs/devtools/agents`, `docs/devtools/ai-assistance` (+ `/chat`), and the `ChromeDevTools/chrome-devtools-mcp` repository (README, client configurations, tool reference, CLI guide). Behaviour cross-checked by driving a live Chrome session.

---

## 1. What it is

Chrome ships **two different AI things** in DevTools, and they are routinely confused:

| | **AI assistance** | **DevTools for agents (MCP)** |
|---|---|---|
| Who drives | You, in the DevTools UI | Your coding agent (Claude Code, Cursor, Copilot, Antigravity) |
| Runs where | Inside DevTools, powered by Gemini | MCP server + CLI, driving Chrome via puppeteer |
| Best at | "Why is this slow/broken?" with the panel already open | Build → verify loop in a live browser |
| Status | **Experimental** | Shipping; stable package, monthly cadence |

The direction is the same from both ends: **agentic development needs a runtime, not just a model** — and DevTools already has the runtime (tracing, network, DOM, accessibility tree).

- **Inside-out (AI assistance):** a human asks Gemini about what they are looking at.
- **Outside-in (MCP):** an agent asks Chrome about what it just built.

They meet at one handoff: AI assistance can generate a prompt for your coding agent, and MCP executes it against the live page.

**At a glance**

| Dimension | Detail |
|---|---|
| MCP package | `chrome-devtools-mcp` (npm), MCP server **and** CLI |
| Engine | MCP → puppeteer → Chrome → CDP → DevTools frontend logic |
| Supported browsers | Chrome and Chrome for Testing (other Chromium "may work") |
| Requirements | Node.js LTS, current stable Chrome, npm |
| Client support | Antigravity, Claude Code, Cursor, VS Code, Copilot, Cline, OpenCode |
| Bundled skills | `chrome-devtools`, `chrome-devtools-cli`, `a11y-debugging` |

---

## 2. What the features are

### 2.1 Debugging and inspection

| Area | Tools |
|---|---|
| Navigation and pages | `navigate_page`, `new_page`, `list_pages`, `select_page` |
| Inspection | `take_snapshot` (a11y/DOM), `take_screenshot`, `evaluate_script`, `get_css_styles` |
| Network | `list_network_requests`, `get_network_request` |
| Console | `list_console_messages`, `get_console_message` — **with source-mapped stack traces** |
| Interaction | `click`, `fill`, `fill_form`, `hover`, `drag`, `press_key`, `type_text`, `upload_file`, `handle_dialog` |
| Emulation | `emulate` (device, network, CPU), `resize_page` |
| Recording | `screencast_start` / `screencast_stop` |

### 2.2 Performance and audits

- **`performance_start_trace` / `performance_stop_trace`** — record real traces.
- **`performance_analyze_insight`** — returns DevTools' own interpretation, not a raw trace. This is what makes an agent able to act on the data.
- **`lighthouse_audit`** — a11y, SEO, performance before pushing.

### 2.3 CLI and skills

Same engine without MCP, for scripts and CI:

```bash
npm i chrome-devtools-mcp@latest -g
chrome-devtools navigate_page 1 --url "https://developers.chrome.com"
chrome-devtools take_screenshot 1 --filePath screenshot.png
chrome-devtools stop
```

The package also ships skills that teach the agent *when* to reach for the tools — the same progressive-disclosure pattern Modern Web Guidance uses.

### 2.4 Auto-connect

By default the MCP launches an isolated Chrome. **Auto-connect** attaches to your already-running session — your tabs, logins, and extensions. This is what lets an agent inspect a page *you* are looking at, including anything behind a login. It is also the feature that most needs a security conversation.

### 2.5 AI assistance (inside DevTools)

- **Autonomous context selection** — narrows to a DOM node, request, or trace event for you.
- **Autonomous actions** — runs audits, records traces.
- **Step-by-step walkthrough** — what it did and why, with links back into the matching panel.
- **Show thinking** — code snippets it executed, copyable into the Console.
- **Save to workspace** — apply suggested changes through a **diff** review.
- **Generate a prompt for your coding agent** — the handoff to MCP.
- **Persistent history** across DevTools and Chrome reloads.

### 2.6 Privacy controls

| Flag / env var | Effect |
|---|---|
| `--no-usage-statistics` | Opt out of Google's invocation/latency telemetry (**on by default**) |
| `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS` / `CI` | Same, via environment |
| `--no-performance-crux` | Stop sending trace URLs to the CrUX API |
| `CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS` | Disable npm version checks |

Google's MCP telemetry is **independent** of Chrome's own metrics — opting out of one does not opt out of the other.

---

## 3. How developers use it

### 3.1 Add the server

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

Verify the handshake — the server starts Chrome lazily, so connecting alone launches nothing:

```
Check the performance of https://developers.chrome.com
```

### 3.2 Prompts that map to real tools

```
Check the performance of https://example.com and tell me what blocks the main thread.

Open my current tab, find the button with aria-label "Apply coupon", click it,
and screenshot the result.

Run a Lighthouse accessibility audit on this page and list failures by severity.

Emulate a Moto G Power on slow 3G and check for layout shift.
```

Each maps to `performance_*` + `performance_analyze_insight`, `take_snapshot` + `click` + `take_screenshot`, `lighthouse_audit`, and `emulate` + `resize_page` — which is why they behave predictably instead of degrading into DOM guessing.

### 3.3 Debug from the panel, then hand off

1. Right-click the failing element / request / trace entry → **Debug with AI** (context is pre-selected).
2. Read the walkthrough; ask for a fix.
3. **Save changes to workspace** and review the diff, or **generate a prompt** and let your agent apply it.

### 3.4 Close the build-and-verify loop

```bash
npx modern-web-guidance@latest install   # teach the agent modern patterns
# + chrome-devtools MCP                    # verify the result
```

MWG teaches how to break long tasks; the MCP trace on a simulated low-end CPU proves you got under 50 ms.

---

## 4. What value it brings

### To web users

- **Bugs caught before production** — including accessibility and performance regressions unit tests never see.
- **Real-device-class testing in CI** — emulated CPU throttling and slow networks, not "works on my laptop".
- **Better accessibility outcomes**, because audits are cheap to run and hard to skip.
- **Their data stays local** unless a trace URL is sent to CrUX, which is now switchable.

### To developers

- **The agent stops guessing.** Source-mapped errors and real traces beat "it looks right in the screenshot".
- **Fewer round trips.** One prompt replaces open-DevTools → reproduce → read → paste-into-chat.
- **Verification is scriptable.** The CLI brings the same capabilities to CI.
- **Institutionalised debugging skill** — the bundled skills encode *how* to debug, not just what to call.
- **Automatic context selection** removes the biggest source of bad AI answers.

### What it costs

- **Two surfaces, one confusion.** Different auth, privacy, and failure modes, freely interlinked in the docs.
- **AI assistance is experimental** — answers can be refused, quality varies, UI can change.
- **MCP telemetry is on by default** — opting out is a manual step, and enterprise rollout needs it in config, not a README note.
- **Auto-connect is a real security boundary.** The agent can read any tab you are logged into. Chrome's disclaimer says to avoid sharing sensitive information; treat it as handing over an unlocked laptop.
- **Only Chrome is supported.** Other Chromium browsers "may work".
- **Traces are expensive** in time and tokens; agents that trace indiscriminately feel slow.
- **CrUX lookups are external** unless `--no-performance-crux`.
- **Not a regression suite.** "The agent verified it" is weaker than "we have a test for it".
- **AI assistance eligibility follows Google's AI terms**, not the DevTools docs — check the in-product notice rather than assuming availability.

---

## Sources

- [Chrome DevTools for agents](https://developer.chrome.com/docs/devtools/agents) · [AI assistance](https://developer.chrome.com/docs/devtools/ai-assistance) · [Chat with AI assistance](https://developer.chrome.com/docs/devtools/ai-assistance/chat)
- [Auto-connect](https://developer.chrome.com/docs/devtools/agents/use-cases/auto-connect) · [Emulation](https://developer.chrome.com/docs/devtools/agents/use-cases/emulation) · [Lighthouse](https://developer.chrome.com/docs/devtools/agents/use-cases/lighthouse-audit)
- [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) · [Tool reference](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/tool-reference.md) · [Client configurations](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/client-configurations.md) · [CLI guide](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/cli.md) · [Design principles](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/design-principles.md)
- [Modern Web Guidance](https://developer.chrome.com/docs/modern-web-guidance) · [Chrome for Testing](https://developer.chrome.com/blog/chrome-for-testing/)
