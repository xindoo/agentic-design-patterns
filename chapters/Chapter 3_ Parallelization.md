# 第 3 章：并行化

# 并行化模式概述

在前面的章节中，我们探讨了用于顺序工作流的提示词链和用于动态决策和不同路径之间转换的路由。虽然这些模式是必不可少的，但许多复杂的 Agent 任务涉及可以*同时*执行而不是一个接一个执行的多个子任务。这就是**并行化**模式变得至关重要的地方。

并行化涉及并发执行多个组件，例如 LLM 调用、工具使用，甚至整个子 Agent（见图 1）。并行执行不是等待一个步骤完成后再开始下一个步骤，而是允许独立任务同时运行，显著减少可分解为独立部分的任务的总执行时间。

考虑一个设计用于研究主题并总结其发现的 Agent。顺序方法可能是：

1. 搜索来源 A。
2. 总结来源 A。
3. 搜索来源 B。
4. 总结来源 B。
5. 从摘要 A 和 B 综合最终答案。

并行方法可以改为：

1. 同时搜索来源 A *和*搜索来源 B。
2. 一旦两个搜索都完成，同时总结来源 A *和*总结来源 B。
3. 从摘要 A 和 B 综合最终答案（此步骤通常是顺序的，等待并行步骤完成）。

核心思想是识别工作流中不依赖于其他部分输出的部分并并行执行它们。当处理具有延迟的外部服务（如 API 或数据库）时，这特别有效，因为您可以并发发出多个请求。

实现并行化通常需要支持异步执行或多线程/多进程的框架。现代 Agent 框架在设计时考虑了异步操作，允许您轻松定义可以并行运行的步骤。

![][image1]

图 1. 带有子 Agent 的并行化示例

像 LangChain、LangGraph 和 Google ADK 这样的框架提供了并行执行的机制。在 LangChain 表达式语言（LCEL）中，您可以通过使用运算符（如 | 用于顺序）组合可运行对象来实现并行执行，并通过构建您的链或图以使分支并发执行。LangGraph 凭借其图结构，允许您定义可以从单个状态转换执行的多个节点，有效地在工作流中启用并行分支。Google ADK 提供了强大的原生机制来促进和管理 Agent 的并行执行，显著提高了复杂多 Agent 系统的效率和可扩展性。ADK 框架内的这种固有能力允许开发人员设计和实现多个 Agent 可以并发操作而不是顺序操作的解决方案。

并行化模式对于提高 Agent 系统的效率和响应性至关重要，特别是在处理涉及多个独立查找、计算或与外部服务交互的任务时。这是优化复杂 Agent 工作流性能的关键技术。

# 实际应用与用例

并行化是在各种应用程序中优化 Agent 性能的强大模式：

1. 信息收集和研究：  
同时从多个来源收集信息是经典用例。

* **用例：** 研究公司的 Agent。
  * **并行任务：** 同时搜索新闻文章、提取股票数据、检查社交媒体提及和查询公司数据库。
  * **好处：** 比顺序查找更快地收集全面视图。

2. 数据处理和分析：  
并发应用不同的分析技术或处理不同的数据段。

* **用例：** 分析客户反馈的 Agent。
  * **并行任务：** 在一批反馈条目中同时运行情感分析、提取关键词、分类反馈和识别紧急问题。
  * **好处：** 快速提供多方面分析。

3. 多 API 或工具交互：  
调用多个独立的 API 或工具以收集不同类型的信息或执行不同的操作。

* **用例：** 旅行规划 Agent。
  * **并行任务：** 并发检查航班价格、搜索酒店可用性、查找当地活动和查找餐厅推荐。
  * **好处：** 更快呈现完整的旅行计划。

4. 具有多个组件的内容生成：  
并行生成复杂内容的不同部分。

* **用例：** 创建营销电子邮件的 Agent。
  * **并行任务：** 同时生成主题行、起草电子邮件正文、查找相关图像和创建号召性用语按钮文本。
  * **好处：** 更有效地组装最终电子邮件。

5. 验证和确认：  
并发执行多个独立检查或验证。

* **用例：** 验证用户输入的 Agent。
  * **并行任务：** 同时检查电子邮件格式、验证电话号码、根据数据库验证地址和检查亵渎内容。
  * **好处：** 更快地提供输入有效性反馈。

6. 多模态处理：  
并发处理相同输入的不同模态（文本、图像、音频）。

* **用例：** 分析带有文本和图像的社交媒体帖子的 Agent。
  * **并行任务：** 同时分析文本的情感和关键词*并*分析图像的对象和场景描述。
  * **好处：** 更快地整合来自不同模态的见解。

7. A/B 测试或多选项生成：  
并行生成响应或输出的多个变体以选择最佳变体。

* **用例：** 生成不同创意文本选项的 Agent。
  * **并行任务：** 使用稍微不同的提示词或模型同时为文章生成三个不同的标题。
  * **好处：** 允许快速比较和选择最佳选项。

并行化是 Agent 设计中的基本优化技术，允许开发人员通过利用独立任务的并发执行来构建更高性能和响应更快的应用程序。

# 实操代码示例（LangChain）

LangChain 框架内的并行执行由 LangChain 表达式语言（LCEL）促进。主要方法涉及在字典或列表构造中构建多个可运行组件。当此集合作为输入传递给链中的后续组件时，LCEL 运行时并发执行包含的可运行对象。

在 LangGraph 的上下文中，此原理应用于图的拓扑。并行工作流通过架构图来定义，使得多个节点（缺乏直接顺序依赖关系）可以从单个公共节点启动。这些并行路径独立执行，然后它们的结果可以在图中的后续汇聚点聚合。

以下实现演示了使用 LangChain 框架构建的并行处理工作流。此工作流设计用于响应单个用户查询并发执行两个独立操作。这些并行过程被实例化为不同的链或函数，它们各自的输出随后被聚合成统一的结果。

此实现的先决条件包括安装必需的 Python 包，例如 langchain、langchain-community 和模型提供商库（如 langchain-openai）。此外，必须在本地环境中配置所选语言模型的有效 API 密钥以进行身份验证。

```python
import os
import asyncio
from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable, RunnableParallel, RunnablePassthrough

# --- 配置 ---
# 确保设置了您的 API 密钥环境变量（例如，OPENAI_API_KEY）
try:
   llm: Optional[ChatOpenAI] = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
except Exception as e:
   print(f"初始化语言模型时出错: {e}")
   llm = None

# --- 定义独立链 ---
# 这三个链代表可以并行执行的不同任务。
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

# --- 构建并行 + 综合链 ---
# 1. 定义要并行运行的任务块。这些的结果，
#    以及原始主题，将被馈送到下一步。
map_chain = RunnableParallel(
   {
       "summary": summarize_chain,
       "questions": questions_chain,
       "key_terms": terms_chain,
       "topic": RunnablePassthrough(),  # 传递原始主题
   }
)

# 2. 定义将组合并行结果的最终综合提示词。
synthesis_prompt = ChatPromptTemplate.from_messages([
   ("system", """基于以下信息：
    摘要：{summary}
    相关问题：{questions}
    关键术语：{key_terms}
    综合一个全面的答案。"""),
   ("user", "原始主题：{topic}")
])

# 3. 通过将并行结果直接管道化
#    到综合提示词，然后是 LLM 和输出解析器，构建完整链。
full_parallel_chain = map_chain | synthesis_prompt | llm | StrOutputParser()

# --- 运行链 ---
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

提供的 Python 代码实现了一个 LangChain 应用程序，旨在通过利用并行执行来高效处理给定主题。请注意，asyncio 提供并发性，而不是并行性。它通过使用事件循环在单个线程上实现这一点，该事件循环在任务空闲时（例如，等待网络请求时）智能地在任务之间切换。这创造了多个任务同时进行的效果，但代码本身仍然只由一个线程执行，受 Python 的全局解释器锁（GIL）约束。

代码首先从 langchain_openai 和 langchain_core 导入基本模块，包括语言模型、提示词、输出解析和可运行结构的组件。代码尝试初始化一个 ChatOpenAI 实例，特别是使用"gpt-4o-mini"模型，具有指定的温度以控制创造性。在语言模型初始化期间使用 try-except 块以增强稳健性。然后定义三个独立的 LangChain"链"，每个链设计用于对输入主题执行不同的任务。第一个链用于简洁地总结主题，使用包含主题占位符的系统消息和用户消息。第二个链配置为生成与主题相关的三个有趣问题。第三个链设置为从输入主题中识别 5 到 10 个关键术语，要求它们用逗号分隔。这些独立链中的每一个都由针对其特定任务定制的 ChatPromptTemplate 组成，然后是初始化的语言模型和用于将输出格式化为字符串的 StrOutputParser。

然后构建一个 RunnableParallel 块来捆绑这三个链，允许它们同时执行。此并行可运行对象还包括一个 RunnablePassthrough，以确保原始输入主题可用于后续步骤。为最终综合步骤定义了一个单独的 ChatPromptTemplate，将摘要、问题、关键术语和原始主题作为输入以生成全面的答案。完整的端到端处理链（名为 full_parallel_chain）是通过将 map_chain（并行块）排序到综合提示词，然后是语言模型和输出解析器来创建的。提供了一个异步函数 run_parallel_example 来演示如何调用此 full_parallel_chain。此函数将主题作为输入并使用 invoke 运行异步链。最后，标准 Python if __name__ == "__main__": 块显示了如何使用样本主题（在本例中为"太空探索的历史"）执行 run_parallel_example，使用 asyncio.run 管理异步执行。

本质上，此代码设置了一个工作流，其中对给定主题同时进行多个 LLM 调用（用于总结、问题和术语），然后最终 LLM 调用组合它们的结果。这展示了使用 LangChain 在 Agent 工作流中并行化的核心思想。

# 实操代码示例（Google ADK）

现在让我们将注意力转向在 Google ADK 框架内说明这些概念的具体示例。我们将研究如何应用 ADK 原语（如 ParallelAgent 和 SequentialAgent）来构建利用并发执行以提高效率的 Agent 流。

```python
from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search

GEMINI_MODEL="gemini-2.0-flash"

# --- 1. 定义研究员子 Agent（并行运行）---
# 研究员 1：可再生能源
researcher_agent_1 = LlmAgent(
    name="RenewableEnergyResearcher",
    model=GEMINI_MODEL,
    instruction="""你是一名专门研究能源的 AI 研究助理。研究"可再生能源"的最新进展。使用提供的 Google 搜索工具。简洁地总结你的主要发现（1-2 句话）。*只*输出摘要。""",
    description="研究可再生能源。",
    tools=[google_search],
    # 将结果存储在状态中供合并 Agent 使用
    output_key="renewable_energy_result"
)

# 研究员 2：电动汽车
researcher_agent_2 = LlmAgent(
    name="EVResearcher",
    model=GEMINI_MODEL,
    instruction="""你是一名专门研究交通的 AI 研究助理。研究"电动汽车技术"的最新发展。使用提供的 Google 搜索工具。简洁地总结你的主要发现（1-2 句话）。*只*输出摘要。""",
    description="研究电动汽车技术。",
    tools=[google_search],
    # 将结果存储在状态中供合并 Agent 使用
    output_key="ev_technology_result"
)

# 研究员 3：碳捕获
researcher_agent_3 = LlmAgent(
    name="CarbonCaptureResearcher",
    model=GEMINI_MODEL,
    instruction="""你是一名专门研究气候解决方案的 AI 研究助理。研究"碳捕获方法"的当前状态。使用提供的 Google 搜索工具。简洁地总结你的主要发现（1-2 句话）。*只*输出摘要。""",
    description="研究碳捕获方法。",
    tools=[google_search],
    # 将结果存储在状态中供合并 Agent 使用
    output_key="carbon_capture_result"
)

# --- 2. 创建 ParallelAgent（并发运行研究员）---
# 此 Agent 协调研究员的并发执行。
# 一旦所有研究员完成并将结果存储在状态中，它就完成。
parallel_research_agent = ParallelAgent(
    name="ParallelWebResearchAgent",
    sub_agents=[researcher_agent_1, researcher_agent_2, researcher_agent_3],
    description="并行运行多个研究 Agent 以收集信息。"
)

# --- 3. 定义合并 Agent（在并行 Agent *之后*运行）---
# 此 Agent 获取并行 Agent 存储在会话状态中的结果
# 并将它们综合成一个带有归属的单一结构化响应。
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
[*只*综合并详细说明上面提供的可再生能源输入摘要。]

### 电动汽车发现
（基于 EVResearcher 的发现）
[*只*综合并详细说明上面提供的电动汽车输入摘要。]

### 碳捕获发现
（基于 CarbonCaptureResearcher 的发现）
[*只*综合并详细说明上面提供的碳捕获输入摘要。]

### 总体结论
[提供一个简短的（1-2 句话）结论性陈述，*只*连接上面提供的发现。]

*只*输出遵循此格式的结构化报告。不要在此结构之外包含介绍性或结论性短语，并严格遵守仅使用提供的输入摘要内容。""",
    description="将并行 Agent 的研究发现组合成结构化的、引用的报告，严格基于提供的输入。",
    # 合并不需要工具
    # 这里不需要 output_key，因为其直接响应是序列的最终输出
)

# --- 4. 创建 SequentialAgent（协调整体流程）---
# 这是将运行的主 Agent。它首先执行 ParallelAgent
# 以填充状态，然后执行 MergerAgent 以产生最终输出。
sequential_pipeline_agent = SequentialAgent(
    name="ResearchAndSynthesisPipeline",
    # 首先运行并行研究，然后合并
    sub_agents=[parallel_research_agent, merger_agent],
    description="协调并行研究并综合结果。"
)

root_agent = sequential_pipeline_agent
```

此代码定义了一个用于研究和综合可持续技术进展信息的多 Agent 系统。它设置了三个 LlmAgent 实例作为专门的研究员。ResearcherAgent_1 专注于可再生能源，ResearcherAgent_2 研究电动汽车技术，ResearcherAgent_3 调查碳捕获方法。每个研究员 Agent 配置为使用 GEMINI_MODEL 和 google_search 工具。它们被指示简洁地总结其发现（1-2 句话）并使用 output_key 将这些摘要存储在会话状态中。

然后创建一个名为 ParallelWebResearchAgent 的 ParallelAgent 来并发运行这三个研究员 Agent。这允许并行进行研究，可能节省时间。一旦其所有子 Agent（研究员）完成并填充状态，ParallelAgent 就完成其执行。

接下来，定义一个 MergerAgent（也是 LlmAgent）来综合研究结果。此 Agent 将并行研究员存储在会话状态中的摘要作为输入。其指令强调输出必须严格基于提供的输入摘要，禁止添加外部知识。MergerAgent 旨在将组合的发现结构化为带有每个主题标题和简短总体结论的报告。

最后，创建一个名为 ResearchAndSynthesisPipeline 的 SequentialAgent 来协调整个工作流。作为主控制器，此主 Agent 首先执行 ParallelAgent 来执行研究。一旦 ParallelAgent 完成，SequentialAgent 然后执行 MergerAgent 来综合收集的信息。sequential_pipeline_agent 被设置为 root_agent，代表运行此多 Agent 系统的入口点。整个过程旨在有效地从多个来源并行收集信息，然后将其组合成单一的结构化报告。

# 概览

**什么：** 许多 Agent 工作流涉及必须完成才能实现最终目标的多个子任务。纯顺序执行，其中每个任务等待前一个任务完成，通常是低效和缓慢的。当任务依赖于外部 I/O 操作（如调用不同的 API 或查询多个数据库）时，这种延迟成为重大瓶颈。如果没有并发执行机制，总处理时间是所有单个任务持续时间的总和，阻碍了系统的整体性能和响应性。

**为什么：** 并行化模式通过启用独立任务的同时执行提供了标准化解决方案。它通过识别工作流的组件（如工具使用或 LLM 调用）来工作，这些组件不依赖于彼此的即时输出。像 LangChain 和 Google ADK 这样的 Agent 框架提供了内置构造来定义和管理这些并发操作。例如，主进程可以调用多个并行运行的子任务，并等待所有子任务完成后再继续下一步。通过同时而不是一个接一个地运行这些独立任务，此模式大大减少了总执行时间。

**经验法则：** 当工作流包含可以同时运行的多个独立操作时使用此模式，例如从多个 API 获取数据、处理不同的数据块或生成多个内容片段以供后续综合。

**视觉摘要**

**![][image2]**

图 2：并行化设计模式

# 关键要点

以下是关键要点：

* 并行化是一种并发执行独立任务以提高效率的模式。
* 当任务涉及等待外部资源（如 API 调用）时，它特别有用。
* 采用并发或并行架构会带来巨大的复杂性和成本，影响设计、调试和系统日志等关键开发阶段。
* 像 LangChain 和 Google ADK 这样的框架提供了定义和管理并行执行的内置支持。
* 在 LangChain 表达式语言（LCEL）中，RunnableParallel 是并行运行多个可运行对象的关键构造。
* Google ADK 可以通过 LLM 驱动的委托促进并行执行，其中协调器 Agent 的 LLM 识别独立的子任务并触发专门子 Agent 的并发处理。
* 并行化有助于减少整体延迟，使 Agent 系统对复杂任务更具响应性。

# 结论

并行化模式是通过并发执行独立子任务来优化计算工作流的方法。这种方法减少了整体延迟，特别是在涉及多个模型推理或对外部服务的调用的复杂操作中。

框架提供了实现此模式的不同机制。在 LangChain 中，使用 RunnableParallel 等构造显式定义和同时执行多个处理链。相反，像 Google Agent Developer Kit (ADK) 这样的框架可以通过多 Agent 委托实现并行化，其中主协调器模型将不同的子任务分配给可以并发操作的专门 Agent。

通过将并行处理与顺序（链接）和条件（路由）控制流集成，可以构建能够有效管理各种复杂任务的复杂、高性能计算系统。

# 参考文献

以下是有关并行化模式和相关概念的一些进一步阅读资源：

1. LangChain Expression Language (LCEL) Documentation (Parallelism): [https://python.langchain.com/docs/concepts/lcel/](https://python.langchain.com/docs/concepts/lcel/)
2. Google Agent Developer Kit (ADK) Documentation (Multi-Agent Systems): [https://google.github.io/adk-docs/agents/multi-agents/](https://google.github.io/adk-docs/agents/multi-agents/)
3. Python asyncio Documentation: [https://docs.python.org/3/library/asyncio.html](https://docs.python.org/3/library/asyncio.html)

[image1]: ../images/chapter-3/image1.png

[image2]: ../images/chapter-3/image2.png