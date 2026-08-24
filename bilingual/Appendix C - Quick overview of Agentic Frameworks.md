---
layout: bilingual
lang: bilingual
---

# Appendix C - Quick overview of Agentic Frameworks

# 附录 C - Agentic 框架快速概览

## LangChain

LangChain is a framework for developing applications powered by LLMs. Its core strength lies in its LangChain Expression Language (LCEL), which allows you to "pipe" components together into a chain. This creates a clear, linear sequence where the output of one step becomes the input for the next. It's built for workflows that are Directed Acyclic Graphs (DAGs), meaning the process flows in one direction without loops.

LangChain 是一个用于开发由大语言模型（LLM）驱动的应用程序的框架。其核心优势在于 LangChain 表达式语言（LCEL），它允许您使用管道操作符将组件连接成链。这种设计形成了清晰的线性序列，每一步的输出自动成为下一步的输入。该框架专为有向无环图（DAG）工作流构建，意味着处理流程单向流动且无循环。

Use it for:

适用场景：

* Simple RAG: Retrieve a document, create a prompt, get an answer from an LLM.  
* Summarization: Take user text, feed it to a summarization prompt, and return the output.  
* Extraction: Extract structured data (like JSON) from a block of text.

* 简单 RAG：检索文档，构建提示，从 LLM 获取答案。
* 文本摘要：接收用户文本，输入至摘要提示，返回摘要结果。
* 数据提取：从文本块中提取结构化数据（如 JSON 格式）。

```python
# A simple LCEL chain conceptually
# (This is not runnable code, just illustrates the flow)
chain = prompt | model | output_parser
```

### LangGraph

LangGraph is a library built on top of LangChain to handle more advanced agentic systems. It allows you to define your workflow as a graph with nodes (functions or LCEL chains) and edges (conditional logic). Its main advantage is the ability to create cycles, allowing the application to loop, retry, or call tools in a flexible order until a task is complete. It explicitly manages the application state, which is passed between nodes and updated throughout the process.

LangGraph 是构建于 LangChain 之上的库，专为处理更高级的 Agentic 系统设计。它允许您将工作流定义为包含节点（函数或 LCEL 链）和边（条件逻辑）的图结构。其主要优势在于支持循环创建，使应用程序能够循环执行、重试操作或以灵活顺序调用工具，直至任务完成。该库显式管理应用程序状态，状态在节点间传递并在整个流程中持续更新。

Use it for:

适用场景：

* Multi-agent Systems: A supervisor agent routes tasks to specialized worker agents, potentially looping until the goal is met.  
* Plan-and-Execute Agents: An agent creates a plan, executes a step, and then loops back to update the plan based on the result.  
* Human-in-the-Loop: The graph can wait for human input before deciding which node to go to next.

* 多智能体系统：监督智能体将任务路由给专业化工作智能体，可能循环执行直至目标达成。
* 规划与执行智能体：智能体制定计划，执行步骤，随后基于结果循环反馈以更新计划。
* 人机协同：图结构可等待人工输入，再决定后续执行节点。

| Feature | LangChain | LangGraph |
| :---- | :---- | :---- |
| Core Abstraction | Chain (using LCEL) | Graph of Nodes |
| Workflow Type | Linear (Directed Acyclic Graph) | Cyclical (Graphs with loops) |
| State Management | Generally stateless per run | Explicit and persistent state object |
| Primary Use | Simple, predictable sequences | Complex, dynamic, stateful agents |

| 特性 | LangChain | LangGraph |
| :---- | :---- | :---- |
| 核心抽象 | 链（使用 LCEL） | 节点图 |
| 工作流类型 | 线性（有向无环图） | 循环（支持循环的图） |
| 状态管理 | 通常单次运行无状态 | 显式且持久的状态对象 |
| 主要用途 | 简单、可预测的序列 | 复杂、动态、有状态的智能体 |

### Which One Should You Use?

### 如何选择？

* Choose LangChain when your application has a clear, predictable, and linear flow of steps. If you can define the process from A to B to C without needing to loop back, LangChain with LCEL is the perfect tool.  
* Choose LangGraph when you need your application to reason, plan, or operate in a loop. If your agent needs to use tools, reflect on the results, and potentially try again with a different approach, you need the cyclical and stateful nature of LangGraph.

* 当应用程序具备清晰、可预测的线性步骤流程时，选择 LangChain。若您能定义从 A 到 B 再到 C 的直连过程而无需回环，则采用 LCEL 的 LangChain 是理想工具。
* 当应用程序需进行推理、规划或循环操作时，选择 LangGraph。若您的智能体使用工具、反思结果并可能尝试不同策略，则需借助 LangGraph 的循环和有状态特性。

```python
# Graph state
class State(TypedDict):
    topic: str
    joke: str
    story: str
    poem: str
    combined_output: str

# Nodes
def call_llm_1(state: State):
    """First LLM call to generate initial joke"""
    msg = llm.invoke(f"Write a joke about {state['topic']}")
    return {"joke": msg.content}

def call_llm_2(state: State):
    """Second LLM call to generate story"""
    msg = llm.invoke(f"Write a story about {state['topic']}")
    return {"story": msg.content}

def call_llm_3(state: State):
    """Third LLM call to generate poem"""
    msg = llm.invoke(f"Write a poem about {state['topic']}")
    return {"poem": msg.content}

def aggregator(state: State):
    """Combine the joke and story into a single output"""
    combined = f"Here's a story, joke, and poem about {state['topic']}!\n\n"
    combined += f"STORY:\n{state['story']}\n\n"
    combined += f"JOKE:\n{state['joke']}\n\n"
    combined += f"POEM:\n{state['poem']}"
    return {"combined_output": combined}

# Build workflow
parallel_builder = StateGraph(State)

# Add nodes
parallel_builder.add_node("call_llm_1", call_llm_1)
parallel_builder.add_node("call_llm_2", call_llm_2)
parallel_builder.add_node("call_llm_3", call_llm_3)
parallel_builder.add_node("aggregator", aggregator)

# Add edges to connect nodes
parallel_builder.add_edge(START, "call_llm_1")
parallel_builder.add_edge(START, "call_llm_2")
parallel_builder.add_edge(START, "call_llm_3")
parallel_builder.add_edge("call_llm_1", "aggregator")
parallel_builder.add_edge("call_llm_2", "aggregator")
parallel_builder.add_edge("call_llm_3", "aggregator")
parallel_builder.add_edge("aggregator", END)

parallel_workflow = parallel_builder.compile()

# Show workflow
display(Image(parallel_workflow.get_graph().draw_mermaid_png()))

# Invoke
state = parallel_workflow.invoke({"topic": "cats"})
print(state["combined_output"])
```

This code defines and runs a LangGraph workflow that operates in parallel. Its main purpose is to simultaneously generate a joke, a story, and a poem about a given topic and then combine them into a single, formatted text output.

这段代码定义并运行了一个并行操作的 LangGraph 工作流。其主要目的是同时生成关于给定主题的笑话、故事和诗歌，然后将它们组合成单个格式化的文本输出。

## Google's ADK

Google's Agent Development Kit, or ADK, provides a high-level, structured framework for building and deploying applications composed of multiple, interacting AI agents. It contrasts with LangChain and LangGraph by offering a more opinionated and production-oriented system for orchestrating agent collaboration, rather than providing the fundamental building blocks for an agent's internal logic.

Google 的智能体开发工具包（ADK）提供了一个高级、结构化的框架，用于构建和部署由多个交互性 AI 智能体组成的应用程序。与 LangChain 和 LangGraph 相比，它提供了一个更具指导性和生产就绪的系统，用于编排智能体协作，而非提供智能体内部逻辑的基础构建块。

LangChain operates at the most foundational level, offering the components and standardized interfaces to create sequences of operations, such as calling a model and parsing its output. LangGraph extends this by introducing a more flexible and powerful control flow; it treats an agent's workflow as a stateful graph. Using LangGraph, a developer explicitly defines nodes, which are functions or tools, and edges, which dictate the path of execution. This graph structure allows for complex, cyclical reasoning where the system can loop, retry tasks, and make decisions based on an explicitly managed state object that is passed between nodes. It gives the developer fine-grained control over a single agent's thought process or the ability to construct a multi-agent system from first principles.

LangChain 在最基础层面运作，提供组件和标准化接口以创建操作序列，例如调用模型并解析其输出。LangGraph 通过引入更灵活强大的控制流对此进行扩展；它将智能体工作流视为有状态图。使用 LangGraph，开发者显式定义节点（函数或工具）和边（决定执行路径）。这种图结构支持复杂循环推理，系统可循环执行、重试任务，并基于节点间传递的显式管理状态对象做出决策。它为开发者提供了对单个智能体行为的细粒度控制，或从第一性原理构建多智能体系统。

Google's ADK abstracts away much of this low-level graph construction. Instead of asking the developer to define every node and edge, it provides pre-built architectural patterns for multi-agent interaction. For instance, ADK has built-in agent types like SequentialAgent or ParallelAgent, which manage the flow of control between different agents automatically. It is architected around the concept of a "team" of agents, often with a primary agent delegating tasks to specialized sub-agents. State and session management are handled more implicitly by the framework, providing a more cohesive but less granular approach than LangGraph's explicit state passing. Therefore, while LangGraph gives you the detailed tools to design the intricate wiring of a single robot or a team, Google's ADK gives you a factory assembly line designed to build and manage a fleet of robots that already know how to work together.

Google 的 ADK 抽象了大部分此类低级图构建工作。ADK 不要求开发者定义每个节点和边，而是为多智能体交互提供预构建的架构模式。例如，ADK 包含 SequentialAgent 或 ParallelAgent 等内置智能体类型，它们自动管理不同智能体间的控制流。其架构围绕智能体"团队"概念设计，通常由主智能体将任务委派给专业化子智能体。状态和会话管理由框架更隐式地处理，提供了比 LangGraph 显式状态传递更连贯但精细度稍低的方法。因此，若将 LangGraph 比作提供详细工具以设计单个机器人或团队复杂接线的工具箱，Google 的 ADK 则如同一个工厂装配线，旨在构建和管理一支已具备协同工作能力的机器人舰队。

```python
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

dice_agent = LlmAgent(
    model="gemini-2.0-flash-exp",
    name="question_answer_agent",
    description="A helpful assistant agent that can answer questions.",
    instruction="""Respond to the query using google search""",
    tools=[google_search],
)
```

This code creates a search-augmented agent. When this agent receives a question, it will not just rely on its pre-existing knowledge. Instead, following its instructions, it will use the Google Search tool to find relevant, real-time information from the web and then use that information to construct its answer.

此代码创建了一个搜索增强型智能体。当该智能体接收问题时，不会仅依赖其既有知识。相反，遵循其指令，它将使用 Google 搜索工具从网络查找相关实时信息，并据此构建答案。

## Crew.AI

CrewAI offers an orchestration framework for building multi-agent systems by focusing on collaborative roles and structured processes. It operates at a higher level of abstraction than foundational toolkits, providing a conceptual model that mirrors a human team. Instead of defining the granular flow of logic as a graph, the developer defines the actors and their assignments, and CrewAI manages their interaction.

CrewAI 提供了一个编排框架，通过聚焦协作角色与结构化流程来构建多智能体系统。它在比基础工具包更高的抽象层级运作，提供模拟人类团队的概念模型。开发者无需将逻辑细粒度流程定义为图，而是定义参与者及其任务分配，由 CrewAI 管理其交互。

The core components of this framework are Agents, Tasks, and the Crew. An Agent is defined not just by its function but by a persona, including a specific role, a goal, and a backstory, which guides its behavior and communication style. A Task is a discrete unit of work with a clear description and expected output, assigned to a specific Agent. The Crew is the cohesive unit that contains the Agents and the list of Tasks, and it executes a predefined Process. This process dictates the workflow, which is typically either sequential, where the output of one task becomes the input for the next in line, or hierarchical, where a manager-like agent delegates tasks and coordinates the workflow among other agents.

该框架核心组件包括智能体、任务和团队。智能体不仅由功能定义，还通过角色、目标和背景故事等角色特征来定义，这些特征指导其行为与沟通风格。任务是具备明确描述和预期输出的离散工作单元，分配给特定智能体。团队是包含智能体和任务列表的协调单元，执行预定义的流程。此流程决定工作流模式，通常为顺序型（一个任务的输出成为下一任务的输入）或层级型（经理型智能体分配任务并协调其他智能体间的交互）。

When compared to other frameworks, CrewAI occupies a distinct position. It moves away from the low-level, explicit state management and control flow of LangGraph, where a developer wires together every node and conditional edge. Instead of building a state machine, the developer designs a team charter. While Google's ADK provides a comprehensive, production-oriented platform for the entire agent lifecycle, CrewAI concentrates specifically on the logic of agent collaboration and for simulating a team of specialists.

与其他框架相比，CrewAI 定位独特。它脱离了 LangGraph 的低层级、显式状态管理与控制流（后者要求开发者连接每个节点与条件边）。开发者不是构建状态机，而是设计团队章程。尽管 Google 的 ADK 为整个智能体生命周期提供了全面、生产就绪的平台，CrewAI 则专注于智能体协作与专家团队模拟。

```python
@crew
def crew(self) -> Crew:
    """Creates the research crew"""
    return Crew(
      agents=self.agents,
      tasks=self.tasks,
      process=Process.sequential,
      verbose=True,
    )
```

This code sets up a sequential workflow for a team of AI agents, where they tackle a list of tasks in a specific order, with detailed logging enabled to monitor their progress.

此代码为 AI 智能体团队配置了顺序工作流，智能体按特定顺序处理任务列表，并启用详细日志以监控进度。

## Other agent development framework

## 其他智能体框架

**Microsoft AutoGen**: AutoGen is a framework centered on orchestrating multiple agents that solve tasks through conversation. Its architecture enables agents with distinct capabilities to interact, allowing for complex problem decomposition and collaborative resolution. The primary advantage of AutoGen is its flexible, conversation-driven approach that supports dynamic and complex multi-agent interactions. However, this conversational paradigm can lead to less predictable execution paths and may require sophisticated prompt engineering to ensure tasks converge efficiently.

**Microsoft AutoGen**：AutoGen 是一个以对话方式编排多智能体任务为核心的框架。其架构使具备不同能力的智能体能够协作，支持复杂问题分解与协作解决。AutoGen 主要优势在于其灵活的对话驱动方法，可应对动态复杂的多智能体交互场景。这种对话范式可能导致执行路径预测性降低，且需复杂提示工程以确保任务高效收敛。

**LlamaIndex**: LlamaIndex is fundamentally a data framework designed to connect large language models with external and private data sources. It excels at creating sophisticated data ingestion and retrieval pipelines, which are essential for building knowledgeable agents that can perform RAG. While its data indexing and querying capabilities are exceptionally powerful for creating context-aware agents, its native tools for complex agentic control flow and multi-agent orchestration are less developed compared to agent-first frameworks. LlamaIndex is optimal when the core technical challenge is data retrieval and synthesis.

**LlamaIndex**：LlamaIndex 本质上是数据框架，旨在连接大语言模型与外部及私有数据源。它擅长构建复杂的数据摄取与检索管道，这对创建能执行 RAG 的知识型智能体至关重要。尽管其数据索引与查询能力对构建情境感知智能体非常关键，但与智能体优先的框架相比，其在复杂智能体控制流和多智能体编排方面提供的工具较少。当核心技术挑战为数据检索与综合时，LlamaIndex 是最佳选择。

**Haystack**: Haystack is an open-source framework engineered for building scalable and production-ready search systems powered by language models. Its architecture is composed of modular, interoperable nodes that form pipelines for document retrieval, question answering, and summarization. The main strength of Haystack is its focus on performance and scalability for large-scale information retrieval tasks, making it suitable for enterprise-grade applications. A potential trade-off is that its design, optimized for search pipelines, can be more rigid for implementing highly dynamic and creative agentic behaviors.

**Haystack**：Haystack 是专为构建语言模型驱动的可扩展、生产就绪搜索系统而设计的开源框架。其架构由模块化、可互操作的节点组成，这些节点构成文档检索、问答和摘要的管道。Haystack 主要优势在于其对大规模信息检索任务性能与可扩展性的专注，使其适用于企业级应用。潜在权衡在于，其针对搜索管道优化的设计在实现高度动态和创造性智能体行为时可能较为僵化。

**MetaGPT**: MetaGPT implements a multi-agent system by assigning roles and tasks based on a predefined set of Standard Operating Procedures (SOPs). This framework structures agent collaboration to mimic a software development company, with agents taking on roles like product managers or engineers to complete complex tasks. This SOP-driven approach results in highly structured and coherent outputs, which is a significant advantage for specialized domains like code generation. The framework's primary limitation is its high degree of specialization, making it less adaptable for general-purpose agentic tasks outside of its core design.

**MetaGPT**：MetaGPT 通过基于预定义标准操作程序（SOP）分配角色和任务来实现多智能体协作。该框架将智能体协作结构化为模拟一家软件开发公司，智能体承担产品经理或工程师等角色完成复杂任务。这种 SOP 驱动方法产生高度结构化且连贯的输出，对代码生成等专业领域是显著优势。该框架主要局限在于其高度专业化，使其在核心设计范畴外的通用智能体任务适应性较弱。

**SuperAGI**: SuperAGI is an open-source framework designed to provide a complete lifecycle management system for autonomous agents. It includes features for agent provisioning, monitoring, and a graphical interface, aiming to enhance the reliability of agent execution. The key benefit is its focus on production-readiness, with built-in mechanisms to handle common failure modes like looping and to provide observability into agent performance. A potential drawback is that its comprehensive platform approach can introduce more complexity and overhead than a more lightweight, library-based framework.

**SuperAGI**：SuperAGI 是旨在为自主智能体提供完整生命周期管理系统的开源框架。它包括智能体配置、监控和图形界面等功能，旨在提升智能体执行的可靠性。其关键优势在于对生产就绪性的关注，具备处理循环等常见故障模式的内置机制，并提供智能体性能可视化。其潜在缺点在于，与更轻量级库框架相比，其全面平台方法可能引入更多复杂性与开销。

**Semantic Kernel**: Developed by Microsoft, Semantic Kernel is an SDK that integrates large language models with conventional programming code through a system of "plugins" and "planners." It allows an LLM to invoke native functions and orchestrate workflows, effectively treating the model as a reasoning engine within a larger software application. Its primary strength is its seamless integration with existing enterprise codebases, particularly in .NET and Python environments. The conceptual overhead of its plugin and planner architecture can present a steeper learning curve compared to more straightforward agent frameworks.

**Semantic Kernel**：由 Microsoft 开发，Semantic Kernel 是通过"插件"和"规划器"系统将大语言模型与传统编程代码集成的 SDK。它允许 LLM 调用原生函数并编排工作流，有效将模型视为大型软件应用中的推理引擎。其主要优势是与现有企业代码库（尤其在 .NET 和 Python 环境）的无缝集成。其插件与规划器架构的概念开销可能带来比更直接的智能体框架更陡峭的学习曲线。

**Strands Agents:** An AWS lightweight and flexible SDK that uses a model-driven approach for building and running AI agents. It is designed to be simple and scalable, supporting everything from basic conversational assistants to complex multi-agent autonomous systems. The framework is model-agnostic, offering broad support for various LLM providers, and includes native integration with the MCP for easy access to external tools. Its core advantage is its simplicity and flexibility, with a customizable agent loop that is easy to get started with. A potential trade-off is that its lightweight design means developers may need to build out more of the surrounding operational infrastructure, such as advanced monitoring or lifecycle management systems, which more comprehensive frameworks might provide out of the box.

**Strands Agents**：AWS 的轻量级灵活 SDK，采用模型驱动方法构建和运行 AI 智能体。其设计简洁且可扩展，支持从基础对话助手到复杂多智能体系统的各类场景。该框架与模型无关，广泛支持多种 LLM 提供商，并包含与 MCP 的原生集成以便轻松访问外部工具。其核心优势是简洁性与灵活性，提供易于上手的可定制智能体构建模块。其权衡在于，其轻量级设计意味着开发者可能需要构建更多周边运营基础设施（如高级监控或生命周期管理系统），而更全面框架可能提供开箱即用功能。

## Conclusion

## 结论

The landscape of agentic frameworks offers a diverse spectrum of tools, from low-level libraries for defining agent logic to high-level platforms for orchestrating multi-agent collaboration. At the foundational level, LangChain enables simple, linear workflows, while LangGraph introduces stateful, cyclical graphs for more complex reasoning. Higher-level frameworks like CrewAI and Google's ADK shift the focus to orchestrating teams of agents with predefined roles, while others like LlamaIndex specialize in data-intensive applications. This variety presents developers with a core trade-off between the granular control of graph-based systems and the streamlined development of more opinionated platforms. Consequently, selecting the right framework hinges on whether the application requires a simple sequence, a dynamic reasoning loop, or a managed team of specialists. Ultimately, this evolving ecosystem empowers developers to build increasingly sophisticated AI systems by choosing the precise level of abstraction their project demands.

智能体框架生态提供了多样化工具，涵盖从定义智能体的低级库到编排多智能体协作的高级平台。在基础层，LangChain 支持简单线性工作流，而 LangGraph 引入有状态循环图以实现更复杂推理。如 CrewAI 和 Google ADK 等高级框架将重心转向编排具预定义角色的智能体团队，而 LlamaIndex 等其他框架则专注数据密集型应用。这种多样性为开发者带来了基于图系统的细粒度控制与更具指导性平台的简化开发之间的核心权衡。因此，框架选择取决于应用需求：简单序列、动态推理循环还是受管专家团队。最终，这一不断演进的技术生态系统使开发者能通过选择项目所需的精确抽象级别，构建日益复杂的 AI 系统。

## References

## 参考文献

1. LangChain, [https://www.langchain.com/](https://www.langchain.com/)
2. LangGraph, [https://www.langchain.com/langgraph](https://www.langchain.com/langgraph)
3. Google's ADK, [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)
4. Crew.AI, [https://docs.crewai.com/en/introduction](https://docs.crewai.com/en/introduction)
