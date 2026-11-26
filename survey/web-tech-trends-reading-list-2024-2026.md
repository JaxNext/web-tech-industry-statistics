# Web Tech & Web Dev Trends — Reading List (2024–2026)

Last checked: 2026-11-24

Companion to [state-of-reports-2024-2026.md](state-of-reports-2024-2026.md). That file is the survey index; this one is the *analysis* shelf — material that argues about what changed in web technology and web development, not just what the numbers are.

**Selection rule ("believable"):** primary sources only — named authors, published data or methodology, peer review, or an established conference/standards body. Excluded: SEO listicles, undated trend posts, and vendor content with no data.

---

## The five shifts this list keeps returning to

1. **The platform caught up** — Baseline/Interop made new CSS and HTML safe to ship, so the browser itself is absorbing features frameworks once provided.
2. **AI became the centre of gravity — and the evidence became contested** — vendor studies claim large gains; a controlled study found experienced developers *slower*.
3. **Toolchain consolidation** — Vite+, Rolldown, and Rust-based tooling collapsed the "many small tools" era into a few stacks.
4. **Architecture debate re-opened** — SPA vs server-first, React Server Components, and a genuine hypermedia revival.
5. **The web's input surface changed** — browser-engine competition (Ladybird) and AI agents as first-class users of the web (WebMCP).

---

## 1. Academic & measurement papers

| Title | Author / Publisher | Date | Angle | Link |
| --- | --- | --- | --- | --- |
| Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity (RCT) | METR | Jul 2025 | Data, critical | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ |
| Evaluating the Efficacy of Next.js: A Comparative Analysis with React.js on Performance, SEO, and Global Network Equity | arXiv preprint | Feb 2025 | Data | https://arxiv.org/abs/2502.15707 |
| Signal-First Architectures: Rethinking Front-End Reactivity | arXiv preprint | Jun 2025 | Data | https://arxiv.org/abs/2506.13815 |
| Exploring React Library Related Questions on Stack Overflow: Answered vs. Unanswered | arXiv preprint | Jul 2025 | Data | https://arxiv.org/abs/2507.04390 |
| DesignBench: A Comprehensive Benchmark for MLLM-based Front-end Code Generation | arXiv preprint | Jun 2025 | Data | https://arxiv.org/abs/2506.06251 |
| Vibe Coding: Practice, Performance, Productivity, and Risk — A State-of-the-Art Review | arXiv preprint | Aug 2026 | Data, balanced | https://arxiv.org/abs/2608.20446 |

Why these: the METR RCT is the strongest counterweight to AI-productivity marketing (16 experienced devs, 246 tasks, 19% *slower* with AI while believing they were 20% faster). The Next.js/React and signal papers give measured comparisons instead of benchmark marketing. DesignBench and the vibe-coding review cover the 2025–2026 "AI writes the frontend" claim with actual evaluation.

---

## 2. Essays, books & engineering blogs

| Title | Author / Publisher | Date | Angle | Link |
| --- | --- | --- | --- | --- |
| From a humble beginning 35 years ago, the Web is now central to the daily lives of billions | W3C / Tim Berners-Lee | Mar 2024 | Mainstream, primary | https://www.w3.org/blog/2024/from-a-humble-beginning-35-years-ago-the-web-is-now-central-to-the-daily-lives-of-billions/ |
| The Two Reacts | Dan Abramov (overreacted.io) | Jan 2024 | Mainstream, primary | https://overreacted.io/the-two-reacts/ |
| If Not React, Then What? | Alex Russell (infrequently.org) | Nov 2024 | Critical | https://infrequently.org/2024/11/if-not-react-then-what/ |
| The Performance Inequality Gap, 2026 | Alex Russell (infrequently.org) | Nov 2025 | Data, critical | https://infrequently.org/2025/11/performance-inequality-gap-2026/ |
| Hypermedia Systems (book) | Carson Gross, Adam Stepinski, Deniz Akşimşek | 2024 | Contrarian | https://hypermedia.systems/ |
| Interop 2025: another year of improvements to the web platform | Rachel Andrew / web.dev | Feb 2025 | Mainstream, primary | https://web.dev/blog/interop-2025 |
| ViteConf 2025 recap: Vite+, Rolldown and the unified toolchain | VoidZero | Oct 2025 | Vendor, primary | https://voidzero.dev/posts/whats-new-viteconf-2025.html |
| What's new in web UI (Google I/O 2026) | Chrome team | Jul 2026 | Vendor, primary | https://developer.chrome.com/blog/new-in-web-ui-io26 |

Why these: Abramov and Russell frame the two poles of the architecture argument — React's own server/client split versus a measurable critique of framework-driven JavaScript cost. "If Not React, Then What?" is the most-cited critical essay of the period. Hypermedia Systems is the intellectual backing for the htmx/server-rendered resurgence. Interop 2025 and the I/O 2026 post document the other story: the platform shipping features developers used to need libraries for.

---

## 3. Conference talks & keynotes

| Title | Speaker / Event | Date | Angle | Link |
| --- | --- | --- | --- | --- |
| React for Two Computers (+ React 19 keynote) | Dan Abramov / React Conf 2024 | May 2024 | Mainstream, primary | https://react.dev/blog/2024/05/22/react-conf-2024-recap |
| React Conf 2025 recap: React 19.2, Activity, RSC direction | React team / React Conf 2025 | Oct 2025 | Mainstream, primary | https://react.dev/blog/2025/10/16/react-conf-2025-recap |
| Frontend's Lost Decade and the Performance Inequality Gap | Alex Russell / JSNation 2025 | Jun 2025 | Critical | https://gitnation.com/person/alex_russell |
| Next.js for AI Agents | Jude Gao / Next.js Conf 2025 | Oct 2025 | Vendor, primary | https://nextjs.org/conf/session/nextjs-for-ai-agents |
| The State of AI for Web Development | Sacha Greif / JSNation 2026 | Jun 2026 | Data | https://jsnation.com/ |
| WebMCP: Clicks n' Clankers | Wes Bos / JSNation US 2026 | Nov 2026 | Mainstream | https://jsnation.us/schedule |
| State of the Browser 13 (incl. Andreas Kling on Ladybird) | Various / State of the Browser 2025 | 2025 | Mainstream | https://2025.stateofthebrowser.com/ |

Why these: the React Conf pair shows the framework's own narrative shifting from "UI library" to "server+client architecture". Sacha Greif's 2026 talk is the clearest live read of the AI-in-web-dev data. WebMCP marks the newest turn: making sites callable by agents, not just humans. State of the Browser is the best single venue for the independent-browser-engine argument.

---

## 4. Reports with explicit trend analysis

| Title | Publisher | Date | Angle | Link |
| --- | --- | --- | --- | --- |
| Web Almanac 2024 | HTTP Archive | 2024 | Data | https://almanac.httparchive.org/en/2024/ |
| Web Almanac 2025 (17.2M sites, 244 TB of data) | HTTP Archive | 2025 | Data | https://almanac.httparchive.org/en/2025/ |
| State of JavaScript 2025 | Devographics | Mar 2026 | Data | https://2025.stateofjs.com/ |
| Stack Overflow Developer Survey 2025 | Stack Overflow | Jul 2025 | Data | https://stackoverflow.blog/2025/07/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here |
| Octoverse 2026 | GitHub | Oct 2026 | Data | https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/ |
| State of AI-assisted Software Development 2025 (DORA) | DORA / Google Cloud | Sep 2025 | Data | https://dora.dev/research/2025/dora-report/ |
| State of Developer Ecosystem 2026 | JetBrains | Nov 2026 | Data | https://blog.jetbrains.com/research/2026/11/state-of-developer-ecosystem-2026/ |
| State of the API 2026 | Postman | 2026 | Data | https://blog.postman.com/the-2026-state-of-the-api-report-agents-are-in-production-and-most-apis-arent-ready/ |
| State of AI Report 2026 | Air Street Capital | Oct 2026 | Data | https://www.stateof.ai/ |

Why these: the Web Almanac is the only large-scale measurement of *what is actually deployed* (page weight, JS, CMS, accessibility). DORA 2025 supplies the "AI is an amplifier, not a fix" framing. Octoverse 2026 and Postman 2026 document the same transition from opposite ends — repos and APIs being consumed by agents. Full inventory of editions in the companion file.

---

## 5. How to use these together

| Claim you want to check | Start with | Then read against |
| --- | --- | --- |
| "AI makes developers faster" | Vendor reports (JetBrains, Octoverse, DORA) | METR RCT; Vibe Coding review |
| "Frameworks are too heavy" | Alex Russell 2024/2025 | React Conf recaps; State of JS satisfaction data |
| "The browser can replace libraries" | Interop 2025; Web Almanac 2025 | Baseline adoption data in State of CSS 2026 |
| "SPA is over / server-first won" | React Conf 2024–2025; Next.js Conf | State of JS 2025 (SPA usage still dominant) |
| "Toolchains are consolidating" | ViteConf 2025 recap | State of JS 2025 build-tool numbers |
| "Agents will be the next web users" | Postman 2026; JSNation US 2026 (WebMCP) | Web Almanac 2025 (readiness of average sites) |

---

## Notes on caveats

- Vendor-authored pieces (VoidZero, Chrome, Next.js) are marked "vendor, primary" — useful for direction of travel, not neutral evidence.
- Preprints on arXiv are not peer-reviewed; treat single-paper results as hypotheses, not consensus.
- Several 2026 sources are recent enough that their findings have not been independently replicated.
- Dates are publication dates, which for surveys often differ from the edition year (see the companion file's note).
