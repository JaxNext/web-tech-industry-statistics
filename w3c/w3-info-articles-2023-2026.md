# W3资讯 — Web Tech 文章索引（近三年）

抓取自微信公众号 **W3资讯**（`__biz=MzA3OTY5NDI0OA==`）的三个文章专辑：Web、CSS、AI。

- **时间范围**：2023-11-27 – 2026-11-25
- **去重后文章数**：137
- **原始条目**：176 条，跨专辑重复 13 条；另 26 条早于 2023-11-26，未收录
- **专辑覆盖**：Web 125 条、CSS 14 条、AI 37 条（含 2023 年前）

**方法**：调用微信专辑接口 `mp/appmsgalbum?action=getalbum&f=json`，按 `begin_msgid` / `begin_itemidx` 分页抓取（每页 20 条），直至返回空页；按 `msgid` 去重、按发布时间倒序。链接保留专辑返回的原始形式（含 `chksm`），因为去掉校验参数的短链会触发微信验证码。

**两点已知局限**：

1. **专辑是人工收录，不是全量发文。** 2025-06 至 2025-09 等月份在专辑中没有条目，这不代表该账号当月未发文，只代表未加入专辑。做趋势统计时，月度缺口不能当作「停更」证据。
2. **专辑划分是公众号的栏目，不是主题分类。** 同一篇文章可能同时属于 Web 和 AI，表中合并为一行。主题归类需要自行按标题二次判断。

---

## 一、年度分布

| 年份 | Web | CSS | AI | 去重合计 |
|---|---|---|---|---|
| 2026 | 1 | 2 | 31 | 34 |
| 2025 | 26 | 6 | 3 | 31 |
| 2024 | 70 | 4 | 3 | 70 |
| 2023 | 2 | 0 | 0 | 2 |
| **合计** | 99 | 12 | 37 | **137** |

## 二、文章清单

### 2026（34 篇）

| 日期 | 标题 | 专辑 | 链接 |
|---|---|---|---|
| 2026-11-25 | W3C发布《用户代理》小组备忘：软件如何真正为用户服务 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247491191&idx=1&sn=e658ebfd483e10214372a7393c82de3c&chksm=9faeceb0a8d947a63f3e3d16fdbae3fb5fae31981e4ed84e32b02dd04ab6a8a7002cd74d5139#rd) |
| 2026-11-24 | 首个公开工作草案：指针驱动动画模块第1级 | CSS | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247491187&idx=1&sn=75978ee19b1da92bfd9367c45cb1c5fa&chksm=9faeceb4a8d947a229c427a8f5e116633c42d542a05456c80a5e6435ff640cf80b7676c7b893#rd) |
| 2026-11-23 | [视频] web-features项目进展：让开发者声音直达Web平台未来 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247491182&idx=1&sn=565e44ba6091734615cd3aefaab7c7b4&chksm=9faecea9a8d947bf3683a4cc2ec1052c28a59f8355eea07067caf0c076c9db3d9c6ca64fb2aa#rd) |
| 2026-09-23 | 总结报告｜探索Agentic Web未来：Web & AI国际标准研讨论坛聚焦生成式UI与WebSkill | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247491089&idx=1&sn=0c7478dae689d03efc852f4e9c91cc88&chksm=9faeced6a8d947c0d900104247395ba9177f137017b111ae0fee4b0941ab4c7ccf361fdde8f5#rd) |
| 2026-09-04 | 即将开启｜Web & AI国际标准研讨论坛聚焦生成式UI与WebSkill | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247491062&idx=1&sn=7a8e8fc78085b4f689165b8ec1db6a7d&chksm=9faecd31a8d94427ee1810d600ef8bc8e76bd62cd8226ab9589428de7934d119c01bfbe32bb4#rd) |
| 2026-08-31 | 议程发布｜Web & AI国际标准研讨聚焦生成式UI与WebSkill | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247491052&idx=1&sn=5471d04d9b646916cd500c8be72785fd&chksm=9faecd2ba8d9443df79b5a01a29bde9609f6de8c001b5630dd19683a18f639d6f76593580e89#rd) |
| 2026-08-20 | 报名开启｜Web & AI国际标准研讨分论坛聚焦生成式UI与WebSkill | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247491034&idx=1&sn=59a19f7d23a78721cf3935adeb5828eb&chksm=9faecd1da8d9440bae77e48a82d7dcaecdea86b697bde2bbb851a7e45a92c0907b808ce5b25f#rd) |
| 2026-08-13 | [会议日程] W3C/GS1“面向人类与AI智能体的电子商务”技术研讨会 · 9月8-9日 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247491029&idx=1&sn=b64a22d8303c70f495b132e30b4109de&chksm=9faecd12a8d9440468cb2d4a5a70268f9fe44197a2b1f71d98cb338db58f1165e80a98217c74#rd) |
| 2026-07-23 | 首个公开工作草案：CSS链接参数模块级别1 | CSS | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247491004&idx=1&sn=47874c17cd06b89117b59a322b0298e7&chksm=9faecd7ba8d9446da286d5d05c2ba882a7ad69154a164b586a8a884b2d6f2dabb885e1c1badb#rd) |
| 2026-07-16 | WebSkill - Agentic Web面向SaaS的进化 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490999&idx=1&sn=d33c307be2d5f793fa2b1a835b1f2eb2&chksm=9faecd70a8d944660a89fea1396f3e46cf8f436ed9701145dd6dc8d4bb4cba2de4f8367d4fcf#rd) |
| 2026-07-13 | [视频] Design Systems与Vibe Coding | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490972&idx=1&sn=c2185526ff7d6deed3810c5647d7c25c&chksm=9faecd5ba8d9444ddca463bbf19793a122d84d8a1775c030d48d16e699ed364001d700bb7692#rd) |
| 2026-07-10 | [视频] OpenTiny GenUI：实时个性化生成式UI，重塑AI交互 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490967&idx=1&sn=45b057769bb701fd2036085771770e53&chksm=9faecd50a8d94446eb64b5693aa799a868404a6d38f9d14881f6bfab9c840074a7485f744559#rd) |
| 2026-06-26 | [视频] AI、Web与标准 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490942&idx=1&sn=08c4b7d50341bfd0628fe6fd608ccb10&chksm=9faecdb9a8d944afa46cd40cf6add701bab7642bfc8bd0f24566e1394bd8d513cfe2e0f1e7b3#rd) |
| 2026-06-23 | [视频] AWiki：基于W3C DID的智能体身份与端到端加密通讯 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490937&idx=1&sn=12f78abb11245025e30b0d597d63514d&chksm=9faecdbea8d944a8d488dc2eab6798e993d3cbf6bf57f779b4498bdaab0b1bba7f043e8de30f#rd) |
| 2026-06-22 | [视频] 基于AI重构Web应用体验 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490932&idx=1&sn=b3483267d4fbc7021a203e5633546952&chksm=9faecdb3a8d944a56bd3d6d86811dd610c647b4ebbf42517ec0b28961d3766bd182828de3853#rd) |
| 2026-06-11 | [视频] 生态智能体互联技术的探索与实践 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490915&idx=1&sn=85e5363ede805376f1c17a00902194a6&chksm=9faecda4a8d944b29a8e05b637607c58ab6a659633b6948340c6048266eeb5829d944122dd73#rd) |
| 2026-06-09 | [视频] AI时代科技向善：C2PA作为AI图像标注的一种可行方案 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490910&idx=1&sn=93e500f16467ec0ffa1335a86000fc43&chksm=9faecd99a8d9448f6940a6a25f94e2edc8181348cbcbd35384e0408f9546e6aba5ce30284c20#rd) |
| 2026-06-08 | [视频] Utoo WASM：AI时代的超快速开发套件 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490903&idx=1&sn=40be9a102ad258be0b2bc789201f5549&chksm=9faecd90a8d94486304e74f8ea1cabe7a8ed12cd6dda9f20c97ee3f83817900133dbe12408be#rd) |
| 2026-06-02 | W3C与GS1将联合举办“面向人类与AI智能体的电子商务”技术研讨会 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490886&idx=1&sn=54b2c484d7db777fe8ed950e9a61a296&chksm=9faecd81a8d944972ae2715654a7bfa36bc5b644a0d5663007a9e9a08ac8d11170f7598481a6#rd) |
| 2026-06-01 | [视频] AI驱动开发对Web标准的影响：变革、挑战与前瞻 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490879&idx=1&sn=4e31c0fe30e66099425960e59ddba65d&chksm=9faecdf8a8d944ee2e8da8e0023ba383cd9710eece36a7c747896f8abeb79586137e8ebb527f#rd) |
| 2026-05-27 | [视频] 企业浏览器观察：重塑Web体验的机遇与挑战 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490865&idx=1&sn=35e18a5ba642bbd02ee4a1abdfe45e20&chksm=9faecdf6a8d944e004011b8665de88f6cd634e8f8a7e2218604e5e5a09e6ff86566694115b1d#rd) |
| 2026-05-26 | [视频] 当Web为Agent重新设计 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490860&idx=1&sn=1a57a0cc18739d7c1d27fd5aed08fab0&chksm=9faecdeba8d944fda69b4c73184613fddd9f218ef3779dc3b5eea83f54b8c0711e5296faa636#rd) |
| 2026-05-25 | [视频] 前端开发中的大模型应用：现状、局限与可能的应对 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490855&idx=1&sn=2da880d2760d625ccc81496ccca34c02&chksm=9faecde0a8d944f661b9316afea82793f047b34d648f8d0d3fcf726e378841afd3b440793c76#rd) |
| 2026-05-21 | [视频] 向用户意图驱动的Web演进 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490848&idx=1&sn=3949e5fcdff34d7c7cb9bbed8efc6071&chksm=9faecde7a8d944f13dac8fafb819dcfbf21a8ca3bb6b7a27e25a1fa4e5b8be882c66e89a1f80#rd) |
| 2026-05-20 | [视频] Web与AI：意图导向范式下的Web未来发展之路 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490843&idx=1&sn=41e720940ab6e480e2389d576a5c92b6&chksm=9faecddca8d944ca2a2db4151a50e8a97ceff2ebecf30629063fb739451825e8352c66815526#rd) |
| 2026-03-20 | [视频] 企业浏览器进化论：「伴随式AI」的探索和实践 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490674&idx=1&sn=4469b94a331232fd5495e00ff063da63&chksm=9faeccb5a8d945a32deadbd3c9eed69bdf398f7989cb123dd1a6178bd7ae22ad2cdb8e561be9#rd) |
| 2026-02-05 | Generative UI专题交流会召开·社区组成立推进标准化探索 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490631&idx=1&sn=253f48a8b26fd397c85eedda0fe839c5&chksm=9faecc80a8d94596148af4b18b06517493129c0e7b539c010462ea7728a87b233ce702804294#rd) |
| 2026-02-03 | [视频] 从端侧推理到智能体：Web AI的今天和明天 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490612&idx=1&sn=d7a29f8d2e93305b984f8cb23ebc2db7&chksm=9faeccf3a8d945e5a22caca6323fbde21753246c8923281b1518f5dab39c45f92da9d1571f57#rd) |
| 2026-01-30 | [视频] 基于ANP构建开放的Agentic Web | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490600&idx=1&sn=cef5b4ecfd9d7eeabbe7424d9064b97d&chksm=9faeccefa8d945f90b470624a980d6242199ebba26a930be64fc8d257ffee6f9a1f8cf8a4ac7#rd) |
| 2026-01-28 | [视频] AI智能体与6G通信 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490595&idx=1&sn=3efd763239cdce22e6851853c1411f04&chksm=9faecce4a8d945f27c2b2fa022163159a8e455418d22217200ece985f3c93b5019ddb622e9ea#rd) |
| 2026-01-27 | [视频] MCP在蚂蚁的应用 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490590&idx=1&sn=4aba0ba915b07c08502235fd8b694e45&chksm=9faeccd9a8d945cfa25d595549222790c16f6535318feb053757bcb2f720cae379846fede3d4#rd) |
| 2026-01-23 | [视频] Web AI标准化方向：生成式UI与MCP服务 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490585&idx=1&sn=9bf20917148a1bf369a6e02deb3c9cd4&chksm=9faeccdea8d945c862b816b149569dc44f9b93ab3384cdb214da54e50cf419f2312aedb8e699#rd) |
| 2026-01-19 | [视频] AI时代的Agentic Web演进趋势与关键要素 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490572&idx=1&sn=9220619b7df66b34f837a883ae7fc6cd&chksm=9faecccba8d945dd14f8ab0d8c5170517c815fd840d62b9f0e7897486ce4c8599c6c4cfb54f4#rd) |
| 2026-01-14 | [视频] Web+AI：从W3C看标准化趋势 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490544&idx=1&sn=0c5ff8a509445ed6e30c6ea9969b5e0e&chksm=9faecb37a8d942219e6735777bed76f8f178f96cf0bba37ced35ca5e08f23a9795fd60419e42#rd) |

### 2025（31 篇）

| 日期 | 标题 | 专辑 | 链接 |
|---|---|---|---|
| 2025-11-28 | [欢迎参与] W3C成立Web与AI兴趣组 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490356&idx=1&sn=9aefe33d008d7f2c3c9f6103b7ec8962&chksm=9faecbf3a8d942e53d813a230be98148ea42d59e5c592e8269b504a3f48ea5f375c754e6ea6b#rd) |
| 2025-11-26 | 首个公开工作草案：CSS背景模块第四版 | CSS | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490351&idx=1&sn=f80650c0db203ae73ddd7e33e773c5ab&chksm=9faecbe8a8d942fee131e506b6683c8ab9ffafe75977f67f4450415fa0406a30242f5979bc26#rd) |
| 2025-10-22 | W3C提议成立Web与AI兴趣组 | AI | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247490301&idx=1&sn=34a8a82b9ea463672694f8d417706e0b&chksm=9faeca3aa8d9432c79ac7252992ffe466f5fe237f3ace2a1bbf8aca8bf488c3415dfcf760826#rd) |
| 2025-05-22 | 首个公开工作草案：CSS函数与混入模块 | CSS | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489941&idx=1&sn=64830efeb365c021f35b3585a5848dc2&chksm=9faec952a8d94044aa31b3efff5fd3d7f6a28abc40ab55325a8d125317dd417d210ed0b20a11#rd) |
| 2025-04-25 | [欢迎加入] 探索Web新技术兴趣组 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489915&idx=1&sn=e30f7e7d45ac68d043f9beff0773c4a9&chksm=9faec9bca8d940aa601f627fc0a937dbd478c9e870ce7ed72532f1a8b3c6ded36d89205d9042#rd) |
| 2025-04-23 | 首个公开工作草案：CSS间隙装饰模块 | CSS / Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489910&idx=1&sn=f0b29279ca57f57c7fdf027ff5346172&chksm=9faec9b1a8d940a73e36002ed7ab2cfa9111b15ca185dabe34d8f33776885a136fd279fd05a7#rd) |
| 2025-04-18 | W3C发布《Web伦理原则》授权中文翻译 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489902&idx=1&sn=d5f7fdb2af6ec662401c719d313d7c29&chksm=9faec9a9a8d940bf2f416a7c6b75a5fdeb0e7d69eaf6012cf59b54285d11bd1bd5fd19a0710a#rd) |
| 2025-04-14 | WebDX社区组推出Web平台功能目录 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489897&idx=1&sn=5871503bdaa4e59bc4ef31da0c99b670&chksm=9faec9aea8d940b8f88388e714cd07cfcc4ed5fb18c2139985de2b2506c572648e3aab66884f#rd) |
| 2025-03-31 | W3C更新EPUB 3.3推荐标准并发布EPUB 3.4规范草案 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489892&idx=1&sn=cfa5fe6c10d1e1944004f9197d8674ae&chksm=9faec9a3a8d940b58bfbcc932cbc6ee1afc258f80118bd8de8d924ecd578eeae61af71523dc9#rd) |
| 2025-03-26 | 首个公开工作草案：CSS表单控件样式模块 | CSS / Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489887&idx=1&sn=de8b16b8b6eee25694e5f4db9277bfae&chksm=9faec998a8d9408e08f7a2eb207c119dd553112f147f99f6a5d9d8bb8200037b87b307934863#rd) |
| 2025-03-25 | [3月26-27日] W3C全球社区热点话题分组讨论 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489877&idx=1&sn=984e5b3542fde77ada095fd38090bdc9&chksm=9faec992a8d9408422d17355210c47d4cfa7bea14aeea0351c1275f453dbe54d571a90328c13#rd) |
| 2025-03-24 | [开放讨论] 构建高性能、多样化的Web引擎生态 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489875&idx=1&sn=27620a246f2e21031cd018110466dcab&chksm=9faec994a8d94082977e52a963658b570a663e550fa778185c98433c1a981b35e71d6ccf5dce#rd) |
| 2025-03-19 | 如何保护Web应用程序免受XSS攻击 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489870&idx=1&sn=68b64a7848ddd261274599731a7c07c8&chksm=9faec989a8d9409ffcc79ef27bd29ca5e15d7c8f95c2318dcd02b0924e422b7ccc8b82a1f81a#rd) |
| 2025-03-17 | W3C候选推荐标准：TTML2的配音和音频描述配置文件（DAPT） | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489865&idx=1&sn=0ba105436e6156afba7114df8f39b8cc&chksm=9faec98ea8d940987b0d3174a97da9023b9b885f3340f6a79ae64f6290431acbae75b84c86fe#rd) |
| 2025-03-14 | W3C提议成立探索Web新技术兴趣小组 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489858&idx=1&sn=646eddf26b32ba9b6ce824957bbbe2e1&chksm=9faec985a8d9409358aac5922c566387c15c3c0417b8782ee9b7510770459a0e74290968e6d0#rd) |
| 2025-03-11 | W3C全球社区热点话题分组讨论（话题征集至3月12日截止） | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489853&idx=1&sn=7ead217a4d8fcc39b23042d3bd6ffb77&chksm=9faec9faa8d940ec91fb9156d086bed199a2169b1638801e76b0c5ce33c7a9232e817285312e#rd) |
| 2025-03-10 | CSS规范快照2024 | CSS | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489851&idx=1&sn=6d6ce341dc352af442c28ea40b39a607&chksm=9faec9fca8d940ea6def1b14b95e65af97555c60e2707b484a137b7ac7d6ac401cfbf840f9a3#rd) |
| 2025-03-06 | 征集审阅：《Web伦理原则》授权中文翻译 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489836&idx=1&sn=d1d758fec111b78fc7c6b37aef7e89fc&chksm=9faec9eba8d940fd5cb436ed3d51fb93689ade26be39c899392bcdc4b7b76d5ff260f1c68ac0#rd) |
| 2025-03-03 | [欢迎参加] Authentic Web系列研讨会 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489834&idx=1&sn=6fc40b411fa8e24e38f0081e22b2141c&chksm=9faec9eda8d940fb249a5bc4495ae9ffd16ebb3419783f7c0da8fe30e21109bd9593e350ea59#rd) |
| 2025-02-27 | W3C联合身份工作组新增规范：数字凭证API | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489826&idx=1&sn=6641e7eee6ba4296c3bc01a7752bf8c8&chksm=9faec9e5a8d940f32c693d279a01b126ecb506e330cf6a13c7bf138988e2f683669c48a24356#rd) |
| 2025-02-24 | [国际化] 世界各地的人名 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489820&idx=1&sn=e4ef2cef3e811c7dd805d1a8ed33b308&chksm=9faec9dba8d940cdc36847571e4aaffc494d687b7b890c48e75acf8bbbb1413728bd22c4c13e#rd) |
| 2025-02-12 | W3C中国DID与VC社区组发布IIFAA分布式可信认证技术文档 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489810&idx=1&sn=411667adf158b11d47e55579076adb29&chksm=9faec9d5a8d940c310146ab5b759a159a07e84d68bbbb1340a15f1ad50d28bece8d4dd3098ed#rd) |
| 2025-02-11 | [征集话题] W3C全球社区热点话题分组讨论 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489809&idx=1&sn=3cb5aa212c25a95756cfeccc887320e5&chksm=9faec9d6a8d940c0a8c1607a0443f9d67561ef66ed3b7784efac2228f0c2acc5c3397f45bcee#rd) |
| 2025-01-23 | 首个公开工作草案：开放屏幕应用协议和网络协议 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489787&idx=1&sn=f33d48a784a8d792078053146db3b0e5&chksm=9faec83ca8d9412a051bb3d2d0c31725020f5be4420d60b3f972093e7bec9a7ba76f87a32dfd#rd) |
| 2025-01-21 | 首个公开工作草案：CSS颜色HDR模块 | CSS / Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489781&idx=1&sn=2825ed09b87075f64b1e2306d2eeaa0b&chksm=9faec832a8d941242251ba987876e0ce4d67af10049059c14d84b73109971db10e246d8a6270#rd) |
| 2025-01-20 | W3C发布WebGPU候选推荐标准 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489775&idx=1&sn=78c9074697f7f712aecfb9d44f2b8790&chksm=9faec828a8d9413e3b10bfdfc9aaedf92be331841a5c86af767a378adba021af2b55ce8be039#rd) |
| 2025-01-17 | W3C计划成立探索Web新技术兴趣小组 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489770&idx=1&sn=bd07f222e8e0ef4786245099ac2dbc1f&chksm=9faec82da8d9413bda10618078c55e97e5685f375c5176b8b4b411e12665771a45b5ce89347b#rd) |
| 2025-01-16 | W3C与Ecma合作通过WinterTC推进Web互操作服务器运行时标准化 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489762&idx=1&sn=e58bc070e83dd4361782d5b1ec1d6ef3&chksm=9faec825a8d9413346d8515f7fc8797a075e5f142a020405448310369b6aa07a74744d164396#rd) |
| 2025-01-14 | 加强数字身份互操作性：受控标识符文档1.0添加SM2算法 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489754&idx=1&sn=fd9512890d91b88591a4b2f7bb89cf46&chksm=9faec81da8d9410bca4009dc222ffef2ccddef9970649120cd4b20cd957a3dd514fde4b47aba#rd) |
| 2025-01-09 | [欢迎参加] Web进化论｜WebAI与高性能Web应用技术研讨会 | AI / Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489727&idx=1&sn=3bccf2f40e9987c46404e9d251e2b6a7&chksm=9faec878a8d9416ea8868cf9fe2d1a2dab435357be4a7bcbc230b3666ee2a5f1f2001ccdc800#rd) |
| 2025-01-01 | 万维网联盟祝大家元旦快乐！ | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489721&idx=1&sn=51eccac30a341e7cb591785e85dae597&chksm=9faec87ea8d94168698d9b0a45a28dcdf382baa18fcee876ef54b264f424f195777de960ef4e#rd) |

### 2024（70 篇）

| 日期 | 标题 | 专辑 | 链接 |
|---|---|---|---|
| 2024-12-19 | W3C发布WebAssembly 2.0候选推荐标准 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489706&idx=1&sn=29b104dd92ff60a5283a256df084d887&chksm=9faec86da8d9417b227400fdb5cb95211fae8aae5f1da898e15ee9aaff6108ae721efc6e664e#rd) |
| 2024-12-17 | 断行的方法：排版各种文字时的换行策略 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489701&idx=1&sn=37dea6cdd08b368299916c3da5c9ee3e&chksm=9faec862a8d9417466baa9dbdf56be395dd219ccd71eb4f9ba39acfacb24853e21fbbfcdde43#rd) |
| 2024-12-13 | 《Web伦理原则》引导全球社区共筑理想Web | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489655&idx=1&sn=8c8d245b00e1ce9060e9c45cbeb54270&chksm=9faec8b0a8d941a63294b8da8a36c62f55990f5aa47e0b291bb53076a5ee00b33a223ae03e97#rd) |
| 2024-12-11 | [专题讨论] 云、边、端协同 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489648&idx=1&sn=dd128aae0df971e69cb7fbd75c1acf12&chksm=9faec8b7a8d941a1aae90390c362872642f0232e1a920e8130cb698fb546a8599329ced2a725#rd) |
| 2024-12-05 | Winter 社区组探索 Web 平台与服务端运行时之间的协作 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489639&idx=1&sn=86060fea090a0d969cbd3dd9c0e3c3dc&chksm=9faec8a0a8d941b68ccacd0508f494ad8b7f986ba730e91ed8baa51d3dcb6ac613911965be97#rd) |
| 2024-12-03 | 首个公开工作草案：DID 解析和 DID URL 解引用 v1.0 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489598&idx=1&sn=7cc96d92e42b1bc077783f0d14bbdf2f&chksm=9faec8f9a8d941efff31fa04f81702963114acb61bc7ae6515f7a570ba2d68589e2b328fa0d7#rd) |
| 2024-11-29 | 首个公开工作草案：全球隐私控制（GPC） | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489592&idx=1&sn=dd1b608baf5cf0f4cadcead32bec71d1&chksm=9faec8ffa8d941e99c5eef4ac3f1a0c1b7e5119efc08dc3922743a186033d91d25cdb742edd1#rd) |
| 2024-11-28 | W3C 候选推荐标准：设备姿态API | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489582&idx=1&sn=105273fe435ec852ee3c8739c0f7d141&chksm=9faec8e9a8d941ff68e6c5dc601dd54ca02cc91d815f3da56c2679fa3cc9fb729c949c488796#rd) |
| 2024-11-27 | 小组备忘：DID扩展、DID方法、DID文档属性扩展、DID解析扩展 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489576&idx=1&sn=ce6f73eb49a8b927a419b1228a1074f0&chksm=9faec8efa8d941f9fef7751c62d4d6105569a2db13bcd0ddc9010a33f9d3abb8e183d3d484a7#rd) |
| 2024-11-22 | 首个公开工作草案：WebDriver BiDi | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489571&idx=1&sn=81a26fdc53cb51c354a086c496f5869e&chksm=9faec8e4a8d941f2c6d0e246512d73d668ced989b768b296298e4ce12c9acaa1b11df4520b59#rd) |
| 2024-11-20 | 首个公开工作草案：Web Audio API 1.1 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489566&idx=1&sn=5038b9e54edb3542929bc077587f7ad8&chksm=9faec8d9a8d941cfbe61570efa2b0c448b76f181d0abc453377b9a7611b73d0c8e4ec995d3fe#rd) |
| 2024-11-18 | [专题讨论] 优化Web推送通知：问题分析与方案探讨 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489555&idx=1&sn=4226a34fe757b7b1b4162abccd17b77d&chksm=9faec8d4a8d941c21733096c85dec6ade2c06561ba7cb0b310f790adcd74c979ac49e04d6bb3#rd) |
| 2024-11-14 | [欢迎参与] W3C成立隐私友好广告技术标准工作组 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489548&idx=1&sn=e3e07d2ee939562d0cc2ca5c515b36df&chksm=9faec8cba8d941dddc59f5b0382d666d16eebcd600f72cda3636a48169d7c2d2b3b72d672c43#rd) |
| 2024-11-12 | [专题讨论] AI 模型管理 | AI / Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489543&idx=1&sn=23456ceeb0fe2875509de61c8a7efa41&chksm=9faec8c0a8d941d69d311931b6ea73c0e0fc64860a9e34ebbecfb9638429bf2a6bc40d5fb750#rd) |
| 2024-11-08 | 首个公开工作草案：音频会话API | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489457&idx=1&sn=a960671e754a80726dcc25864bbb1825&chksm=9faec776a8d94e60d7edc62f543231c8fb8c1ef2372348593dae14d98993c96586014273c62f#rd) |
| 2024-11-07 | [专题讨论] DID方法标准化 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489452&idx=1&sn=feaa380e36c7e414b01a648e1be88dd7&chksm=9faec76ba8d94e7d57b6ef7492916eaa7276cb49ae8d1b5c3cc0b54144b070c0343dd5538258#rd) |
| 2024-11-05 | [专题讨论] 提升ServiceWorker性能的新特性 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489446&idx=1&sn=f6cd90a3682131397596aefb7dc7ba6c&chksm=9faec761a8d94e773c505ab89cc13b628cab56e67e10468db95fb41941101db2123850399926#rd) |
| 2024-11-01 | [专题讨论] Web Install API | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489388&idx=1&sn=4b6a27511b8c25825a683a20a6e50b00&chksm=9faec7aba8d94ebdaf2403c14079689b309c44a5ba3888e3e54445e82a69d3ebdc7d0beae259#rd) |
| 2024-10-30 | [欢迎参与] W3C成立Web可持续发展兴趣组 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489350&idx=1&sn=42a8c3f09d096799bdbf29f0d6ca5a5c&chksm=9faec781a8d94e973d423de2f3737b1f87ad90aba02ffc99fe506d2ee1497873a3eaaf020277#rd) |
| 2024-10-29 | [专题讨论] Ladybird：全新独立的浏览器引擎——从头开始编写 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489340&idx=1&sn=cd8b596a0c33c44887d5505f1a351188&chksm=9faec7fba8d94eedca4bdc1158de0995c04cded602f44375f98fef9960449ab0d116ff5803dd#rd) |
| 2024-10-24 | [专题讨论] 共建一个标准开放、全球共享的 Web Wide World | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489334&idx=1&sn=26de589967f8d27cf5e63ad301694007&chksm=9faec7f1a8d94ee765de9fe17e21dc1384881024b61e23ecfed7af83ca2fda830a92e4e20ebf#rd) |
| 2024-10-23 | [视频] W3C无障碍指南标准工作最新进展及后续计划 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489307&idx=1&sn=bed5534fa618baced3c6eea0435139e7&chksm=9faec7dca8d94eca47a4d46279217a1ab5ae268d35b346d2f2ffa4f22f1d589d224a33e454e6#rd) |
| 2024-10-21 | [视频] reading-flow属性以及Chrome的实验性实现 | CSS / Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489302&idx=1&sn=13415e720d2094196b8b44c70e1ef7b3&chksm=9faec7d1a8d94ec77615c2f76e78aee973cc238cad3e6730bf90ee221333a4a660828068b053#rd) |
| 2024-10-16 | 首个公开工作草案：CSS缓动函数第二版 | CSS / Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489293&idx=1&sn=9a131856f59b4d780025e9b82fa900b6&chksm=9faec7caa8d94edc8c7a6cb0956b1dd7da84c5f2fa02b750e766ee89f668b859ddd9522125f9#rd) |
| 2024-10-15 | [欢迎参与] W3C成立隐私标准工作组 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489285&idx=1&sn=32d5f1afd51bc9c11c99484bb6041693&chksm=9faec7c2a8d94ed47ba5d931fe7026ca28d89dd72476d987720214ebe76d5300284524fee306#rd) |
| 2024-09-11 | [欢迎参与] W3C 成立 Linked Web Storage 标准工作组 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489263&idx=1&sn=272cae093d27b594f44695f340da83b3&chksm=9faec628a8d94f3e51c78047616d24d587109429fb75402af2593559036075d410745ad79dca#rd) |
| 2024-09-03 | 欢迎参与W3C WebView社区调查 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489255&idx=1&sn=f1aaa1dba99d5e9943f9a0285c1cc5a1&chksm=9faec620a8d94f365101129f57f2e6361c05682be369b9905a8a8add7c0bae4ac4c293a2f911#rd) |
| 2024-09-02 | 首个公开工作草案：联合凭证管理 API | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489238&idx=1&sn=5b3e1d6ac9751cfcd8086de7cd63bf28&chksm=9faec611a8d94f07f2949eb437675a0ccd4b4bcd842f57d7f802b3407bf0317e9d63b4610d3a#rd) |
| 2024-08-28 | [回顾] 数字身份：技术、标准与策略研讨会 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489233&idx=1&sn=40a1547985f9a219bfb1214f413a960c&chksm=9faec616a8d94f0066cb05830560b94b97ea0e419e7759633c46215047abc9006d30b57a2c6b#rd) |
| 2024-08-27 | W3C 推荐标准：数据目录词汇表第三版（DCAT-3） | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489227&idx=1&sn=c65de0d5407793ae65a22ea1871446b6&chksm=9faec60ca8d94f1a2935601f815a6c07fd7bb9c48a738859dd71aa3c1f232fdaba0d89ac8020#rd) |
| 2024-08-26 | 征集意见：数字身份对社会、伦理和技术的影响 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489223&idx=1&sn=bf94b4b0b1891308eb6a802cf06fc587&chksm=9faec600a8d94f1684bec18119a004f4fa64a1c382109e5792541a8c0d7ee3785bc6eaa5805c#rd) |
| 2024-08-14 | 欢迎参与W3C WebView社区调查 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489212&idx=1&sn=0e32d56f05aa69f96d1af462fda20a38&chksm=9faec67ba8d94f6d3e4c1c9603069816816b973bd3fd2c614a123cc06582991fa1bb1ef006ef#rd) |
| 2024-08-08 | 欢迎参与W3C社区调查 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489199&idx=1&sn=8dc231ab773a4992f4b3ad7e0a48223e&chksm=9faec668a8d94f7e985f1b484d4ad019b5830a0da095bee0a42da45e14dc7e5fd62aa1da5a31#rd) |
| 2024-08-02 | W3C技术架构组意见：必须消除第三方cookies | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489188&idx=1&sn=8dc2c7df5a2d825dafa477478f2501ec&chksm=9faec663a8d94f75e5da6d29156847b2e54a7edbc0a1089022e77070f610c99da590a848100e#rd) |
| 2024-07-31 | W3C 沉浸式 Web 工作组拟新增 “WebXR 人体追踪模块” | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489181&idx=1&sn=0a1c6496f341f41ec0f81b77c70ab399&chksm=9faec65aa8d94f4c461fc95de2b7e9b25b0666d0267ed9adce9790a660ab2383f36aa19f7592#rd) |
| 2024-07-30 | 首个公开工作草案：CSS滚动吸附模块第二版 | CSS / Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489173&idx=1&sn=fc27ab67f3b3f783d04700ad08fcfe28&chksm=9faec652a8d94f441e258f2d52757ab5707fb365857d68058d69fad9b47ac4586af9d7324114#rd) |
| 2024-07-17 | W3C浏览器测试与工具工作组新增AT Driver规范 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489120&idx=1&sn=48f4a5f54927b6ab098cb8e78d726161&chksm=9faec6a7a8d94fb17a7a81af9c65576e15c7a3b4ee739f44be20f8788f2b93100c8d03128241#rd) |
| 2024-07-08 | 国际化助力实现 “Web for All” | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489107&idx=1&sn=443f9bf0f646544d2f19b99f6d004ac8&chksm=9faec694a8d94f823e0e40a24f74afb6eece4f5d77b34bee532f34d3db865bd0c526006c9102#rd) |
| 2024-07-03 | 首个公开工作草案：无障碍一致性测试（ACT）规则格式1.1 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489105&idx=1&sn=f83cb4d17d3b7aa4b7058492613539ed&chksm=9faec696a8d94f8031effc0f3de34355b756fbb2eac78b1efcbb2ad1e80b60d40d6aac945623#rd) |
| 2024-07-02 | [回顾] 国际重大赛事中的沉浸式技术线上沙龙 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489100&idx=1&sn=a3b3aea466c67e9dce4f69d33d67250a&chksm=9faec68ba8d94f9d0f26ec6532df0295feb5f17b1ffc03b134aaebc0fd019a7778877ac7918e#rd) |
| 2024-06-28 | [6月28日14:00开始直播] 国际重大赛事中的沉浸式技术线上沙龙 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489035&idx=1&sn=156a6ae5752484b0df6b95e5394d37a2&chksm=9faec6cca8d94fda28e192cf5f710dad3a9b4c253b6c18d3e1d35667b85297562018348f78ca#rd) |
| 2024-06-25 | 总结报告[上]：“Web 进化论” 2024 年度大会：机器学习、WebGPU、媒体技术 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489016&idx=1&sn=72f815581a57919416fd7d9b101beb63&chksm=9faec53fa8d94c29ecb537f7be5afc7b5691bae52de2e9c1eae55d14c7799d5bcedc4043e123#rd) |
| 2024-06-24 | W3C 提议成立 Web 可持续发展工作组 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247489004&idx=1&sn=27ef48d2d0ecd86beb1f22fb1fe615e8&chksm=9faec52ba8d94c3dacf8d631e67784af5333e7bbca8fb5949abbe680ae2192473c26105f42f8#rd) |
| 2024-06-12 | W3C 候选推荐标准：分布式上下文的传播格式：Baggage | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488992&idx=1&sn=c852b55f81bbe7325e0d7b93993fe2ad&chksm=9faec527a8d94c3147d819b1e007485e7769090db677ab1d184c2a232ca26b00b19ce748c140#rd) |
| 2024-06-06 | W3C 提议成立基于 Web 的智慧城市数字孪生兴趣小组 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488986&idx=1&sn=aec1bab45956a76278c3e321101e3bc7&chksm=9faec51da8d94c0b89f7a40dde36cb5586a376ed9d81178123a49d64e6102263f30f7640fc7e#rd) |
| 2024-06-04 | 首个公开工作草案：Controller Documents 1.0 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488977&idx=1&sn=a31a5f787daf38da62687fba229f0fa2&chksm=9faec516a8d94c0038e496036f5f8e719e570c23be24d98231469e63cd21f80e5b60bd66276f#rd) |
| 2024-05-24 | [观看直播 · 5月28-29日] Web 进化论 — 机器学习、WebGPU、媒体技术 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488959&idx=1&sn=e6e237fa00402e73b77678828e6a875d&chksm=9faec578a8d94c6e1b1e3343084e6d55b90946d54649479c98a5dc089f45dddff9b967f1e802#rd) |
| 2024-05-17 | [大会议程] “Web 进化论” 2024 年度大会：机器学习、WebGPU、媒体技术 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488941&idx=1&sn=4fda5be18ee5b34c2ef8d8c804f2cf80&chksm=9faec56aa8d94c7c8328d148252ccf16dc1e052e0a8fef1d5695b787d503dce80f27723ae0a5#rd) |
| 2024-05-10 | W3C DID 工作组新增  DID Resolution 规范 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488937&idx=1&sn=5ed643bdaf755750d16899d29c230102&chksm=9faec56ea8d94c7875daf9d56baf93b0f4123fb0ad782a3fbf79d06652af6d6b146710b1aa3e#rd) |
| 2024-05-09 | [开放注册] “Web 进化论” 2024 年度大会：机器学习、WebGPU、媒体技术 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488931&idx=1&sn=b0db635f4d754c25349cd22e20e1ef10&chksm=9faec564a8d94c723eb32838ddce7e6a4ee403033fa2174cf06f57bf232ea432a9ccfa8ad678#rd) |
| 2024-04-18 | W3C 联合身份工作组拟新增“数字凭证”规范 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488916&idx=1&sn=4c65f28cc0362145a11a2a28c3e00582&chksm=9faec553a8d94c4507d9a97f6d24763962ab3942c2fa650c603a431f0edb94e2aa351baf7329#rd) |
| 2024-04-16 | W3C 候选推荐标准：数据完整性 BBS 加密套件1.0 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488911&idx=1&sn=4253783378044c0397ce8424c5be8936&chksm=9faec548a8d94c5eb8cb64d71c6a9117706ed964c8f093116057deeb1c451e5b4bf4364e52eb#rd) |
| 2024-04-10 | W3C 计划成立安全兴趣组 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488899&idx=1&sn=f383f444f1aeff25c367ca62f2cc5346&chksm=9faec544a8d94c52873820a0ec779c9d88e0285060b951dfaf8a56b0090e1244483d0c227c59#rd) |
| 2024-03-28 | [欢迎参与] W3C 成立联合身份标准工作组 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488893&idx=1&sn=b00d00d1fc31c29ce03147cbaeb6330c&chksm=9faec5baa8d94caca9e8f6dbce9c769a9a6404ebd6e3a331054cc8c8875c1073ebfdd684e0b4#rd) |
| 2024-03-22 | AI 与 Web：分析机器学习模型对 Web 的影响 | AI / Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488888&idx=1&sn=39592059d3daaca48d9c24e850245d3d&chksm=9faec5bfa8d94ca9a1737e56c01bc07dab1e6a3d253e5b1f2312c6d90c0585fc986916477413#rd) |
| 2024-03-18 | [视频] Web 支付——安全支付确认（SPC） | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488881&idx=1&sn=0477b7206b63edc434ac3d61e3c7a2cc&chksm=9faec5b6a8d94ca06c66e1e8f77b69674700e5721537ab74c8764450615585dab44aad6e78f1#rd) |
| 2024-03-15 | [视频] 深入了解 W3C 万维物联网（WoT） | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488876&idx=1&sn=42e56ddb9fce63a2094411f8534f8e88&chksm=9faec5aba8d94cbd030df0abd9147e3fde4dcf133ef7da7a7901e10bb8a520c4cde802319101#rd) |
| 2024-03-14 | W3C 计划成立 Web 可持续发展工作组 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488850&idx=1&sn=7adc7b7778b85d93b43a496c3219d86b&chksm=9faec595a8d94c83ab454dec8259261ce32eb1ba0122e616f02dea371415088b23b15b12ec53#rd) |
| 2024-03-12 | 纪念万维网诞生35周年！ | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488844&idx=1&sn=629e042428c129a98cc134ae39121c60&chksm=9faec58ba8d94c9d23fd9cc8f9b88eb5cc6b5532607a6987149c70dba2560cdfd98502dc22d3#rd) |
| 2024-03-07 | W3C 候选推荐标准：DPub-ARIA 1.1、DPub-AAM 1.1 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488817&idx=1&sn=60c6603f8e548db4b2949a0cd5c115e9&chksm=9faec5f6a8d94ce08af9f9baf67008c8851f866e24af982f75037d4151337f949491c01c00e3#rd) |
| 2024-03-04 | W3C Web 应用标准工作组新增三份规范 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488809&idx=1&sn=1a6ba8957a6fc0f70825aa89b4616fb4&chksm=9faec5eea8d94cf8154d98d836c860fa03bbacc4d033db3c87f2410779b49d80e62a4fdde898#rd) |
| 2024-02-26 | W3C 发布 Web 安全技术研讨会报告 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488793&idx=1&sn=435affeb8aa91e44d3cda48b8e68ce05&chksm=9faec5dea8d94cc8105d7ebcff3107adc5f27dd2f8da392c0126ff214eba87f18aff1081785f#rd) |
| 2024-02-05 | W3C 游戏社区组话题：生成式 AI | AI / Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488777&idx=1&sn=e8fc0aa7ee2f954b6ba393df5b67c1d5&chksm=9faec5cea8d94cd8b2e3740375e70b32cdf80d94f4e7191584744ea471ae5d486cad0fa77c09#rd) |
| 2024-02-04 | W3C 提议成立联合身份标准工作组 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488770&idx=1&sn=daeb283578c14b6e009a7dda850d0d61&chksm=9faec5c5a8d94cd30095148741ec3a1d2578a4deb7b304b280ac3f2f6b58034fdacfbe380005#rd) |
| 2024-02-02 | 薛富侨全面负责 W3C 国际化标准活动 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488761&idx=1&sn=e98d03025b0a4d8ca0707c51c66680a1&chksm=9faec43ea8d94d280d4ca1d4be7b0011e0a0f5f72c85564fdf12b9ea99a12b59f97d38a0662e#rd) |
| 2024-02-01 | 首个公开工作草案：MiniApp Addressing | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488753&idx=1&sn=fa946750de986cc22bb243ed5ba400b4&chksm=9faec436a8d94d209dd79f7ab2f134f485f50dc62cbe7b70ebd93753564e0b0fe312bdce5f81#rd) |
| 2024-01-29 | 首个公开工作草案：CSS 视口模块 | CSS / Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488726&idx=1&sn=5ad5f6f645696df841887cd525039a1f&chksm=9faec411a8d94d070d507fc7d684e16f6e8144a8072c8dd4803896902a01f9f8af6abf5d213d#rd) |
| 2024-01-26 | Web 进化论 — Solid 技术、标准与生态专题活动报告 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488725&idx=1&sn=24988de6bed39649235f3e09cfff5fe6&chksm=9faec412a8d94d04ed8d51e3291a211a018727b5bac2dba78bc605ce26d4da544cab72d21569#rd) |
| 2024-01-23 | 首个公开工作草案：可访问富互联应用（WAI-ARIA）1.3版 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488695&idx=1&sn=d5a46ca3ecab439cb6c5b312393640c3&chksm=9faec470a8d94d66f67dc50fb0c9754c9023e9a7ad7bd1f0a9bcee79a27f8662f07cb3aa9cc5#rd) |
| 2024-01-19 | W3C 候选推荐标准：数据目录词汇表第三版（DCAT-3） | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488687&idx=1&sn=2f32af77bb0df36a42c5a68699a2b44c&chksm=9faec468a8d94d7e91903fa0925324d52f04bc88d808064b893616b4d1c163c4834a8476920e#rd) |

### 2023（2 篇）

| 日期 | 标题 | 专辑 | 链接 |
|---|---|---|---|
| 2023-11-28 | [视频] 为 Web 上的 cookies 建立稳健的长期安全模型 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488242&idx=1&sn=2e019bdf842a88d801c58f25acb8fb3d&chksm=9faec235a8d94b23f19a282ccf7b74b50576826cdeb53fba7fa8876f5c11cdc16ecc8d01aaca#rd) |
| 2023-11-27 | [视频] WIP 解决方案避免 Web 应用安全工具中的 Javascript realms 安全绕过 | Web | [原文](http://mp.weixin.qq.com/s?__biz=MzA3OTY5NDI0OA==&mid=2247488205&idx=1&sn=287d3ca470210c38ba10371731ebba64&chksm=9faec20aa8d94b1c64b3e506f3008162fcb5c2959956b3cc8ada8eee921e68a88d1d8761e085#rd) |
