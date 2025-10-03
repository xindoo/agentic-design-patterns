# 附录 E - 命令行界面中的 AI Agent

## 引言

开发者的命令行界面，长期以来作为精确命令式指令的堡垒，正经历一场深刻变革。它正从简单的 shell 演变为由新型工具驱动的智能协作工作空间：AI Agent 命令行界面（CLI）。这些 Agent 不仅限于执行命令；它们能理解自然语言，维护整个代码库的上下文，并可执行复杂的多步骤任务，自动化开发生命周期的关键环节。

本指南深入剖析这一新兴领域的四位主要参与者，探索其独特优势、适用场景及设计理念，助你甄选最适合工作流程的工具。需注意的是，针对特定工具列出的许多用例示例，通常也可由其他 Agent 完成。这些工具的核心差异往往体现在它们为给定任务所达成结果的质量、效率与精细度上。后续章节将讨论专门设计用于衡量这些能力的基准测试。

## Claude CLI (Claude Code)

Anthropic 的 Claude CLI 被设计为一款具备项目架构深度全局认知的高级编码 Agent。其核心优势在于其"agentic"特性，能为复杂多步骤任务构建代码库的心智模型。交互过程高度对话化，类似结对编程会话，它在执行前会阐述其计划。这使其成为从事涉及重大重构或具有广泛架构影响功能实现的大型项目的专业开发者的理想选择。

**示例用例：**

1. **大规模重构：** 你可指示："我们当前的用户认证依赖会话 cookie。请重构整个代码库以采用无状态 JWT，更新登录/登出端点、中间件及前端令牌处理逻辑。"Claude 将读取所有相关文件并执行协调一致的更改。
2. **API 集成：** 在提供新天气服务的 OpenAPI 规范后，你可指令："集成此新天气 API。创建服务模块处理 API 调用，新增组件展示天气信息，并更新主仪表板以包含该组件。"
3. **文档生成：** 指向文档匮乏的复杂模块，你可要求："分析 ./src/utils/data\_processing.js 文件。为每个函数生成全面的 TSDoc 注释，阐明其用途、参数及返回值。"

Claude CLI 作为专业化编码助手，内置了核心开发任务工具，包括文件摄取、代码结构分析与编辑生成。其与 Git 的深度集成支持直接分支与提交管理。Agent 的可扩展性通过多工具控制协议（MCP）实现，允许用户定义并集成自定义工具。这使其能与私有 API 交互、执行数据库查询及运行项目特定脚本。此架构将开发者定位为 Agent 功能范畴的决策者，实质上将 Claude 塑造为由用户定义工具增强的推理引擎。

## Gemini CLI

Google 的 Gemini CLI 是一款多功能开源 AI Agent，专为强大性能与易用性设计。其凭借先进的 Gemini 2.5 Pro 模型、超大上下文窗口及多模态能力（可处理图像与文本）脱颖而出。开源特性、慷慨的免费额度及"推理-行动"循环机制，使其成为透明、可控且卓越的全能型工具，受众广泛——从爱好者到企业开发者，尤其适合 Google Cloud 生态系统的用户。

**示例用例：**

1. **多模态开发：** 你提供设计稿中的 Web 组件截图（gemini describe component.png）并指示："编写 HTML 和 CSS 代码，构建外观与此完全一致的 React 组件。确保具备响应式设计。"
2. **云资源管理：** 利用其内置 Google Cloud 集成，你可命令："查找生产项目中所有运行版本低于 1.28 的 GKE 集群，并生成逐个升级这些集群的 gcloud 命令。"
3. **企业工具集成（通过 MCP）：** 开发者为 Gemini 配置名为 get-employee-details 的自定义工具，该工具连接公司内部 HR API。提示词为："为新员工起草欢迎文档。首先使用 get-employee-details \--id=E90210 工具获取其姓名与团队信息，随后用该信息填充 welcome\_template.md。"
4. **大规模重构：** 开发者需重构大型 Java 代码库，以新型结构化日志框架替换已弃用的日志库。他们可对 Gemini 使用如下提示：读取 'src/main/java' 目录下所有 \*.java 文件。针对每个文件，将 'org.apache.log4j' 导入及其 'Logger' 类实例替换为 'org.slf4j.Logger' 与 'LoggerFactory'。重写日志记录器实例化及所有 .info()、.debug() 和 .error() 调用，采用带键值对的新结构化格式。

Gemini CLI 配备一套内置工具，使其能与环境交互。这些工具涵盖文件系统操作（如读写）、运行命令的 shell 工具，以及通过网页抓取与搜索访问互联网的工具。为获取更广泛上下文，它使用专用工具批量读取文件，并利用内存工具保存信息供后续会话使用。此功能构建于安全基础之上：沙箱机制隔离模型操作以防范风险，而 MCP 服务器充当桥梁，使 Gemini 能安全连接至本地环境或其他 API。

## Aider

Aider 是一款开源 AI 编码助手，通过直接操作文件并将变更提交至 Git，扮演真正的结对程序员角色。其标志性特征是直接性：它应用编辑，运行测试进行验证，并自动提交每个成功变更。作为模型无关工具，它赋予用户对成本与能力的完全控制权。其以 Git 为中心的工作流，使其成为注重效率、控制力及代码修改全程透明可审计的开发者的理想选择。

**示例用例：**

1. **测试驱动开发（TDD）：** 开发者可指令："为计算数字阶乘的函数创建失败测试。"Aider 编写测试并确认失败后，后续提示为："现在编写代码使测试通过。"Aider 实现函数后再次运行测试以验证。
2. **精准 Bug 修复：** 给定 bug 报告，你可指示 Aider："billing.py 中的 calculate\_total 函数在闰年计算失败。将文件添加上下文，修复此 bug，并依据现有测试套件验证修复。"
3. **依赖项更新：** 你可指令："我们项目使用的 'requests' 库版本过时。请检查所有 Python 文件，更新导入语句及任何已弃用的函数调用以兼容最新版本，随后更新 requirements.txt。"

## GitHub Copilot CLI

GitHub Copilot CLI 将广受欢迎的 AI 结对编程体验延伸至终端环境，其核心优势在于与 GitHub 生态系统的原生深度集成。它能理解项目*在 GitHub 中*的上下文。其 Agent 能力支持分配 GitHub issue、实施修复并提交拉取请求供人工审核。

**示例用例：**

1. **自动化 Issue 解决：** 管理者将 bug 工单（如"Issue \#123：修复分页差一错误"）分配给 Copilot Agent。随后 Agent 创建新分支、编写代码并提交关联该 issue 的拉取请求，全程无需开发者手动介入。
2. **仓库感知问答：** 团队新成员可询问："本仓库中数据库连接逻辑定义于何处？需要哪些环境变量？"Copilot CLI 利用其对整个仓库的认知提供包含文件路径的精确答案。
3. **Shell 命令助手：** 当面对复杂 shell 命令不确定时，用户可输入：gh? find all files larger than 50MB, compress them, and place them in an archive folder. Copilot 将生成执行该任务所需的确切 shell 命令。

## Terminal-Bench：命令行界面中 AI Agent 的基准测试框架

Terminal-Bench 是一套创新的评估框架，专用于衡量 AI Agent 在命令行界面中执行复杂任务的熟练度。鉴于其基于文本的沙箱特性，终端被确认为 AI Agent 运行的理想环境。初始版本 Terminal-Bench-Core-v0 包含 80 项精心设计的手工任务，涵盖科学工作流与数据分析等领域。为确保公平对比，开发了极简 Agent Terminus 作为各类语言模型的标准化测试平台。该框架具备高度可扩展性，支持通过容器化或直接连接集成多样化 Agent。未来规划包括实现大规模并行评估及整合现有基准测试。项目鼓励开源社区贡献任务扩展与框架协同优化。

## 结论

这些功能强大的 AI 命令行 Agent 的涌现，标志着软件开发范式的根本性转变——将终端转化为动态协作环境。如我们所见，不存在单一的"最佳"工具；相反，一个生机勃勃的生态系统正在成型，每个 Agent 都提供独特专长。理想选择完全取决于开发者需求：Claude 擅長复杂架构任务，Gemini 强于多功能多模态问题求解，Aider 专注 Git 中心化直接代码编辑，GitHub Copilot 则无缝融入 GitHub 工作流。随着这些工具的持续演进，熟练运用它们将成为核心技能，从根本上重塑开发者构建、调试与管理软件的方式。

## 参考文献

1. Anthropic. *Claude*. [https://docs.anthropic.com/en/docs/claude-code/cli-reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)
2. Google Gemini Cli [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
3. Aider. [https://aider.chat/](https://aider.chat/)
4. GitHub *Copilot CLI* [https://docs.github.com/en/copilot/github-copilot-enterprise/copilot-cli](https://docs.github.com/en/copilot/github-copilot-enterprise/copilot-cli)
5. Terminal Bench: [https://www.tbench.ai/](https://www.tbench.ai/)