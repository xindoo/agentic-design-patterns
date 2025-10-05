# 第 3 章：并行化

## 并行化模式概述

在前面的章节中，我们探讨了用于顺序工作流的提示链和用于动态决策及不同路径间转换的路由。虽然这些模式不可或缺，但许多复杂的 Agent 任务涉及多个可*同时*执行而非顺序执行的子任务。这正是**并行化**模式变得至关重要的场景。

并行化涉及并发执行多个组件，包括 LLM 调用、工具使用乃至整个子 Agent（见图 1）。与等待一个步骤完成再开始下一个步骤不同，并行执行允许独立任务同时运行，从而显著缩短可分解为独立部分的任务的总执行时间。

设想一个旨在研究主题并总结其发现的 Agent。顺序方法可能如下：

1. 搜索来源 A
2. 总结来源 A
3. 搜索来源 B
4. 总结来源 B
5. 基于摘要 A 和 B 合成最终答案

而并行方法则可改为：

1. *同时*搜索来源 A 和来源 B
2. 两个搜索完成后，*同时*总结来源 A 和来源 B
3. 基于摘要 A 和 B 合成最终答案（此步骤通常为顺序执行，需等待并行步骤完成）

其核心思想在于识别工作流中不依赖其他部分输出的环节并并行执行。这在处理具有延迟的外部服务（如 API 或数据库）时尤其有效，因为您可以并发发出多个请求。

实现并行化通常需要支持异步执行或多线程/多进程的框架。现代 Agent 框架在设计时已充分考虑异步操作，使您能够轻松定义可并行运行的步骤。

![][image1]

图 1. 带有子 Agent 的并行化示例

像 LangChain、LangGraph 和 Google ADK 这样的框架提供了并行执行机制。在 LangChain 表达式语言（LCEL）中，您可以通过使用运算符（如 | 用于顺序）组合可运行对象来实现并行执行，并通过构建支持分支并发执行的链或图。LangGraph 凭借其图结构，允许您定义可从单个状态转换执行的多个节点，从而在工作流中有效启用并行分支。Google ADK 提供了强大的原生机制来促进和管理 Agent 的并行执行，显著提升了复杂多 Agent 系统的效率和可扩展性。ADK 框架的这一固有能力使开发人员能够设计并实现多个 Agent 并发而非顺序操作的解决方案。

并行化模式对于提升 Agent 系统的效率和响应能力至关重要，特别是在处理涉及多个独立查询、计算或与外部服务交互的任务时。这是优化复杂 Agent 工作流性能的关键技术。

## 实际应用与用例

并行化是优化 Agent 性能的强大模式，适用于多种应用场景：

1. 信息收集与研究：
同时从多个来源收集信息是经典用例。

* **用例：** 公司调研 Agent
  * **并行任务：** 同步搜索新闻文章、获取股票数据、监控社交媒体提及和查询公司数据库
  * **优势：** 相比顺序查询能更快获得全面视图

2. 数据处理与分析：
对数据的不同部分或应用不同分析技术进行并发处理

* **用例：** 客户反馈分析 Agent
  * **并行任务：** 对一批反馈条目同时执行情感分析、关键词提取、反馈分类和紧急问题识别
  * **优势：** 快速提供多维度分析结果

3. 多 API 或工具交互：
调用多个独立的 API 或工具以获取不同类型信息或执行不同操作

* **用例：** 旅行规划 Agent
  * **并行任务：** 并发查询航班价格、酒店可用性、当地活动和餐厅推荐
  * **优势：** 更快呈现完整的旅行方案

4. 多组件内容生成：
并行生成复杂内容的不同组成部分

* **用例：** 营销邮件创建 Agent
  * **并行任务：** 同时生成邮件主题、起草正文内容、查找相关图片和创建行动号召按钮文本
  * **优势：** 更高效地组装最终邮件

5. 验证与核实：
并发执行多个独立检查或验证操作

* **用例：** 用户输入验证 Agent
  * **并行任务：** 同时验证邮箱格式、手机号码、地址信息数据库匹配和不当内容检测
  * **优势：** 更快提供输入有效性反馈

6. 多模态处理：
并发处理同一输入的不同模态（文本、图像、音频）

* **用例：** 社交媒体帖子分析 Agent（包含文本和图像）
  * **并行任务：** 同时分析文本情感与关键词*并*识别图像中的对象和场景描述
  * **优势：** 更快速整合来自不同模态的洞察

7. A/B 测试或多选项生成：
并行生成多个响应或输出变体以选择最佳方案

* **用例：** 创意文本生成 Agent
  * **并行任务：** 使用略有不同的提示或模型同时为文章生成三个不同标题
  * **优势：** 便于快速比较并选择最佳选项

并行化是 Agent 设计中的基础优化技术，使开发人员能够通过利用独立任务的并发执行来构建更高性能和响应更快的应用程序。

## 实操代码示例（LangChain）

LangChain 框架中的并行执行由 LangChain 表达式语言（LCEL）实现。主要方法是在字典或列表结构中组织多个可运行组件。当该集合作为输入传递给链中的后续组件时，LCEL 运行时会并发执行其中包含的可运行对象。

在 LangGraph 中，这一原理应用于图的拓扑结构。并行工作流通过设计图结构来定义，使得多个无直接顺序依赖关系的节点可从单个公共节点启动。这些并行路径独立执行，其结果可在图中的后续汇聚点进行聚合。

以下实现展示了使用 LangChain 框架构建的并行处理工作流。该工作流设计用于响应单个用户查询并发执行多个独立操作。这些并行过程被实例化为不同的链或函数，各自的输出随后被聚合成统一结果。

此实现的先决条件包括安装必要的 Python 包，如 langchain、langchain-community 以及模型提供商库（如 langchain-openai）。此外，还需在本地环境中配置所选语言模型的有效 API 密钥以完成身份验证。

```python
import os
import asyncio
from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable, RunnableParallel, RunnablePassthrough

## --- 配置 ---
## 确保设置了您的 API 密钥环境变量（例如，OPENAI_API_KEY）
try:
    llm: Optional[ChatOpenAI] = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
except Exception as e:
    print(f"初始化语言模型时出错: {e}")
    llm = None

## --- 定义独立链 ---
## 这三个链代表可以并行执行的不同任务。
summarize_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "简洁地总结以下主题："),
        ("user", "{topic}")
    ])
    | llm
    | StrOutputParser()
)

questions_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "生成关于以下主题的三个有趣问题："),
        ("user", "{topic}")
    ])
    | llm
    | StrOutputParser()
)

terms_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "从以下主题中识别 5-10 个关键术语，用逗号分隔："),
        ("user", "{topic}")
    ])
    | llm
    | StrOutputParser()
)

## --- 构建并行 + 综合链 ---
## 1. 定义要并行运行的任务块。这些的结果，
##    以及原始主题，将被馈送到下一步。
map_chain = RunnableParallel(
    {
        "summary": summarize_chain,
        "questions": questions_chain,
        "key_terms": terms_chain,
        "topic": RunnablePassthrough(),  # 传递原始主题
    }
)

## 2. 定义将组合并行结果的最终综合提示词。
synthesis_prompt = ChatPromptTemplate.from_messages([
    ("system", """基于以下信息：
    摘要：{summary}
    相关问题：{questions}
    关键术语：{key_terms}
    综合一个全面的答案。"""),
    ("user", "原始主题：{topic}")
])

## 3. 通过将并行结果直接管道化
##    到综合提示词，然后是 LLM 和输出解析器，构建完整链。
full_parallel_chain = map_chain | synthesis_prompt | llm | StrOutputParser()

## --- 运行链 ---
async def run_parallel_example(topic: str) -> None:
    """
    异步调用具有特定主题的并行处理链
    并打印综合结果。
    参数：
        topic: 要由 LangChain 链处理的输入主题。
    """
    if not llm:
        print("LLM 未初始化。无法运行示例。")
        return
    
    print(f"\n--- 运行主题的并行 LangChain 示例：'{topic}' ---")
    try:
        # `ainvoke` 的输入是单个 'topic' 字符串，
        # 然后传递给 `map_chain` 中的每个可运行对象。
        response = await full_parallel_chain.ainvoke(topic)
        print("\n--- 最终响应 ---")
        print(response)
    except Exception as e:
        print(f"\n链执行期间发生错误：{e}")

if __name__ == "__main__":
    test_topic = "太空探索的历史"
    # 在 Python 3.7+ 中，asyncio.run 是运行异步函数的标准方式。
    asyncio.run(run_parallel_example(test_topic))
```

提供的 Python 代码实现了一个 LangChain 应用程序，旨在通过并行执行高效处理给定主题。请注意，asyncio 提供的是并发性而非真正的并行性。它通过事件循环在单线程上实现这一点，在任务空闲时（如等待网络请求）智能地在任务间切换。这创造了多个任务同时进行的效果，但代码实际上仍由单个线程执行，受 Python 全局解释器锁（GIL）限制。

代码首先从 langchain_openai 和 langchain_core 导入必要模块，包括语言模型、提示模板、输出解析器和可运行结构组件。代码尝试初始化 ChatOpenAI 实例，使用"gpt-4o-mini"模型并设置温度参数以控制创造性。语言模型初始化采用 try-except 块以确保健壮性。随后定义三个独立的 LangChain"链"，每个链设计用于对输入主题执行不同任务：第一个链负责简洁总结主题，第二个链生成与主题相关的三个有趣问题，第三个链从输入主题中识别 5-10 个关键术语并以逗号分隔。每个独立链都由针对特定任务定制的 ChatPromptTemplate、初始化的语言模型和用于字符串格式输出的 StrOutputParser 组成。

然后构建 RunnableParallel 块来捆绑这三个链以实现同时执行。此并行可运行对象还包含 RunnablePassthrough 以确保原始输入主题可用于后续步骤。为最终综合步骤定义了单独的 ChatPromptTemplate，接收摘要、问题、关键术语和原始主题作为输入以生成全面答案。完整的端到端处理链（full_parallel_chain）通过将 map_chain（并行块）连接到综合提示模板，再接入语言模型和输出解析器来创建。提供的异步函数 run_parallel_example 演示了如何调用此完整并行链，该函数接收主题作为输入并使用 invoke 运行异步链。最后，标准 Python if __name__ == "__main__": 块展示了如何使用示例主题"太空探索的历史"执行 run_parallel_example，通过 asyncio.run 管理异步执行。

本质上，此代码建立了一个工作流，对给定主题同时执行多个 LLM 调用（用于总结、生成问题和提取术语），最终通过另一个 LLM 调用整合结果。这展示了在 Agent 工作流中使用 LangChain 实现并行化的核心思想。

## 实操代码示例（Google ADK）

现在让我们关注 Google ADK 框架中说明这些概念的具体示例。我们将探讨如何应用 ADK 原语（如 ParallelAgent 和 SequentialAgent）来构建利用并发执行提升效率的 Agent 流程。

```python
from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search

GEMINI_MODEL = "gemini-2.0-flash"

## --- 1. 定义研究员子 Agent（并行运行）---
## 研究员 1：可再生能源
researcher_agent_1 = LlmAgent(
    name="RenewableEnergyResearcher",
    model=GEMINI_MODEL,
    instruction="""你是一名专门研究能源的 AI 研究助理。研究"可再生能源"的最新进展。使用提供的 Google 搜索工具。简洁地总结你的主要发现（1-2 句话）。*只*输出摘要。""",
    description="研究可再生能源。",
    tools=[google_search],
    # 将结果存储在状态中供合并 Agent 使用
    output_key="renewable_energy_result"
)

## 研究员 2：电动汽车
researcher_agent_2 = LlmAgent(
    name="EVResearcher",
    model=GEMINI_MODEL,
    instruction="""你是一名专门研究交通的 AI 研究助理。研究"电动汽车技术"的最新发展。使用提供的 Google 搜索工具。简洁地总结你的主要发现（1-2 句话）。*只*输出摘要。""",
    description="研究电动汽车技术。",
    tools=[google_search],
    # 将结果存储在状态中供合并 Agent 使用
    output_key="ev_technology_result"
)

## 研究员 3：碳捕获
researcher_agent_3 = LlmAgent(
    name="CarbonCaptureResearcher",
    model=GEMINI_MODEL,
    instruction="""你是一名专门研究气候解决方案的 AI 研究助理。研究"碳捕获方法"的当前状态。使用提供的 Google 搜索工具。简洁地总结你的主要发现（1-2 句话）。*只*输出摘要。""",
    description="研究碳捕获方法。",
    tools=[google_search],
    # 将结果存储在状态中供合并 Agent 使用
    output_key="carbon_capture_result"
)

## --- 2. 创建 ParallelAgent（并发运行研究员）---
## 此 Agent 协调研究员的并发执行。
## 一旦所有研究员完成并将结果存储在状态中，它就完成。
parallel_research_agent = ParallelAgent(
    name="ParallelWebResearchAgent",
    sub_agents=[researcher_agent_1, researcher_agent_2, researcher_agent_3],
    description="并行运行多个研究 Agent 以收集信息。"
)

## --- 3. 定义合并 Agent（在并行 Agent *之后*运行）---
## 此 Agent 获取并行 Agent 存储在会话状态中的结果
## 并将它们综合成一个带有归属的单一结构化响应。
merger_agent = LlmAgent(
    name="SynthesisAgent",
    model=GEMINI_MODEL,  # 或者如果需要，可以使用更强大的模型进行综合
    instruction="""你是一名负责将研究发现组合成结构化报告的 AI 助理。你的主要任务是综合以下研究摘要，清楚地将发现归属于其来源领域。使用每个主题的标题构建你的响应。确保报告连贯并平滑地整合关键点。
**关键：你的整个响应必须*完全*基于下面"输入摘要"中提供的信息。不要添加这些特定摘要中不存在的任何外部知识、事实或细节。**

**输入摘要：**
*   **可再生能源：**
    {renewable_energy_result}
*   **电动汽车：**
    {ev_technology_result}
*   **碳捕获：**
    {carbon_capture_result}

**输出格式：**
## 近期可持续技术进展摘要

### 可再生能源发现
（基于 RenewableEnergyResearcher 的发现）
[*仅*综合并详细说明上面提供的可再生能源输入摘要。]

### 电动汽车发现
（基于 EVResearcher 的发现）
[*仅*综合并详细说明上面提供的电动汽车输入摘要。]

### 碳捕获发现
（基于 CarbonCaptureResearcher 的发现）
[*仅*综合并详细说明上面提供的碳捕获输入摘要。]

### 总体结论
[提供一个简短的（1-2 句话）结论性陈述，*仅*连接上面提供的发现。]

*仅*输出遵循此格式的结构化报告。不要在此结构之外包含介绍性或结论性短语，并严格遵守仅使用提供的输入摘要内容。""",
    description="将并行 Agent 的研究发现组合成结构化的、引用的报告，严格基于提供的输入。",
    # 合并不需要工具
    # 这里不需要 output_key，因为其直接响应是序列的最终输出
)

## --- 4. 创建 SequentialAgent（协调整体流程）---
## 这是将运行的主 Agent。它首先执行 ParallelAgent
## 以填充状态，然后执行 MergerAgent 以产生最终输出。
sequential_pipeline_agent = SequentialAgent(
    name="ResearchAndSynthesisPipeline",
    # 首先运行并行研究，然后合并
    sub_agents=[parallel_research_agent, merger_agent],
    description="协调并行研究并综合结果。"
)

root_agent = sequential_pipeline_agent
```

此代码定义了一个用于研究和综合可持续技术进展信息的多 Agent 系统。系统设置了三个 LlmAgent 实例作为专门的研究员：ResearcherAgent_1 专注于可再生能源，ResearcherAgent_2 研究电动汽车技术，ResearcherAgent_3 调查碳捕获方法。每个研究员 Agent 配置使用 GEMINI_MODEL 和 google_search 工具，被指示用 1-2 句话简洁总结发现，并通过 output_key 将摘要存储在会话状态中。

随后创建名为 ParallelWebResearchAgent 的 ParallelAgent 来并发运行这三个研究员 Agent，实现并行研究以节省时间。当所有子 Agent（研究员）完成并填充状态后，ParallelAgent 结束执行。

接下来定义 MergerAgent（同样是 LlmAgent）来综合研究结果。该 Agent 以并行研究员存储在会话状态中的摘要作为输入，其指令强调输出必须严格基于提供的输入摘要，禁止添加外部知识。MergerAgent 旨在将组合的发现结构化为带有各主题标题和简短总体结论的报告。

最后创建名为 ResearchAndSynthesisPipeline 的 SequentialAgent 来协调整个工作流。作为主控制器，该主 Agent 首先执行 ParallelAgent 进行研究，待其完成后执行 MergerAgent 综合收集的信息。sequential_pipeline_agent 被设置为 root_agent，作为运行此多 Agent 系统的入口点。整个过程旨在高效地从多个来源并行收集信息，并将其整合为单一结构化报告。

## 概览

**是什么：** 许多 Agent 工作流包含多个必须完成才能达成最终目标的子任务。纯顺序执行（每个任务等待前一个完成）通常低效且缓慢。当任务依赖外部 I/O 操作（如调用不同 API 或查询多个数据库）时，这种延迟成为主要瓶颈。若无并发执行机制，总处理时间等于所有单个任务持续时间之和，严重制约系统整体性能和响应能力。

**为什么：** 并行化模式通过启用独立任务的同时执行提供标准化解决方案。该模式通过识别工作流中不依赖彼此即时输出的组件（如工具使用或 LLM 调用）来实现。像 LangChain 和 Google ADK 这样的 Agent 框架提供内置构造来定义和管理这些并发操作。例如，主进程可调用多个并行运行的子任务，等待所有子任务完成后再继续下一步。通过同时而非顺序执行这些独立任务，该模式显著减少总执行时间。

**经验法则：** 当工作流包含多个可同时运行的独立操作时使用此模式，例如从多个 API 获取数据、处理不同数据块或生成多个内容片段供后续综合。

**视觉摘要**

**![][image2]**

图 2：并行化设计模式

## 关键要点

以下是本章的核心要点：

* 并行化是一种通过并发执行独立任务来提高效率的模式
* 在涉及等待外部资源（如 API 调用）的任务中特别有效
* 采用并发或并行架构会引入显著复杂性和成本，影响设计、调试和系统日志等关键开发环节
* 像 LangChain 和 Google ADK 这样的框架提供定义和管理并行执行的内置支持
* 在 LangChain 表达式语言（LCEL）中，RunnableParallel 是并行运行多个可运行对象的关键构造
* Google ADK 可通过 LLM 驱动的委托实现并行执行，协调器 Agent 的 LLM 识别独立子任务并触发专门子 Agent 的并发处理
* 并行化有助于减少整体延迟，使 Agent 系统在处理复杂任务时更具响应性

## 结论

并行化模式是通过并发执行独立子任务来优化计算工作流的方法。该模式有效减少整体延迟，在涉及多个模型推理或对外部服务调用的复杂操作中尤为显著。

不同框架为此模式提供了不同的实现机制。在 LangChain 中，通过 RunnableParallel 等构造显式定义并同时执行多个处理链。而 Google Agent Developer Kit (ADK) 等框架则通过多 Agent 委托实现并行化，由主协调器模型将不同子任务分配给可并发操作的专门 Agent。

通过将并行处理与顺序（链式）和条件（路由）控制流相结合，可以构建能够高效管理各类复杂任务的复杂、高性能计算系统。

## 参考文献

以下是有关并行化模式和相关概念的一些进一步阅读资源：

1. LangChain Expression Language (LCEL) Documentation (Parallelism): [https://python.langchain.com/docs/concepts/lcel/](https://python.langchain.com/docs/concepts/lcel/)
2. Google Agent Developer Kit (ADK) Documentation (Multi-Agent Systems): [https://google.github.io/adk-docs/agents/multi-agents/](https://google.github.io/adk-docs/agents/multi-agents/)
3. Python asyncio Documentation: [https://docs.python.org/3/library/asyncio.html](https://docs.python.org/3/library/asyncio.html)

[image1]: ../images/chapter-3/image1.png

[image2]: ../images/chapter-3/image2.png