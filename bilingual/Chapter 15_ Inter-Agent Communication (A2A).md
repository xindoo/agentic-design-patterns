# Chapter 15: Inter-Agent Communication (A2A)

# 第 15 章：智能体间通信（A2A）

Individual AI agents often face limitations when tackling complex, multifaceted problems, even with advanced capabilities. To overcome this, Inter-Agent Communication (A2A) enables diverse AI agents, potentially built with different frameworks, to collaborate effectively. This collaboration involves seamless coordination, task delegation, and information exchange.

尽管单个 AI 智能体具备先进能力，但在处理复杂、多方面问题时仍然常常面临局限性。为了克服这一限制，智能体间通信（A2A）使得不同 AI 智能体（可能基于不同框架构建）能够进行有效协作。这种协作涉及无缝协调、任务委派和信息交换。

Google's A2A protocol is an open standard designed to facilitate this universal communication. This chapter will explore A2A, its practical applications, and its implementation within the Google ADK.

Google A2A 协议是一个旨在促进此类通用通信的开放标准。本章将探讨 A2A 的基本概念、实际应用以及在 Google ADK 中的具体实现。

## Inter-Agent Communication Pattern Overview

## 智能体间通信模式速览

The Agent2Agent (A2A) protocol is an open standard designed to enable communication and collaboration between different AI agent frameworks. It ensures interoperability, allowing AI agents developed with technologies like LangGraph, CrewAI, or Google ADK to work together regardless of their origin or framework differences.

Agent2Agent（A2A）协议是一个旨在实现不同 AI 智能体框架间通信与协作的开放标准。它确保了互操作性，允许使用 LangGraph、CrewAI 或 Google ADK 等技术开发的 AI 智能体协同工作，无论其来源或框架差异如何。

A2A is supported by a range of technology companies and service providers, including Atlassian, Box, LangChain, MongoDB, Salesforce, SAP, and ServiceNow. Microsoft plans to integrate A2A into Azure AI Foundry and Copilot Studio, demonstrating its commitment to open protocols. Additionally, Auth0 and SAP are integrating A2A support into their platforms and agents.

A2A 获得了众多技术公司和服务提供商的支持，包括 Atlassian、Box、LangChain、MongoDB、Salesforce、SAP 和 ServiceNow。Microsoft 计划将 A2A 集成到 Azure AI Foundry 和 Copilot Studio，这展示了其对开放协议的承诺。此外，Auth0 和 SAP 正在将 A2A 支持集成到其平台和智能体中。

As an open-source protocol, A2A welcomes community contributions to facilitate its evolution and widespread adoption.

作为开源协议，A2A 欢迎社区贡献，以促进其发展和广泛采用。

## Core Concepts of A2A

## A2A 的核心概念

The A2A protocol provides a structured approach for agent interactions, built upon several core concepts. A thorough grasp of these concepts is crucial for anyone developing or integrating with A2A-compliant systems. The foundational pillars of A2A include Core Actors, Agent Card, Agent Discovery, Communication and Tasks,  Interaction mechanisms, and Security, all of which will be reviewed in detail.

A2A 协议为智能体提供了结构化方法，建立在若干核心概念之上。深入理解这些概念对于任何开发或集成 A2A 兼容系统的开发者都至关重要。A2A 的基础支柱包括核心参与者、Agent 卡片、Agent 发现、通信和任务、交互机制及安全性，所有这些都将详细讨论。

**Core Actors:** A2A involves three main entities:

**核心参与者**：A2A 涉及三个主要实体：

* User: Initiates requests for agent assistance.  
* A2A Client (Client Agent): An application or an AI agent that acts on the user's behalf to request actions or information.  
* A2A Server (Remote Agent): An AI agent or system that provides an HTTP endpoint to process client requests and return results. The remote agent operates as an "opaque" system, meaning the client does not need to understand its internal operational details.

* 用户：发起对智能体的请求。
* A2A 客户端（客户端 Agent）：代表用户请求操作或信息的应用程序或 AI Agent。
* A2A 服务器（远程 Agent）：提供 HTTP 端点处理客户端请求并返回结果的 AI 智能体系统。远程智能体以"不透明"方式运行，意味着客户端无需了解其内部操作细节。

**Agent Card:** An agent's digital identity is defined by its Agent Card, usually a JSON file. This file contains key information for client interaction and automatic discovery, including the agent's identity, endpoint URL, and version. It also details supported capabilities like streaming or push notifications, specific skills, default input/output modes, and authentication requirements. Below is an example of an Agent Card for a WeatherBot.

**Agent 卡片**：Agent 的数字身份由其智能体卡片定义，通常是 JSON 文件。此文件包含用于客户端交互和自动发现的关键信息，包括智能体身份、端点 URL 和版本。它还详细说明支持的功能（如流式传输或推送通知）、特定技能、默认输入/输出模式以及身份验证要求。以下是 WeatherBot 的智能体卡片示例：

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

**Agent discovery:** it allows clients to find Agent Cards, which describe the capabilities of available A2A Servers. Several strategies exist for this process:

**Agent 发现**：Agent 发现机制允许客户端找到描述可用 A2A 服务器能力的智能体卡片。此过程存在几种策略：

* Well-Known URI: Agents host their Agent Card at a standardized path (e.g., /.well-known/agent.json). This approach offers broad, often automated, accessibility for public or domain-specific use.  
* Curated Registries: These provide a centralized catalog where Agent Cards are published and can be queried based on specific criteria. This is well-suited for enterprise environments needing centralized management and access control.  
* Direct Configuration: Agent Card information is embedded or privately shared. This method is appropriate for closely coupled or private systems where dynamic discovery isn't crucial.

* 标准 URI：Agent 在标准化路径（如 /.well-known/agent.json）托管其智能体卡片。此方法为公共或特定领域使用提供广泛、通常自动化的可访问性。
* 精选注册表：这些注册表提供集中目录，其中发布智能体卡片，可根据特定标准查询。这非常适合需要集中管理和访问控制的企业环境。
* 直接配置：Agent 卡片信息被嵌入或私下共享。此方法适用于紧密耦合或私有系统，其中动态发现并不重要。

Regardless of the chosen method, it is important to secure Agent Card endpoints. This can be achieved through access control, mutual TLS (mTLS), or network restrictions, especially if the card contains sensitive (though non-secret) information.

无论选择何种方法，保护智能体卡片端点都很重要。这可通过访问控制、双向 TLS（mTLS）或网络限制实现，特别是当卡片包含敏感（虽非秘密）信息时。

**Communications and Tasks:** In the A2A framework, communication is structured around asynchronous tasks, which represent the fundamental units of work for long-running processes. Each task is assigned a unique identifier and moves through a series of states—such as submitted, working, or completed—a design that supports parallel processing in complex operations. Communication between agents occurs through a Message.

**通信和任务**：在 A2A 框架中，通信围绕异步任务结构化，这些任务代表长时间运行进程的基本工作单元。每个任务被分配唯一标识符，并通过一系列状态（如已提交、工作中或已完成）移动，此设计支持复杂操作中的并行处理。智能体间通信通过消息进行。

This communication  contains attributes, which are key-value metadata describing the message (like its priority or creation time), and one or more parts, which carry the actual content being delivered, such as plain text, files, or structured JSON data. The tangible outputs generated by an agent during a task are called artifacts. Like messages, artifacts are also composed of one or more parts and can be streamed incrementally as results become available. All communication within the A2A framework is conducted over HTTP(S) using the JSON-RPC 2.0 protocol for payloads. To maintain continuity across multiple interactions, a server-generated contextId is used to group related tasks and preserve context.

此通信包含属性（描述消息的键值元数据，如其优先级或创建时间）以及一个或多个部分（承载传递的实际内容，如纯文本、文件或结构化 JSON 数据）。Agent 在任务期间生成的有形输出称为工件。与消息类似，工件也由一个或多个部分组成，并可在结果可用时逐步流式传输。A2A 框架内所有通信都通过 HTTP(S) 进行，使用 JSON-RPC 2.0 协议作为有效载荷。为在多次交互中保持连续性，使用服务器生成的 contextId 来分组相关任务并保留上下文。

**Interaction Mechanisms**: Request/Response (Polling) Server-Sent Events (SSE). A2A provides multiple interaction methods to suit a variety of AI application needs, each with a distinct mechanism:

**交互机制**：A2A 提供多种交互方法以适应各种 AI 应用需求，每种方法都有独特机制：

* Synchronous Request/Response: For quick, immediate operations. In this model, the client sends a request and actively waits for the server to process it and return a complete response in a single, synchronous exchange.  
* Asynchronous Polling: Suited for tasks that take longer to process. The client sends a request, and the server immediately acknowledges it with a "working" status and a task ID. The client is then free to perform other actions and can periodically poll the server by sending new requests to check the status of the task until it is marked as "completed" or "failed."  
* Streaming Updates (Server-Sent Events \- SSE): Ideal for receiving real-time, incremental results. This method establishes a persistent, one-way connection from the server to the client. It allows the remote agent to continuously push updates, such as status changes or partial results, without the client needing to make multiple requests.  
* Push Notifications (Webhooks): Designed for very long-running or resource-intensive tasks where maintaining a constant connection or frequent polling is inefficient. The client can register a webhook URL, and the server will send an asynchronous notification (a "push") to that URL when the task's status changes significantly (e.g., upon completion).

* 同步请求/响应：用于快速、即时操作。在此模型中，客户端发送请求并主动等待服务器处理并在单个同步交换中返回完整响应。
* 异步轮询：适用于需要更长时间处理的任务。客户端发送请求，服务器立即以"工作中"状态和任务 ID 确认。然后客户端可自由执行其他操作，并可通过发送新请求定期轮询服务器检查任务状态，直至标记为"已完成"或"失败"。
* 流式更新（服务器发送事件 - SSE）：适用于接收实时、增量结果。此方法建立从服务器到客户端的持久单向连接。它允许远程智能体推送更新（如状态更改或部分结果），而无需客户端发出多个请求。
* 推送通知（Webhook）：专为非常长时间运行或资源密集型任务设计，其中维护恒定连接或频繁轮询效率低下。客户端可注册 webhook URL，当任务状态发生重大变化（如完成时），服务器将向该 URL 发送异步通知（"推送"）。

The Agent Card specifies whether an agent supports streaming or push notification capabilities. Furthermore, A2A is modality-agnostic, meaning it can facilitate these interaction patterns not just for text, but also for other data types like audio and video, enabling rich, multimodal AI applications. Both streaming and push notification capabilities are specified within the Agent Card.

Agent 卡片指定智能体是否支持流式传输或推送通知功能。此外，A2A 是模态无关的，意味着它不仅可以为文本促进这些交互模式，还可为音频和视频等其他数据类型促进，从而实现丰富的多模态 AI 应用。流式传输和推送通知功能均在智能体卡片中指定。

```json
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

The synchronous request uses the sendTask method, where the client asks for and expects a single, complete answer to its query. In contrast, the streaming request uses the sendTaskSubscribe method to establish a persistent connection, allowing the agent to send back multiple, incremental updates or partial results over time.

同步请求使用 sendTask 方法，其中客户端请求并期望对其查询的单个完整答案。相比之下，流式请求使用 sendTaskSubscribe 方法建立持久连接，允许智能体发回多个增量更新或部分结果。

```json
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

**Security:** Inter-Agent Communication (A2A) is a vital component of system architecture, enabling secure and seamless data exchange among agents. It ensures robustness and integrity through several built-in mechanisms.

**安全性**：智能体间通信（A2A）是系统架构的关键组成部分，能够在智能体间实现安全、无缝的数据交换。它通过多个内置机制确保系统的稳健性和完整性。

* **Mutual Transport Layer Security (TLS):** Encrypted and authenticated connections are established to prevent unauthorized access and data interception, ensuring secure communication.

* **双向传输层安全（TLS）**：建立加密和认证连接，防止未经授权访问和数据拦截，确保通信安全。

* **Comprehensive Audit Logs:** All inter-agent communications are meticulously recorded, detailing information flow, involved agents, and actions. This audit trail is crucial for accountability, troubleshooting, and security analysis.

* **全面审计日志**：所有智能体间通信均被详细记录，明确信息流、涉及的智能体和操作。此审计轨迹对问责、故障排除和安全分析至关重要。

* **Agent Card Declaration:** Authentication requirements are explicitly declared in the Agent Card, a configuration artifact outlining the agent's identity, capabilities, and security policies. This centralizes and simplifies authentication management.

* **Agent 卡片声明**：身份验证要求在智能体卡片中明确声明，这是概述智能体身份、能力和安全策略的配置工件。这集中并简化了身份验证管理。

* **Credential Handling:** Agents typically authenticate using secure credentials like OAuth 2.0 tokens or API keys, passed via HTTP headers. This method prevents credential exposure in URLs or message bodies, enhancing overall security.

* **凭据处理**：Agent 通常使用安全凭据（如 OAuth 2.0 令牌或 API 密钥）进行身份验证，通过 HTTP 头传递。此方法防止凭据在 URL 或消息正文中暴露，增强整体安全性。

## A2A vs. MCP

## A2A 与 MCP

A2A is a protocol that complements Anthropic's Model Context Protocol (MCP) (see Fig. 1). While MCP focuses on structuring context for agents and their interaction with external data and tools, A2A facilitates coordination and communication among agents, enabling task delegation and collaboration.

A2A 是补充 Anthropic 模型上下文协议（MCP）的协议（见图 1）。MCP 专注于为智能体构建上下文结构及其与外部数据和工具的交互，而 A2A 则促进智能体间发现和通信，实现任务委派与协作。

![][image1]

Fig.1: Comparison A2A and MCP Protocols

图 1：A2A 和 MCP 协议比较

The goal of A2A is to enhance efficiency, reduce integration costs, and foster innovation and interoperability in the development of complex, multi-agent AI systems. Therefore, a thorough understanding of A2A's core components and operational methods is essential for its effective design, implementation, and application in building collaborative and interoperable AI agent systems.

A2A 旨在提高效率、降低集成成本，并促进复杂多智能体系统开发中的创新和互操作性。因此，深入理解 A2A 的核心组件和操作方法对于在构建协作式、互操作的 AI 智能体系统时进行有效设计、实施和应用至关重要。

## Practical Applications & Use Cases

## 实际应用和用例

Inter-Agent Communication is indispensable for building sophisticated AI solutions across diverse domains, enabling modularity, scalability, and enhanced intelligence.

智能体间通信对于跨不同领域构建复杂 AI 解决方案不可或缺，实现了模块化、可扩展性和增强智能。

* **Multi-Framework Collaboration:** A2A's primary use case is enabling independent AI agents, regardless of their underlying frameworks (e.g., ADK, LangChain, CrewAI), to communicate and collaborate. This is fundamental for building complex multi-agent systems where different agents specialize in different aspects of a problem.  
* **Automated Workflow Orchestration:** In enterprise settings, A2A can facilitate complex workflows by enabling agents to delegate and coordinate tasks. For instance, an agent might handle initial data collection, then delegate to another agent for analysis, and finally to a third for report generation, all communicating via the A2A protocol.  
* **Dynamic Information Retrieval:** Agents can communicate to retrieve and exchange real-time information. A primary agent might request live market data from a specialized "data fetching agent," which then uses external APIs to gather the information and send it back.

* **多框架协作**：A2A 的主要用例是使独立 AI 智能体能够通信和协作，无论其底层框架（如 ADK、LangChain、CrewAI）如何。这对构建复杂多智能体系统非常重要，其中不同智能体专注于问题的不同方面。
* **自动化工作流编排**：在企业环境中，A2A 可通过使智能体通信和协调任务来促进复杂工作流。例如，一个智能体可以处理初始数据收集，然后委派给另一个智能体进行分析，随后委派给第三个智能体生成报告，所有通信均通过 A2A 协议进行。
* **动态信息检索**：智能体可以通过通信来检索和交换实时信息。主智能体从专门的"数据获取智能体"请求实时市场数据，后者然后使用外部 API 收集信息并发送回来。

## Hands-On Code Example

## 实践代码示例

Let's examine the practical applications of the A2A protocol. The repository at [https://github.com/google-a2a/a2a-samples/tree/main/samples](https://github.com/google-a2a/a2a-samples/tree/main/samples) provides examples in Java, Go, and Python that illustrate how various agent frameworks, such as LangGraph, CrewAI, Azure AI Foundry, and AG2, can communicate using A2A. All code in this repository is released under the Apache 2.0 license. To further illustrate A2A's core concepts, we will review code excerpts focusing on setting up an A2A Server using an ADK-based agent with Google-authenticated tools. Looking at [https://github.com/google-a2a/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/adk_agent.py](https://github.com/google-a2a/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/adk_agent.py)

让我们检查 A2A 协议的实际应用。位于 [https://github.com/google-a2a/a2a-samples/tree/main/samples](https://github.com/google-a2a/a2a-samples/tree/main/samples) 的仓库提供 Java、Go 和 Python 示例，说明各种智能体框架（如 LangGraph、CrewAI、Azure AI Foundry 和 AG2）如何使用 A2A 通信。此仓库中所有代码均在 Apache 2.0 许可证下发布。为进一步说明 A2A 核心概念，我们将审查代码摘录，重点是基于 ADK 的智能体和 Google 身份验证工具设置 A2A 服务器。查看 [https://github.com/google-a2a/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/adk_agent.py](https://github.com/google-a2a/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/adk_agent.py)

```python
import datetime
from google.adk.agents import LlmAgent  # type: ignore[import-untyped]
from google.adk.tools.google_api_tool import CalendarToolset  # type: ignore[import-untyped]

async def create_agent(client_id, client_secret) -> LlmAgent:
    """Constructs the ADK agent."""
    toolset = CalendarToolset(client_id=client_id, client_secret=client_secret)
    return LlmAgent(
        model='gemini-2.0-flash-001',
        name='calendar_agent',
        description="An agent that can help manage a user's calendar",
        instruction=f"""
You are an agent that can help manage a user's calendar.
Users will request information about the state of their calendar or to make changes to their calendar.
Use the provided tools for interacting with the calendar API.
If not specified, assume the calendar the user wants is the 'primary' calendar.
When using the Calendar API tools, use well-formed RFC3339 timestamps.
Today is {datetime.datetime.now()}.
        """,
        tools=await toolset.get_tools(),
    )
```

This Python code defines an asynchronous function `create_agent` that constructs an ADK LlmAgent. It begins by initializing a `CalendarToolset` using the provided client credentials to access the Google Calendar API. Subsequently, an `LlmAgent` instance is created, configured with a specified Gemini model, a descriptive name, and instructions for managing a user's calendar. The agent is furnished with calendar tools from the `CalendarToolset`, enabling it to interact with the Calendar API and respond to user queries regarding calendar states or modifications. The agent's instructions dynamically incorporate the current date for temporal context. To illustrate how an agent is constructed, let's examine a key section from the calendar_agent found in the A2A samples on GitHub.

此 Python 代码定义异步函数 `create_agent`，用于构造 ADK LlmAgent。它首先使用提供的客户端凭据初始化 `CalendarToolset` 以访问 Google Calendar API。随后创建 `LlmAgent` 实例，配置指定 Gemini 模型、描述性名称和管理用户日历的指令。智能体配备来自 `CalendarToolset` 的日历工具，使其能与 Calendar API 交互并响应有关日历状态或修改的用户查询。智能体指令动态合并当前日期以提供时间上下文。为说明如何构造智能体，让我们检查 GitHub 上 A2A 示例中 calendar_agent 的关键部分。

The code below shows how the agent is defined with its specific instructions and tools. Please note that only the code required to explain this functionality is shown; you can access the complete file here: [https://github.com/a2aproject/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/__main__.py](https://github.com/a2aproject/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/__main__.py)

以下代码显示智能体使用其特定指令和工具定义。请注意，仅显示解释此功能所需代码；您可在此处访问完整文件：[https://github.com/a2aproject/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/__main__.py](https://github.com/a2aproject/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/__main__.py)

```python
def main(host: str, port: int):
    # Verify an API key is set.
    # Not required if using Vertex AI APIs.
    if os.getenv('GOOGLE_GENAI_USE_VERTEXAI') != 'TRUE' and not os.getenv('GOOGLE_API_KEY'):
        raise ValueError(
            'GOOGLE_API_KEY environment not set and '
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

This Python code demonstrates setting up an A2A-compliant "Calendar Agent" for checking user availability using Google Calendar. It involves verifying API keys or Vertex AI configurations for authentication purposes. The agent's capabilities, including the "check_availability" skill, are defined within an AgentCard, which also specifies the agent's network address. Subsequently, an ADK agent is created, configured with in-memory services for managing artifacts, sessions, and memory. The code then initializes a Starlette web application, incorporates an authentication callback and the A2A protocol handler, and executes it using Uvicorn to expose the agent via HTTP.

此 Python 代码演示了设置符合 A2A 的"日历 Agent"，用于通过 Google Calendar 检查用户可用性。它涉及验证 API 密钥或 Vertex AI 配置以用于身份验证目的。智能体能力（包括"check_availability"技能）在 AgentCard 中定义，该卡片还指定智能体地址。随后创建 ADK 智能体，配置内存服务以管理工件、会话和内存。然后代码初始化 Starlette Web 应用程序，合并身份验证回调和 A2A 协议处理程序，并使用 Uvicorn 执行它以通过 HTTP 公开智能体。

These examples illustrate the process of building an A2A-compliant agent, from defining its capabilities to running it as a web service. By utilizing Agent Cards and ADK, developers can create interoperable AI agents capable of integrating with tools like Google Calendar. This practical approach demonstrates the application of A2A in establishing a multi-agent ecosystem.

这些示例说明了构建符合 A2A 的智能体的过程，从定义其能力到将其作为 Web 服务运行。通过利用智能体卡片和 ADK，开发人员可创建能与 Google Calendar 等工具集成的互操作 AI 智能体。此实用方法展示了 A2A 在建立多智能体生态系统的应用。

Further exploration of A2A is recommended through the code demonstration at [https://www.trickle.so/blog/how-to-build-google-a2a-project](https://www.trickle.so/blog/how-to-build-google-a2a-project). Resources available at this link include sample A2A clients and servers in Python and JavaScript, multi-agent web applications, command-line interfaces, and example implementations for various agent frameworks.

建议通过 [https://www.trickle.so/blog/how-to-build-google-a2a-project](https://www.trickle.so/blog/how-to-build-google-a2a-project) 上的代码演示进一步探索 A2A。此链接提供的资源包括 Python 和 JavaScript 中的示例 A2A 客户端和服务器、多智能体 Web 应用程序、命令行界面以及各种智能体框架的示例实现。

## At a Glance

## 速览

**What:** Individual AI agents, especially those built on different frameworks, often struggle with complex, multi-faceted problems on their own. The primary challenge is the lack of a common language or protocol that allows them to communicate and collaborate effectively. This isolation prevents the creation of sophisticated systems where multiple specialized agents can combine their unique skills to solve larger tasks. Without a standardized approach, integrating these disparate agents is costly, time-consuming, and hinders the development of more powerful, cohesive AI solutions.

**问题背景：** 单个 AI 智能体（特别是基于不同框架构建的智能体）在处理复杂、多方面问题时通常会遇到困难。主要挑战是缺乏允许它们有效通信协作的通用语言或协议。这种隔离阻止了创建复杂系统，其中多个专门智能体结合独特技能解决更大的任务。如果没有标准化方法，集成这些不同的智能体成本高昂、非常耗时，并阻碍了更强大、更具凝聚力的 AI 解决方案的开发。

**Why:** The Inter-Agent Communication (A2A) protocol provides an open, standardized solution for this problem. It is an HTTP-based protocol that enables interoperability, allowing distinct AI agents to coordinate, delegate tasks, and share information seamlessly, regardless of their underlying technology. A core component is the Agent Card, a digital identity file that describes an agent's capabilities, skills, and communication endpoints, facilitating discovery and interaction. A2A defines various interaction mechanisms, including synchronous and asynchronous communication, to support diverse use cases. By creating a universal standard for agent collaboration, A2A fosters a modular and scalable ecosystem for building complex, multi-agent Agentic systems.

**解决方案**：智能体间通信（A2A）协议为此问题提供了开放、标准化的解决方案。它是基于 HTTP 的协议，能够实现互操作性，允许不同 AI 智能体协调、委派任务和共享信息，无论其底层技术如何。核心组件是智能体卡片，它是描述智能体能力和通信端点的数字身份文件，促进了发现和交互。A2A 定义了各种交互机制，包括同步和异步通信，以支持不同的用例。通过为智能体协作创建标准，A2A 促进了构建复杂、多智能体系统的模块化和可扩展生态系统。

**Rule of thumb:** Use this pattern when you need to orchestrate collaboration between two or more AI agents, especially if they are built using different frameworks (e.g., Google ADK, LangGraph, CrewAI). It is ideal for building complex, modular applications where specialized agents handle specific parts of a workflow, such as delegating data analysis to one agent and report generation to another. This pattern is also essential when an agent needs to dynamically discover and consume the capabilities of other agents to complete a task.

**实践建议**：当您需要协调两个或多个 AI 智能体协作时使用此模式，特别是如果它们使用不同框架（如 Google ADK、LangGraph、CrewAI）构建。它非常适合构建复杂、模块化应用程序，其中专门智能体处理工作流的特定部分，例如将数据分析委派给一个智能体，将报告生成委派给另一个智能体。当智能体需要发现和使用其他智能体能力完成任务时，此模式也必不可少。

**Visual summary**

**可视化摘要**

**![][image2]**

Fig.2: A2A inter-agent communication pattern

图 2：A2A 智能体间通信模式

## Key Takeaways

## 关键要点

Key Takeaways:

* The Google A2A protocol is an open, HTTP-based standard that facilitates communication and collaboration between AI agents built with different frameworks.  
* An AgentCard serves as a digital identifier for an agent, allowing for automatic discovery and understanding of its capabilities by other agents.  
* A2A offers both synchronous request-response interactions (using `tasks/send`) and streaming updates (using `tasks/sendSubscribe`) to accommodate varying communication needs.  
* The protocol supports multi-turn conversations, including an `input-required` state, which allows agents to request additional information and maintain context during interactions.  
* A2A encourages a modular architecture where specialized agents can operate independently on different ports, enabling system scalability and distribution.  
* Tools such as Trickle AI aid in visualizing and tracking A2A communications, which helps developers monitor, debug, and optimize multi-agent systems.  
* While A2A is a high-level protocol for managing tasks and workflows between different agents, the Model Context Protocol (MCP) provides a standardized interface for LLMs to interface with external resources.

* Google A2A 协议是一个开放、基于 HTTP 的标准，促进使用不同框架构建的 AI 智能体进行通信和协作。
* AgentCard 作为智能体的数字标识符，允许其他智能体发现和理解其能力。
* A2A 提供同步请求-响应交互（使用 `tasks/send`）和流式更新（使用 `tasks/sendSubscribe`）以适应不同的通信需求。
* 该协议支持多轮对话，包括 `input-required` 状态，允许智能体请求额外信息并在交互期间维护上下文。
* A2A 鼓励模块化架构，其中专门智能体在不同端口上独立运行，实现系统的可扩展性和分布式部署。
* Trickle AI 等工具有助于可视化和跟踪 A2A 通信，帮助开发人员监控、调试和优化多智能体系统。
* 虽然 A2A 是用于管理不同智能体间任务和工作流的高级协议，但模型上下文协议（MCP）为 LLM 提供与外部资源交互的标准化接口。

## Conclusions

## 结论

The Inter-Agent Communication (A2A) protocol establishes a vital, open standard to overcome the inherent isolation of individual AI agents. By providing a common HTTP-based framework, it ensures seamless collaboration and interoperability between agents built on different platforms, such as Google ADK, LangGraph, or CrewAI. A core component is the Agent Card, which serves as a digital identity, clearly defining an agent's capabilities and enabling dynamic discovery by other agents. The protocol's flexibility supports various interaction patterns, including synchronous requests, asynchronous polling, and real-time streaming, catering to a wide range of application needs.

智能体间通信（A2A）协议建立了一个重要的开放标准，以克服单个 AI 智能体的固有隔离。通过提供通用的基于 HTTP 的框架，它确保了在不同平台上构建的智能体能够协作和互操作性，例如 Google ADK、LangGraph 或 CrewAI。核心组件是智能体卡片，它是智能体的数字身份，清楚定义了智能体的能力，使其他智能体能够动态发现和交互。其灵活性支持各种交互模式，包括同步请求、异步轮询和实时流式传输，满足广泛的应用需求。

This enables the creation of modular and scalable architectures where specialized agents can be combined to orchestrate complex automated workflows. Security is a fundamental aspect, with built-in mechanisms like mTLS and explicit authentication requirements to protect communications. While complementing other standards like MCP, A2A's unique focus is on the high-level coordination and task delegation between agents. The strong backing from major technology companies and the availability of practical implementations highlight its growing importance. This protocol paves the way for developers to build more sophisticated, distributed, and intelligent multi-agent systems. Ultimately, A2A is a foundational pillar for fostering an innovative and interoperable ecosystem of collaborative AI.

这使得能够创建模块化和可扩展的架构，其中专门智能体组合以编排复杂的自动化工作流。安全性是基本方面，具有内置机制（如 mTLS 和明确身份验证要求）来保护通信。虽然补充了 MCP 等其他标准，但 A2A 的独特焦点是智能体间协调和任务委派。主要技术公司的强大支持以及实际实现的可用性突显了其日益增长的重要性。该协议为开发人员构建更复杂、分布式和智能的多智能体系统铺平了道路。最终，A2A 是促进创新和互操作的协作 AI 生态系统的基础支柱。

## References

## 参考文献

 1. Chen, B. (2025, April 22). *How to Build Your First Google A2A Project: A Step-by-Step Tutorial*. Trickle.so Blog. [https://www.trickle.so/blog/how-to-build-google-a2a-project](https://www.trickle.so/blog/how-to-build-google-a2a-project)
 2. Google A2A GitHub Repository. [https://github.com/google-a2a/A2A](https://github.com/google-a2a/A2A)
 3. Google Agent Development Kit (ADK) [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)
 4. Getting Started with Agent-to-Agent (A2A) Protocol: [https://codelabs.developers.google.com/intro-a2a-purchasing-concierge#0](https://codelabs.developers.google.com/intro-a2a-purchasing-concierge#0)
 5. Google AgentDiscovery - [https://a2a-protocol.org/latest/](https://a2a-protocol.org/latest/)
 6. Communication between different AI frameworks such as LangGraph, CrewAI, and Google ADK [https://www.trickle.so/blog/how-to-build-google-a2a-project#setting-up-your-a2a-development-environment](https://www.trickle.so/blog/how-to-build-google-a2a-project#setting-up-your-a2a-development-environment)
 7. Designing Collaborative Multi-Agent Systems with the A2A Protocol [https://www.oreilly.com/radar/designing-collaborative-multi-agent-systems-with-the-a2a-protocol/](https://www.oreilly.com/radar/designing-collaborative-multi-agent-systems-with-the-a2a-protocol/)

[image1]: ../images/chapter-15/image1.png
[image2]: ../images/chapter-15/image2.png
