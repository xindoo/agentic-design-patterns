# 附录 C \- Agentic 框架快速概览

# LangChain 

LangChain 是一个用于开发由大语言模型驱动的应用程序的框架。其核心优势在于 LangChain 表达式语言（LCEL），它允许你将组件"管道化"到一个链中。这创建了一个清晰的线性序列，其中一个步骤的输出成为下一个步骤的输入。它专为有向无环图（DAG）工作流而构建，这意味着处理流程单向流动，没有循环。

适用场景：

* 简单的 RAG：检索文档，创建提示词，从 LLM 获取答案。  
* 摘要生成：获取用户文本，将其提供给摘要提示词，并返回输出。  
* 信息提取：从文本块中提取结构化数据（如 JSON）。

Python

| `# 一个简单的 LCEL 链概念示例 # （这不是可运行的代码，只是说明流程） chain = prompt | model | output_parse` |
| :---- |

### LangGraph 

LangGraph 是建立在 LangChain 之上的库，用于处理更高级的 agentic 系统。它允许你将工作流定义为图，包含节点（函数或 LCEL 链）和边（条件逻辑）。其主要优势是能够创建循环，允许应用程序循环、重试或以灵活的顺序调用工具，直到任务完成。它显式管理应用程序状态，该状态在节点之间传递并在整个过程中更新。

适用场景：

* 多 Agent 系统：监督 Agent 将任务路由到专门的工作 Agent，可能循环直到达成目标。  
* 规划与执行 Agent：Agent 创建计划，执行一个步骤，然后根据结果循环回来更新计划。  
* 人机协同：图可以等待人工输入，然后决定下一步转到哪个节点。

| 特性 | LangChain | LangGraph |
| :---- | :---- | :---- |
| 核心抽象 | 链（使用 LCEL） | 节点图 |
| 工作流类型 | 线性（有向无环图） | 循环（带循环的图） |
| 状态管理 | 通常每次运行无状态 | 显式且持久的状态对象 |
| 主要用途 | 简单、可预测的序列 | 复杂、动态、有状态的 Agent |

### 应该使用哪一个？

* 当应用程序具有清晰、可预测且线性的步骤流程时，选择 LangChain。如果你可以定义从 A 到 B 到 C 的过程而无需循环回来，那么使用 LCEL 的 LangChain 就是完美的工具。  
* 当你需要应用程序进行推理、规划或循环操作时，选择 LangGraph。如果你的 Agent 需要使用工具、反思结果，并可能用不同的方法重试，你就需要 LangGraph 的循环和有状态特性。

Python

| `# 图状态 class State(TypedDict):    topic: str    joke: str    story: str    poem: str    combined_output: str # 节点 def call_llm_1(state: State):    """第一次 LLM 调用以生成初始笑话"""    msg = llm.invoke(f"Write a joke about {state['topic']}")    return {"joke": msg.content} def call_llm_2(state: State):    """第二次 LLM 调用以生成故事"""    msg = llm.invoke(f"Write a story about {state['topic']}")    return {"story": msg.content} def call_llm_3(state: State):    """第三次 LLM 调用以生成诗歌"""    msg = llm.invoke(f"Write a poem about {state['topic']}")    return {"poem": msg.content} def aggregator(state: State):    """将笑话和故事组合成单个输出"""    combined = f"Here's a story, joke, and poem about {state['topic']}!\n\n"    combined += f"STORY:\n{state['story']}\n\n"    combined += f"JOKE:\n{state['joke']}\n\n"    combined += f"POEM:\n{state['poem']}"    return {"combined_output": combined} # 构建工作流 parallel_builder = StateGraph(State) # 添加节点 parallel_builder.add_node("call_llm_1", call_llm_1) parallel_builder.add_node("call_llm_2", call_llm_2) parallel_builder.add_node("call_llm_3", call_llm_3) parallel_builder.add_node("aggregator", aggregator) # 添加边来连接节点 parallel_builder.add_edge(START, "call_llm_1") parallel_builder.add_edge(START, "call_llm_2") parallel_builder.add_edge(START, "call_llm_3") parallel_builder.add_edge("call_llm_1", "aggregator") parallel_builder.add_edge("call_llm_2", "aggregator") parallel_builder.add_edge("call_llm_3", "aggregator") parallel_builder.add_edge("aggregator", END) parallel_workflow = parallel_builder.compile() # 显示工作流 display(Image(parallel_workflow.get_graph().draw_mermaid_png())) # 调用 state = parallel_workflow.invoke({"topic": "cats"}) print(state["combined_output"])` |
| :---- |

这段代码定义并运行了一个并行操作的 LangGraph 工作流。其主要目的是同时生成关于给定主题的笑话、故事和诗歌，然后将它们组合成单个格式化的文本输出。

# Google's ADK

Google 的 Agent 开发工具包（ADK）提供了一个高级、结构化的框架，用于构建和部署由多个交互式 AI Agent 组成的应用程序。与 LangChain 和 LangGraph 相比，它提供了一个更具主观性和面向生产的系统来编排 Agent 协作，而不是提供 Agent 内部逻辑的基础构建块。

LangChain 在最基础的层面运作，提供组件和标准化接口来创建操作序列，例如调用模型并解析其输出。LangGraph 通过引入更灵活和强大的控制流扩展了这一点；它将 Agent 的工作流视为有状态图。使用 LangGraph，开发者显式定义节点（函数或工具）和边（决定执行路径）。这种图结构允许复杂的循环推理，系统可以循环、重试任务，并基于在节点之间传递的显式管理状态对象做出决策。它为开发者提供了对单个 Agent 思维过程的细粒度控制，或从第一原理构建多 Agent 系统的能力。

Google 的 ADK 抽象掉了大部分这种低级图构建。ADK 不要求开发者定义每个节点和边，而是为多 Agent 交互提供预构建的架构模式。例如，ADK 有内置的 Agent 类型，如 SequentialAgent 或 ParallelAgent，它们自动管理不同 Agent 之间的控制流。它围绕 Agent "团队" 的概念进行架构，通常由主 Agent 将任务委托给专门的子 Agent。状态和会话管理由框架更隐式地处理，提供了比 LangGraph 的显式状态传递更连贯但不那么精细的方法。因此，虽然 LangGraph 为你提供详细的工具来设计单个机器人或团队的复杂接线，Google 的 ADK 为你提供了一个工厂装配线，旨在构建和管理一支已经知道如何协同工作的机器人车队。

Python

| `from google.adk.agents import LlmAgent from google.adk.tools import google_Search dice_agent = LlmAgent(    model="gemini-2.0-flash-exp",     name="question_answer_agent",    description="A helpful assistant agent that can answer questions.",    instruction="""Respond to the query using google search""",    tools=[google_search], )` |
| :---- |

这段代码创建了一个搜索增强的 Agent。当这个 Agent 收到问题时，它不会仅仅依赖其现有知识。相反，按照其指令，它将使用 Google 搜索工具从网络查找相关的实时信息，然后使用该信息构建答案。

Crew.AI

CrewAI 提供了一个编排框架，通过专注于协作角色和结构化流程来构建多 Agent 系统。它在比基础工具包更高的抽象级别上运作，提供了一个模仿人类团队的概念模型。开发者不是将逻辑的细粒度流程定义为图，而是定义参与者及其任务分配，CrewAI 管理它们的交互。

该框架的核心组件是 Agent、Task 和 Crew。Agent 不仅由其功能定义，还由角色、目标和背景故事等人格特征定义，这些特征指导其行为和沟通风格。Task 是具有明确描述和预期输出的离散工作单元，分配给特定的 Agent。Crew 是包含 Agent 和 Task 列表的凝聚单元，它执行预定义的 Process。这个流程决定了工作流，通常是顺序的（一个任务的输出成为下一个任务的输入）或层次的（类似经理的 Agent 委派任务并协调其他 Agent 之间的工作流）。

与其他框架相比，CrewAI 占据了独特的位置。它摆脱了 LangGraph 的低级、显式状态管理和控制流，在 LangGraph 中，开发者连接每个节点和条件边。开发者不是构建状态机，而是设计团队章程。虽然 Google 的 ADK 为整个 Agent 生命周期提供了一个全面的、面向生产的平台，但 CrewAI 专门专注于 Agent 协作的逻辑和模拟专家团队。

Python

| `@crew def crew(self) -> Crew:    """创建研究团队"""    return Crew(      agents=self.agents,      tasks=self.tasks,      process=Process.sequential,      verbose=True,    )` |
| :---- |

这段代码为一组 AI Agent 设置了一个顺序工作流，它们按特定顺序处理任务列表，并启用详细日志记录以监控其进度。

其他 Agent 开发框架

**Microsoft AutoGen**：AutoGen 是一个以编排多个 Agent 通过对话解决任务为中心的框架。其架构使具有不同能力的 Agent 能够交互，允许复杂的问题分解和协作解决。AutoGen 的主要优势是其灵活的、对话驱动的方法，支持动态和复杂的多 Agent 交互。然而，这种对话范式可能导致执行路径不那么可预测，并且可能需要复杂的提示词工程来确保任务高效收敛。

**LlamaIndex**：LlamaIndex 从根本上是一个数据框架，旨在将大语言模型与外部和私有数据源连接。它擅长创建复杂的数据摄取和检索管道，这对于构建能够执行 RAG 的知识型 Agent 至关重要。虽然其数据索引和查询能力对于创建上下文感知 Agent 非常强大，但与以 Agent 为先的框架相比，其用于复杂 agentic 控制流和多 Agent 编排的原生工具开发较少。当核心技术挑战是数据检索和综合时，LlamaIndex 是最佳选择。

**Haystack**：Haystack 是一个开源框架，专为构建由语言模型驱动的可扩展且生产就绪的搜索系统而设计。其架构由模块化、可互操作的节点组成，这些节点形成文档检索、问答和摘要的管道。Haystack 的主要优势是其对大规模信息检索任务的性能和可扩展性的关注，使其适合企业级应用。潜在的权衡是，其针对搜索管道优化的设计在实现高度动态和创造性的 agentic 行为时可能更加刚性。

**MetaGPT**：MetaGPT 通过基于预定义的标准操作程序（SOP）集分配角色和任务来实现多 Agent 系统。该框架将 Agent 协作结构化，以模拟软件开发公司，Agent 承担产品经理或工程师等角色来完成复杂任务。这种 SOP 驱动的方法产生高度结构化和连贯的输出，这对于代码生成等专业领域是一个显著优势。该框架的主要限制是其高度专业化，使其对其核心设计之外的通用 agentic 任务的适应性较差。

**SuperAGI**：SuperAGI 是一个开源框架，旨在为自主 Agent 提供完整的生命周期管理系统。它包括 Agent 配置、监控和图形界面等功能，旨在增强 Agent 执行的可靠性。关键优势是其对生产就绪的关注，具有处理循环等常见故障模式的内置机制，并提供对 Agent 性能的可观察性。潜在的缺点是，与更轻量级的基于库的框架相比，其全面的平台方法可能引入更多的复杂性和开销。

**Semantic Kernel**：由 Microsoft 开发，Semantic Kernel 是一个 SDK，通过"插件"和"规划器"系统将大语言模型与传统编程代码集成。它允许 LLM 调用原生函数并编排工作流，有效地将模型视为更大软件应用程序中的推理引擎。其主要优势是与现有企业代码库的无缝集成，特别是在 .NET 和 Python 环境中。与更直接的 Agent 框架相比，其插件和规划器架构的概念开销可能呈现更陡峭的学习曲线。

**Strands Agents**：AWS 的轻量级灵活 SDK，使用模型驱动的方法来构建和运行 AI Agent。它设计简单且可扩展，支持从基本对话助手到复杂的多 Agent 自主系统的一切。该框架与模型无关，为各种 LLM 提供商提供广泛支持，并包括与 MCP 的原生集成，以便轻松访问外部工具。其核心优势是简单性和灵活性，具有易于入门的可定制 Agent 循环。潜在的权衡是，其轻量级设计意味着开发者可能需要构建更多周边的运营基础设施，例如高级监控或生命周期管理系统，而更全面的框架可能会提供开箱即用的功能。

结论

Agentic 框架的格局提供了多样化的工具，从用于定义 Agent 逻辑的低级库到用于编排多 Agent 协作的高级平台。在基础层面，LangChain 支持简单的线性工作流，而 LangGraph 引入了有状态的循环图以实现更复杂的推理。像 CrewAI 和 Google 的 ADK 这样的高级框架将重点转移到编排具有预定义角色的 Agent 团队，而 LlamaIndex 等其他框架则专注于数据密集型应用。这种多样性为开发者提供了基于图的系统的细粒度控制和更具主观性平台的简化开发之间的核心权衡。因此，选择正确的框架取决于应用程序是需要简单序列、动态推理循环还是受管理的专家团队。最终，这个不断发展的生态系统使开发者能够通过选择其项目所需的精确抽象级别来构建日益复杂的 AI 系统。

参考文献

1. LangChain, [https://www.langchain.com/](https://www.langchain.com/)   
2. LangGraph, [https://www.langchain.com/langgraph](https://www.langchain.com/langgraph)   
3. Google's ADK, [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)   
4. Crew.AI, [https://docs.crewai.com/en/introduction](https://docs.crewai.com/en/introduction) 