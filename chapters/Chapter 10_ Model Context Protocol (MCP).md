# 第 10 章：模型上下文协议 (MCP)

要使 LLM 作为 Agent 有效运作，其能力必须超越多模态生成。与外部环境的交互不可或缺，包括访问实时数据、使用外部软件以及执行特定操作任务。模型上下文协议（MCP）通过提供标准化接口满足此需求，使 LLM 能与外部资源交互。该协议是实现一致和可预测集成的关键机制。

## MCP 模式概述

想象一个通用适配器，允许任何 LLM 连接到任何外部系统、数据库或工具，无需为每个连接进行自定义集成。这本质上就是模型上下文协议（MCP）的功能。它是一个开放标准，旨在标准化 Gemini、OpenAI 的 GPT 模型、Mixtral 和 Claude 等 LLM 与外部应用程序、数据源和工具的通信方式。可将其视为通用连接机制，简化 LLM 获取上下文、执行操作以及与各类系统交互的方式。

MCP 基于客户端-服务器架构运行。它定义了不同元素——数据（称为资源）、交互模板（本质是提示）和可操作函数（称为工具）——如何由 MCP 服务器公开。这些元素随后由 MCP 客户端使用，客户端可以是 LLM 宿主应用程序或 AI Agent 本身。这种标准化方法显著降低了将 LLM 集成到多样化操作环境中的复杂性。

然而，MCP 是"Agent 接口"的契约，其有效性很大程度上取决于其所公开底层 API 的设计。存在开发人员仅简单包装现有遗留 API 而不进行修改的风险，这对 Agent 可能并非最优。例如，若票务系统 API 仅允许逐个检索完整票务详情，被要求总结高优先级票务的 Agent 在处理大量数据时将变得缓慢且不准确。为真正有效，底层 API 应通过过滤和排序等确定性特性进行改进，以帮助非确定性 Agent 高效工作。这凸显了 Agent 无法神奇替代确定性工作流；它们通常需要更强确定性支持才能成功。

此外，MCP 可包装输入或输出对 Agent 仍非固有可理解的 API。仅当 API 数据格式对 Agent 友好时才有用，而 MCP 本身无法保证此点。例如，为返回 PDF 文件的文档存储创建 MCP 服务器基本无用，若消费 Agent 无法解析 PDF 内容。更好方法是首先创建返回文档文本版本（如 Markdown）的 API，使 Agent 能实际阅读和处理。这表明开发人员必须考虑的不只是连接，还有所交换数据的性质，以确保真正兼容性。

## MCP 与工具函数调用

模型上下文协议（MCP）和工具函数调用是使 LLM 能与外部能力（含工具）交互并执行操作的不同机制。虽然两者都服务于扩展 LLM 超越文本生成的能力，但它们在方法和抽象级别上存在差异。

工具函数调用可视为 LLM 对特定预定义工具或函数的直接请求。请注意，在此上下文中我们交替使用"工具"和"函数"二词。这种交互特点是一对一通信模型，LLM 根据其对需要外部操作用户意图的理解格式化请求。随后应用程序代码执行此请求并将结果返回 LLM。此过程通常为专有，且在不同 LLM 提供商间存在差异。

相比之下，模型上下文协议（MCP）作为 LLM 发现、通信和使用外部能力的标准化接口运行。它作为开放协议促进与各种工具和系统交互，旨在建立任何兼容工具可被任何兼容 LLM 访问的生态系统。这促进了不同系统和实现间的互操作性、可组合性和可重用性。通过采用联合模型，我们显著提升互操作性并释放现有资产价值。此策略允许我们通过简单包装符合 MCP 接口将分散和遗留服务引入现代生态系统。这些服务继续独立运行，但现可组合到新应用程序和工作流中，其协作由 LLM 协调。这促进了敏捷性和可重用性，而无需对基础系统进行昂贵重写。

以下是 MCP 与工具函数调用的基本区别：

| 特性 | 工具函数调用 | 模型上下文协议（MCP） |
| ----- | ----- | ----- |
| **标准化** | 专有和供应商特定。格式和实现在不同 LLM 提供商间各异 | 开放标准化协议，促进不同 LLM 和工具间互操作性 |
| **范围** | LLM 请求执行特定预定义函数的直接机制 | 更广泛框架，定义 LLM 和外部工具如何相互发现和通信 |
| **架构** | LLM 与应用程序工具处理逻辑间的一对一交互 | 客户端-服务器架构，LLM 驱动应用程序（客户端）可连接并使用各种 MCP 服务器（工具） |
| **发现** | LLM 被明确告知特定对话上下文中哪些工具可用 | 支持动态发现可用工具。MCP 客户端可查询服务器以查看其提供能力 |
| **可重用性** | 工具集成通常与所用特定应用程序和 LLM 紧密耦合 | 促进开发可重用独立"MCP 服务器"，可被任何兼容应用程序访问 |

可将工具函数调用想象为给 AI 一组特定定制工具，如特定扳手和螺丝刀。这对具有固定任务集的车间高效。另一方面，MCP（模型上下文协议）如同创建通用标准化电源插座系统。它本身不提供工具，但允许任何制造商任何兼容工具插入工作，从而实现动态不断扩展的车间。

简而言之，函数调用提供对少数特定函数的直接访问，而 MCP 是标准化通信框架，让 LLM 发现和使用广泛外部资源。对简单应用程序，特定工具足够；对需要适应的复杂互联 AI 系统，像 MCP 的通用标准必不可少。

## MCP 的其他考虑因素

虽然 MCP 提供了强大框架，但全面评估需考虑影响其适用性的几个关键方面。让我们详细探讨某些方面：

* **工具 vs. 资源 vs. 提示**：理解这些组件的特定角色很重要。资源是静态数据（如 PDF 文件、数据库记录）。工具是执行操作的可执行函数（如发送电子邮件、查询 API）。提示是指导 LLM 如何与资源或工具交互的模板，确保交互结构化和有效
* **可发现性**：MCP 的关键优势是 MCP 客户端可动态查询服务器了解其提供的工具和资源。这种"即时"发现机制对需要适应新能力而无需重新部署的 Agent 非常强大
* **安全性**：通过任何协议公开工具和数据都需要强大安全措施。MCP 实现必须包含身份验证和授权，以控制哪些客户端可访问哪些服务器及允许执行哪些特定操作
* **实现**：虽然 MCP 是开放标准，但其实现可能复杂。然而提供商正开始简化此过程。例如 Anthropic 或 FastMCP 等模型提供商提供 SDK，抽象大部分样板代码，使开发人员更易创建和连接 MCP 客户端和服务器
* **错误处理**：全面错误处理策略至关重要。协议必须定义如何将错误（如工具执行失败、服务器不可用、无效请求）传达回 LLM，使其能理解失败并可能尝试替代方法
* **本地 vs. 远程服务器**：MCP 服务器可部署在与 Agent 相同机器本地，或远程部署在不同服务器。本地服务器可能因速度和敏感数据安全性被选择，而远程服务器架构允许组织内共享可扩展访问公共工具
* **按需 vs. 批处理**：MCP 可支持按需交互式会话和大规模批处理。选择取决于应用程序，从需要立即工具访问的实时对话 Agent 到批量处理记录的数据分析管道
* **传输机制**：协议还定义通信的底层传输层。对本地交互，使用基于 STDIO（标准输入/输出）的 JSON-RPC 实现高效进程间通信。对远程连接，利用 Web 友好协议如可流式 HTTP 和服务器发送事件（SSE）实现持久高效客户端-服务器通信

模型上下文协议使用客户端-服务器模型标准化信息流。理解组件交互是 MCP 高级 Agent 行为关键：

1. **大型语言模型（LLM）**：核心智能。处理用户请求，制定计划，决定何时需要访问外部信息或执行操作
2. **MCP 客户端**：围绕 LLM 的应用程序或包装器。充当中介，将 LLM 意图转换为符合 MCP 标准的正式请求。负责发现、连接和与 MCP 服务器通信
3. **MCP 服务器**：通往外部世界的网关。向任何授权 MCP 客户端公开一组工具、资源和提示。每个服务器通常负责特定领域，如连接公司内部数据库、电子邮件服务或公共 API
4. **可选的第三方（3P）服务**：代表 MCP 服务器管理和公开的实际外部工具、应用程序或数据源。是执行请求操作的最终端点，如查询专有数据库、与 SaaS 平台交互或调用公共天气 API

交互流程如下：

1. **发现**：MCP 客户端代表 LLM 查询 MCP 服务器询问其提供能力。服务器响应清单列出可用工具（如 send_email）、资源（如 customer_database）和提示
2. **请求制定**：LLM 确定需要使用发现的工具之一。例如决定发送电子邮件。制定请求指定要使用的工具（send_email）和必要参数（收件人、主题、正文）
3. **客户端通信**：MCP 客户端获取 LLM 制定的请求，将其作为标准化调用发送到适当 MCP 服务器
4. **服务器执行**：MCP 服务器接收请求。对客户端进行身份验证，验证请求，然后通过与底层软件交互执行指定操作（如调用电子邮件 API 的 send() 函数）
5. **响应和上下文更新**：执行后，MCP 服务器将标准化响应发送回 MCP 客户端。此响应指示操作是否成功，包括任何相关输出（如已发送电子邮件的确认 ID）。然后客户端将此结果传递回 LLM，更新其上下文并使其能继续任务的下一步

## 实际应用和用例

MCP 显著扩展了 AI/LLM 能力，使其更加多功能强大。以下是九个关键用例：

* **数据库集成**：MCP 允许 LLM 和 Agent 无缝访问数据库中结构化数据并与之交互。例如使用数据库 MCP 工具箱，Agent 可查询 Google BigQuery 数据集检索实时信息、生成报告或更新记录，所有由自然语言命令驱动
* **生成媒体编排**：MCP 使 Agent 能与高级生成媒体服务集成。通过生成媒体服务的 MCP 工具，Agent 可编排涉及 Google Imagen 图像生成、Google Veo 视频创建、Google Chirp 3 HD 逼真语音或 Google Lyria 音乐创作的工作流，允许在 AI 应用程序中进行动态内容创建
* **外部 API 交互**：MCP 为 LLM 提供调用任何外部 API 并接收响应的标准化方式。这意味着 Agent 可获取实时天气数据、拉取股票价格、发送电子邮件或与 CRM 系统交互，将其能力扩展到核心语言模型之外
* **基于推理的信息提取**：利用 LLM 强大推理能力，MCP 促进有效的依赖查询信息提取，超越传统搜索和检索系统。Agent 可分析文本并提取精确回答用户复杂问题的特定条款、数字或陈述，而非传统搜索工具返回整个文档
* **自定义工具开发**：开发人员可构建自定义工具并通过 MCP 服务器公开（如使用 FastMCP）。这允许以标准化易于使用格式向 LLM 和其他 Agent 提供专门内部函数或专有系统，而无需直接修改 LLM
* **标准化的 LLM 到应用程序通信**：MCP 确保 LLM 与它们交互的应用程序间有一致通信层。这减少了集成开销，促进不同 LLM 提供商和宿主应用程序间互操作性，并简化复杂 Agent 系统开发
* **复杂工作流编排**：通过组合各种 MCP 公开工具和数据源，Agent 可编排高度复杂多步骤工作流。例如 Agent 可从数据库检索客户数据，生成个性化营销图像，起草定制电子邮件，然后发送，所有通过与不同 MCP 服务交互完成
* **物联网设备控制**：MCP 可促进 LLM 与物联网（IoT）设备交互。Agent 可使用 MCP 向智能家居电器、工业传感器或机器人发送命令，实现自然语言控制和物理系统自动化
* **金融服务自动化**：在金融服务中，MCP 可使 LLM 与各种金融数据源、交易平台或合规系统交互。Agent 可能分析市场数据、执行交易、生成个性化财务建议或自动化监管报告，同时保持安全和标准化通信

简而言之，模型上下文协议（MCP）使 Agent 能从数据库、API 和 Web 资源访问实时信息。还允许 Agent 执行如发送电子邮件、更新记录、控制设备以及通过集成和处理来自各种来源数据执行复杂任务等操作。此外，MCP 支持 AI 应用程序的媒体生成工具

## 使用 ADK 的实践代码示例

本节概述了如何连接到提供文件系统操作的本地 MCP 服务器，使 ADK Agent 能够与本地文件系统交互。

## 使用 MCPToolset 的 Agent 设置

要配置 Agent 进行文件系统交互，必须创建一个 `agent.py` 文件（例如，在 `./adk_agent_samples/mcp_agent/agent.py`）。`MCPToolset` 在 `LlmAgent` 对象的 `tools` 列表中实例化。至关重要的是，必须将 `args` 列表中的 `"/path/to/your/folder"` 替换为本地系统上 MCP 服务器可以访问的目录的绝对路径。此目录将是 Agent 执行的文件系统操作的根目录。

```python
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

## 创建一个可靠的绝对路径，指向名为 'mcp_managed_files' 的文件夹
## 该文件夹位于此 Agent 脚本所在的同一目录中。
## 这确保了 Agent 开箱即用地进行演示。
## 对于生产环境，您需要将此路径指向一个更持久和安全的位置。
TARGET_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mcp_managed_files")

## 在 Agent 需要之前确保目标目录存在。
os.makedirs(TARGET_FOLDER_PATH, exist_ok=True)

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='filesystem_assistant_agent',
    instruction=(
        'Help the user manage their files. You can list files, read files, and write files. '
        f'You are operating in the following directory: {TARGET_FOLDER_PATH}'
    ),
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command='npx',
                args=[
                    "-y",  # npx 的参数，用于自动确认安装
                    "@modelcontextprotocol/server-filesystem",
                    # 这必须是文件夹的绝对路径。
                    TARGET_FOLDER_PATH,
                ],
            ),
            # 可选：您可以过滤从 MCP 服务器公开的工具。
            # 例如，仅允许读取：
            # tool_filter=['list_directory', 'read_file']
        )
    ],
)
```

`npx`（Node Package Execute）与 npm（Node Package Manager）版本 5.2.0 及更高版本捆绑在一起，是一个实用程序，可以直接从 npm 注册表执行 Node.js 包。这消除了全局安装的需要。本质上，`npx` 作为 npm 包运行器，它通常用于运行许多社区 MCP 服务器，这些服务器作为 Node.js 包分发。

创建 __init__.py 文件是必要的，以确保 agent.py 文件被识别为 Agent 开发工具包（ADK）的可发现 Python 包的一部分。此文件应与 [agent.py](http://agent.py) 位于同一目录中。

```python
## ./adk_agent_samples/mcp_agent/__init__.py
from . import agent
```

当然，还可以使用其他受支持的命令。例如，可以按如下方式连接到 python3：

```python
connection_params = StdioConnectionParams(
    server_params={
        "command": "python3",
        "args": ["./agent/mcp_server.py"],
        "env": {
            "SERVICE_ACCOUNT_PATH": SERVICE_ACCOUNT_PATH,
            "DRIVE_FOLDER_ID": DRIVE_FOLDER_ID
        }
    }
)
```

在 Python 的上下文中，UVX 是指一个命令行工具，它利用 uv 在临时的、隔离的 Python 环境中执行命令。本质上，它允许您运行 Python 工具和包，而无需全局安装或在项目环境中安装它们。您可以通过 MCP 服务器运行它。

```python
connection_params = StdioConnectionParams(
    server_params={
        "command": "uvx",
        "args": ["mcp-google-sheets@latest"],
        "env": {
            "SERVICE_ACCOUNT_PATH": SERVICE_ACCOUNT_PATH,
            "DRIVE_FOLDER_ID": DRIVE_FOLDER_ID
        }
    }
)
```

创建 MCP 服务器后，下一步是连接到它。

## 使用 ADK Web 连接 MCP 服务器

首先，执行 'adk web'。在终端中导航到 mcp_agent 的父目录（例如，adk_agent_samples）并运行：

```bash
cd ./adk_agent_samples # 或您的等效父目录
adk web
```

ADK Web UI 在浏览器中加载后，从 Agent 菜单中选择 `filesystem_assistant_agent`。接下来，尝试以下提示：

* "Show me the contents of this folder."
* "Read the `sample.txt` file."（假设 `sample.txt` 位于 `TARGET_FOLDER_PATH`。）
* "What's in `another_file.md`?"

## 使用 FastMCP 创建 MCP 服务器

FastMCP 是一个高级 Python 框架，旨在简化 MCP 服务器的开发。它提供了一个抽象层，简化了协议复杂性，允许开发人员专注于核心逻辑。

该库使用简单的 Python 装饰器能够快速定义工具、资源和提示词。一个显著的优势是其自动模式生成，它智能地解释 Python 函数签名、类型提示和文档字符串，以构建必要的 AI 模型接口规范。这种自动化最大限度地减少了手动配置并减少了人为错误。

除了基本的工具创建之外，FastMCP 还促进了高级架构模式，如服务器组合和代理。这使得能够模块化开发复杂的、多组件系统，并将现有服务无缝集成到 AI 可访问的框架中。此外，FastMCP 包括针对高效、分布式和可扩展的 AI 驱动应用程序的优化。

## 使用 FastMCP 设置服务器

为了说明，考虑服务器提供的基本"greet"工具。一旦激活，ADK Agent 和其他 MCP 客户端可以使用 HTTP 与此工具交互。

```python
## fastmcp_server.py
## 此脚本演示如何使用 FastMCP 创建一个简单的 MCP 服务器。
## 它公开一个生成问候语的单一工具。

## 1. 确保您已安装 FastMCP：
## pip install fastmcp

from fastmcp import FastMCP, Client

## 初始化 FastMCP 服务器。
mcp_server = FastMCP()

## 定义一个简单的工具函数。
## `@mcp_server.tool` 装饰器将此 Python 函数注册为 MCP 工具。
## 文档字符串成为 LLM 的工具描述。
@mcp_server.tool
def greet(name: str) -> str:
    """
    生成个性化的问候语。

    参数：
        name: 要问候的人的名字。

    返回：
        问候语字符串。
    """
    return f"Hello, {name}! Nice to meet you."

## 或者如果您想从脚本运行它：
if __name__ == "__main__":
    mcp_server.run(
        transport="http",
        host="127.0.0.1",
        port=8000
    )
```

这个 Python 脚本定义了一个名为 greet 的单一函数，它接受一个人的名字并返回个性化的问候语。此函数上方的 @tool() 装饰器自动将其注册为 AI 或其他程序可以使用的工具。函数的文档字符串和类型提示被 FastMCP 用来告诉 Agent 工具的工作原理、需要什么输入以及它将返回什么。

当脚本执行时，它启动 FastMCP 服务器，该服务器在 localhost:8000 上监听请求。这使得 greet 函数作为网络服务可用。然后可以将 Agent 配置为连接到此服务器，并使用 greet 工具生成问候语，作为更大任务的一部分。服务器持续运行，直到手动停止。

## 使用 ADK Agent 消费 FastMCP 服务器

可以将 ADK Agent 设置为 MCP 客户端，以使用正在运行的 FastMCP 服务器。这需要使用 FastMCP 服务器的网络地址配置 HttpServerParameters，通常是 http://localhost:8000。

可以包含 tool_filter 参数以限制 Agent 对服务器提供的特定工具的使用，例如 'greet'。当提示"Greet John Doe"等请求时，Agent 的嵌入式 LLM 识别通过 MCP 可用的 'greet' 工具，使用参数"John Doe"调用它，并返回服务器的响应。此过程演示了通过 MCP 公开的用户定义工具与 ADK Agent 的集成。

要建立此配置，需要一个 Agent 文件（例如，位于 ./adk_agent_samples/fastmcp_client_agent/ 的 agent.py）。此文件将实例化一个 ADK Agent，并使用 HttpServerParameters 与正在运行的 FastMCP 服务器建立连接。

```python
## ./adk_agent_samples/fastmcp_client_agent/agent.py
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, HttpServerParameters

## 定义 FastMCP 服务器的地址。
## 确保您的 fastmcp_server.py（之前定义的）正在此端口上运行。
FASTMCP_SERVER_URL = "http://localhost:8000"

root_agent = LlmAgent(
    model='gemini-2.0-flash',  # 或您首选的模型
    name='fastmcp_greeter_agent',
    instruction='You are a friendly assistant that can greet people by their name. Use the "greet" tool.',
    tools=[
        MCPToolset(
            connection_params=HttpServerParameters(
                url=FASTMCP_SERVER_URL,
            ),
            # 可选：过滤从 MCP 服务器公开的工具
            # 对于此示例，我们只期望 'greet'
            tool_filter=['greet']
        )
    ],
)
```

该脚本定义了一个名为 fastmcp_greeter_agent 的 Agent，它使用 Gemini 语言模型。它被赋予特定的指令，作为一个友好的助手，其目的是问候人们。至关重要的是，该代码为此 Agent 配备了执行其任务的工具。它配置了一个 MCPToolset 来连接到在 localhost:8000 上运行的独立服务器，该服务器应该是前面示例中的 FastMCP 服务器。Agent 被明确授予访问该服务器上托管的 greet 工具的权限。本质上，此代码设置了系统的客户端，创建了一个智能 Agent，它理解其目标是问候人们，并确切地知道使用哪个外部工具来完成它。

在 fastmcp_client_agent 目录中创建 __init__.py 文件是必要的。这确保了 Agent 被识别为 ADK 的可发现 Python 包。

首先，打开一个新终端并运行 `python fastmcp_server.py` 来启动 FastMCP 服务器。接下来，在终端中转到 `fastmcp_client_agent` 的父目录（例如，`adk_agent_samples`）并执行 `adk web`。一旦 ADK Web UI 在浏览器中加载，从 Agent 菜单中选择 `fastmcp_greeter_agent`。然后可以通过输入"Greet John Doe"等提示来测试它。Agent 将使用 FastMCP 服务器上的 `greet` 工具创建响应。

## 概览

**是什么**：要作为有效 Agent 运作，LLM 必须超越简单文本生成。它们需要与外部环境交互能力以访问当前数据并使用外部软件。若无标准化通信方法，LLM 与外部工具或数据源间每次集成都成为定制复杂不可重用工作。这种临时方法阻碍可扩展性，并使构建复杂互联 AI 系统变得困难低效

**为什么**：模型上下文协议（MCP）通过充当 LLM 和外部系统间通用接口提供标准化解决方案。它建立开放标准化协议，定义如何发现和使用外部能力。基于客户端-服务器模型运行，MCP 允许服务器向任何兼容客户端公开工具、数据资源和交互式提示。LLM 驱动应用程序充当这些客户端，以可预测方式动态发现和与可用资源交互。这种标准化方法促进了可互操作和可重用组件生态系统，显著简化复杂 Agent 工作流开发

**经验法则**：在构建需要与各种不断发展的外部工具、数据源和 API 交互的复杂可扩展或企业级 Agent 系统时，使用模型上下文协议（MCP）。当不同 LLM 和工具间互操作性是优先考虑事项时，以及当 Agent 需要能够动态发现新能力而无需重新部署时，它是理想选择。对具有固定有限数量预定义函数的简单应用程序，直接工具函数调用可能足够

**可视化摘要**

![](../images/chapter-10/image1.png)

图 1：模型上下文协议

## 关键要点

以下是本章核心要点：

* 模型上下文协议（MCP）是开放标准，促进 LLM 与外部应用程序、数据源和工具间标准化通信
* 它采用客户端-服务器架构，定义公开和使用资源、提示和工具的方法
* Agent 开发工具包（ADK）支持使用现有 MCP 服务器以及通过 MCP 服务器公开 ADK 工具
* FastMCP 简化了 MCP 服务器开发和管理，特别用于公开在 Python 中实现的工具
* 生成媒体服务的 MCP 工具允许 Agent 与 Google Cloud 的生成媒体能力（Imagen、Veo、Chirp 3 HD、Lyria）集成
* MCP 使 LLM 和 Agent 能与现实世界系统交互，访问动态信息，并执行超越文本生成的操作

## 结论

模型上下文协议（MCP）是开放标准，促进大型语言模型（LLM）与外部系统间通信。它采用客户端-服务器架构，使 LLM 能通过标准化工具访问资源、使用提示和执行操作。MCP 允许 LLM 与数据库交互、管理生成媒体工作流、控制物联网设备以及自动化金融服务。实际示例演示了设置 Agent 与 MCP 服务器通信的方法，包括文件系统服务器和使用 FastMCP 构建的服务器，说明了其与 Agent 开发工具包（ADK）的集成。MCP 是开发超越基本语言能力的交互式 AI Agent 的关键组件

## 参考文献

1. Model Context Protocol (MCP) Documentation. (Latest). *Model Context Protocol (MCP)*. [https://google.github.io/adk-docs/mcp/](https://google.github.io/adk-docs/mcp/)
2. FastMCP Documentation. FastMCP. [https://github.com/jlowin/fastmcp](https://github.com/jlowin/fastmcp)
3. MCP Tools for Genmedia Services. *MCP Tools for Genmedia Services*. [https://google.github.io/adk-docs/mcp/#mcp-servers-for-google-cloud-genmedia](https://google.github.io/adk-docs/mcp/#mcp-servers-for-google-cloud-genmedia)
4. MCP Toolbox for Databases Documentation. (Latest). *MCP Toolbox for Databases*. [https://google.github.io/adk-docs/mcp/databases/](https://google.github.io/adk-docs/mcp/databases/)