# DF'26 Shenzhen 幻灯片模板 — 风格与布局指南

> 用途：下次生成幻灯片时，先用 HTML 出预览（16:9、本指南配色/字体），用户确认后一次性生成 .pptx。
> 源模板：`Jax-DF'26-Shenzhen.pptx`（**56 页**风格参考，含 halftone 底图 PNG）。
> 工具：`tools/pptx_deck.py`（unpack / keep / replace-text / fonts / pack / check / dump）。

---

## 1. 配色（Google Material）

| 角色 | 色值 | 说明 |
|---|---|---|
| Blue | `#4285f4` | 主蓝 |
| Green | `#34a853` | 主绿 |
| Red | `#ea4335` | 主红 |
| Yellow | `#fbbc04` | 主黄 |
| Halftone Blue | `#57caff` | 底图网点蓝 |
| Halftone Green | `#5cdb6d` | 底图网点绿 |
| Halftone Pink | `#ff7daf` | 底图网点粉 |
| Halftone Yellow | `#ffd427` | 底图网点黄 |
| Pastel Blue | `#c3ecf6` | 浅色块 |
| Pastel Green | `#ccf6c5` | 浅色块 |
| Pastel Red | `#f8d8d8` | 浅色块 |
| Pastel Yellow | `#ffe7a5` | 浅色块 |
| Off-White | `#f0f0f0` | 页面底色 |
| Black 02 | `#1e1e1e` | 正文黑 |

主色规则：一页只用 1 个主色 + 同色系 halftone + 同色系 pastel。

## 2. 字体

| 用途 | 字体 | 字号（pt） |
|---|---|---|
| 大标题/声明 | Google Sans Bold | 30 |
| 副标题/kicker | Roboto Mono Light | 16 |
| 正文/条目 | Google Sans Normal | 25 / 20 |
| 大数字（stat） | Google Sans Medium | 110 |

⚠️ **中文字体**：Google Sans 无 CJK 字形。生成中文时，`a:ea` 字体改为 **PingFang SC**（Mac 原生）；Windows 放映建议改「微软雅黑」。拉丁字符/数字仍用 Google Sans。

## 3. 布局清单（放映页序 → slide 文件）

> ⚠️ **页序 ≠ 文件名**。下表「页」是放映顺序，右列才是要 `keep` 的 `slideN.xml`。以 `python3 tools/pptx_deck.py dump` 输出为准。

| 页 | slide 文件 | 布局 | 用途 |
|---|---|---|---|
| 1–3 | slide1–3 | 配色字体规格 / 分隔页 | 参考，跳过 |
| 4–7 | slide4–7 | 标题页（标题 + 讲者 + 地点） | 封面/开场 |
| 8–12 | slide8–12 | 小节页（单行→5 行，编号 01–05） | 章节页 |
| 13–16 | slide13–16 | 小节标题 + 副标题 + 地点 | 章节页 |
| 17 | slide17 | 「Content Slides」分隔页 | 跳过 |
| 18–20 | slide18–20 | 整屏 / 大段文字 | 长文本 |
| 21 | slide21 | 条目排版规格（20pt 主条 / 25pt 正文） | 参考，跳过 |
| **22** | slide22 | **单行标题 + 4 条** | 观点总览 |
| **23** | slide23 | **双行标题 + 4 条** | 观点总览 |
| 24–28 | slide24–28 | 陈述/引述 + 地点 | 大字陈述 |
| **29** | slide29 | **大数字 stat**（50% + 2 标签） | 关键数据 |
| 30–31 | slide30–31 | 纯图 stat 变体（无可编辑文本） | 关键数据 |
| 32 | slide32 | 半屏讲者 | 讲者出镜 |
| **33–34** | slide33–34 | **无标题大字声明** | 封面 / 金句 |
| 35–40 | slide35–40 | 大数字 stat 变体 | 关键数据 |
| 41 | slide41 | 无标题大字声明 | 金句 |
| **42** | slide42 | **单行标题 + 引述** | 论点 + 证据 |
| **43** | slide43 | **双行标题 + 引述** | 论点 + 证据 |
| **44** | slide44 | 单行标题 + 4 条（照片拼贴，**窄**） | 条目 |
| **45** | slide45 | 双行标题 + 4 条（照片拼贴，**窄**） | 条目 |
| **46** | slide46 | **引述 + 署名 + 地点** | 结论 / 判定 |
| 47–56 | slide47–56 | 图表：元素/简单/全能/大组合/流程/流式/分组/分层/折线 | 图表 |

**关键约束（实测）**：
- 宽版条目页（22/23）：每条 1–2 行，约 **28 字/行**。
- 窄版照片拼贴页（44/45）：每条 ≤ 2 行，约 **12 字/行**，总行数 ≤ 7，否则溢出（上次溢出的正是这类）。
- 标题上限：单行最安全；5 行标题仅 slide12/16。

## 4. 推荐内容映射（7 页范式）

| 页 | 用途 | slide 文件 |
|---|---|---|
| 1 | 封面 / 论点（无标题大字声明） | slide34 |
| 2 | 核心观点总览（单行标题 + 4 条） | slide22 |
| 3 | 论断 A 数据（大数字 stat） | slide29 |
| 4 | 论断 B（单行标题 + 引述） | slide42 |
| 5 | 论断 C+D（双行标题 + 4 条） | slide23 |
| 6 | 判定 / 结论（引述 + 署名） | slide46 |
| 7 | 中国视角（双行标题 + 4 条，窄版） | slide45 |

## 5. Google Slides 导入（最终格式）

> 最终目标是 Google Slides，不是 .pptx。`.pptx` 是导入 Slides 的原生桥：`File → Import slides`（或把 .pptx 拖进 Drive 后用 Slides 打开）即可，halftone 底图/形状/配色/文本框几乎无损保留。

**字体映射（生成 .pptx 时直接写 Slides 原生字体，导入后无需手动改字体）：**

| 模板字体 | 目标（Google Slides 原生） |
|---|---|
| Google Sans Bold / Normal / Medium | Roboto（Bold / Regular / Medium） |
| Roboto Mono Light | Roboto Mono |
| PingFang SC（CJK） | Noto Sans SC |

## 6. 生成工作流（备忘）

**本地工具 `tools/pptx_deck.py`**（纯标准库，Python 3.9+ 可用）：

**模板缓存 `unpacked/`**：已解包并常驻（13 MB，`unpacked/.cache-source.json` 记录源文件 sha1）。
下次直接用，不必重新解包；`unpacked/` 已在 `.gitignore` 中，不会污染 git。

```bash
T="Jax-DF'26-Shenzhen.pptx"
python3 tools/pptx_deck.py status       unpacked/          # 先确认缓存未过期
python3 tools/pptx_deck.py dump         unpacked/          # 看真实页序 + 全部文本
python3 tools/pptx_deck.py keep         unpacked/ 34,22,29,42,23,46,45
python3 tools/pptx_deck.py replace-text unpacked/ slide22.xml "Example with slide title" "一个悖论，四个论断"
python3 tools/pptx_deck.py fonts        unpacked/ Roboto "Noto Sans SC"
python3 tools/pptx_deck.py pack         unpacked/ out.pptx
python3 tools/pptx_deck.py check        out.pptx           # XML 完整性 + 关系链
```

⚠️ **模板一改，缓存即失效**（本次就发生过：模板从 40 页 5.4 MB 换成 56 页 12.4 MB，旧页码全部作废）。
先跑 `status`：报 `STALE` 就按提示重新 `unpack`，再重新 `dump` 核对页序。

- ⚠️ `keep` 会改 `presentation.xml`，缓存就不再是原始模板；改完想恢复就重新 `unpack`。
- `keep` 只重写 `presentation.xml` 的 `sldIdLst`；未引用的页/媒体仍留在包里，但不会放映（体积略大，无害）。需要瘦身再跑插件的 `clean.py`。
- `replace-text` 只匹配**完整文本 run**，找不到就报错退出（避免 `.replace()` 静默失败）。文本被拆成多个 run 时用 `set-text <slide> <n> <text>` 按序号改。
- `fonts` 同时改 `slides / slideLayouts / slideMasters / notesSlides`，并跳过 `+mj-lt` 这类主题引用。
- ⚠️ 插件的 `pack.py` 用 `str | None` 语法，**需 Python 3.10+**；本工具的 `pack` 用 `zipfile`，3.9 也能跑。
- `validate_layout.py` 的「Picture 越界/重叠」告警是模板 halftone 底图**故意出血**，属误报；只需关注「content bottom edge」文字溢出。
- 输出样例：`front-end-paradox-DF26-Shenzhen.pptx`（7 页，已验证 0 溢出，已导入 Google Slides）。
