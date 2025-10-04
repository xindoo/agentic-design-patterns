# 第 15 章：Agent 间通信（A2A）

即便拥有先进能力，单个 AI Agent 在处理复杂、多方面问题时仍常面临局限。为克服此限制，Agent 间通信（A2A）使不同 AI Agent（可能基于不同框架构建）能够有效协作。这种协作涉及无缝协调、任务委派和信息交换。

Google A2A 协议是旨在促进此类通用通信的开放标准。本章将探讨 A2A、其实际应用以及在 Google ADK 中的实现。

## Agent 间通信模式概述

Agent2Agent（A2A）协议是旨在实现不同 AI Agent 框架间通信与协作的开放标准。它确保互操作性，允许使用 LangGraph、CrewAI 或 Google ADK 等技术开发的 AI Agent 能够协同工作，无论其来源或框架差异如何。

A2A 获得了众多技术公司和服务提供商支持，包括 Atlassian、Box、LangChain、MongoDB、Salesforce、SAP 和 ServiceNow。Microsoft 计划将 A2A 集成至 Azure AI Foundry 和 Copilot Studio，展示了其对开放协议的承诺。此外，Auth0 和 SAP 正在将 A2A 支持集成到其平台和 Agent 中。

作为开源协议，A2A 欢迎社区贡献，以促进其发展和广泛采用。

## A2A 的核心概念

A2A 协议为 Agent 交互提供结构化方法，建立在若干核心概念之上。深入理解这些概念对任何开发或集成 A2A 兼容系统者都至关重要。A2A 的基础支柱包括核心参与者、Agent 卡片、Agent 发现、通信和任务、交互机制及安全性，所有这些都将详细审查。

**核心参与者**：A2A 涉及三个主要实体：

* 用户：发起对 Agent 协助的请求。
* A2A 客户端（客户端 Agent）：代表用户请求操作或信息的应用程序或 AI Agent。
* A2A 服务器（远程 Agent）：提供 HTTP 端点处理客户端请求并返回结果的 AI Agent 或系统。远程 Agent 作为"不透明"系统运行，意味着客户端无需了解其内部操作细节。

**Agent 卡片**：Agent 的数字身份由其 Agent 卡片定义，通常是 JSON 文件。此文件包含用于客户端交互和自动发现的关键信息，包括 Agent 身份、端点 URL 和版本。它还详细说明支持功能（如流式传输或推送通知）、特定技能、默认输入/输出模式以及身份验证要求。以下是 WeatherBot 的 Agent 卡片示例。

```json
{
  "name": "WeatherBot",
  "description": "Provides accurate weather forecasts and historical data.",
  "url": "http://weather-service.example.com/a2a",
  "version": "1.0.0",
  "capabilities": {
    "streaming": true,
    "pushNotifications": false,
    "stateTransitionHistory": true
  },
  "authentication": {
    "schemes": [
      "apiKey"
    ]
  },
  "defaultInputModes": [
    "text"
  ],
  "defaultOutputModes": [
    "text"
  ],
  "skills": [
    {
      "id": "get_current_weather",
      "name": "Get Current Weather",
      "description": "Retrieve real-time weather for any location.",
      "inputModes": [
        "text"
      ],
      "outputModes": [
        "text"
      ],
      "examples": [
        "What's the weather in Paris?",
        "Current conditions in Tokyo"
      ],
      "tags": [
        "weather",
        "current",
        "real-time"
      ]
    },
    {
      "id": "get_forecast",
      "name": "Get Forecast",
      "description": "Get 5-day weather predictions.",
      "inputModes": [
        "text"
      ],
      "outputModes": [
        "text"
      ],
      "examples": [
        "5-day forecast for New York",
        "Will it rain in London this weekend?"
      ],
      "tags": [
        "weather",
        "forecast",
        "prediction"
      ]
    }
  ]
}
```

**Agent 发现**：它允许客户端找到描述可用 A2A 服务器能力的 Agent 卡片。此过程存在几种策略：

* 知名 URI：Agent 在标准化路径（如 /.well-known/agent.json）托管其 Agent 卡片。此方法为公共或特定领域使用提供广泛、通常自动化的可访问性。
* 策展注册表：这些注册表提供集中目录，其中发布 Agent 卡片，可根据特定标准查询。这非常适合需要集中管理和访问控制的企业环境。
* 直接配置：Agent 卡片信息被嵌入或私下共享。此方法适用于紧密耦合或私有系统，其中动态发现并不重要。

无论选择何种方法，保护 Agent 卡片端点都很重要。这可通过访问控制、双向 TLS（mTLS）或网络限制实现，特别是当卡片包含敏感（虽非秘密）信息时。

**通信和任务**：在 A2A 框架中，通信围绕异步任务结构化，这些任务代表长时间运行进程的基本工作单元。每个任务被分配唯一标识符，并通过一系列状态（如已提交、工作中或已完成）移动，此设计支持复杂操作中的并行处理。Agent 间通信通过消息进行。

此通信包含属性（描述消息的键值元数据，如其优先级或创建时间）以及一个或多个部分（承载传递的实际内容，如纯文本、文件或结构化 JSON 数据）。Agent 在任务期间生成的有形输出称为工件。与消息类似，工件也由一个或多个部分组成，并可在结果可用时逐步流式传输。A2A 框架内所有通信都通过 HTTP(S) 进行，使用 JSON-RPC 2.0 协议作为有效载荷。为在多次交互中保持连续性，使用服务器生成的 contextId 来分组相关任务并保留上下文。

**交互机制**：请求/响应（轮询）服务器发送事件（SSE）。A2A 提供多种交互方法以适应各种 AI 应用需求，每种方法都有独特机制：

* 同步请求/响应：用于快速、即时操作。在此模型中，客户端发送请求并主动等待服务器处理并在单个同步交换中返回完整响应。
* 异步轮询：适用于需要更长时间处理的任务。客户端发送请求，服务器立即以"工作中"状态和任务 ID 确认。然后客户端可自由执行其他操作，并可通过发送新请求定期轮询服务器检查任务状态，直至标记为"已完成"或"失败"。
* 流式更新（服务器发送事件 - SSE）：适用于接收实时、增量结果。此方法建立从服务器到客户端的持久单向连接。它允许远程 Agent 持续推送更新（如状态更改或部分结果），而无需客户端发出多个请求。
* 推送通知（Webhook）：专为非常长时间运行或资源密集型任务设计，其中维护恒定连接或频繁轮询效率低下。客户端可注册 webhook URL，当任务状态发生重大变化（如完成时），服务器将向该 URL 发送异步通知（"推送"）。

Agent 卡片指定 Agent 是否支持流式传输或推送通知功能。此外，A2A 是模态无关的，意味着它不仅可以为文本促进这些交互模式，还可为音频和视频等其他数据类型促进，从而实现丰富的多模态 AI 应用。流式传输和推送通知功能均在 Agent 卡片中指定。

```json
## 同步请求示例
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "sendTask",
  "params": {
    "id": "task-001",
    "sessionId": "session-001",
    "message": {
      "role": "user",
      "parts": [
        {
          "type": "text",
          "text": "What is the exchange rate from USD to EUR?"
        }
      ]
    },
    "acceptedOutputModes": ["text/plain"],
    "historyLength": 5
  }
}
```

同步请求使用 sendTask 方法，其中客户端请求并期望对其查询的单个完整答案。相比之下，流式请求使用 sendTaskSubscribe 方法建立持久连接，允许 Agent 随时间发送多个增量更新或部分结果。

```json
## 流式请求示例
{
  "jsonrpc": "2.0",
  "id": "2",
  "method": "sendTaskSubscribe",
  "params": {
    "id": "task-002",
    "sessionId": "session-001",
    "message": {
      "role": "user",
      "parts": [
        {
          "type": "text",
          "text": "What's the exchange rate for JPY to GBP today?"
        }
      ]
    },
    "acceptedOutputModes": ["text/plain"],
    "historyLength": 5
  }
}
```

**安全性**：Agent 间通信（A2A）是系统架构的关键组成部分，能够在 Agent 间实现安全、无缝的数据交换。它通过多个内置机制确保稳健性和完整性。

双向传输层安全（TLS）：建立加密和认证连接，防止未经授权访问和数据拦截，确保安全通信。

全面审计日志：所有 Agent 间通信均被详细记录，明确信息流、涉及 Agent 和操作。此审计轨迹对问责、故障排除和安全分析至关重要。

Agent 卡片声明：身份验证要求在 Agent 卡片中明确声明，这是概述 Agent 身份、能力和安全策略的配置工件。这集中并简化了身份验证管理。

凭据处理：Agent 通常使用安全凭据（如 OAuth 2.0 令牌或 API 密钥）进行身份验证，通过 HTTP 头传递。此方法防止凭据在 URL 或消息正文中暴露，增强整体安全性。

## A2A 与 MCP

A2A 是补充 Anthropic 模型上下文协议（MCP）的协议（见图 1）。MCP 专注于为 Agent 构建上下文及其与外部数据和工具的交互，而 A2A 则促进 Agent 间协调和通信，实现任务委派与协作。

![][image1]

图 1：A2A 和 MCP 协议比较

A2A 旨在提高效率、降低集成成本，并促进复杂多 Agent AI 系统开发中的创新和互操作性。因此，深入理解 A2A 的核心组件和操作方法对有效设计、实施和应用协作式、互操作 AI Agent 系统至关重要。

## 实际应用和用例

Agent 间通信对跨不同领域构建复杂 AI 解决方案不可或缺，实现模块化、可扩展性和增强智能。

* **多框架协作**：A2A 主要用例是使独立 AI Agent 能够通信协作，无论其底层框架（如 ADK、LangChain、CrewAI）如何。这对构建复杂多 Agent 系统至关重要，不同 Agent 专门处理问题不同方面。
* **自动化工作流编排**：在企业环境中，A2A 可通过使 Agent 委派和协调任务促进复杂工作流。例如，一个 Agent 可能处理初始数据收集，然后委派给另一 Agent 分析，最后委派给第三 Agent 生成报告，所有通信均通过 A2A 协议进行。
* **动态信息检索**：Agent 可通信以检索和交换实时信息。主 Agent 可能从专门"数据获取 Agent"请求实时市场数据，后者然后使用外部 API 收集信息并发送回来。

## 实践代码示例

让我们检查 A2A 协议的实际应用。位于 [https://github.com/google-a2a/a2a-samples/tree/main/samples](https://github.com/google-a2a/a2a-samples/tree/main/samples) 的存储库提供 Java、Go 和 Python 示例，说明各种 Agent 框架（如 LangGraph、CrewAI、Azure AI Foundry 和 AG2）如何使用 A2A 通信。此存储库中所有代码均在 Apache 2.0 许可证下发布。为进一步说明 A2A 核心概念，我们将审查代码摘录，重点是基于 ADK 的 Agent 和 Google 身份验证工具设置 A2A 服务器。查看 [https://github.com/google-a2a/a2a-samples/blob/main/samples/python/agents/birthday\_planner\_adk/calendar\_agent/adk\_agent.py](https://github.com/google-a2a/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/adk_agent.py)

```python
import datetime
from google.adk.agents import LlmAgent  # type: ignore[import-untyped]
from google.adk.tools.google_api_tool import CalendarToolset  # type: ignore[import-untyped]

async def create_agent(client_id, client_secret) -> LlmAgent:
    """构造 ADK agent。"""
    toolset = CalendarToolset(client_id=client_id, client_secret=client_secret)
    return LlmAgent(
        model='gemini-2.0-flash-001',
        name='calendar_agent',
        description="An agent that can help manage a user's calendar",
        instruction=f"""
您是一个可以帮助管理用户日历的Agent。用户将请求有关其日历状态的信息或对其日历进行更改。
使用提供的工具与日历API交互。如果未指定，假定用户所需的日历是"primary"日历。
使用日历API工具时，请使用格式正确的RFC3339时间戳。今天是 {datetime.datetime.now()}。
        """,
        tools=await toolset.get_tools(),
    )
```

此 Python 代码定义异步函数 `create_agent`，用于构造 ADK LlmAgent。它首先使用提供的客户端凭据初始化 `CalendarToolset` 以访问 Google Calendar API。随后创建 `LlmAgent` 实例，配置指定 Gemini 模型、描述性名称和管理用户日历的指令。Agent 配备来自 `CalendarToolset` 的日历工具，使其能与 Calendar API 交互并响应有关日历状态或修改的用户查询。Agent 指令动态合并当前日期以提供时间上下文。为说明如何构造 Agent，让我们检查 GitHub 上 A2A 示例中 calendar_agent 的关键部分。

以下代码显示 Agent 如何使用其特定指令和工具定义。请注意，仅显示解释此功能所需代码；您可在此处访问完整文件：[https://github.com/a2aproject/a2a-samples/blob/main/samples/python/agents/birthday\_planner\_adk/calendar\_agent/\_\_main\_\_.py](https://github.com/a2aproject/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/__main__.py)

```python
def main(host: str, port: int):
    # 验证是否设置了 API 密钥。
    # 如果使用 Vertex AI API，则不需要。
    if os.getenv('GOOGLE_GENAI_USE_VERTEXAI') != 'TRUE' and not os.getenv(
        'GOOGLE_API_KEY'
    ):
        raise ValueError(
            'GOOGLE_API_KEY environment variable not set and '
            'GOOGLE_GENAI_USE_VERTEXAI is not TRUE.'
        )

    skill = AgentSkill(
        id='check_availability',
        name='Check Availability',
        description="Checks a user's availability for a time using their Google Calendar",
        tags=['calendar'],
        examples=['Am I free from 10am to 11am tomorrow?'],
    )

    agent_card = AgentCard(
        name='Calendar Agent',
        description="An agent that can manage a user's calendar",
        url=f'http://{host}:{port}/',
        version='1.0.0',
        defaultInputModes=['text'],
        defaultOutputModes=['text'],
        capabilities=AgentCapabilities(streaming=True),
        skills=[skill],
    )

    adk_agent = asyncio.run(create_agent(
        client_id=os.getenv('GOOGLE_CLIENT_ID'),
        client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    ))

    runner = Runner(
        app_name=agent_card.name,
        agent=adk_agent,
        artifact_service=InMemoryArtifactService(),
        session_service=InMemorySessionService(),
        memory_service=InMemoryMemoryService(),
    )

    agent_executor = ADKAgentExecutor(runner, agent_card)

    async def handle_auth(request: Request) -> PlainTextResponse:
        await agent_executor.on_auth_callback(
            str(request.query_params.get('state')), str(request.url)
        )
        return PlainTextResponse('Authentication successful.')

    request_handler = DefaultRequestHandler(
        agent_executor=agent_executor, task_store=InMemoryTaskStore()
    )

    a2a_app = A2AStarletteApplication(
        agent_card=agent_card, http_handler=request_handler
    )

    routes = a2a_app.routes()
    routes.append(
        Route(
            path='/authenticate',
            methods=['GET'],
            endpoint=handle_auth,
        )
    )

    app = Starlette(routes=routes)
    uvicorn.run(app, host=host, port=port)

if __name__ == '__main__':
    main()
```

此 Python 代码演示了设置符合 A2A 的"日历 Agent"，用于通过 Google Calendar 检查用户可用性。它涉及验证 API 密钥或 Vertex AI 配置以用于身份验证目的。Agent 能力（包括"check_availability"技能）在 AgentCard 中定义，该卡片还指定 Agent 网络地址。随后创建 ADK agent，配置内存服务以管理工件、会话和内存。然后代码初始化 Starlette Web 应用程序，合并身份验证回调和 A2A 协议处理程序，并使用 Uvicorn 执行它以通过 HTTP 公开 Agent。

这些示例说明了构建符合 A2A 的 Agent 的过程，从定义其能力到将其作为 Web 服务运行。通过利用 Agent 卡片和 ADK，开发人员可创建能与 Google Calendar 等工具集成的互操作 AI Agent。此实用方法展示了 A2A 在建立多 Agent 生态系统中的应用。

建议通过 [https://www.trickle.so/blog/how-to-build-google-a2a-project](https://www.trickle.so/blog/how-to-build-google-a2a-project) 上的代码演示进一步探索 A2A。此链接提供的资源包括 Python 和 JavaScript 中的示例 A2A 客户端和服务器、多 Agent Web 应用程序、命令行界面以及各种 Agent 框架的示例实现。

## 概览

**什么**：单个 AI Agent（特别是基于不同框架构建的 Agent）在处理复杂、多方面问题时通常会遇到困难。主要挑战是缺乏允许它们有效通信协作的通用语言或协议。这种隔离阻止了创建复杂系统，其中多个专门 Agent 可结合独特技能解决更大任务。若无标准化方法，集成这些不同 Agent 既昂贵又耗时，并阻碍更强大、更具凝聚力 AI 解决方案的开发。

**为什么**：Agent 间通信（A2A）协议为此问题提供开放、标准化解决方案。它是基于 HTTP 的协议，能实现互操作性，允许不同 AI Agent 无缝协调、委派任务和共享信息，无论其底层技术如何。核心组件是 Agent 卡片，这是描述 Agent 能力、技能和通信端点的数字身份文件，促进发现和交互。A2A 定义各种交互机制，包括同步和异步通信，以支持不同用例。通过为 Agent 协作创建通用标准，A2A 促进了构建复杂、多 Agent Agentic 系统的模块化和可扩展生态系统。

**经验法则**：当您需要协调两个或多个 AI Agent 间协作时使用此模式，特别是如果它们使用不同框架（如 Google ADK、LangGraph、CrewAI）构建。它非常适合构建复杂、模块化应用程序，其中专门 Agent 处理工作流特定部分，例如将数据分析委派给一个 Agent，将报告生成委派给另一 Agent。当 Agent 需要动态发现和使用其他 Agent 能力完成任务时，此模式也必不可少。

**视觉摘要**

**![][image2]**

图 2：A2A Agent 间通信模式

## 关键要点

关键要点：

* Google A2A 协议是开放、基于 HTTP 的标准，促进使用不同框架构建的 AI Agent 间通信协作。
* AgentCard 作为 Agent 数字标识符，允许其他 Agent 自动发现和理解其能力。
* A2A 提供同步请求-响应交互（使用 `tasks/send`）和流式更新（使用 `tasks/sendSubscribe`）以适应不同通信需求。
* 该协议支持多轮对话，包括 `input-required` 状态，允许 Agent 请求额外信息并在交互期间维护上下文。
* A2A 鼓励模块化架构，其中专门 Agent 可在不同端口上独立运行，实现系统可扩展性和分布。
* Trickle AI 等工具有助于可视化和跟踪 A2A 通信，帮助开发人员监控、调试和优化多 Agent 系统。
* 虽然 A2A 是用于管理不同 Agent 间任务和工作流的高级协议，但模型上下文协议（MCP）为 LLM 提供与外部资源交互的标准化接口。

## 结论

Agent 间通信（A2A）协议建立了重要的开放标准，以克服单个 AI Agent 的固有隔离。通过提供通用的基于 HTTP 的框架，它确保在不同平台上构建的 Agent 间的无缝协作和互操作性，例如 Google ADK、LangGraph 或 CrewAI。核心组件是 Agent 卡片，它作为数字身份，清楚定义 Agent 能力并使其他 Agent 能够动态发现。协议灵活性支持各种交互模式，包括同步请求、异步轮询和实时流式传输，满足广泛应用需求。

这使得能够创建模块化和可扩展架构，其中专门 Agent 可组合以编排复杂自动化工作流。安全性是基本方面，具有内置机制（如 mTLS 和明确身份验证要求）来保护通信。虽补充 MCP 等其他标准，但 A2A 的独特焦点是 Agent 间的高级协调和任务委派。主要技术公司的强大支持以及实际实现的可用性突显了其日益增长的重要性。该协议为开发人员构建更复杂、分布式和智能的多 Agent 系统铺平道路。最终，A2A 是促进创新和互操作的协作 AI 生态系统的基础支柱。

## 参考文献

1. Chen, B. (2025, April 22). *How to Build Your First Google A2A Project: A Step-by-Step Tutorial*. Trickle.so Blog. [https://www.trickle.so/blog/how-to-build-google-a2a-project](https://www.trickle.so/blog/how-to-build-google-a2a-project)
2. Google A2A GitHub Repository. [https://github.com/google-a2a/A2A](https://github.com/google-a2a/A2A)
3. Google Agent Development Kit (ADK) [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)
4. Getting Started with Agent-to-Agent (A2A) Protocol: [https://codelabs.developers.google.com/intro-a2a-purchasing-concierge\#0](https://codelabs.developers.google.com/intro-a2a-purchasing-concierge#0)
5. Google AgentDiscovery - [https://a2a-protocol.org/latest/](https://a2a-protocol.org/latest/)
6. Communication between different AI frameworks such as LangGraph, CrewAI, and Google ADK [https://www.trickle.so/blog/how-to-build-google-a2a-project](https://www.trickle.so/blog/how-to-build-google-a2a-project#setting-up-your-a2a-development-environment)
7. Designing Collaborative Multi-Agent Systems with the A2A Protocol [https://www.oreilly.com/radar/designing-collaborative-multi-agent-systems-with-the-a2a-protocol/](https://www.oreilly.com/radar/designing-collaborative-multi-agent-systems-with-the-a2a-protocol/)

[image1]: ../images/chapter-15/image1.png

[image2]: ../images/chapter-15/image2.png