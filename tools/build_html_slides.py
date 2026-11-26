import html, os, json

OUT = "/Users/jax-gua/Dev/web-tech-industry-statsics/slides"
os.makedirs(OUT, exist_ok=True)

def esc(s):
    return html.escape(s, quote=False)

CSS = """*{box-sizing:border-box}
:root{--ink:#1e1e1e;--bg:#f0f0f0;--paper:#fff;--line:#d7d7d7;--muted:#5f6368}
html{scroll-snap-type:y mandatory;scroll-behavior:smooth}
body{margin:0;background:#202124;font-family:'Google Sans','Roboto','Noto Sans SC','PingFang SC',system-ui,sans-serif;color:var(--ink)}
.deck{--s:1;display:flex;flex-direction:column;align-items:center;gap:40px;padding:40px 0 80px}
.slide{width:calc(1280px*var(--s));height:calc(720px*var(--s));scroll-snap-align:center;position:relative;flex:0 0 auto}
.canvas{width:1280px;height:720px;background:var(--bg);position:relative;overflow:hidden;transform:scale(var(--s));transform-origin:top left;box-shadow:0 12px 40px rgba(0,0,0,.45)}
.titlechip{position:absolute;left:46px;top:45px;height:97px;display:inline-flex;align-items:center;padding:0 32px 0 18px;background:#fff;border:2.5px solid var(--ink);border-radius:27px;font-size:38px;font-weight:500;letter-spacing:-.01em;max-width:980px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.logo{position:absolute;right:34px;top:48px;height:38px;width:auto}
.body{position:absolute;left:46px;right:46px;top:172px;bottom:52px;display:flex;flex-direction:column;justify-content:flex-start}
.content{flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:14px}
.content.panel{flex:0 0 auto;margin:auto 0;background:#fff;border:1.5px solid var(--ink);border-radius:22px;padding:28px 36px;box-shadow:none}
.content.panel .two{gap:56px}
.content.panel .bullets li{font-size:23px;margin-bottom:15px}
.body.cover{flex-direction:row;align-items:center;justify-content:center;gap:56px}
.cover-left{flex:1.45;min-width:0}
.cover-left h1{font-size:70px;line-height:1.1;margin:0 0 22px}
.body.cover .lead{font-size:19.5px;line-height:1.55}
.panel{flex:1;min-width:340px;background:var(--pastel);color:var(--ink);border:1.5px solid rgba(30,30,30,.16);border-radius:26px;padding:30px 34px}
.panel-title{font-family:'Roboto Mono',monospace;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:rgba(30,30,30,.55);margin-bottom:12px}
.fact{display:flex;align-items:center;gap:13px;font-size:22px;line-height:1.35;padding:16px 0;border-bottom:1px solid rgba(30,30,30,.14)}
.fact:last-child{border-bottom:none}
.fact .dot{flex:0 0 auto;width:10px;height:10px;border-radius:50%;background:var(--accent)}
.label{font-family:'Roboto Mono','SFMono-Regular',monospace;font-size:13.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:12px}
h2{font-size:46px;line-height:1.16;margin:0 0 20px;font-weight:700;letter-spacing:-.02em;max-width:1080px}
h1{font-size:58px;line-height:1.12;margin:0 0 20px;font-weight:700;letter-spacing:-.02em;max-width:1050px}
.lead{font-size:21px;line-height:1.5;color:#3c4043;max-width:1000px}
.chips{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}
.chip{font-size:15px;padding:8px 16px;border-radius:999px;background:#fff;border:1.5px solid var(--ink);color:var(--ink)}
.chip.on{background:var(--ink);color:#fff;font-weight:500}
.grid{display:grid;gap:16px;margin-top:2px}
.g2{grid-template-columns:1fr 1fr}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.card{background:#fff;border:1.5px solid var(--ink);border-radius:16px;padding:17px 19px;min-height:122px}
.card .n{font-family:'Roboto Mono',monospace;font-size:11.5px;letter-spacing:.08em;color:var(--accent);margin-bottom:6px}
.card h3{margin:0 0 6px;font-size:18.5px;font-weight:600}
.card p{margin:0;font-size:14.5px;line-height:1.45;color:#3c4043}
.bullets{list-style:none;padding:0;margin:2px 0 0}
.bullets li{position:relative;padding-left:26px;margin-bottom:17px;font-size:25px;line-height:1.45}
.bullets li:before{content:"";position:absolute;left:0;top:10px;width:9px;height:9px;border-radius:50%;background:var(--ink)}
.stat{display:flex;align-items:baseline;gap:20px}
.stat .num{font-size:150px;line-height:.95;font-weight:700;letter-spacing:-.04em;color:var(--accent)}
.stat .unit{font-size:38px;font-weight:500;color:var(--accent)}
.stat-label{font-size:23px;line-height:1.4;margin-top:10px;max-width:820px}
table{width:100%;border-collapse:collapse;font-size:16px}
th{text-align:left;font-weight:600;color:var(--muted);font-size:12.5px;text-transform:uppercase;letter-spacing:.06em;padding:0 10px 9px;border-bottom:2px solid var(--ink)}
td{padding:10px 10px;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:none}
code{font-family:'Roboto Mono',monospace;font-size:.92em;background:#e4e4e4;padding:1px 6px;border-radius:4px}
pre{margin:0;max-height:452px;overflow:hidden;background:var(--ink);color:#e8eaed;border-radius:16px;padding:24px 26px;font-family:'Roboto Mono',monospace;font-size:15px;line-height:1.55;white-space:pre-wrap}
pre.sm{font-size:13px;line-height:1.5;padding:20px 22px}
pre .k{color:#8ab4f8}
.codewrap{display:grid;grid-template-columns:1.4fr 1fr;gap:22px;align-items:start;margin-top:2px}
.codewrap .side{font-size:16.5px;line-height:1.5;color:#3c4043}
.codewrap .side b{display:block;font-size:18px;color:var(--ink);margin-bottom:8px}
.codewrap .bullets li{font-size:17px;margin-bottom:10px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:72px}
.col h4{margin:0 0 10px;font-size:13px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);font-weight:600}
.col ul{list-style:none;padding:0;margin:0}
.col li{font-size:21px;line-height:1.45;margin-bottom:15px;padding-left:20px;position:relative}
.col li:before{content:"";position:absolute;left:0;top:9px;width:6px;height:6px;border-radius:50%;background:var(--ink)}
@media print{
  html,body{background:#fff}
  .deck{gap:0;padding:0}
  .slide{page-break-after:always;box-shadow:none}
  .canvas{box-shadow:none}
}"""

JS = """
const deck=document.querySelector('.deck');
function fit(){
  const s=Math.min(1,(window.innerWidth-64)/1280,(window.innerHeight-96)/720);
  deck.style.setProperty('--s',s.toFixed(4));
}
addEventListener('resize',fit);fit();
const slides=[...document.querySelectorAll('.slide')];
let i=0;
addEventListener('keydown',e=>{
  if(e.key==='ArrowDown'||e.key==='ArrowRight'||e.key===' '){e.preventDefault();i=Math.min(i+1,slides.length-1);slides[i].scrollIntoView({behavior:'smooth'});}
  if(e.key==='ArrowUp'||e.key==='ArrowLeft'){e.preventDefault();i=Math.max(i-1,0);slides[i].scrollIntoView({behavior:'smooth'});}
});
const io=new IntersectionObserver(es=>{es.forEach(x=>{if(x.isIntersecting)i=slides.indexOf(x.target);});},{threshold:.55});
slides.forEach(s=>io.observe(s));
"""

LOGO = "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"

SHORT = {
    "Chrome Built-in AI APIs": "Chrome Built-in AI",
    "WebMCP": "WebMCP",
    "WebGPU": "WebGPU",
    "Baseline": "Baseline",
    "Modern Web Guidance": "Modern Web Guidance",
    "DevTools for agents": "DevTools",
    "New Web UI Features": "New Web UI",
}

def slide(body, cls="", accent="#4285f4", pastel="#e8eaed"):
    return f'''<section class="slide {cls}">
  <div class="canvas" style="--accent:{accent};--pastel:{pastel}">
    {body}
  </div>
</section>'''

def cover(kicker, title, lead, chips, accent, halftone, pastel, foot):
    rows = "".join(f'<div class="fact"><span class="dot"></span>{c}</div>' for c in chips)
    return slide(f'''<div class="titlechip">{SHORT.get(foot, foot)}</div>
    <img class="logo" alt="DevFest" src="data:image/png;base64,{LOGO}">
    <div class="body cover">
      <div class="cover-left">
        <div class="label">{kicker}</div>
        <h1>{title}</h1>
        <div class="lead">{lead}</div>
      </div>
      <aside class="panel"><div class="panel-title">速览</div>{rows}</aside>
    </div>''', "cover", accent, pastel)

def page(kicker, title, inner, accent, halftone, pastel, foot, cls=""):
    section = kicker.split("/")[-1].strip()
    panel = " panel" if not any(k in inner for k in ('class="grid', '<table', '<pre')) else ""
    crumb = f"{SHORT.get(foot, foot)} / {section}"
    return slide(f'''<div class="titlechip">{crumb}</div>
    <img class="logo" alt="DevFest" src="data:image/png;base64,{LOGO}">
    <div class="body"><h2>{title}</h2><div class="content{panel}">{inner}</div></div>''', cls, accent, pastel)


def bullets(items):
    return '<ul class="bullets">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"

def cards(items, cols=3):
    cs = "".join(f'<div class="card"><div class="n">{n}</div><h3>{t}</h3><p>{d}</p></div>' for n, t, d in items)
    return f'<div class="grid g{cols}">{cs}</div>'

def table(head, rows):
    h = "".join(f"<th>{x}</th>" for x in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f"<table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table>"

def codeblock(code, side_title, side_items, small=False):
    c = esc(code)
    for kw in ["const", "await", "async", "function", "return", "if", "new", "for"]:
        c = c.replace(kw, f'<span class="k">{kw}</span>')
    side = "".join(f"<li>{x}</li>" for x in side_items)
    return f'''<div class="codewrap">
      <pre class="{'sm' if small else ''}">{c}</pre>
      <div class="side"><b>{side_title}</b><ul class="bullets" style="font-size:17px">{side}</ul></div>
    </div>'''

def stats_page(kicker, title, num, unit, label, support, accent, halftone, pastel, foot):
    return page(kicker, title, f'''<div style="margin-top:10px">
      <div class="stat"><span class="num">{num}</span><span class="unit">{unit}</span></div>
      <div class="stat-label">{label}</div>
      <div class="chips" style="margin-top:34px">{support}</div>
    </div>''', accent, halftone, pastel, foot)

def shell(title, slides_html):
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{CSS}</style></head>
<body><main class="deck">
{slides_html}
</main><script>{JS}</script></body></html>'''

FOOT = ""

# ============ 1. Chrome Built-in AI ============
A, H, P = "#4285f4", "#57caff", "#c3ecf6"
s = []
s.append(cover("CHROME BUILT-IN AI · 2024–2026", "浏览器里<br>已经有了模型",
  "不联网、不付费、不上传。七个内置 API，把推理搬到了用户设备上。",
  ["7 个 API", "4 个已稳定", "1 个已废弃"], A, H, P, "Chrome Built-in AI APIs"))
s.append(page("01 / 它是什么", "设备端模型，藏在浏览器里", f'''<div class="two">
  <div class="col"><h4>本质</h4><ul>
    <li>Gemini Nano 默认，Gemma 4 进入 Dev Trial</li>
    <li>无需 API Key、无需后端、无按 token 计费</li>
    <li>隐私是结构性的：文本不离开设备</li>
  </ul></div>
  <div class="col"><h4>代价</h4><ul>
    <li>模型需要下载，几百 MB</li>
    <li>能力取决于硬件与配额</li>
    <li>API 表面仍在变动</li>
  </ul></div></div>''', A, H, P, "Chrome Built-in AI APIs"))
s.append(page("02 / 有什么", "七个 API，一个模型底座", cards([
  ("PROMPT", "LanguageModel", "通用会话，Chrome 148 起稳定"),
  ("SUMMARIZER", "Summarizer", "四种类型、三档长度、可流式"),
  ("TRANSLATOR", "Translator", "按语言对创建，支持流式翻译"),
  ("DETECTOR", "Language Detector", "识别源语言，已稳定"),
  ("PROOFREADER", "Proofreader", "纠错并给出逐条解释"),
  ("EMBEDDING", "embeddinggemma", "设备端向量，Dev Trial"),
  ("DECISIONS", "DecisionModel", "只打分不生成，意图分类"),
  ("DEPRECATED", "Writer / Rewriter", "2026 年宣布移除，迁到 Prompt"),
  ("MTP", "非 API", "投机解码，解码吞吐 +20–30%"),
], 3), A, H, P, "Chrome Built-in AI APIs"))
s.append(page("03 / 怎么用", "先查可用性，再开流式会话", codeblock(
'''const availability = await LanguageModel.availability();
if (availability === "unavailable") return fallback();

const session = await LanguageModel.create({
  initialPrompts: [
    { role: "system", content: "你是简洁的无障碍审阅者。" },
  ],
});

for await (const chunk of session.promptStreaming(markup)) {
  output.textContent += chunk;   // 边生成边渲染
}
await session.destroy();''',
"三个要点", [
 "availability() 有四种返回值，先判空再调用",
 "promptStreaming() 让首字延迟变成首字可见",
 "sampling 参数已废弃，改用预设",
]), A, H, P, "Chrome Built-in AI APIs"))
s.append(page("04 / 价值", "省掉后端，也省掉一次上传", f'''<div class="two">
  <div class="col"><h4>对用户</h4><ul>
    <li>文本不出设备，隐私是结构保证</li>
    <li>模型就绪后完全离线可用</li>
    <li>摘要、翻译、校对变成免费能力</li>
  </ul></div>
  <div class="col cost"><h4>代价</h4><ul>
    <li>硬件与下载状态决定可用性，必须准备降级</li>
    <li>Writer/Rewriter 已宣布移除，旧代码会断</li>
    <li>官方文档比实际能力滞后最多 14 个月</li>
  </ul></div></div>''', A, H, P, "Chrome Built-in AI APIs"))

open(f"{OUT}/chrome-ai.html", "w", encoding="utf-8").write(
    shell("Chrome Built-in AI APIs", "\n".join(s)))

# ============ 2. WebMCP ============
A, H, P = "#34a853", "#5cdb6d", "#ccf6c5"
s = []
s.append(cover("WEBMCP · 2026", "让智能体调用页面，<br>而不是猜按钮",
  "站点自己声明能力：名字、描述、JSON Schema、执行函数。智能体照着调，不再靠 DOM 猜测。",
  ["Chrome 149 Origin Trial", "2027 年初目标发布", "声明式仅两个属性"], A, H, P, "WebMCP"))
s.append(page("01 / 它是什么", "三个支柱，一个反方向的协议", f'''<div class="two">
  <div class="col"><h4>三支柱</h4><ul>
    <li>发现：页面当前能做什么，有标准说法</li>
    <li>Schema：输入输出有类型，减少幻觉参数</li>
    <li>共享状态：明确“当前页面能操作什么”</li>
  </ul></div>
  <div class="col"><h4>关键区别</h4><ul>
    <li>MCP 连远程服务器，WebMCP 连用户正开着的页面</li>
    <li>渐进增强：不支持就退回 DOM 操作</li>
    <li>工具在页面里跑，用户看得见</li>
  </ul></div></div>''', A, H, P, "WebMCP"))
s.append(page("02 / 有什么", "两条注册路径，一套安全注解", cards([
  ("IMPERATIVE", "registerTool()", "name / description / inputSchema / execute"),
  ("DECLARATIVE", "表单属性", "toolname + tooldescription，Schema 自动派生"),
  ("ANNOTATIONS", "四个提示", "只读、不可信内容、高影响、仅调试"),
  ("DISCOVERY", "getTools()", "同源默认，跨源要显式 fromOrigins"),
  ("EXECUTION", "executeTool()", "带 AbortSignal，可取消"),
  ("CROSS-ORIGIN", "三重开关", "allow=tools + exposedTo + fromOrigins"),
], 3), A, H, P, "WebMCP"))
s.append(page("03 / 怎么用", "一个工具，两个属性，零胶水代码", codeblock(
'''await document.modelContext.registerTool({
  name: "book_flight",
  description: "为用户预订已确认的航班。",
  inputSchema: {
    type: "object",
    properties: {
      flightId: { type: "string" },
      passengers: { type: "number" },
    },
    required: ["flightId", "passengers"],
  },
  annotations: { consequentialHint: true },
  execute: async ({ flightId, passengers }, { signal }) =>
    bookFlight({ flightId, passengers, signal }),
});''',
"三点提醒", [
 "description 是提示词，不是 UI 标签",
 "consequentialHint 让浏览器强制二次确认",
 "返回结果建议加 outputSchema 做校验",
]), A, H, P, "WebMCP"))
s.append(page("04 / 价值", "更准的智能体，更低的成本", f'''<div class="two">
  <div class="col"><h4>对用户</h4><ul>
    <li>工具在页面上执行，过程可见</li>
    <li>高影响操作被强制确认</li>
    <li>数据留在浏览器，不送到自动化服务器</li>
  </ul></div>
  <div class="col cost"><h4>代价</h4><ul>
    <li>2026 年约 12 次破坏性变更，API 仍在动</li>
    <li>注解只是提示，客户端可以不遵守</li>
    <li>跨源要三方同时开，缺一不可</li>
  </ul></div></div>''', A, H, P, "WebMCP"))

open(f"{OUT}/webmcp.html", "w", encoding="utf-8").write(
    shell("WebMCP", "\n".join(s)))

# ============ 3. WebGPU ============
A, H, P = "#ff7daf", "#ff7daf", "#f8d8d8"
s = []
s.append(cover("WEBGPU · 2023–2026", "GPU 不再<br>长得像 WebGL",
  "显式的管线、真正的计算着色器、一个 API 打通 Vulkan / Metal / D3D12。",
  ["Chrome 113 桌面", "Chrome 144 Linux", "兼容模式到 OpenGL ES 3.1"], "#ea4335", "#ff7daf", "#f8d8d8", "WebGPU"))
s.append(page("01 / 它是什么", "从状态机到显式对象模型", f'''<div class="grid g2" style="margin-top:0">
  <div class="card"><div class="n">WEBGL 2</div><h3>全局状态机</h3><p>隐式状态、GLSL、无计算着色器、仅主线程</p></div>
  <div class="card"><div class="n">WEBGPU</div><h3>显式管线</h3><p>adapter → device → pipeline → command buffer；WGSL；一等公民的计算</p></div>
</div>
<div style="margin-top:26px">{bullets(["Dawn 负责跨平台：Vulkan / Metal / D3D12 / OpenGL ES","兼容模式让老设备也能跑，代价是特性子集","几乎所有高级特性都是可选的，必须探测"])}</div>''', "#ea4335", "#ff7daf", "#f8d8d8", "WebGPU"))
s.append(page("02 / 有什么", "三条主线：算力、语言、覆盖", cards([
  ("COMPUTE", "为设备端 ML 成熟", "子组大小控制、immediates、subgroup_id"),
  ("WGSL", "写起来更像语言", "buffer_view、swizzle_assignment、linear_indexing"),
  ("REACH", "覆盖更多设备", "Linux、NVIDIA、兼容模式 OpenGL ES 3.1"),
  ("DIAGNOSE", "可调试", "getCompilationInfo() 给出行列号"),
  ("ASYNC", "不阻塞主线程", "createComputePipelineAsync 等"),
  ("LIFECYCLE", "设备会丢", "device.lost 是常态，不是异常"),
], 3), "#ea4335", "#ff7daf", "#f8d8d8", "WebGPU"))
s.append(page("03 / 怎么用", "一个计算着色器，端到端", codeblock(
'''const shader = device.createShaderModule({ code: `
  @group(0) @binding(0) var<storage, read>       input  : array<f32>;
  @group(0) @binding(1) var<storage, read_write> output : array<f32>;

  @compute @workgroup_size(64)
  fn main(@builtin(global_invocation_id) id : vec3u) {
    let i = id.x;
    if (i >= arrayLength(&input)) { return; }
    output[i] = input[i] * 2.0;
  }
`});

const pass = encoder.beginComputePass();
pass.setPipeline(pipeline);
pass.setBindGroup(0, bindGroup);
pass.dispatchWorkgroups(Math.ceil(N / 64));
pass.end();''',
"容易踩的两点", [
 "管线创建是异步的，生产环境用 Async 版本",
 "bind group 要自己布局，@group/@binding 必须对齐",
 "Chrome 140 起，请求设备会消耗 adapter",
], small=True), "#ea4335", "#ff7daf", "#f8d8d8", "WebGPU"))
s.append(page("04 / 价值", "桌面级图形，进了一个标签页", f'''<div class="two">
  <div class="col"><h4>对用户</h4><ul>
    <li>游戏、CAD、视频编辑不用装客户端</li>
    <li>设备端 AI 不上传数据</li>
    <li>HDR 与广色域终于对得上屏幕</li>
  </ul></div>
  <div class="col cost"><h4>代价</h4><ul>
    <li>关键特性全是可选的，没有保证的基线</li>
    <li>API 仍会破坏性变更（140 就移除过两个）</li>
    <li>文档碎裂：核心内容在 changelog 里</li>
  </ul></div></div>''', "#ea4335", "#ff7daf", "#f8d8d8", "WebGPU"))

open(f"{OUT}/webgpu.html", "w", encoding="utf-8").write(
    shell("WebGPU", "\n".join(s)))

# ============ 4. Baseline ============
A, H, P = "#fbbc04", "#ffd427", "#ffe7a5"
s = []
s.append(cover("BASELINE · WEB PLATFORM DX", "一个词，<br>替代一张版本表",
  "不是技术，是共识。MDN、Can I Use、Babel、stylelint 读同一份定义。",
  ["三态：Limited / Newly / Widely", "30 个月规则", "2026 新增告警"], A, H, P, "Baseline"))
s.append(page("01 / 它是什么", "把“能不能用”变成一个状态", f'''<div class="grid g3" style="margin-top:0">
  <div class="card"><div class="n">LIMITED</div><h3>尚未互通</h3><p>不能在无降级的情况下上线</p></div>
  <div class="card"><div class="n">NEWLY</div><h3>四大内核都支持</h3><p>可互操作，但仍很新</p></div>
  <div class="card"><div class="n">WIDELY</div><h3>新可用满 30 个月</h3><p>多数站点可以放心用的默认值</p></div>
</div>
<div style="margin-top:26px">{bullets(["核心浏览器 = Chrome / Edge / Firefox / Safari，桌面 + 移动","数据源是 web-features，由 W3C WebDX 社区组维护","下游 Chromium 浏览器要显式 opt-in"])}</div>''', A, H, P, "Baseline"))
s.append(page("02 / 有什么", "目标可声明，工具链直接继承", f'''<div class="two">
  <div class="col"><h4>两类目标</h4><ul>
    <li>移动目标：newly / widely available</li>
    <li>固定目标：baseline 2023 / 2024，写死不再变</li>
    <li> downstream 可加：Samsung Internet、Opera</li>
  </ul></div>
  <div class="col"><h4>接入面</h4><ul>
    <li>MDN 徽章、Can I Use、webstatus.dev</li>
    <li>Browserslist → Babel / postcss / stylelint</li>
    <li>baseline-browser-mapping 对接自有 RUM</li>
  </ul></div></div>''', A, H, P, "Baseline"))
s.append(page("03 / 怎么用", "一行配置，管住整条工具链", codeblock(
'''// package.json
{
  "browserslist": [
    "baseline widely available"
  ]
}

// .stylelintrc.js
module.exports = {
  plugins: ["stylelint-browser-compat"],
  rules: {
    "plugin/browser-compat": [true, {
      browserslist: ["baseline widely available"],
    }],
  },
};''',
"实测效果", [
 "同一份源码，12 KB → 1.5 KB",
 "Babel、Autoprefixer、stylelint 自动继承",
 "固定年份会过期，widely 会随生态推进",
]), A, H, P, "Baseline"))
s.append(page("04 / 价值", "少吵版本，多做功能", f'''<div class="two">
  <div class="col"><h4>对用户</h4><ul>
    <li>少一些“只在 Chrome 能用”的页面</li>
    <li>包更小，页面更快</li>
    <li>四内核一致，不是单一厂商的实现</li>
  </ul></div>
  <div class="col cost"><h4>代价</h4><ul>
    <li>30 个月是政策选择，不覆盖企业内网与 kiosk</li>
    <li>“Widely”描述核心浏览器，不描述你的用户</li>
    <li>不评价性能、无障碍与安全质量</li>
  </ul></div></div>''', A, H, P, "Baseline"))

open(f"{OUT}/baseline.html", "w", encoding="utf-8").write(
    shell("Baseline", "\n".join(s)))

# ============ 5. Modern Web Guidance ============
A, H, P = "#4285f4", "#57caff", "#c3ecf6"
s = []
s.append(cover("MODERN WEB GUIDANCE · 1.0", "让编码智能体<br>写 2026 年的 Web 代码",
  "不是一个 API，是一个装进智能体的技能：200+ 篇浏览器工程师写的指南。",
  ["1.0 · 2026-11-10", "Chrome + Firefox + Edge", "检索命中率 95.4%"], A, H, P, "Modern Web Guidance"))
s.append(page("01 / 它是什么", "一份技能，不是运行时", f'''<div class="two">
  <div class="col"><h4>解决的问题</h4><ul>
    <li>模型默认用 JS，即使 HTML/CSS 已能做</li>
    <li>手写 div + 焦点陷阱，替代 &lt;dialog&gt;</li>
    <li>能跑，但更差</li>
  </ul></div>
  <div class="col"><h4>关键性质</h4><ul>
    <li>人工策展，不是抓取，1.7 MB Markdown</li>
    <li>感知 Baseline，按支持目标过滤</li>
    <li>有公开评测看“用与不用”的差别</li>
  </ul></div></div>''', A, H, P, "Modern Web Guidance"))
s.append(page("02 / 有什么", "渐进披露，是设计约束", f'''<div class="grid g3" style="margin-top:0">
  <div class="card"><div class="n">AT REST</div><h3>~205 tokens</h3><p>只有技能描述，挂在智能体上下文里</p></div>
  <div class="card"><div class="n">SEARCH</div><h3>~530 tokens</h3><p>10 条紧凑结果，不返回相似度与计数</p></div>
  <div class="card"><div class="n">RETRIEVE</div><h3>~800 tokens</h3><p>只拉真正需要的那一篇完整指南</p></div>
</div>
<div style="margin-top:30px">
{table(["检索引擎","包体积","命中率"], [["Gen 2 · TF.js + MiniLM","23.4 MB","80.6%"],["Gen 3 · Int8 + BM25 混合","<b>7.1 MB</b>","<b>95.4%</b>"]])}
</div>''', A, H, P, "Modern Web Guidance"))
s.append(page("03 / 怎么用", "装一次，之后由智能体自己调用", codeblock(
'''npx modern-web-guidance@latest install

# 智能体在后台执行
npx modern-web-guidance search "animate height auto"
npx modern-web-guidance retrieve animate-to-intrinsic-sizes

# 改造存量代码
/modern-web-guidance Modernize the code in this directory''',
"为什么是 CLI", [
 "MCP 要么浪费 token，要么触发不稳",
 "网页搜索会给回 2015 年的答案",
 "本地 CLI 毫秒级、离线、可复现",
]), A, H, P, "Modern Web Guidance"))
s.append(page("04 / 价值", "让智能体少写一点，写对一点", f'''<div class="two">
  <div class="col"><h4>对用户</h4><ul>
    <li>焦点管理与 reduced-motion 默认正确</li>
    <li>结账与登录不再被自定义控件搞坏自动填充</li>
    <li>页面更轻，布局偏移更少</li>
  </ul></div>
  <div class="col cost"><h4>代价</h4><ul>
    <li>它只指导，不验证，必须配 DevTools 实测</li>
    <li>1.0 的现代化改造是基于模式的静态分析</li>
    <li>遥测默认开启，需要手动关</li>
  </ul></div></div>''', A, H, P, "Modern Web Guidance"))

open(f"{OUT}/modern-web-guidance.html", "w", encoding="utf-8").write(
    shell("Modern Web Guidance", "\n".join(s)))

# ============ 6. DevTools ============
A, H, P = "#34a853", "#5cdb6d", "#ccf6c5"
s = []
s.append(cover("CHROME DEVTOOLS · 2025–2026", "DevTools 成了<br>智能体的运行时",
  "两个产品：面板里的 Gemini，和给编码智能体的 MCP 服务器。",
  ["MCP 已发布", "AI 辅助仍实验", "支持 6 种客户端"], A, H, P, "DevTools for agents"))
s.append(page("01 / 它是什么", "两个产品，别混为一谈", f'''<div class="grid g2" style="margin-top:0">
  <div class="card"><div class="n">INSIDE-OUT</div><h3>AI 辅助</h3><p>你在面板里问 Gemini：为什么慢、为什么坏。实验性。</p></div>
  <div class="card"><div class="n">OUTSIDE-IN</div><h3>DevTools for agents</h3><p>智能体通过 MCP 驱动真实 Chrome，验证它刚写的东西。</p></div>
</div>
<div style="margin-top:26px">{bullets(["两者在一个点上交接：AI 辅助可以生成提示词交给智能体","MCP 走 puppeteer → CDP → DevTools 前端逻辑","只支持 Chrome 与 Chrome for Testing"])}</div>''', A, H, P, "DevTools for agents"))
s.append(page("02 / 有什么", "把面板能力变成可调用工具", cards([
  ("PERF", "真实 trace", "performance_analyze_insight 返回 DevTools 的解读"),
  ("NETWORK", "请求与响应", "列表 + 单条详情，带 source map"),
  ("DOM", "快照与样式", "take_snapshot、get_css_styles"),
  ("INTERACT", "点击与填写", "click / fill_form / upload_file / handle_dialog"),
  ("EMULATE", "设备与网络", "CPU、网络、视口一起模拟"),
  ("AUDIT", "Lighthouse", "无障碍、SEO、性能随手跑"),
], 3), A, H, P, "DevTools for agents"))
s.append(page("03 / 怎么用", "三行配置，接进任意 MCP 客户端", codeblock(
'''{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}

// 或者不进 MCP，直接用 CLI
chrome-devtools navigate_page 1 --url "https://example.com"
chrome-devtools take_screenshot 1 --filePath shot.png''',
"为什么好用", [
 "source map 让智能体看到真实错误位置",
 "screencast 让它能“看”动画效果",
 "auto-connect 可接管你已登录的标签页",
]), A, H, P, "DevTools for agents"))
s.append(page("04 / 价值", "从“看着像对”到“实测通过”", f'''<div class="two">
  <div class="col"><h4>对开发者</h4><ul>
    <li>省掉“打开面板 → 复现 → 复制到聊天”的往返</li>
    <li>无障碍与性能审计变得便宜</li>
    <li>CLI 让同一套能力进 CI</li>
  </ul></div>
  <div class="col cost"><h4>代价</h4><ul>
    <li>auto-connect 等于交出一台已解锁的电脑</li>
    <li>MCP 遥测默认开启，需显式关闭</li>
    <li>trace 又慢又费 token，不能无脑跑</li>
  </ul></div></div>''', A, H, P, "DevTools for agents"))

open(f"{OUT}/devtools.html", "w", encoding="utf-8").write(
    shell("Chrome DevTools MCP & AI", "\n".join(s)))

# ============ 7. Web UI features ============
A, H, P = "#ea4335", "#ff7daf", "#f8d8d8"
s = []
s.append(cover("NEW WEB UI · 2024–2026", "平台正在<br>吞掉 JavaScript",
  "HTML 拿到声明式行为，CSS 拿到逻辑，JS 拿到状态保持。",
  [":has() 80.4% 使用率", "dialog 52.8%", "moveBefore 仅 6.3% 知道"], A, H, P, "New Web UI Features"))
s.append(page("01 / 它是什么", "不是更多框架，是更少代码", f'''<div class="two">
  <div class="col"><h4>五条 UX 原则</h4><ul>
    <li>尊重用户偏好：对比度、配色、字号</li>
    <li>自然交互：物理动效，不靠库</li>
    <li>引导式导航：跨状态、跨页面保留上下文</li>
    <li>内容优先：去掉边框与浮层噪音</li>
    <li>适配形态：输入方式、视口与画布</li>
  </ul></div>
  <div class="col"><h4>一句话</h4><ul>
    <li>把常见 UI 工作从 JS 移进标记与样式</li>
    <li>约 35 项特性，多数已稳定</li>
    <li>全部按 Baseline 追踪</li>
  </ul></div></div>''', A, H, P, "New Web UI Features"))
s.append(page("02 / 有什么", "三条线，同一个方向", f'''<div class="grid g3" style="margin-top:0">
  <div class="card"><div class="n">HTML</div><h3>声明式行为</h3><p>text-scale、closedby、layoutsubtree</p></div>
  <div class="card"><div class="n">CSS</div><h3>逻辑与动效</h3><p>@function、if()、容器样式查询、四种 view transition</p></div>
  <div class="card"><div class="n">JS</div><h3>状态保持</h3><p>moveBefore()、pseudo()、awaitable scroll</p></div>
</div>
<div style="margin-top:28px">
{table(["需求信号（State of CSS / HTML 2025）","数值"], [
 ["最常用也最喜爱：:has()","80.4%"],["&lt;dialog&gt; 使用率","52.8%"],["Popover API 使用率","20.6%"],["moveBefore() 从未听说","74.5%"]])}
</div>''', A, H, P, "New Web UI Features"))
s.append(page("03 / 怎么用", "三个特性协作，零 JS 弹窗", codeblock(
'''<dialog id="confirm" closedby="any">…</dialog>
<button commandfor="confirm" command="show-modal">删除</button>

<style>
dialog { opacity:0; transform:translateY(8px);
  transition: opacity .2s, transform .2s, overlay .2s allow-discrete; }
dialog[open] { opacity:1; transform:none; }
@starting-style { dialog[open] { opacity:0; transform:translateY(8px); } }
</style>

<script>
// 换父节点，但不丢播放、焦点、iframe 状态
newParent.moveBefore(video, null);
</script>''',
"三件事同时消失", [
 "没有 click 处理器（commandfor）",
 "没有外部点击监听（closedby）",
 "没有动画库（@starting-style）",
], small=True), A, H, P, "New Web UI Features"))
s.append(page("04 / 价值", "用户少等，开发者少写", f'''<div class="two">
  <div class="col"><h4>对用户</h4><ul>
    <li>字号跟随系统设置，一行 meta 解决</li>
    <li>原生弹窗自带焦点管理与顶层</li>
    <li>滚动动效离开主线程，不卡</li>
  </ul></div>
  <div class="col cost"><h4>代价</h4><ul>
    <li>Chrome-first 不等于可用，最大痛点是浏览器支持</li>
    <li>认知落后支持 12–24 个月</li>
    <li>“无 JS”在旧浏览器降级为“没有”</li>
  </ul></div></div>''', A, H, P, "New Web UI Features"))

open(f"{OUT}/web-ui-features.html", "w", encoding="utf-8").write(
    shell("New Web UI Features", "\n".join(s)))

# ============ index ============
DECKS = [
 ("chrome-ai.html", "Chrome Built-in AI APIs", "七个设备端 API：提示、摘要、翻译、校对、向量、分类", "5 页", "#4285f4"),
 ("webmcp.html", "WebMCP", "让页面把能力声明成工具，给智能体调用", "5 页", "#34a853"),
 ("webgpu.html", "WebGPU", "计算着色器与显式管线，跨 Vulkan / Metal / D3D12", "5 页", "#ea4335"),
 ("baseline.html", "Baseline", "把“能不能用”变成三态共识，驱动整条工具链", "5 页", "#fbbc04"),
 ("modern-web-guidance.html", "Modern Web Guidance", "装进编码智能体的 200+ 篇 Web 平台指南", "5 页", "#4285f4"),
 ("devtools.html", "DevTools MCP & AI", "面板里的 Gemini，与给智能体的浏览器运行时", "5 页", "#34a853"),
 ("web-ui-features.html", "New Web UI Features", "HTML 拿到行为、CSS 拿到逻辑、JS 拿到状态保持", "5 页", "#ea4335"),
]
cards_html = ""
for href, name, desc, pages, color in DECKS:
    cards_html += f'''<a class="deck-card" href="{href}">
      <span class="bar" style="background:{color}"></span>
      <h3>{name}</h3><p>{desc}</p><span class="pages">{pages} →</span></a>'''

index = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>New Web Features — 幻灯片预览</title><style>
body{{margin:0;background:#f0f0f0;color:#1e1e1e;
font-family:'Google Sans','Roboto','Noto Sans SC','PingFang SC',system-ui,sans-serif}}
.wrap{{max-width:1060px;margin:0 auto;padding:64px 32px 96px}}
.top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:42px}}
.top img{{height:34px}}
.kicker{{font-family:'Roboto Mono',monospace;font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:#5f6368}}
h1{{font-size:50px;letter-spacing:-.02em;margin:0 0 10px}}
.lead{{font-size:19px;color:#3c4043;margin-bottom:40px;max-width:760px}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.deck-card{{position:relative;background:#fff;border:1.5px solid #1e1e1e;border-radius:18px;
padding:24px 26px 20px;text-decoration:none;color:inherit}}
.deck-card:hover{{background:#fafafa}}
.bar{{display:inline-block;width:26px;height:6px;border-radius:3px;margin-bottom:14px}}
.deck-card h3{{margin:0 0 8px;font-size:21px}}
.deck-card p{{margin:0 0 16px;font-size:14.5px;line-height:1.5;color:#3c4043}}
.pages{{font-family:'Roboto Mono',monospace;font-size:12.5px;color:#5f6368}}
@media(max-width:760px){{.grid{{grid-template-columns:1fr}}h1{{font-size:36px}}}}
</style></head><body><div class="wrap">
<div class="top"><div class="kicker">DF'26 SHENZHEN · HTML PREVIEW</div><img alt="DevFest" src="data:image/png;base64,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"></div>
<h1>New Web Features</h1>
<div class="lead">七份报告，按同一模板生成：封面 → 是什么 → 有什么 → 怎么用 → 价值。方向键或滚动翻页。</div>
<div class="grid">{cards_html}</div>
</div></body></html>'''

open(f"{OUT}/index.html", "w", encoding="utf-8").write(index)
print("files:", sorted(os.listdir(OUT)))
