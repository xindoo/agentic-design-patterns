# Chapter 10: Model Context Protocol 

# 第 10 章：模型上下文协议 (MCP)

To enable LLMs to function effectively as agents, their capabilities must extend beyond multimodal generation. Interaction with the external environment is necessary, including access to current data, utilization of external software, and execution of specific operational tasks. The Model Context Protocol (MCP) addresses this need by providing a standardized interface for LLMs to interface with external resources. This protocol serves as a key mechanism to facilitate consistent and predictable integration.

要使 LLM 作为智能体运作，其能力必须超越多模态生成。与外部环境交互不可或缺，包括访问实时数据、使用外部软件以及执行特定操作任务。模型上下文协议（Model Context Protocol，简称 MCP）通过提供标准化接口使 LLM 能与外部资源交互，是实现一致性和可预测性集成的关键机制。

## MCP Pattern Overview

## MCP 速览

Imagine a universal adapter that allows any LLM to plug into any external system, database, or tool without a custom integration for each one. That's essentially what the Model Context Protocol (MCP) is. It's an open standard designed to standardize how LLMs like Gemini, OpenAI's GPT models, Mixtral, and Claude communicate with external applications, data sources, and tools. Think of it as a universal connection mechanism that simplifies how LLMs obtain context, execute actions, and interact with various systems.

想象一个通用适配器，允许任何 LLM 连接到任何外部系统、数据库或工具，无需为每个连接进行自定义集成。这本质上就是模型上下文协议（MCP）的功能。它作为开放标准，旨在标准化 Gemini、OpenAI 的 GPT 模型、Mixtral 和 Claude 等 LLM 与外部应用程序、数据源和工具的通信方式。可将其视为通用连接机制，简化 LLM 获取上下文、执行操作以及与各类系统交互的方式。

MCP operates on a client-server architecture. It defines how different elements—data (referred to as resources), interactive templates (which are essentially prompts), and actionable functions (known as tools)—are exposed by an MCP server. These are then consumed by an MCP client, which could be an LLM host application or an AI agent itself. This standardized approach dramatically reduces the complexity of integrating LLMs into diverse operational environments.

MCP 基于客户端-服务器架构运行。它定义了不同元素——数据（称为资源）、交互模板（本质是提示）和可操作函数（称为工具）——如何由 MCP 服务器公开。这些元素随后由 MCP 客户端使用，客户端可以是 LLM 宿主应用程序或 AI 智能体本身。这种标准化方法显著降低了将 LLM 集成到多样化操作环境中的复杂性。

However, MCP is a contract for an "agentic interface," and its effectiveness depends heavily on the design of the underlying APIs it exposes. There is a risk that developers simply wrap pre-existing, legacy APIs without modification, which can be suboptimal for an agent. For example, if a ticketing system's API only allows retrieving full ticket details one by one, an agent asked to summarize high-priority tickets will be slow and inaccurate at high volumes. To be truly effective, the underlying API should be improved with deterministic features like filtering and sorting to help the non-deterministic agent work efficiently. This highlights that agents do not magically replace deterministic workflows; they often require stronger deterministic support to succeed.

然而，MCP 是一份"智能体接口"契约，其有效性很大程度上取决于它所公开的底层 API 的设计。存在这样的风险：开发者只是简单地包装现有的遗留 API 而不做任何修改，这对智能体来说可能并不是最优的。例如，如果一个票务系统的 API 只允许逐个检索完整的票务详情，那么当被要求总结高优先级票务时，智能体在处理大量数据时会变得缓慢且不准确。要真正发挥效用，底层 API 应该通过过滤和排序等确定性功能进行改进，以帮助非确定性的智能体高效工作；这凸显了智能体无法神奇地替代确定性工作流，它们通常需要更强的确定性支持才能取得成功。

Furthermore, MCP can wrap an API whose input or output is still not inherently understandable by the agent. An API is only useful if its data format is agent-friendly, a guarantee that MCP itself does not enforce. For instance, creating an MCP server for a document store that returns files as PDFs is mostly useless if the consuming agent cannot parse PDF content. The better approach would be to first create an API that returns a textual version of the document, such as Markdown, which the agent can actually read and process. This demonstrates that developers must consider not just the connection, but the nature of the data being exchanged to ensure true compatibility.

此外，MCP 可以包装那些输入或输出对智能体来说仍然不是固有可理解的 API。一个 API 只有在其数据格式对智能体友好时才有用，而 MCP 本身并不保证这一点。例如，为一个返回 PDF 文件的文档存储创建 MCP 服务器，如果使用该服务的智能体无法解析 PDF 内容，那么这基本上是无用的。更好的方法是首先创建一个返回文档文本版本（如 Markdown）的 API，这样智能体才能真正读取和处理。这表明开发者必须考虑的不只是连接，还有所交换数据的性质，以确保真正的兼容性。

## MCP vs. Tool Function Calling

## MCP 与工具函数调用

The Model Context Protocol (MCP) and tool function calling are distinct mechanisms that enable LLMs to interact with external capabilities (including tools) and execute actions. While both serve to extend LLM capabilities beyond text generation, they differ in their approach and level of abstraction.

模型上下文协议（MCP）和工具函数调用是使 LLM 能与外部能力（含工具）交互并执行操作的不同机制。虽然两者都服务于扩展 LLM 超越文本生成的能力，但它们在方法和抽象级别上存在差异。

Tool function calling can be thought of as a direct request from an LLM to a specific, pre-defined tool or function. Note that in this context we use the words "tool" and "function” interchangeably. This interaction is characterized by a one-to-one communication model, where the LLM formats a request based on its understanding of a user's intent requiring external action. The application code then executes this request and returns the result to the LLM. This process is often proprietary and varies across different LLM providers.

工具函数调用可以被视为 LLM 对特定预定义工具或函数的直接请求。请注意，在此上下文中我们交替使用"工具"和"函数"这两个词。这种交互采用一对一的通信模型，LLM 根据其对需要外部操作用户意图的理解来格式化请求。然后应用程序代码执行此请求并将结果返回给 LLM。这个过程通常是专有的，并且在不同的 LLM 提供商之间存在差异。

In contrast, the Model Context Protocol (MCP) operates as a standardized interface for LLMs to discover, communicate with, and utilize external capabilities. It functions as an open protocol that facilitates interaction with a wide range of tools and systems, aiming to establish an ecosystem where any compliant tool can be accessed by any compliant LLM. This fosters interoperability, composability and reusability across different systems and implementations. By adopting a federated model, we significantly improve interoperability and unlock the value of existing assets. This strategy allows us to bring disparate and legacy services into a modern ecosystem simply by wrapping them in an MCP-compliant interface. These services continue to operate independently, but can now be composed into new applications and workflows, with their collaboration orchestrated by LLMs. This fosters agility and reusability without requiring costly rewrites of foundational systems.

相比之下，模型上下文协议（MCP）作为 LLM 发现、通信和使用外部能力的标准化接口运行。它作为一个开放协议，促进与各种工具和系统的交互，旨在建立一个任何兼容工具都可以被任何兼容 LLM 访问的生态系统。这促进了不同系统和实现之间的互操作性、可组合性和可重用性。通过采用联合模型，我们显著提升了互操作性并释放了现有资产的价值。这种策略允许我们通过简单地用符合 MCP 接口的包装器包装它们，将分散和遗留的服务引入现代生态系统。这些服务继续独立运行，但现在可以组合到新的应用程序和工作流中，它们的协作由 LLM 编排。这促进了敏捷性和可重用性，而无需对基础系统进行昂贵的重写。

Here's a breakdown of the fundamental distinctions between MCP and tool function calling:

以下是 MCP 与工具函数调用的基本区别：

| Feature | Tool Function Calling | Model Context Protocol (MCP) |
| ----- | ----- | ----- |
| **Standardization** | Proprietary and vendor-specific. The format and implementation differ across LLM providers. | An open, standardized protocol, promoting interoperability between different LLMs and tools. |
| **Scope** | A direct mechanism for an LLM to request the execution of a specific, predefined function. | A broader framework for how LLMs and external tools discover and communicate with each other. |
| **Architecture** | A one-to-one interaction between the LLM and the application's tool-handling logic. | A client-server architecture where LLM-powered applications (clients) can connect to and utilize various MCP servers (tools). |
| **Discovery** | The LLM is explicitly told which tools are available within the context of a specific conversation. | Enables dynamic discovery of available tools. An MCP client can query a server to see what capabilities it offers. |
| **Reusability** | Tool integrations are often tightly coupled with the specific application and LLM being used. | Promotes the development of reusable, standalone "MCP servers" that can be accessed by any compliant application. |

| 特性 | 工具函数调用 | 模型上下文协议（MCP） |
| ----- | ----- | ----- |
| **标准化** | 专有和供应商特定。格式和实现在不同 LLM 提供商间各异 | 开放标准化协议，促进不同 LLM 和工具间互操作性 |
| **范围** | LLM 请求执行特定预定义函数的直接机制 | 更广泛框架，定义 LLM 和外部工具如何相互发现和通信 |
| **架构** | LLM 与应用程序工具处理逻辑间的一对一交互 | 客户端-服务器架构，LLM 驱动应用程序（客户端）可连接并使用各种 MCP 服务器（工具） |
| **发现** | LLM 被明确告知特定对话上下文中哪些工具可用 | 支持动态发现可用工具。MCP 客户端可查询服务器以查看其提供能力 |
| **可重用性** | 工具集成通常与所用特定应用程序和 LLM 紧密耦合 | 促进开发可重用独立"MCP 服务器"，可被任何兼容应用程序访问 |

Think of tool function calling as giving an AI a specific set of custom-built tools, like a particular wrench and screwdriver. This is efficient for a workshop with a fixed set of tasks. MCP (Model Context Protocol), on the other hand, is like creating a universal, standardized power outlet system. It doesn't provide the tools itself, but it allows any compliant tool from any manufacturer to plug in and work, enabling a dynamic and ever-expanding workshop.

可以将工具函数调用想象为给 AI 一组特定的定制工具，比如特定的扳手和螺丝刀。这对于具有固定任务集的车间来说是高效的。另一方面，MCP（模型上下文协议）就像创建一个通用的标准化电源插座系统。它本身不提供工具，但允许任何制造商的任何兼容工具插入并工作，从而实现一个动态且不断扩展的车间。

In short, function calling provides direct access to a few specific functions, while MCP is the standardized communication framework that lets LLMs discover and use a vast range of external resources. For simple applications, specific tools are enough; for complex, interconnected AI systems that need to adapt, a universal standard like MCP is essential.

简而言之，函数调用提供对少数特定函数的直接访问，而 MCP 是让 LLM 发现和使用广泛外部资源的标准化通信框架。对于简单应用程序，特定工具就足够了；对于需要适应的复杂互联 AI 系统，像 MCP 这样的通用标准是必不可少的。

## Additional considerations for MCP

## MCP 的其他考虑因素

While MCP presents a powerful framework, a thorough evaluation requires considering several crucial aspects that influence its suitability for a given use case. Let's see some aspects in more details:

虽然 MCP 提供了强大框架，但全面评估需考虑影响其适用性的几个关键方面。让我们详细探讨某些方面：

* **Tool vs. Resource vs. Prompt**: It's important to understand the specific roles of these components. A resource is static data (e.g., a PDF file, a database record). A tool is an executable function that performs an action (e.g., sending an email, querying an API). A prompt is a template that guides the LLM in how to interact with a resource or tool, ensuring the interaction is structured and effective.  

* **工具 vs. 资源 vs. 提示**：理解这些组件的特定角色很重要。资源是静态数据（如 PDF 文件、数据库记录）。工具是执行操作的可执行函数（如发送电子邮件、查询 API）。提示是指导 LLM 如何与资源或工具交互的模板，确保交互是结构化且有效的。

* **Discoverability**: A key advantage of MCP is that an MCP client can dynamically query a server to learn what tools and resources it offers. This "just-in-time" discovery mechanism is powerful for agents that need to adapt to new capabilities without being redeployed.  

* **可发现性**：MCP 的一个关键优势是 MCP 客户端可以动态查询服务器以了解其提供的工具和资源。这种"即时"发现机制对于需要适应新能力而无需重新部署的智能体来说非常强大。

* **Security**: Exposing tools and data via any protocol requires robust security measures. An MCP implementation must include authentication and authorization to control which clients can access which servers and what specific actions they are permitted to perform.  

* **安全性**：通过任何协议公开工具和数据都需要强大的安全措施。MCP 实现必须包含身份验证和授权，以控制哪些客户端可以访问哪些服务器以及允许执行哪些特定操作。

* **Implementation**: While MCP is an open standard, its implementation can be complex. However, providers are beginning to simplify this process. For example, some model providers like Anthropic or FastMCP offer SDKs that abstract away much of the boilerplate code, making it easier for developers to create and connect MCP clients and servers.  

* **实现**：虽然 MCP 是一个开放标准，但其实现可能很复杂。然而，提供商正开始简化这个过程。例如，Anthropic 或 FastMCP 等模型提供商提供 SDK，抽象了大部分样板代码，使开发者更容易创建和连接 MCP 客户端和服务器。

* **Error Handling**: A comprehensive error-handling strategy is critical. The protocol must define how errors (e.g., tool execution failure, unavailable server, invalid request) are communicated back to the LLM so it can understand the failure and potentially try an alternative approach.  

* **错误处理**：全面的错误处理策略至关重要。协议必须定义如何将错误（如工具执行失败、服务器不可用、无效请求）传达回 LLM，使其能够理解失败并可能尝试替代方法。

* **Local vs. Remote Server**: MCP servers can be deployed locally on the same machine as the agent or remotely on a different server. A local server might be chosen for speed and security with sensitive data, while a remote server architecture allows for shared, scalable access to common tools across an organization.  

* **本地 vs. 远程服务器**：MCP 服务器可以部署在与智能体相同的机器上本地运行，也可以部署在不同的服务器上远程运行。本地服务器可能因速度和敏感数据的安全性而被选择，而远程服务器架构允许组织内共享、可扩展地访问公共工具的能力。

* **On-demand vs. Batch**: MCP can support both on-demand, interactive sessions and larger-scale batch processing. The choice depends on the application, from a real-time conversational agent needing immediate tool access to a data analysis pipeline that processes records in batches.  

* **按需 vs. 批处理**：MCP 可以支持按需交互式会话和大规模批处理。选择取决于应用程序，从需要即时工具访问的实时对话式智能体，到批量处理记录的数据分析管道。

* **Transportation Mechanism**: The protocol also defines the underlying transport layers for communication. For local interactions, it uses JSON-RPC over STDIO (standard input/output) for efficient inter-process communication. For remote connections, it leverages web-friendly protocols like Streamable HTTP and Server-Sent Events (SSE) to enable persistent and efficient client-server communication.

* **传输机制**：协议还定义了通信的底层传输层。对于本地交互，使用基于 STDIO（标准输入/输出）的 JSON-RPC 实现高效的进程间通信。对于远程连接，利用 Web 友好协议如可流式 HTTP 和服务器发送事件（SSE）实现持久高效的客户端-服务器通信。

The Model Context Protocol uses a client-server model to standardize information flow. Understanding component interaction is key to MCP's advanced agentic behavior:

模型上下文协议使用客户端-服务器模型来标准化信息流。理解组件交互是 MCP 高级智能体行为的关键：

1. **Large Language Model (LLM)**: The core intelligence. It processes user requests, formulates plans, and decides when it needs to access external information or perform an action.  

1. **大型语言模型（LLM）**：核心智能。处理用户请求，制定计划，并决定何时需要访问外部信息或执行操作。

2. **MCP Client**: This is an application or wrapper around the LLM. It acts as the intermediary, translating the LLM's intent into a formal request that conforms to the MCP standard. It is responsible for discovering, connecting to, and communicating with MCP Servers.  

2. **MCP 客户端**：围绕 LLM 的应用程序或包装器。充当中介，将 LLM 的意图转换为符合 MCP 标准的正式请求。负责发现、连接和与 MCP 服务器通信。

3. **MCP Server**: This is the gateway to the external world. It exposes a set of tools, resources, and prompts to any authorized MCP Client. Each server is typically responsible for a specific domain, such as a connection to a company's internal database, an email service, or a public API.  

3. **MCP 服务器**：通往外部世界的网关。向任何授权的 MCP 客户端公开一组工具、资源和提示。每个服务器通常负责特定领域，例如连接公司内部数据库、电子邮件服务或公共 API。

4. **Optional Third-Party (3P) Service:** This represents the actual external tool, application, or data source that the MCP Server manages and exposes. It is the ultimate endpoint that performs the requested action, such as querying a proprietary database, interacting with a SaaS platform, or calling a public weather API.

4. **可选的第三方（3P）服务**：代表 MCP 服务器管理和公开的实际外部工具、应用程序或数据源。是执行请求操作的最终端点，如查询专有数据库、与 SaaS 平台交互或调用公共天气 API。

The interaction flows as follows:

交互流程如下：

1. **Discovery**: The MCP Client, on behalf of the LLM, queries an MCP Server to ask what capabilities it offers. The server responds with a manifest listing its available tools (e.g., send\_email), resources (e.g., customer\_database), and prompts.  

1. **发现**：MCP 客户端代表 LLM 查询 MCP 服务器，询问其提供的能力。服务器响应一个清单，列出可用工具（如 send_email）、资源（如 customer_database）和提示。

2. **Request Formulation**: The LLM determines that it needs to use one of the discovered tools. For instance, it decides to send an email. It formulates a request, specifying the tool to use (send\_email) and the necessary parameters (recipient, subject, body).  

2. **请求制定**：LLM 确定需要使用其中一个发现的工具。例如决定发送电子邮件。制定请求，指定要使用的工具（send_email）和必要参数（收件人、主题、正文）。

3. **Client Communication**: The MCP Client takes the LLM's formulated request and sends it as a standardized call to the appropriate MCP Server.  

3. **客户端通信**：MCP 客户端获取 LLM 制定的请求，将其作为标准化调用发送到适当的 MCP 服务器。

4. **Server Execution**: The MCP Server receives the request. It authenticates the client, validates the request, and then executes the specified action by interfacing with the underlying software (e.g., calling the send() function of an email API).  

4. **服务器执行**：MCP 服务器接收请求。对客户端进行身份验证，验证请求，然后通过与底层软件交互执行指定操作（如调用电子邮件 API 的 send() 函数）。

5. **Response and Context Update**: After execution, the MCP Server sends a standardized response back to the MCP Client. This response indicates whether the action was successful and includes any relevant output (e.g., a confirmation ID for the sent email). The client then passes this result back to the LLM, updating its context and enabling it to proceed with the next step of its task.

5. **响应和上下文更新**：执行后，MCP 服务器将标准化响应发送回 MCP 客户端。此响应指示操作是否成功，包括任何相关输出（如已发送电子邮件的确认 ID）。然后客户端将此结果传递回 LLM，更新其上下文并使其能够继续任务的下一步。

## Practical Applications & Use Cases

## 实际应用和用例

MCP significantly broadens AI/LLM capabilities, making them more versatile and powerful. Here are nine key use cases:

MCP 显著扩展了 AI/LLM 能力，使其更加多功能强大。以下是九个关键用例：

* **Database Integration:** MCP allows LLMs and agents to seamlessly access and interact with structured data in databases. For instance, using the MCP Toolbox for Databases, an agent can query Google BigQuery datasets to retrieve real-time information, generate reports, or update records, all driven by natural language commands.  

* **数据库集成**：MCP 允许 LLM 和智能体无缝访问数据库中的结构化数据并与之交互。例如，使用数据库 MCP 工具箱，智能体可以查询 Google BigQuery 数据集以检索实时信息、生成报告或更新记录，所有这些都由自然语言命令驱动。

* **Generative Media Orchestration:** MCP enables agents to integrate with advanced generative media services. Through MCP Tools for Genmedia Services, an agent can orchestrate workflows involving Google's Imagen for image generation, Google's Veo for video creation, Google's Chirp 3 HD for realistic voices, or Google's Lyria for music composition, allowing for dynamic content creation within AI applications.  

* **生成媒体编排**：MCP 使智能体能够与高级生成媒体服务集成。通过生成媒体服务的 MCP 工具，智能体可以编排涉及 Google Imagen 图像生成、Google Veo 视频创建、Google Chirp 3 HD 逼真语音或 Google Lyria 音乐创作的工作流，允许在 AI 应用程序中进行动态内容创建。

* **External API Interaction:** MCP provides a standardized way for LLMs to call and receive responses from any external API. This means an agent can fetch live weather data, pull stock prices, send emails, or interact with CRM systems, extending its capabilities far beyond its core language model.  

* **外部 API 交互**：MCP 为 LLM 提供调用任何外部 API 并接收响应的标准化方式。这意味着智能体可以获取实时天气数据、拉取股票价格、发送电子邮件或与 CRM 系统交互，将其能力扩展到核心语言模型之外。

* **Reasoning-Based Information Extraction:** Leveraging an LLM's strong reasoning skills, MCP facilitates effective, query-dependent information extraction that surpasses conventional search and retrieval systems. Instead of a traditional search tool returning an entire document, an agent can analyze the text and extract the precise clause, figure, or statement that directly answers a user's complex question.  

* **基于推理的信息提取**：利用 LLM 强大的推理能力，MCP 促进有效的、依赖查询的信息提取，超越传统的搜索和检索系统。智能体可以分析文本并提取精确回答用户复杂问题的特定条款、数字或陈述，而不是传统搜索工具返回整个文档。

* **Custom Tool Development:** Developers can build custom tools and expose them via an MCP server (e.g., using FastMCP). This allows specialized internal functions or proprietary systems to be made available to LLMs and other agents in a standardized, easily consumable format, without needing to modify the LLM directly.  

* **自定义工具开发**：开发者可以构建自定义工具并通过 MCP 服务器公开（如使用 FastMCP）。这允许以标准化、易于使用的格式向 LLM 和其他智能体暴露专门的内部函数或专有系统，而无需直接修改 LLM。

* **Standardized LLM-to-Application Communication:** MCP ensures a consistent communication layer between LLMs and the applications they interact with. This reduces integration overhead, promotes interoperability between different LLM providers and host applications, and simplifies the development of complex agentic systems.  

* **标准化的 LLM 到应用程序通信**：MCP 确保 LLM 与它们交互的应用程序之间有一致的通信层。这减少了集成开销，促进了不同 LLM 提供商和宿主应用程序之间的互操作性，并简化了复杂智能体系统的开发。

* **Complex Workflow Orchestration:** By combining various MCP-exposed tools and data sources, agents can orchestrate highly complex, multi-step workflows. An agent could, for example, retrieve customer data from a database, generate a personalized marketing image, draft a tailored email, and then send it, all by interacting with different MCP services.  

* **复杂工作流编排**：通过组合各种 MCP 公开的工具和数据源，智能体可以编排高度复杂的多步骤工作流。例如，智能体可以从数据库检索客户数据，生成个性化营销图像，起草定制电子邮件，然后发送，所有这些都通过与不同的 MCP 服务交互完成。

* **IoT Device Control:** MCP can facilitate LLM interaction with Internet of Things (IoT) devices. An agent could use MCP to send commands to smart home appliances, industrial sensors, or robotics, enabling natural language control and automation of physical systems.  

* **物联网设备控制**：MCP 可促进 LLM 与物联网（IoT）设备交互。智能体可以使用 MCP 向智能家居电器、工业传感器或机器人发送命令，实现自然语言控制和物理系统自动化。

* **Financial Services Automation:** In financial services, MCP could enable LLMs to interact with various financial data sources, trading platforms, or compliance systems. An agent might analyze market data, execute trades, generate personalized financial advice, or automate regulatory reporting, all while maintaining secure and standardized communication.

* **金融服务自动化**：在金融服务中，MCP 可使 LLM 与各种金融数据源、交易平台或合规系统交互。智能体可以分析市场数据、执行交易、生成个性化财务建议或自动化监管报告，同时保持安全和标准化的通信。

In short, the Model Context Protocol (MCP) enables agents to access real-time information from databases, APIs, and web resources. It also allows agents to perform actions like sending emails, updating records, controlling devices, and executing complex tasks by integrating and processing data from various sources. Additionally, MCP supports media generation tools for AI applications.

简而言之，模型上下文协议（MCP）使智能体可以从数据库、API 和 Web 资源访问实时信息。还允许智能体执行发送电子邮件、更新记录、控制设备以及通过集成和处理多源数据执行复杂任务等操作。此外，MCP 支持 AI 应用程序的媒体生成工具。

## Hands-On Code Example with ADK

## 使用 ADK 的实践代码示例

This section outlines how to connect to a local MCP server that provides file system operations, enabling an ADK  agent to interact with the local file system.

本节概述了如何连接到提供文件系统操作的本地 MCP 服务器，使 ADK 智能体能够与本地文件系统交互。

## Agent Setup with MCPToolset 

## 使用 MCPToolset 的智能体

To configure an agent for file system interaction, an `agent.py` file must be created (e.g., at `./adk_agent_samples/mcp_agent/agent.py`). The `MCPToolset` is instantiated within the `tools` list of the `LlmAgent` object. It is crucial to replace `"/path/to/your/folder"` in the `args` list with the absolute path to a directory on the local system that the MCP server can access. This directory will be the root for the file system operations performed by the agent.

要配置智能体进行文件系统交互，必须创建一个 `agent.py` 文件（例如，在 `./adk_agent_samples/mcp_agent/agent.py`）。`MCPToolset` 在 `LlmAgent` 对象的 `tools` 列表中实例化。至关重要的是，必须将 `args` 列表中的 `"/path/to/your/folder"` 替换为本地系统上 MCP 服务器可以访问的目录的绝对路径。此目录将是智能体文件系统操作的根目录。

```python
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

## Create a reliable absolute path to a folder named 'mcp_managed_files'
## within the same directory as this agent script.
## This ensures the agent works out-of-the-box for demonstration.
## For production, you would point this to a more persistent and secure location.
TARGET_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mcp_managed_files")

## Ensure the target directory exists before the agent needs it.
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
                   "-y",  # Argument for npx to auto-confirm install
                   "@modelcontextprotocol/server-filesystem",
                   # This MUST be an absolute path to a folder.
                   TARGET_FOLDER_PATH,
               ],
           ),
           # Optional: You can filter which tools from the MCP server are exposed.
           # For example, to only allow reading:
           # tool_filter=['list_directory', 'read_file']
       )
   ],
)
```

`npx` (Node Package Execute), bundled with npm (Node Package Manager) versions 5.2.0 and later, is a utility that enables direct execution of Node.js packages from the npm registry. This eliminates the need for global installation. In essence, `npx` serves as an npm package runner, and it is commonly used to run many community MCP servers, which are distributed as Node.js packages.

`npx`（Node Package Execute）与 npm（Node Package Manager）5.2.0 及更高版本捆绑在一起，是一个实用程序，可以直接从 npm 注册表执行 Node.js 包。这消除了全局安装的需要。本质上，`npx` 作为 npm 包运行器，它通常用于运行许多社区 MCP 服务器，这些服务器作为 Node.js 包分发。

Creating an `__init__.py` file is necessary to ensure the agent.py file is recognized as part of a discoverable Python package for the Agent Development Kit (ADK). This file should reside in the same directory as [agent.py](http://agent.py).

创建 __init__.py 文件是必要的，以确保 agent.py 文件被识别为智能体开发工具包（ADK）的可发现 Python 包的一部分。此文件应与 [agent.py](http://agent.py) 位于同一目录中。

```python
## ./adk_agent_samples/mcp_agent/__init__.py
from . import agent
```

Certainly, other supported commands are available for use. For example, connecting to python3 can be achieved as follows:

当然，还可以使用其他受支持的命令。例如，可以按如下方式连接到 python3：

```python
connection_params = StdioConnectionParams(
 server_params={
     "command": "python3",
     "args": ["./agent/mcp_server.py"],
     "env": {
       "SERVICE_ACCOUNT_PATH":SERVICE_ACCOUNT_PATH,
       "DRIVE_FOLDER_ID": DRIVE_FOLDER_ID
     }
 }
)
```

UVX, in the context of Python, refers to a command-line tool that utilizes uv to execute commands in a temporary, isolated Python environment. Essentially, it allows you to run Python tools and packages without needing to install them globally or within your project's environment. You can run it via the MCP server.

在 Python 的上下文中，UVX 是指一个命令行工具，它利用 uv 在临时的、隔离的 Python 环境中执行命令。本质上，它允许您运行 Python 工具和包，而无需全局安装或在项目环境中安装它们。您可以通过 MCP 服务器运行它。

```python
connection_params = StdioConnectionParams(
 server_params={
   "command": "uvx",
   "args": ["mcp-google-sheets@latest"],
   "env": {
     "SERVICE_ACCOUNT_PATH":SERVICE_ACCOUNT_PATH,
     "DRIVE_FOLDER_ID": DRIVE_FOLDER_ID
   }
 }
)
```

Once the MCP Server is created, the next step is to connect to it.

创建 MCP 服务器后，下一步是连接到它。

## Connecting the MCP Server with ADK Web 

## 使用 ADK Web 连接 MCP 服务器

To begin, execute 'adk web'. Navigate to the parent directory of mcp\_agent (e.g., adk\_agent\_samples) in your terminal and run:

首先，执行 'adk web'。在终端中导航到 mcp_agent 的父目录（例如，adk_agent_samples）并运行：

```bash
cd ./adk_agent_samples # Or your equivalent parent directory
adk web
```

Once the ADK Web UI has loaded in your browser, select the `filesystem_assistant_agent` from the agent menu. Next, experiment with prompts such as:

ADK Web UI 在浏览器中加载后，从智能体菜单中选择 `filesystem_assistant_agent`。接下来，尝试以下提示：

* "Show me the contents of this folder."  
* "Read the `sample.txt` file." (This assumes `sample.txt` is located at `TARGET_FOLDER_PATH`.)  
* "What's in `another_file.md`?"

* "Show me the contents of this folder."
* "Read the `sample.txt` file."（假设 `sample.txt` 位于 `TARGET_FOLDER_PATH`。）
* "What's in `another_file.md`?"

## Creating an MCP Server with FastMCP 

## 使用 FastMCP 创建 MCP 服务器

FastMCP is a high-level Python framework designed to streamline the development of MCP servers. It provides an abstraction layer that simplifies protocol complexities, allowing developers to focus on core logic.

FastMCP 是一个高级 Python 框架，旨在简化 MCP 服务器的开发。它提供了一个抽象层，简化了协议的复杂性，允许开发者专注于核心逻辑。

The library enables rapid definition of tools, resources, and prompts using simple Python decorators. A significant advantage is its automatic schema generation, which intelligently interprets Python function signatures, type hints, and documentation strings to construct necessary AI model interface specifications. This automation minimizes manual configuration and reduces human error.

该库使用简单的 Python 装饰器能够快速定义工具、资源和提示词。一个显著的优势是其自动模式生成，它智能地解释 Python 函数签名、类型提示和文档字符串，以构建必要的 AI 模型接口规范。这种自动化最大限度地减少了手动配置并减少了人为错误。

Beyond basic tool creation, FastMCP facilitates advanced architectural patterns like server composition and proxying. This enables modular development of complex, multi-component systems and seamless integration of existing services into an AI-accessible framework. Additionally, FastMCP includes optimizations for efficient, distributed, and scalable AI-driven applications.

除了基本的工具创建之外，FastMCP 还促进了服务器组合和代理等高级架构模式。这使得能够模块化开发复杂的、多组件系统，并将现有服务无缝集成到 AI 可访问的框架中。此外，FastMCP 包括针对高效、分布式和可扩展的 AI 驱动应用程序的优化。

## Server setup with FastMCP

## 使用 FastMCP 设置服务器

## To illustrate, consider a basic "greet" tool provided by the server. ADK agents and other MCP clients can interact with this tool using HTTP once it is active.

为了说明，考虑服务器提供的基本"greet"工具。一旦激活，ADK 智能体和其他 MCP 客户端可以使用 HTTP 与此工具交互。

```python
## fastmcp_server.py
## This script demonstrates how to create a simple MCP server using FastMCP.
## It exposes a single tool that generates a greeting.

## 1. Make sure you have FastMCP installed:
## pip install fastmcp
from fastmcp import FastMCP, Client

## Initialize the FastMCP server.
mcp_server = FastMCP()

## Define a simple tool function.
## The `@mcp_server.tool` decorator registers this Python function as an MCP tool.
## The docstring becomes the tool's description for the LLM.
@mcp_server.tool
def greet(name: str) -> str:
    """
    Generates a personalized greeting.
    Args:
        name: The name of the person to greet.
    Returns:
        A greeting string.
    """
    return f"Hello, {name}! Nice to meet you."

## Or if you want to run it from the script:
if __name__ == "__main__":
    mcp_server.run(
        transport="http",
        host="127.0.0.1",
        port=8000
    )
```

This Python script defines a single function called greet, which takes a person's name and returns a personalized greeting. The @tool() decorator above this function automatically registers it as a tool that an AI or another program can use. The function's documentation string and type hints are used by FastMCP to tell the Agent how the tool works, what inputs it needs, and what it will return.

这个 Python 脚本定义了一个名为 greet 的单一函数，它接受一个人的名字并返回个性化的问候语。此函数上方的 @tool() 装饰器自动将其注册为 AI 或其他程序可以使用的工具。函数的文档字符串和类型提示被 FastMCP 用来告诉智能体该工具的工作原理、需要什么输入以及它将返回什么。

When the script is executed, it starts the FastMCP server, which listens for requests on localhost:8000. This makes the greet function available as a network service. An  agent could then be configured to connect to this server and use the greet tool to generate greetings as part of a larger task. The server runs continuously until it is manually stopped.

当脚本执行时，它启动 FastMCP 服务器，该服务器在 localhost:8000 上监听请求。这使得 greet 函数作为网络服务可用。然后可以将智能体配置为连接到此服务器，并使用 greet 工具生成问候语，作为更大任务的一部分。服务器持续运行，直到手动停止。

## Consuming the FastMCP Server with an ADK Agent

## 使用 ADK 智能体消费 FastMCP 服务器

An ADK agent can be set up as an MCP client to use a running FastMCP server. This requires configuring HttpServerParameters with the FastMCP server's network address, which is usually http://localhost:8000.

可以将 ADK 智能体设置为 MCP 客户端，以使用正在运行的 FastMCP 服务器。这需要使用 FastMCP 服务器的网络地址配置 HttpServerParameters，通常是 http://localhost:8000。

A tool\_filter parameter can be included to restrict the agent's tool usage to specific tools offered by the server, such as 'greet'. When prompted with a request like "Greet John Doe," the agent's embedded LLM identifies the 'greet' tool available via MCP, invokes it with the argument "John Doe," and returns the server's response. This process demonstrates the integration of user-defined tools exposed through MCP with an ADK agent.

可以包含 tool_filter 参数以限制智能体对服务器提供的特定工具的使用，例如 'greet'。当提示"Greet John Doe"等请求时，智能体的嵌入式 LLM 识别通过 MCP 可用的 'greet' 工具，使用参数"John Doe"调用它，并返回服务器的响应。此过程演示了通过 MCP 公开的用户定义工具与 ADK 智能体的集成。

To establish this configuration, an agent file (e.g., agent.py located in ./adk\_agent\_samples/fastmcp\_client\_agent/) is required. This file will instantiate an ADK agent and use HttpServerParameters to establish a connection with the operational FastMCP server.

要建立此配置，需要一个智能体文件（例如，位于 ./adk_agent_samples/fastmcp_client_agent/ 的 agent.py）。此文件将实例化一个 ADK 智能体，并使用 HttpServerParameters 与正在运行的 FastMCP 服务器建立连接。

```python
## ./adk_agent_samples/fastmcp_client_agent/agent.py
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, HttpServerParameters

## Define the FastMCP server's address.
## Make sure your fastmcp_server.py (defined previously) is running on this port.
FASTMCP_SERVER_URL = "http://localhost:8000"

root_agent = LlmAgent(
   model='gemini-2.0-flash', # Or your preferred model
   name='fastmcp_greeter_agent',
   instruction='You are a friendly assistant that can greet people by their name. Use the "greet" tool.',
   tools=[
       MCPToolset(
           connection_params=HttpServerParameters(
               url=FASTMCP_SERVER_URL,
           ),
           # Optional: Filter which tools from the MCP server are exposed
           # For this example, we're expecting only 'greet'
           tool_filter=['greet']
       )
   ],
)
```

The script defines an Agent named fastmcp\_greeter\_agent that uses a Gemini language model. It's given a specific instruction to act as a friendly assistant whose purpose is to greet people. Crucially, the code equips this agent with a tool to perform its task. It configures an MCPToolset to connect to a separate server running on localhost:8000, which is expected to be the FastMCP server from the previous example. The agent is specifically granted access to the greet tool hosted on that server. In essence, this code sets up the client side of the system, creating an intelligent agent that understands its goal is to greet people and knows exactly which external tool to use to accomplish it.

该脚本定义了一个名为 fastmcp_greeter_agent 的智能体，它使用 Gemini 语言模型。它被赋予特定的指令，作为一个友好的助手，其目的是问候人们。至关重要的是，该代码为此智能体配备了执行其任务的工具。它配置了一个 MCPToolset 来连接到在 localhost:8000 上运行的独立服务器，该服务器应该是前面示例中的 FastMCP 服务器。智能体被明确授予访问该服务器上托管的 greet 工具的权限。本质上，此代码设置了系统的客户端，创建了一个智能智能体，它理解其目标是问候人们，并确切地知道使用哪个外部工具来完成它。

Creating an `__init__.py` file within the fastmcp\_client\_agent directory is necessary. This ensures the agent is recognized as a discoverable Python package for the ADK.

在 fastmcp_client_agent 目录中创建 __init__.py 文件是必要的。这确保了智能体被识别为 ADK 的可发现 Python 包。

To begin, open a new terminal and run `python fastmcp_server.py` to start the FastMCP server. Next, go to the parent directory of `fastmcp_client_agent` (for example, `adk_agent_samples`) in your terminal and execute `adk web`. Once the ADK Web UI loads in your browser, select the `fastmcp_greeter_agent` from the agent menu. You can then test it by entering a prompt like "Greet John Doe." The agent will use the `greet` tool on your FastMCP server to create a response.

首先，打开一个新终端并运行 `python fastmcp_server.py` 来启动 FastMCP 服务器。接下来，在终端中转到 `fastmcp_client_agent` 的父目录（例如，`adk_agent_samples`）并执行 `adk web`。一旦 ADK Web UI 在浏览器中加载，从智能体菜单中选择 `fastmcp_greeter_agent`。然后可以通过输入"Greet John Doe"等提示来测试它。智能体将使用 FastMCP 服务器上的 `greet` 工具创建响应。

## At a Glance

## 速览

**What:** To function as effective agents, LLMs must move beyond simple text generation. They require the ability to interact with the external environment to access current data and utilize external software. Without a standardized communication method, each integration between an LLM and an external tool or data source becomes a custom, complex, and non-reusable effort. This ad-hoc approach hinders scalability and makes building complex, interconnected AI systems difficult and inefficient.

**问题背景**：要作为有效的智能体，LLM 必须超越简单的文本生成。它们需要与外部环境交互的能力，以访问当前数据并使用外部软件。如果没有标准化的通信方法，LLM 与外部工具或数据源之间的每次集成都将成为定制、复杂且不可重用的工作。这种临时方法阻碍了可扩展性，并使构建复杂、互联的 AI 系统变得困难且低效。

**Why:** The Model Context Protocol (MCP) offers a standardized solution by acting as a universal interface between LLMs and external systems. It establishes an open, standardized protocol that defines how external capabilities are discovered and used. Operating on a client-server model, MCP allows servers to expose tools, data resources, and interactive prompts to any compliant client. LLM-powered applications act as these clients, dynamically discovering and interacting with available resources in a predictable manner. This standardized approach fosters an ecosystem of interoperable and reusable components, dramatically simplifying the development of complex agentic workflows.

**解决方案**：模型上下文协议（MCP）通过充当 LLM 和外部系统之间的通用接口，提供了标准化的解决方案。它建立了一个开放的标准化协议，定义了如何发现和使用外部能力。基于客户端-服务器模型运行，MCP 允许服务器向任何兼容的客户端公开工具、数据资源和交互式提示。LLM 驱动的应用程序充当这些客户端，以可预测的方式动态发现和与可用资源交互。这种标准化方法促进了可互操作和可重用组件的生态系统，显著简化了复杂智能体工作流的开发。

**Rule of thumb:** Use the Model Context Protocol (MCP) when building complex, scalable, or enterprise-grade agentic systems that need to interact with a diverse and evolving set of external tools, data sources, and APIs. It is ideal when interoperability between different LLMs and tools is a priority, and when agents require the ability to dynamically discover new capabilities without being redeployed. For simpler applications with a fixed and limited number of predefined functions, direct tool function calling may be sufficient.

**实践建议**：在构建需要与各种不断发展的外部工具、数据源和 API 交互的复杂、可扩展或企业级智能体系统时，使用模型上下文协议（MCP）。当不同 LLM 和工具之间的互操作性是优先考虑事项时，以及当智能体需要动态发现新能力而无需重新部署时，它是理想选择。对于具有固定有限数量预定义函数的简单应用程序，直接工具函数调用可能就足够了。

**Visual summary**

**可视化摘要**

![](../images/chapter-10/image1.png)

Fig.1: Model Context protocol

图 1：模型上下文协议

## Key Takeaways

## 关键要点

These are the key takeaways:

以下是本章核心要点：

* The Model Context Protocol (MCP) is an open standard facilitating standardized communication between LLMs and external applications, data sources, and tools.  
* 模型上下文协议（MCP）是一个开放标准，促进 LLM 与外部应用程序、数据源和工具之间的标准化通信。

* It employs a client-server architecture, defining the methods for exposing and consuming resources, prompts, and tools.  
* 它采用客户端-服务器架构，定义了公开和使用资源、提示和工具的方法。

* The Agent Development Kit (ADK) supports both utilizing existing MCP servers and exposing ADK tools via an MCP server.  
* 智能体开发工具包（ADK）支持使用现有 MCP 服务器以及通过 MCP 服务器公开 ADK 工具。

* FastMCP simplifies the development and management of MCP servers, particularly for exposing tools implemented in Python.  
* FastMCP 简化了 MCP 服务器的开发和管理，特别是用于公开在 Python 中实现的工具。

* MCP Tools for Genmedia Services allows agents to integrate with Google Cloud's generative media capabilities (Imagen, Veo, Chirp 3 HD, Lyria).  
* 生成媒体服务的 MCP 工具允许智能体与 Google Cloud 的生成媒体能力（Imagen、Veo、Chirp 3 HD、Lyria）集成。

* MCP enables LLMs and agents to interact with real-world systems, access dynamic information, and perform actions beyond text generation.

* MCP 使 LLM 和智能体能够与现实世界系统交互，访问动态信息，并执行超越文本生成的操作。

## Conclusion

## 结论

The Model Context Protocol (MCP) is an open standard that facilitates communication between Large Language Models (LLMs) and external systems. It employs a client-server architecture, enabling LLMs to access resources, utilize prompts, and execute actions through standardized tools. MCP allows LLMs to interact with databases, manage generative media workflows, control IoT devices, and automate financial services. Practical examples demonstrate setting up agents to communicate with MCP servers, including filesystem servers and servers built with FastMCP, illustrating its integration with the Agent Development Kit (ADK). MCP is a key component for developing interactive AI agents that extend beyond basic language capabilities.

模型上下文协议（MCP）是一个开放标准，促进大型语言模型（LLM）与外部系统之间的通信。它采用客户端-服务器架构，使 LLM 能够通过标准化工具访问资源、使用提示和执行操作。MCP 允许 LLM 与数据库交互、管理生成媒体工作流、控制物联网设备以及自动化金融服务。实际示例演示了设置智能体与 MCP 服务器通信的方法，包括文件系统服务器和使用 FastMCP 构建的服务器，说明了其与智能体开发工具包（ADK）的集成。MCP 是开发超越基本语言能力的交互式 AI 智能体的关键组件。

## References

## 参考文献

1. Model Context Protocol (MCP) Documentation. (Latest). *Model Context Protocol (MCP)*. [https://google.github.io/adk-docs/mcp/](https://google.github.io/adk-docs/mcp/)  
2. FastMCP Documentation. FastMCP. [https://github.com/jlowin/fastmcp](https://github.com/jlowin/fastmcp)  
3. MCP Tools for Genmedia Services. *MCP Tools for Genmedia Services*. [https://google.github.io/adk-docs/mcp/#mcp-servers-for-google-cloud-genmedia](https://google.github.io/adk-docs/mcp/#mcp-servers-for-google-cloud-genmedia)  
4. MCP Toolbox for Databases Documentation. (Latest). *MCP Toolbox for Databases*. [https://google.github.io/adk-docs/mcp/databases/](https://google.github.io/adk-docs/mcp/databases/)
