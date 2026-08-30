---
layout: bilingual
lang: bilingual
---

# Appendix E - AI Agents on the CLI

# 附录 E - 命令行界面中的 AI 智能体

## Introduction

## 引言

The developer's command line, long a bastion of precise, imperative commands, is undergoing a profound transformation. It is evolving from a simple shell into an intelligent, collaborative workspace powered by a new class of tools: AI Agent Command-Line Interfaces (CLIs). These agents move beyond merely executing commands; they understand natural language, maintain context about your entire codebase, and can perform complex, multi-step tasks that automate significant parts of the development lifecycle.

开发者的命令行界面，长期以来都是精确命令式指令的堡垒，如今正经历着深刻的变革。它正在从一个简单的 Shell 演变为由一类新型工具驱动的智能协作工作空间：AI 智能体命令行界面（CLI）。这些智能体不仅仅是执行命令；它们理解自然语言，维护整个代码库的上下文，并能执行复杂的多步骤任务，自动化开发生命周期的重要环节。

This guide provides an in-depth look at four leading players in this burgeoning field, exploring their unique strengths, ideal use cases, and distinct philosophies to help you determine which tool best fits your workflow. It is important to note that many of the example use cases provided for a specific tool can often be accomplished by the other agents as well. The key differentiator between these tools frequently lies in the quality, efficiency, and nuance of the results they are able to achieve for a given task. There are specific benchmarks designed to measure these capabilities, which will be discussed in the following sections.

本指南深入剖析了这一新兴领域中的四个主要参与者，探索它们的独特优势、理想用例和设计理念，以帮助您确定最适合您工作流的工具。需要注意的是，为特定工具提供的许多示例用例通常也可以由其他智能体完成。这些工具之间的关键区别往往在于它们为给定任务所能达成结果的质量、效率和精细度。后续章节将讨论专门设计用于衡量这些能力的基准测试。

## Claude CLI (Claude Code)

## Claude CLI (Claude Code)

Anthropic's Claude CLI is engineered as a high-level coding agent with a deep, holistic understanding of a project's architecture. Its core strength is its "agentic" nature, allowing it to create a mental model of your repository for complex, multi-step tasks. The interaction is highly conversational, resembling a pair programming session where it explains its plans before executing. This makes it ideal for professional developers working on large-scale projects involving significant refactoring or implementing features with broad architectural impacts.

Anthropic 的 Claude CLI 被设计为一款高级编码智能体，对项目架构具有深度的全局理解。其核心优势在于它的"智能体"特性，能够为复杂的多步骤任务构建代码库的心智模型。交互过程高度对话化，类似于结对编程会话，它会在执行前阐述其计划。这使其成为从事大型项目的专业开发者的理想选择，这些项目涉及重大重构或实现具有广泛架构影响的功能。

**Example Use Cases:**

1. **Large-Scale Refactoring:** You can instruct it: "Our current user authentication relies on session cookies. Refactor the entire codebase to use stateless JWTs, updating the login/logout endpoints, middleware, and frontend token handling." Claude will then read all relevant files and perform the coordinated changes.
2. **API Integration:** After being provided with an OpenAPI specification for a new weather service, you could say: "Integrate this new weather API. Create a service module to handle the API calls, add a new component to display the weather, and update the main dashboard to include it."
3. **Documentation Generation**: Pointing it to a complex module with poorly documented code, you can ask: "Analyze the ./src/utils/data_processing.js file. Generate comprehensive TSDoc comments for every function, explaining its purpose, parameters, and return value."

**示例用例：**

1. **大规模重构：** 您可以指示："我们当前的用户认证依赖会话 cookie。请重构整个代码库以采用无状态 JWT，更新登录/登出端点、中间件及前端令牌处理逻辑。"Claude 将读取所有相关文件并执行协调一致的更改。
2. **API 集成：** 在提供新天气服务的 OpenAPI 规范后，您可以指令："集成此新天气 API。创建服务模块处理 API 调用，新增组件展示天气信息，并更新主仪表板以包含该组件。"
3. **文档生成：** 指向文档匮乏的复杂模块，您可以要求："分析 ./src/utils/data_processing.js 文件。为每个函数生成全面的 TSDoc 注释，阐明其用途、参数及返回值。"

Claude CLI functions as a specialized coding assistant, with inherent tools for core development tasks, including file ingestion, code structure analysis, and edit generation. Its deep integration with Git facilitates direct branch and commit management. The agent's extensibility is mediated by the Multi-tool Control Protocol (MCP), enabling users to define and integrate custom tools. This allows for interactions with private APIs, database queries, and execution of project-specific scripts. This architecture positions the developer as the arbiter of the agent's functional scope, effectively characterizing Claude as a reasoning engine augmented by user-defined tooling.

Claude CLI 作为专业化的编码助手，内置了核心开发任务工具，包括文件读取、代码结构分析和编辑生成。它与 Git 的深度集成支持直接进行分支和提交管理。该智能体的可扩展性通过多工具控制协议（MCP）实现，允许用户定义和集成自定义工具。这使其能够与私有 API 交互、执行数据库查询及运行项目特定脚本。这种架构将开发者定位为智能体功能范围的决策者，实质上是将 Claude 塑造为由用户定义工具增强的推理引擎。

## Gemini CLI

## Gemini CLI

Google's Gemini CLI is a versatile, open-source AI agent designed for power and accessibility. It stands out with the advanced Gemini 2.5 Pro model, a massive context window, and multimodal capabilities (processing images and text). Its open-source nature, generous free tier, and "Reason and Act" loop make it a transparent, controllable, and excellent all-rounder for a broad audience, from hobbyists to enterprise developers, especially those within the Google Cloud ecosystem.

Google 的 Gemini CLI 是一款功能强大的开源 AI 智能体，专为高性能和易用性而设计。它凭借先进的 Gemini 2.5 Pro 模型、超大上下文窗口以及多模态能力（可处理图像和文本）脱颖而出。其开源特性、慷慨的免费额度以及"推理与行动"循环机制，使其成为一款透明、可控且出色的全能型工具，受众广泛——从业余爱好者到企业开发者，尤其适合 Google Cloud 生态系统的用户。

**Example Use Cases:**

1. **Multimodal Development:** You provide a screenshot of a web component from a design file (gemini describe component.png) and instruct it: "Write the HTML and CSS code to build a React component that looks exactly like this. Make sure it's responsive."
2. **Cloud Resource Management:** Using its built-in Google Cloud integration, you can command: "Find all GKE clusters in the production project that are running versions older than 1.28 and generate a gcloud command to upgrade them one by one."
3. **Enterprise Tool Integration (via MCP):** A developer provides Gemini with a custom tool called get-employee-details that connects to the company's internal HR API. The prompt is: "Draft a welcome document for our new hire. First, use the get-employee-details --id=E90210 tool to fetch their name and team, and then populate the welcome_template.md with that information."
4. **Large-Scale Refactoring**: A developer needs to refactor a large Java codebase to replace a deprecated logging library with a new, structured logging framework. They can use Gemini with a prompt like: Read all *.java files in the 'src/main/java' directory. For each file, replace all instances of the 'org.apache.log4j' import and its 'Logger' class with 'org.slf4j.Logger' and 'LoggerFactory'. Rewrite the logger instantiation and all .info(), .debug(), and .error() calls to use the new structured format with key-value pairs.

**示例用例：**

1. **多模态开发：** 您提供设计稿中的 Web 组件截图（gemini describe component.png）并指示："编写 HTML 和 CSS 代码，构建外观与此完全一致的 React 组件。确保具备响应式设计。"
2. **云资源管理：** 利用其内置 Google Cloud 集成，您可以命令："查找生产项目中所有运行版本低于 1.28 的 GKE 集群，并生成逐个升级这些集群的 gcloud 命令。"
3. **企业工具集成（通过 MCP）：** 开发者为 Gemini 配置名为 get-employee-details 的自定义工具，该工具连接公司内部 HR API。提示词为："为新员工起草欢迎文档。首先使用 get-employee-details --id=E90210 工具获取其姓名与团队信息，随后用该信息填充 welcome_template.md。"
4. **大规模重构：** 开发者需重构大型 Java 代码库，以新型结构化日志框架替换已弃用的日志库。他们可对 Gemini 使用如下提示：读取 'src/main/java' 目录下所有 *.java 文件。针对每个文件，将 'org.apache.log4j' 导入及其 'Logger' 类实例替换为 'org.slf4j.Logger' 与 'LoggerFactory'。重写日志记录器实例化及所有 .info()、.debug() 和 .error() 调用，采用带键值对的新结构化格式。

Gemini CLI is equipped with a suite of built-in tools that allow it to interact with its environment. These include tools for file system operations (like reading and writing), a shell tool for running commands, and tools for accessing the internet via web fetching and searching. For broader context, it uses specialized tools to read multiple files at once and a memory tool to save information for later sessions. This functionality is built on a secure foundation: sandboxing isolates the model's actions to prevent risk, while MCP servers act as a bridge, enabling Gemini to safely connect to your local environment or other APIs.

Gemini CLI 配备了一套内置工具，使其能够与环境交互。这些工具包括用于文件系统操作（如读取和写入）的工具、用于运行命令的 Shell 工具，以及通过网页抓取和搜索访问互联网的工具。为获取更广泛的上下文，它使用专用工具批量读取文件，并利用内存工具保存信息供后续会话使用。这些功能构建在安全基础之上：沙箱机制隔离模型操作以防范风险，而 MCP 服务器充当桥梁，使 Gemini 能够安全连接至本地环境或其他 API。

## Aider

## Aider

Aider is an open-source AI coding assistant that acts as a true pair programmer by working directly on your files and committing changes to Git. Its defining feature is its directness; it applies edits, runs tests to validate them, and automatically commits every successful change. Being model-agnostic, it gives users complete control over cost and capabilities. Its git-centric workflow makes it perfect for developers who value efficiency, control, and a transparent, auditable trail of all code modifications.

Aider 是一款开源 AI 编码助手，通过直接操作文件并将变更提交至 Git，扮演真正的结对程序员角色。其标志性特征是直接性：它应用编辑、运行测试进行验证，并自动提交每个成功的变更。作为与模型无关的工具，它赋予用户对成本和能力的完全控制权。其以 Git 为中心的工作流，使其成为注重效率、控制力以及代码修改全程透明可审计的开发者的理想选择。

**Example Use Cases:**

1. **Test-Driven Development (TDD):** A developer can say: "Create a failing test for a function that calculates the factorial of a number." After Aider writes the test and it fails, the next prompt is: "Now, write the code to make the test pass." Aider implements the function and runs the test again to confirm.
2. **Precise Bug Squashing:** Given a bug report, you can instruct Aider: "The calculate_total function in billing.py fails on leap years. Add the file to the context, fix the bug, and verify your fix against the existing test suite."
3. **Dependency Updates:** You could instruct it: "Our project uses an outdated version of the 'requests' library. Please go through all Python files, update the import statements and any deprecated function calls to be compatible with the latest version, and then update requirements.txt."

**示例用例：**

1. **测试驱动开发（TDD）：** 开发者可指令："为计算数字阶乘的函数创建失败测试。"Aider 编写测试并确认失败后，后续提示为："现在编写代码使测试通过。"Aider 实现函数后再次运行测试以验证。
2. **精准 Bug 修复：** 给定 bug 报告，您可以指示 Aider："billing.py 中的 calculate_total 函数在闰年计算失败。将文件添加上下文，修复此 bug，并依据现有测试套件验证修复。"
3. **依赖项更新：** 您可以指令："我们项目使用的 'requests' 库版本过时。请检查所有 Python 文件，更新导入语句及任何已弃用的函数调用以兼容最新版本，随后更新 requirements.txt。"

## GitHub Copilot CLI

## GitHub Copilot CLI

GitHub Copilot CLI extends the popular AI pair programmer into the terminal, with its primary advantage being its native, deep integration with the GitHub ecosystem. It understands the context of a project *within GitHub*. Its agent capabilities allow it to be assigned a GitHub issue, work on a fix, and submit a pull request for human review.

GitHub Copilot CLI 将广受欢迎的 AI 结对编程体验延伸至终端环境，其核心优势在于与 GitHub 生态系统的原生深度集成。它能理解项目*在 GitHub 中*的上下文。其智能体功能支持分配 GitHub issue、实施修复并提交拉取请求供人工审核。

**Example Use Cases:**

1. **Automated Issue Resolution:** A manager assigns a bug ticket (e.g., "Issue #123: Fix off-by-one error in pagination") to the Copilot agent. The agent then checks out a new branch, writes the code, and submits a pull request referencing the issue, all without manual developer intervention.
2. **Repository-Aware Q&A:** A new developer on the team can ask: "Where in this repository is the database connection logic defined, and what environment variables does it require?" Copilot CLI uses its awareness of the entire repo to provide a precise answer with file paths.
3. **Shell Command Helper:** When unsure about a complex shell command, a user can ask: gh? find all files larger than 50MB, compress them, and place them in an archive folder. Copilot will generate the exact shell command needed to perform the task.

**示例用例：**

1. **自动化 Issue 解决：** 管理者将 bug 工单（如"Issue #123：修复分页差一错误"）分配给 Copilot 智能体。随后智能体创建新分支、编写代码并提交关联该 issue 的拉取请求，全程无需开发者手动介入。
2. **仓库感知问答：** 团队新成员可询问："本仓库中数据库连接逻辑定义于何处？需要哪些环境变量？"Copilot CLI 利用其对整个仓库的认知提供包含文件路径的精确答案。
3. **Shell 命令助手：** 当面对复杂 shell 命令不确定时，用户可输入：gh? find all files larger than 50MB, compress them, and place them in an archive folder. Copilot 将生成执行该任务所需的确切 shell 命令。

## Terminal-Bench: A Benchmark for AI Agents in Command-Line Interfaces

## Terminal-Bench：命令行界面中 AI 智能体基准测试框架

Terminal-Bench is a novel evaluation framework designed to assess the proficiency of AI agents in executing complex tasks within a command-line interface. The terminal is identified as an optimal environment for AI agent operation due to its text-based, sandboxed nature. The initial release, Terminal-Bench-Core-v0, comprises 80 manually curated tasks spanning domains such as scientific workflows and data analysis. To ensure equitable comparisons, Terminus, a minimalistic agent, was developed to serve as a standardized testbed for various language models. The framework is designed for extensibility, allowing for the integration of diverse agents through containerization or direct connections. Future developments include enabling massively parallel evaluations and incorporating established benchmarks. The project encourages open-source contributions for task expansion and collaborative framework enhancement.

Terminal-Bench 是一套创新的评估框架，专用于衡量 AI 智能体在命令行界面中执行复杂任务的熟练程度。鉴于其基于文本的沙箱特性，终端被确认为 AI 智能体的理想环境。初始版本 Terminal-Bench-Core-v0 包含 80 项人工精选的任务，涵盖科学工作流与数据分析等领域。为确保公平对比，开发了极简智能体 Terminus 作为各类语言模型的标准化测试平台。该框架具备高度可扩展性，支持通过容器化或直接连接集成多样化智能体。未来规划包括实现大规模并行评估及整合现有基准测试。项目鼓励开源社区贡献任务扩展与框架协同优化。

## Conclusion

## 结论

The emergence of these powerful AI command-line agents marks a fundamental shift in software development, transforming the terminal into a dynamic and collaborative environment. As we've seen, there is no single "best" tool; instead, a vibrant ecosystem is forming where each agent offers a specialized strength. The ideal choice depends entirely on the developer's needs: Claude for complex architectural tasks, Gemini for versatile and multimodal problem-solving, Aider for git-centric and direct code editing, and GitHub Copilot for seamless integration into the GitHub workflow. As these tools continue to evolve, proficiency in leveraging them will become an essential skill, fundamentally changing how developers build, debug, and manage software.

这些功能强大的 AI 命令行智能体的出现，标志着软件开发范式的根本性转变——将终端转化为动态协作环境。正如我们所见，不存在单一的"最佳"工具；相反，一个生机勃勃的生态系统正在成型，每个智能体都有其独特专长。理想选择完全取决于开发者需求：Claude 擅长复杂架构任务，Gemini 强于多功能多模态问题求解，Aider 专注 Git 中心化直接代码编辑，GitHub Copilot 则无缝融入 GitHub 工作流。随着这些工具的持续演进，熟练运用它们将成为核心技能，从根本上重塑开发者构建、调试与管理软件的方式。

## References

## 参考文献

 1. Anthropic. *Claude*. [https://docs.anthropic.com/en/docs/claude-code/cli-reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)
 2. Google Gemini Cli [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
 3. Aider. [https://aider.chat/](https://aider.chat/)
 4. GitHub *Copilot CLI* [https://docs.github.com/en/copilot/github-copilot-enterprise/copilot-cli](https://docs.github.com/en/copilot/github-copilot-enterprise/copilot-cli)
 5. Terminal Bench: [https://www.tbench.ai/](https://www.tbench.ai/)
