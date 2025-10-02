# 附录 E \- 命令行上的 AI Agent

## 引言

开发者的命令行长期以来一直是精确、命令式指令的堡垒，正在经历深刻的转变。它正在从一个简单的 shell 演变为由新一类工具驱动的智能协作工作空间：AI Agent 命令行界面（CLI）。这些 Agent 不仅仅是执行命令；它们理解自然语言，维护关于整个代码库的上下文，并且可以执行复杂的多步骤任务，自动化开发生命周期的重要部分。

本指南深入探讨了这个新兴领域的四个领先参与者，探索它们独特的优势、理想用例和不同的理念，以帮助你确定哪个工具最适合你的工作流程。需要注意的是，为特定工具提供的许多示例用例通常也可以由其他 Agent 完成。这些工具之间的关键区别通常在于它们能够为给定任务实现的结果的质量、效率和细微差别。有专门设计用于测量这些能力的基准测试，将在以下部分中讨论。

## Claude CLI (Claude Code)

Anthropic 的 Claude CLI 被设计为具有对项目架构深刻、整体理解的高级编码 Agent。其核心优势是其"agentic"特性，允许它为复杂的多步骤任务创建代码库的心智模型。交互是高度对话式的，类似于结对编程会话，它在执行前解释其计划。这使其成为从事涉及重大重构或实现具有广泛架构影响的功能的大型项目的专业开发人员的理想选择。

**示例用例：**

1. **大规模重构：** 你可以指示它："我们当前的用户身份验证依赖于会话 cookie。重构整个代码库以使用无状态 JWT，更新登录/登出端点、中间件和前端令牌处理。"Claude 将读取所有相关文件并执行协调的更改。  
2. **API 集成：** 在提供新天气服务的 OpenAPI 规范后，你可以说："集成这个新的天气 API。创建一个服务模块来处理 API 调用，添加一个新组件来显示天气，并更新主仪表板以包含它。"  
3. **文档生成：** 指向一个文档记录不佳的复杂模块，你可以要求："分析 ./src/utils/data\_processing.js 文件。为每个函数生成全面的 TSDoc 注释，解释其目的、参数和返回值。"

Claude CLI 作为专门的编码助手，具有用于核心开发任务的固有工具，包括文件摄取、代码结构分析和编辑生成。它与 Git 的深度集成促进了直接的分支和提交管理。Agent 的可扩展性由 Multi-tool Control Protocol（MCP）介导，使用户能够定义和集成自定义工具。这允许与私有 API 交互、数据库查询和执行项目特定的脚本。这种架构将开发者定位为 Agent 功能范围的仲裁者，有效地将 Claude 表征为由用户定义的工具增强的推理引擎。

## Gemini CLI

Google 的 Gemini CLI 是一个多功能的开源 AI Agent，专为强大性和可访问性而设计。它以先进的 Gemini 2.5 Pro 模型、巨大的上下文窗口和多模态能力（处理图像和文本）而脱颖而出。其开源特性、慷慨的免费层级和"推理与行动"循环使其成为一个透明、可控且出色的全能工具，适用于从爱好者到企业开发人员的广泛受众，特别是那些在 Google Cloud 生态系统中的人。

**示例用例：**

1. **多模态开发：** 你提供来自设计文件的 Web 组件截图（gemini describe component.png）并指示它："编写 HTML 和 CSS 代码来构建一个看起来完全像这样的 React 组件。确保它是响应式的。"  
2. **云资源管理：** 使用其内置的 Google Cloud 集成，你可以命令："在生产项目中查找所有运行版本早于 1.28 的 GKE 集群，并生成一个 gcloud 命令来逐个升级它们。"  
3. **企业工具集成（通过 MCP）：** 开发者为 Gemini 提供一个名为 get-employee-details 的自定义工具，该工具连接到公司的内部 HR API。提示词是："为我们的新员工起草欢迎文档。首先，使用 get-employee-details \--id=E90210 工具获取他们的姓名和团队，然后用该信息填充 welcome\_template.md。"  
4. **大规模重构：** 开发者需要重构一个大型 Java 代码库，用新的结构化日志框架替换已弃用的日志库。他们可以使用 Gemini 并使用如下提示词：读取 'src/main/java' 目录中的所有 \*.java 文件。对于每个文件，将所有 'org.apache.log4j' 导入及其 'Logger' 类的实例替换为 'org.slf4j.Logger' 和 'LoggerFactory'。重写日志记录器实例化以及所有 .info()、.debug() 和 .error() 调用，使用带有键值对的新结构化格式。

Gemini CLI 配备了一套内置工具，允许它与环境交互。这些工具包括用于文件系统操作（如读写）的工具、用于运行命令的 shell 工具，以及用于通过 Web 获取和搜索访问互联网的工具。为了更广泛的上下文，它使用专门的工具一次读取多个文件，以及用于保存信息以供以后会话使用的内存工具。这一功能建立在安全基础之上：沙箱隔离模型的操作以防止风险，而 MCP 服务器充当桥梁，使 Gemini 能够安全地连接到你的本地环境或其他 API。

## Aider

Aider 是一个开源 AI 编码助手，通过直接处理你的文件并将更改提交到 Git 来充当真正的结对程序员。其定义特征是其直接性；它应用编辑，运行测试来验证它们，并自动提交每个成功的更改。作为模型无关的工具，它为用户提供了对成本和能力的完全控制。其以 git 为中心的工作流使其成为重视效率、控制和所有代码修改的透明、可审计跟踪的开发人员的完美选择。

**示例用例：**

1. **测试驱动开发（TDD）：** 开发者可以说："为计算数字阶乘的函数创建一个失败的测试。"在 Aider 编写测试并失败后，下一个提示词是："现在，编写代码使测试通过。"Aider 实现该函数并再次运行测试以确认。  
2. **精确的 Bug 修复：** 给定一个 bug 报告，你可以指示 Aider："billing.py 中的 calculate\_total 函数在闰年上失败。将文件添加到上下文中，修复 bug，并根据现有测试套件验证你的修复。"  
3. **依赖项更新：** 你可以指示它："我们的项目使用过时版本的 'requests' 库。请检查所有 Python 文件，更新导入语句和任何已弃用的函数调用以与最新版本兼容，然后更新 requirements.txt。"

## GitHub Copilot CLI

GitHub Copilot CLI 将流行的 AI 结对程序员扩展到终端，其主要优势是与 GitHub 生态系统的原生深度集成。它理解*在 GitHub 中*项目的上下文。其 Agent 能力允许为其分配 GitHub issue，处理修复，并提交拉取请求供人工审查。

**示例用例：**

1. **自动化 Issue 解决：** 经理将 bug 工单（例如，"Issue \#123：修复分页中的差一错误"）分配给 Copilot Agent。然后 Agent 检出一个新分支，编写代码，并提交引用该 issue 的拉取请求，所有这些都无需手动开发者干预。  
2. **仓库感知的问答：** 团队中的新开发者可以问："在这个仓库中，数据库连接逻辑在哪里定义，它需要哪些环境变量？"Copilot CLI 使用其对整个仓库的感知提供带有文件路径的精确答案。  
3. **Shell 命令助手：** 当不确定复杂的 shell 命令时，用户可以问：gh? find all files larger than 50MB, compress them, and place them in an archive folder. Copilot 将生成执行任务所需的确切 shell 命令。

## Terminal-Bench：命令行界面中 AI Agent 的基准测试

Terminal-Bench 是一个新颖的评估框架，旨在评估 AI Agent 在命令行界面中执行复杂任务的熟练程度。由于其基于文本的沙箱特性，终端被确定为 AI Agent 操作的最佳环境。初始版本 Terminal-Bench-Core-v0 包含 80 个手动策划的任务，涵盖科学工作流和数据分析等领域。为了确保公平比较，开发了 Terminus（一个极简 Agent）作为各种语言模型的标准化测试平台。该框架设计为可扩展的，允许通过容器化或直接连接集成各种 Agent。未来的发展包括实现大规模并行评估和整合已建立的基准测试。该项目鼓励开源贡献以进行任务扩展和协作框架增强。

## 结论

这些强大的 AI 命令行 Agent 的出现标志着软件开发的根本转变，将终端转变为一个动态和协作的环境。正如我们所看到的，没有单一的"最佳"工具；相反，一个充满活力的生态系统正在形成，其中每个 Agent 都提供专门的优势。理想的选择完全取决于开发者的需求：Claude 适用于复杂的架构任务，Gemini 适用于多功能和多模态问题解决，Aider 适用于以 git 为中心和直接的代码编辑，GitHub Copilot 适用于无缝集成到 GitHub 工作流程中。随着这些工具的不断发展，利用它们的熟练程度将成为一项基本技能，从根本上改变开发者构建、调试和管理软件的方式。

## 参考文献

1. Anthropic. *Claude*. [https://docs.anthropic.com/en/docs/claude-code/cli-reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)   
2. Google Gemini Cli [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)   
3. Aider. [https://aider.chat/](https://aider.chat/)  
4. GitHub *Copilot CLI* [https://docs.github.com/en/copilot/github-copilot-enterprise/copilot-cli](https://docs.github.com/en/copilot/github-copilot-enterprise/copilot-cli)  
5. Terminal Bench: [https://www.tbench.ai/](https://www.tbench.ai/) 