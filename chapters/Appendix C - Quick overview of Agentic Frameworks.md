# 附录 C - Agentic 框架快速概览

## LangChain

LangChain 是一个用于开发由大语言模型驱动的应用程序的框架。其核心优势在于 LangChain 表达式语言（LCEL），它允许你将组件通过"管道"操作符连接成链。这种设计创建了清晰的线性序列，其中每一步的输出自动成为下一步的输入。该框架专为有向无环图（DAG）工作流构建，意味着处理流程单向流动且无循环。

适用场景：

* 简单 RAG：检索文档，构建提示，从 LLM 获取答案。
* 文本摘要：接收用户文本，输入至摘要提示，返回摘要结果。
* 数据提取：从文本块中提取结构化数据（如 JSON 格式）。

Python

```python
## 一个简单的 LCEL 链概念示例
## （此为示意性代码，展示流程结构）
chain = prompt | model | output_parse
```

### LangGraph

LangGraph 是构建于 LangChain 之上的库，专为处理更高级的 Agentic 系统设计。它允许你将工作流定义为包含节点（函数或 LCEL 链）和边（条件逻辑）的图结构。其主要优势在于支持循环创建，使应用程序能够循环执行、重试操作或以灵活顺序调用工具，直至任务完成。该库显式管理应用程序状态，状态在节点间传递并在整个流程中持续更新。

适用场景：

* 多 Agent 系统：监督 Agent 将任务路由至专业化工作 Agent，可能循环执行直至目标达成。
* 规划与执行 Agent：Agent 制定计划，执行步骤，随后基于结果循环反馈以更新计划。
* 人机协同：图结构可等待人工输入，再决定后续执行节点。

| 特性 | LangChain | LangGraph |
| :---- | :---- | :---- |
| 核心抽象 | 链（使用 LCEL） | 节点图 |
| 工作流类型 | 线性（有向无环图） | 循环（支持循环的图） |
| 状态管理 | 通常单次运行无状态 | 显式且持久的状态对象 |
| 主要用途 | 简单、可预测的序列 | 复杂、动态、有状态的 Agent |

### 如何选择？

* 当应用程序具备清晰、可预测的线性步骤流程时，选择 LangChain。若你能定义从 A 到 B 再到 C 的直连过程而无需回环，则采用 LCEL 的 LangChain 是理想工具。
* 当应用程序需进行推理、规划或循环操作时，选择 LangGraph。若你的 Agent 需使用工具、反思结果并可能尝试不同策略，则需借助 LangGraph 的循环和有状态特性。

Python

```python
## 图状态
class State(TypedDict):
    topic: str
    joke: str
    story: str
    poem: str
    combined_output: str

## 节点
def call_llm_1(state: State):
    """第一次 LLM 调用以生成初始笑话"""
    msg = llm.invoke(f"Write a joke about {state['topic']}")
    return {"joke": msg.content}

def call_llm_2(state: State):
    """第二次 LLM 调用以生成故事"""
    msg = llm.invoke(f"Write a story about {state['topic']}")
    return {"story": msg.content}

def call_llm_3(state: State):
    """第三次 LLM 调用以生成诗歌"""
    msg = llm.invoke(f"Write a poem about {state['topic']}")
    return {"poem": msg.content}

def aggregator(state: State):
    """将笑话和故事组合成单个输出"""
    combined = f"Here's a story, joke, and poem about {state['topic']}!\n\n"
    combined += f"STORY:\n{state['story']}\n\n"
    combined += f"JOKE:\n{state['joke']}\n\n"
    combined += f"POEM:\n{state['poem']}"
    return {"combined_output": combined}

## 构建工作流
parallel_builder = StateGraph(State)

## 添加节点
parallel_builder.add_node("call_llm_1", call_llm_1)
parallel_builder.add_node("call_llm_2", call_llm_2)
parallel_builder.add_node("call_llm_3", call_llm_3)
parallel_builder.add_node("aggregator", aggregator)

## 添加边来连接节点
parallel_builder.add_edge(START, "call_llm_1")
parallel_builder.add_edge(START, "call_llm_2")
parallel_builder.add_edge(START, "call_llm_3")
parallel_builder.add_edge("call_llm_1", "aggregator")
parallel_builder.add_edge("call_llm_2", "aggregator")
parallel_builder.add_edge("call_llm_3", "aggregator")
parallel_builder.add_edge("aggregator", END)

parallel_workflow = parallel_builder.compile()

## 显示工作流
display(Image(parallel_workflow.get_graph().draw_mermaid_png()))

## 调用
state = parallel_workflow.invoke({"topic": "cats"})
print(state["combined_output"])
```

这段代码定义并运行了一个并行操作的 LangGraph 工作流。其主要目的是同时生成关于给定主题的笑话、故事和诗歌，然后将它们组合成单个格式化的文本输出。

## Google's ADK

Google 的 Agent 开发工具包（ADK）提供了一个高级、结构化的框架，用于构建和部署由多个交互式 AI Agent 组成的应用程序。与 LangChain 和 LangGraph 相比，它提供了一个更具指导性和生产就绪的系统来编排 Agent 协作，而非提供 Agent 内部逻辑的基础构建块。

LangChain 在最基础层面运作，提供组件和标准化接口以创建操作序列，例如调用模型并解析其输出。LangGraph 通过引入更灵活强大的控制流对此进行扩展；它将 Agent 工作流视为有状态图。使用 LangGraph，开发者显式定义节点（函数或工具）和边（决定执行路径）。这种图结构支持复杂循环推理，系统可循环执行、重试任务，并基于节点间传递的显式管理状态对象做出决策。它为开发者提供了对单个 Agent 认知过程的细粒度控制，或从第一性原理构建多 Agent 系统的能力。

Google 的 ADK 抽象了大部分此类低级图构建工作。ADK 不要求开发者定义每个节点和边，而是为多 Agent 交互提供预构建的架构模式。例如，ADK 包含 SequentialAgent 或 ParallelAgent 等内置 Agent 类型，它们自动管理不同 Agent 间的控制流。其架构围绕 Agent"团队"概念设计，通常由主 Agent 将任务委派给专业化子 Agent。状态和会话管理由框架更隐式地处理，提供了比 LangGraph 显式状态传递更连贯但精细度稍低的方法。因此，若将 LangGraph 比作提供详细工具以设计单个机器人或团队复杂接线的工具箱，Google 的 ADK 则如同一个工厂装配线，旨在构建和管理一支已具备协同工作能力的机器人舰队。

Python

```python
from google.adk.agents import LlmAgent
from google.adk.tools import google_Search

dice_agent = LlmAgent(
    model="gemini-2.0-flash-exp",
    name="question_answer_agent",
    description="一个能回答问题的有用助手 Agent。",
    instruction="""使用谷歌搜索响应查询""",
    tools=[google_search],
)
```

此代码创建了一个搜索增强型 Agent。当该 Agent 收到问题时，不会仅依赖其既有知识。相反，遵循其指令，它将使用 Google 搜索工具从网络查找相关实时信息，并据此构建答案。

Crew.AI

CrewAI 提供了一个编排框架，通过聚焦协作角色与结构化流程来构建多 Agent 系统。它在比基础工具包更高的抽象层级运作，提供模拟人类团队的概念模型。开发者无需将逻辑细粒度流程定义为图，而是定义参与者及其任务分配，由 CrewAI 管理其交互。

该框架核心组件包括 Agent、Task 和 Crew。Agent 不仅由功能定义，还通过角色、目标和背景故事等角色特征来定义，这些特征指导其行为与沟通风格。Task 是具备明确描述和预期输出的离散工作单元，分配给特定 Agent。Crew 是包含 Agent 和 Task 列表的协调单元，执行预定义的 Process。此流程决定工作流模式，通常为顺序型（一个任务的输出成为下一任务的输入）或层级型（经理型 Agent 委派任务并协调其他 Agent 间的工作流）。

与其他框架相比，CrewAI 定位独特。它脱离了 LangGraph 的低层级、显式状态管理与控制流（后者要求开发者连接每个节点与条件边）。开发者不是构建状态机，而是设计团队章程。尽管 Google 的 ADK 为整个 Agent 生命周期提供了全面、生产就绪的平台，CrewAI 则专注于 Agent 协作逻辑与专家团队模拟。

Python

```python
@crew
def crew(self) -> Crew:
    """创建研究团队"""
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        process=Process.sequential,
        verbose=True,
    )
```

此代码为 AI Agent 组配置了顺序工作流，Agent 按特定顺序处理任务列表，并启用详细日志以监控进度。

其他 Agent 开发框架

**Microsoft AutoGen**：AutoGen 是一个以对话方式编排多 Agent 解决任务为核心的框架。其架构使具备不同能力的 Agent 能够交互，支持复杂问题分解与协作解决。AutoGen 主要优势在于其灵活的对话驱动方法，可应对动态复杂的多 Agent 交互。然而，这种对话范式可能导致执行路径预测性降低，且需复杂提示工程以确保任务高效收敛。

**LlamaIndex**：LlamaIndex 本质上是数据框架，旨在连接大语言模型与外部及私有数据源。它擅长构建复杂的数据摄取与检索管道，这对创建能执行 RAG 的知识型 Agent 至关重要。尽管其数据索引与查询能力对构建情境感知 Agent 极为强大，但与 Agent 优先框架相比，其在复杂 agentic 控制流和多 Agent 编排方面的原生工具较少。当核心技术挑战为数据检索与综合时，LlamaIndex 是最佳选择。

**Haystack**：Haystack 是专为构建语言模型驱动的可扩展、生产就绪搜索系统而设计的开源框架。其架构由模块化、可互操作的节点组成，这些节点构成文档检索、问答和摘要的管道。Haystack 主要优势在于其对大规模信息检索任务性能与可扩展性的专注，使其适用于企业级应用。潜在权衡在于，其针对搜索管道优化的设计在实现高度动态和创造性 agentic 行为时可能较为僵化。

**MetaGPT**：MetaGPT 通过基于预定义标准操作程序（SOP）分配角色和任务来实现多 Agent 系统。该框架将 Agent 协作结构化以模拟软件开发公司，Agent 承担产品经理或工程师等角色完成复杂任务。这种 SOP 驱动方法产生高度结构化且连贯的输出，对代码生成等专业领域是显著优势。该框架主要局限在于其高度专业化，使其在核心设计范畴外的通用 agentic 任务适应性较弱。

**SuperAGI**：SuperAGI 是旨在为自主 Agent 提供完整生命周期管理系统的开源框架。它包括 Agent 配置、监控和图形界面等功能，旨在提升 Agent 执行可靠性。关键优势在于其对生产就绪性的关注，具备处理循环等常见故障模式的内置机制，并提供 Agent 性能可观测性。潜在缺点在于，与更轻量级库框架相比，其全面平台方法可能引入更多复杂性与开销。

**Semantic Kernel**：由 Microsoft 开发，Semantic Kernel 是通过"插件"和"规划器"系统将大语言模型与传统编程代码集成的 SDK。它允许 LLM 调用原生函数并编排工作流，有效将模型视为大型软件应用中的推理引擎。其主要优势是与现有企业代码库（尤其在 .NET 和 Python 环境）的无缝集成。其插件与规划器架构的概念开销可能带来比更直接 Agent 框架更陡峭的学习曲线。

**Strands Agents**：AWS 的轻量级灵活 SDK，采用模型驱动方法构建和运行 AI Agent。其设计简洁且可扩展，支持从基础对话助手到复杂多 Agent 自主系统的各类场景。该框架与模型无关，广泛支持多种 LLM 提供商，并包含与 MCP 的原生集成以便轻松访问外部工具。其核心优势是简洁性与灵活性，提供易于上手的可定制 Agent 循环。潜在权衡在于，其轻量级设计意味着开发者可能需要构建更多周边运营基础设施（如高级监控或生命周期管理系统），而更全面框架可能提供开箱即用功能。

结论

Agentic 框架生态提供了多样化工具，涵盖从定义 Agent 逻辑的低级库到编排多 Agent 协作的高级平台。在基础层，LangChain 支持简单线性工作流，而 LangGraph 引入有状态循环图以实现更复杂推理。如 CrewAI 和 Google ADK 等高级框架将重心转向编排具预定义角色的 Agent 团队，而 LlamaIndex 等其他框架则专注数据密集型应用。这种多样性为开发者带来了基于图系统的细粒度控制与更具指导性平台的简化开发之间的核心权衡。因此，框架选择取决于应用需求：简单序列、动态推理循环还是受管专家团队。最终，这一不断演进的技术生态系统使开发者能通过选择项目所需的精确抽象级别，构建日益复杂的 AI 系统。

参考文献

1. LangChain, [https://www.langchain.com/](https://www.langchain.com/)   
2. LangGraph, [https://www.langchain.com/langgraph](https://www.langchain.com/langgraph)   
3. Google's ADK, [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)   
4. Crew.AI, [https://docs.crewai.com/en/introduction](https://docs.crewai.com/en/introduction) 