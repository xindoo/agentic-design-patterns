# 第 7 章：多智能体协作

虽然单体智能体对于定义明确的问题可能行之有效，但在面对复杂的多领域任务时，其能力往往受到限制。多智能体协作模式通过将系统构建为由不同专门化智能体组成的协作集合来解决这些限制。这种方法基于任务分解原则，将高级目标拆解为离散的子问题，然后将每个子问题分配给拥有最适合该任务的特定工具、数据访问或推理能力的智能体。

例如，一个复杂的研究查询可能被分解并分配给研究智能体进行信息检索、数据分析智能体进行处理，以及综合智能体生成最终输出。这种系统的效能不仅源于劳动分工，更关键的是依赖于智能体间的通信机制。这需要标准化的通信协议和共享本体，允许智能体交换数据、分配任务并协调其行动，以确保最终输出的连贯性。

这种分布式架构提供了几个优势，包括增强的模块化、可扩展性和稳健性，因为单个智能体故障不一定会导致整个系统故障。协作允许产生协同结果，其中多智能体系统的性能超过集合内任何单个智能体的能力。

## 多智能体协作模式概述

多智能体协作模式涉及设计系统，其中多个独立或半独立的智能体协同工作以实现共同目标。每个智能体有明确定义的角色、与总体目标一致的特定目标，并且可能访问不同的工具或知识库。此模式的力量在于这些智能体之间的协同作用。

协作可以采取各种形式：

* **顺序交接：** 一个智能体处理任务并将其输出传递给另一个智能体进行流水线中的下一步（类似于规划模式，但明确涉及不同的智能体）。
* **并行处理：** 多个智能体同时处理问题的不同部分，然后它们的结果稍后被组合。
* **辩论与共识：** 多个智能体协作，持有不同观点和信息来源的智能体通过讨论评估选项，最终达成共识或做出更明智的决策。
* **层次结构：** 管理者智能体根据工具访问或插件能力动态将任务委托给工作智能体，并综合其结果。每个智能体管理一组相关工具，而非由单个智能体处理所有事务。
* **专家团队：** 在不同领域具有专业知识的智能体（例如，研究员、作家、编辑）协作产生复杂输出。

* **批评者-审查者：** 一个智能体生成初始输出，如计划、草稿或答案。第二组智能体批判性地评估此输出是否符合政策、安全性、合规性、正确性、质量以及与组织目标的一致性。原始创建者或最终智能体根据反馈修订输出。此模式对于代码生成、研究写作、逻辑检查和确保道德一致性特别有效。这种方法的优势包括增强的稳健性、改进的质量以及减少幻觉或错误的可能性。

多智能体系统（见图1）从根本上包括界定智能体角色与职责、建立智能体交换信息的通信渠道，以及制定指导其协作努力的任务流或交互协议。

![][image1]

图 1：多智能体系统示例

像 CrewAI 和 Google ADK 这样的框架旨在通过提供智能体、任务及其交互程序的规范结构来促进这种范式。这种方法对于需要各种专业知识、包含多个离散阶段或能从并发处理和跨智能体确认中获益的挑战特别有效。

## 实际应用与用例

多智能体协作是一种适用于众多领域的强大模式：

* **复杂研究和分析：** 一组智能体协作完成研究项目。一个智能体搜索学术数据库，另一个总结发现，第三个识别趋势，第四个将信息综合成报告。这反映了人类研究团队可能如何运作。
* **软件开发：** 想象智能体构建软件。一个智能体是需求分析师，另一个是代码生成器，第三个是测试员，第四个是文档编写者。他们可以在彼此之间传递输出以构建和验证组件。
* **创意内容生成：** 创建营销活动可能涉及市场研究智能体、文案撰写智能体、图形设计智能体（使用图像生成工具）和社交媒体调度智能体，所有这些都在一起工作。
* **财务分析：** 多智能体可以分析金融市场。智能体可能专门获取股票数据、分析新闻情绪、执行技术分析和生成投资建议。
* **客户支持升级：** 前线支持智能体处理初始查询，在需要时将复杂问题升级给专家智能体（例如，技术专家或计费专家），展示基于问题复杂性的顺序交接。
* **供应链优化：** 多个智能体代表供应链中的不同节点（供应商、制造商、分销商）并协作优化库存水平、物流和调度以响应需求变化或中断。
* **网络分析与修复**：自主操作从多智能体协作中受益匪浅，特别是在故障定位方面。多个智能体协作分类和修复问题，建议最佳行动。这些智能体还可以与传统机器学习模型和工具集成，充分利用现有系统，同时提供生成式 AI 的优势。

界定专门智能体以及编排其相互关系的能力使开发人员能够构建展现增强模块化、可扩展性以及处理单个集成智能体无法处理的复杂性的系统。

## 多智能体协作：探索相互关系和通信结构

理解智能体交互和通信的复杂方式对于设计有效的多智能体系统至关重要。如图 2 所示，存在一系列相互关系和通信模型，从最简单的单智能体场景，到定制设计的协作框架。每个模型都呈现独特的优势和挑战，影响多智能体系统的整体稳健性和适应性。

**1. 单智能体：** 在最基本的层面上，"单智能体"在没有与其他实体直接交互或通信的情况下自主运行。虽然此模型易于实现和管理，但其能力固有地受到单个智能体的技能和资源的限制。它适用于可分解为独立子问题的任务，每个子问题都可由单个自给自足的智能体处理。

**2. 网络：** "网络"模型代表向协作迈出的重要一步，其中多个智能体以去中心化方式直接相互交互。通信通常以点对点方式进行，允许共享信息、资源甚至任务。此模型促进弹性，因为一个智能体的故障不一定会使整个系统瘫痪。然而，管理通信开销并确保大型非结构化网络中的连贯决策可能具有挑战性。

**3. 监督者：** 在"监督者"模型中，专用智能体（"监督者"）监督和协调一组下属智能体的活动。监督者充当通信、任务分配和冲突解决的中心枢纽。这种层次结构提供了清晰的权限线，可以简化管理和控制。然而，它引入了单点故障（监督者），如果监督者被大量下属或复杂任务压倒，可能会成为瓶颈。

**4. 监督者作为工具：** 此模型是"监督者"概念的细微扩展，其中监督者的角色不太关乎直接命令和控制，而更多关乎向其他智能体提供资源、指导或分析支持。监督者可能提供工具、数据或计算服务，使其他智能体更有效地执行其任务，而不必规定其每一个行动。这种方法旨在利用监督者的能力，而不施加严格的自上而下控制。

**5. 层次化：** "层次化"模型扩展了监督者概念，创建了多层组织结构。这涉及多个监督者级别，高级监督者监督低级监督者，最终在最低层有一组操作智能体。此结构非常适合可分解为子问题的复杂问题，每个子问题由层次结构的特定层管理。它提供了一种结构化的可扩展性和复杂性管理方法，允许在定义的边界内进行分布式决策。

![][image2]

图 2：智能体以各种方式进行通信和交互。

**6. 自定义：** "自定义"模型代表了多智能体设计的终极灵活性。它允许创建根据给定问题或应用程序的特定要求精确定制的独特相互关系和通信结构。这可能涉及结合前述模型元素的混合方法，或从环境的独特约束和机会中产生的全新设计。自定义模型通常源于需要针对特定性能指标进行优化、处理高度动态的环境或将特定领域知识纳入系统架构。设计和实现自定义模型通常需要对多智能体系统有深入理解，并仔细考虑通信协议、协调机制和涌现行为。

总之，为多智能体系统选择相互关系和通信模型是关键的设计决策。每个模型提供不同的优势和劣势，最佳选择取决于诸如任务复杂性、智能体数量、期望的自主程度、对稳健性的需求以及可接受的通信开销等因素。多智能体系统的未来进展可能会继续探索和完善这些模型，以及开发协作智能的新范式。

## 实操代码（Crew AI）

此 Python 代码使用 CrewAI 框架定义了一个 AI 驱动的团队来生成关于 AI 趋势的博客文章。它首先设置环境，从 .env 文件加载 API 密钥。应用程序的核心涉及定义两个智能体：一个研究员用于查找和总结 AI 趋势，一个作家用于基于研究创建博客文章。

相应地定义了两个任务：一个用于研究趋势，另一个用于撰写博客文章，写作任务依赖于研究任务的输出。然后将这些智能体和任务组装成一个团队，指定顺序流程，其中任务按顺序执行。团队使用智能体、任务和语言模型（特别是"gemini-2.0-flash"模型）初始化。主函数使用 kickoff() 方法执行此团队，编排智能体之间的协作以产生所需的输出。最后，代码打印团队执行的最终结果，即生成的博客文章。

```python
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI

def setup_environment():
    """加载环境变量并检查所需的 API 密钥。"""
    load_dotenv()
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("未找到 GOOGLE_API_KEY。请在您的 .env 文件中设置它。")

def main():
    """
    使用最新的 Gemini 模型初始化并运行用于内容创建的 AI 团队。
    """
    setup_environment()

    # 定义要使用的语言模型。
    # 更新为 Gemini 2.0 系列中的模型以获得更好的性能和功能。
    # 对于尖端（预览）功能，您可以使用 "gemini-2.5-flash"。
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    # 定义具有特定角色和目标的 Agent
    researcher = Agent(
        role='高级研究分析师',
        goal='查找并总结 AI 的最新趋势。',
        backstory="你是一位经验丰富的研究分析师，擅长识别关键趋势和综合信息。",
        verbose=True,
        allow_delegation=False,
    )

    writer = Agent(
        role='技术内容作家',
        goal='基于研究发现撰写清晰且引人入胜的博客文章。',
        backstory="你是一位熟练的作家，可以将复杂的技术主题转化为易于理解的内容。",
        verbose=True,
        allow_delegation=False,
    )

    # 为智能体定义任务
    research_task = Task(
        description="研究 2024-2025 年人工智能中出现的前 3 个趋势。重点关注实际应用和潜在影响。",
        expected_output="前 3 个 AI 趋势的详细摘要，包括关键点和来源。",
        agent=researcher,
    )

    writing_task = Task(
        description="基于研究发现撰写一篇 500 字的博客文章。文章应该引人入胜且易于普通读者理解。",
        expected_output="一篇关于最新 AI 趋势的完整 500 字博客文章。",
        agent=writer,
        context=[research_task],
    )

    # 创建团队
    blog_creation_crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        llm=llm,
        verbose=2 # 为详细的团队执行日志设置详细程度
    )

    # 执行团队
    print("## 使用 Gemini 2.0 Flash 运行博客创建团队... ##")
    try:
        result = blog_creation_crew.kickoff()
        print("\n------------------\n")
        print("## 团队最终输出 ##")
        print(result)
    except Exception as e:
        print(f"\n发生意外错误：{e}")

if __name__ == "__main__":
    main()
```

我们现在将深入研究 Google ADK 框架中的更多示例，特别强调层次化、并行和顺序协调范式，以及将智能体作为操作工具。

## 实操代码（Google ADK）

以下代码示例演示了通过创建父子关系在 Google ADK 中建立层次化智能体结构。代码定义了两种类型的智能体：LlmAgent 和从 BaseAgent 派生的自定义 TaskExecutor 智能体。TaskExecutor 专为特定的非 LLM 任务而设计，在此示例中，它只是生成"任务成功完成"事件。使用指定的模型和指令初始化名为 greeter 的 LlmAgent，以充当友好的欢迎者。自定义 TaskExecutor 实例化为 task_doer。创建名为 coordinator 的父 LlmAgent，也带有模型和指令。coordinator 的指令引导它将欢迎委托给 greeter，将任务执行委托给 task_doer。greeter 和 task_doer 作为子智能体添加到 coordinator，建立父子关系。然后代码断言此关系设置正确。最后，它打印一条消息，指示已成功创建智能体层次结构。

```python
from google.adk.agents import LlmAgent, BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from typing import AsyncGenerator

## 通过扩展 BaseAgent 正确实现自定义智能体
class TaskExecutor(BaseAgent):
    """具有自定义非 LLM 行为的专门智能体。"""
    name: str = "TaskExecutor"
    description: str = "执行预定义的任务。"

    async def _run_async_impl(self, context: InvocationContext) -> AsyncGenerator[Event, None]:
        """任务的自定义实现逻辑。"""
        # 这是您的自定义逻辑所在的地方。
        # 对于此示例，我们只会生成一个简单的事件。
        yield Event(author=self.name, content="任务成功完成。")

## 使用适当的初始化定义单个智能体
## LlmAgent 需要指定模型。
greeter = LlmAgent(
    name="Greeter",
    model="gemini-2.0-flash-exp",
    instruction="你是一个友好的欢迎者。"
)

task_doer = TaskExecutor() # 实例化我们的具体自定义智能体

## 创建父智能体并分配其子智能体
## 父智能体的描述和指令应该引导其委托逻辑。
coordinator = LlmAgent(
    name="Coordinator",
    model="gemini-2.0-flash-exp",
    description="可以欢迎用户并执行任务的协调者。",
    instruction="当被要求欢迎时，委托给 Greeter。当被要求执行任务时，委托给 TaskExecutor。",
    sub_agents=[
        greeter,
        task_doer
    ]
)

## ADK 框架自动建立父子关系。
## 如果在初始化后检查，这些断言将通过。
assert greeter.parent_agent == coordinator
assert task_doer.parent_agent == coordinator

print("智能体层次结构创建成功。")
```

此代码摘录说明了在 Google ADK 框架中使用 LoopAgent 建立迭代工作流。代码定义了两个智能体：ConditionChecker 和 ProcessingStep。ConditionChecker 是一个自定义智能体，检查会话状态中的"status"值。如果"status"为"completed"，ConditionChecker 触发升级事件以停止循环。否则，它生成事件以继续循环。ProcessingStep 是使用"gemini-2.0-flash-exp"模型的 LlmAgent。其指令是执行任务，如果是最后一步则将会话"status"设置为"completed"。创建名为 StatusPoller 的 LoopAgent。StatusPoller 配置为 max_iterations=10。StatusPoller 包括 ProcessingStep 和 ConditionChecker 实例作为子智能体。LoopAgent 将顺序执行子智能体最多 10 次迭代，如果 ConditionChecker 发现状态为"completed"则停止。

```python
import asyncio
from typing import AsyncGenerator
from google.adk.agents import LoopAgent, LlmAgent, BaseAgent
from google.adk.events import Event, EventActions
from google.adk.agents.invocation_context import InvocationContext

## 最佳实践：将自定义智能体实现为完整的、自描述的类。
class ConditionChecker(BaseAgent):
    """检查会话状态中"completed"状态的自定义智能体。"""
    name: str = "ConditionChecker"
    description: str = "检查流程是否完成并向循环发出停止信号。"

    async def _run_async_impl(
        self, context: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        """检查状态并生成事件以继续或停止循环。"""
        status = context.session.state.get("status", "pending")
        is_done = (status == "completed")

        if is_done:
            # 在满足条件时升级以终止循环。
            yield Event(author=self.name, actions=EventActions(escalate=True))
        else:
            # 生成简单事件以继续循环。
            yield Event(author=self.name, content="条件未满足，继续循环。")

## 更正：LlmAgent 必须有模型和清晰的指令。
process_step = LlmAgent(
    name="ProcessingStep",
    model="gemini-2.0-flash-exp",
    instruction="你是较长流程中的一步。执行你的任务。如果你是最后一步，通过将 'status' 设置为 'completed' 来更新会话状态。"
)

## LoopAgent 编排工作流。
poller = LoopAgent(
    name="StatusPoller",
    max_iterations=10,
    sub_agents=[
        process_step,
        ConditionChecker() # 实例化定义良好的自定义 Agent。
    ]
)

## 此轮询器现在将执行 'process_step'
## 然后执行 'ConditionChecker'
## 重复直到状态为 'completed' 或已经过
## 10 次迭代。
```

此代码摘录介绍了 Google ADK 中的 SequentialAgent 模式，专为构建线性工作流而设计。此代码使用 google.adk.agents 库定义顺序智能体管道。管道由两个智能体组成，step1 和 step2。step1 命名为"Step1_Fetch"，其输出将存储在会话状态中的键"data"下。step2 命名为"Step2_Process"，并被指示分析存储在 session.state["data"] 中的信息并提供摘要。名为"MyPipeline"的 SequentialAgent 编排这些子智能体的执行。当使用初始输入运行管道时，step1 将首先执行。来自 step1 的响应将保存到键"data"下的会话状态中。随后，step2 将执行，根据其指令利用 step1 放入状态的信息。此结构允许构建工作流，其中一个智能体的输出成为下一个智能体的输入。这是创建多步 AI 或数据处理管道的常见模式。

```python
from google.adk.agents import SequentialAgent, LlmAgent

## 此智能体的输出将保存到 session.state["data"]
step1 = LlmAgent(name="Step1_Fetch", output_key="data", model="gemini-2.0-flash-exp")

## 此智能体使用前一步的数据。
## 我们指示它如何查找和使用此数据。
step2 = LlmAgent(
    name="Step2_Process",
    instruction="分析在 state['data'] 中找到的信息并提供摘要。",
    model="gemini-2.0-flash-exp"
)

pipeline = SequentialAgent(
    name="MyPipeline",
    sub_agents=[step1, step2]
)

## 当使用初始输入运行管道时，Step1 将执行，
## 其响应将存储在 session.state["data"] 中，然后
## Step2 将执行，按指示使用来自状态的信息。
```

以下代码示例说明了 Google ADK 中的 ParallelAgent 模式，它促进多个智能体并发执行任务。data_gatherer 设计为并发运行两个子智能体：weather_fetcher 和 news_fetcher。weather_fetcher 智能体被指示获取给定位置的天气并将结果存储在 session.state["weather_data"] 中。同样，news_fetcher 智能体被指示检索给定主题的头条新闻故事并将其存储在 session.state["news_data"] 中。每个子智能体都配置为使用"gemini-2.0-flash-exp"模型。ParallelAgent 编排这些子智能体的执行，允许它们并行工作。来自 weather_fetcher 和 news_fetcher 的结果将被收集并存储在会话状态中。最后，示例展示了如何在智能体执行完成后从 final_state 访问收集的天气和新闻数据。

```python
from google.adk.agents import LlmAgent, ParallelAgent

## 最好将获取逻辑定义为智能体工具
## 为了简化此示例，我们将逻辑嵌入智能体指令中。
## 在实际场景中，您将使用工具。

## 定义将并行运行的各个智能体
weather_fetcher = LlmAgent(
    name="weather_fetcher",
    model="gemini-2.0-flash-exp",
    instruction="获取给定位置的天气并仅返回天气报告。",
    output_key="weather_data"  # 结果将存储在 session.state["weather_data"] 中
)

news_fetcher = LlmAgent(
    name="news_fetcher",
    model="gemini-2.0-flash-exp",
    instruction="获取给定主题的头条新闻故事并仅返回该故事。",
    output_key="news_data"      # 结果将存储在 session.state["news_data"] 中
)

## 创建 ParallelAgent 以编排子智能体
data_gatherer = ParallelAgent(
    name="data_gatherer",
    sub_agents=[
        weather_fetcher,
        news_fetcher
    ]
)
```

提供的代码段示例了 Google ADK 中的"智能体作为工具"范式，使智能体能够以类似于工具调用的方式利用另一个智能体的能力。具体来说，代码使用 Google 的 LlmAgent 和 AgentTool 类定义了一个图像生成系统。它由两个智能体组成：父 artist_agent 和子智能体 image_generator_agent。generate_image 函数是一个简单的工具，模拟图像创建，返回模拟图像数据。image_generator_agent 负责根据其接收的文本提示词使用此工具。artist_agent 的角色是首先构思一个创意图像提示词。然后它通过 AgentTool 包装器调用 image_generator_agent。AgentTool 充当桥梁，允许一个智能体将另一个智能体用作工具。当 artist_agent 调用 image_tool 时，AgentTool 使用艺术家构思的提示词调用 image_generator_agent。image_generator_agent 然后使用该提示词调用 generate_image 函数。最后，生成的图像（或模拟数据）通过智能体返回。此架构演示了一个分层智能体系统，其中更高级别的智能体编排较低级别的专门智能体以执行任务。

```python
from google.adk.agents import LlmAgent
from google.adk.tools import agent_tool
from google.genai import types

## 1. 核心能力的简单函数工具。
## 这遵循将操作与推理分离的最佳实践。
def generate_image(prompt: str) -> dict:
    """
    基于文本提示词生成图像。
    参数：
        prompt：要生成的图像的详细描述。
    返回：
        包含状态和生成的图像字节的字典。
    """
    print(f"工具：为提示词生成图像：'{prompt}'")
    # 在真实实现中，这将调用图像生成 API。
    # 对于此示例，我们返回模拟图像数据。
    mock_image_bytes = b"mock_image_data_for_a_cat_wearing_a_hat"
    return {
        "status": "success",
        # 工具返回原始字节，智能体将处理 Part 创建。
        "image_bytes": mock_image_bytes,
        "mime_type": "image/png"
    }

## 2. 将 ImageGeneratorAgent 重构为 LlmAgent。
## 它现在正确使用传递给它的输入。
image_generator_agent = LlmAgent(
    name="ImageGen",
    model="gemini-2.0-flash",
    description="基于详细的文本提示词生成图像。",
    instruction=(
        "你是图像生成专家。你的任务是接受用户的请求 "
        "并使用 `generate_image` 工具创建图像。"
        "用户的整个请求应用作工具的 'prompt' 参数。"
        "工具返回图像字节后，你必须输出图像。"
    ),
    tools=[generate_image]
)

## 3. 将更正的智能体包装在 AgentTool 中。
## 这里的描述是父智能体的。
image_tool = agent_tool.AgentTool(
    agent=image_generator_agent,
    description="使用此工具生成图像。输入应该是所需图像的描述性提示词。"
)

## 4. 父智能体不变。其逻辑是正确的。
artist_agent = LlmAgent(
    name="Artist",
    model="gemini-2.0-flash",
    instruction=(
        "你是一位富有创造力的艺术家。首先，为图像发明一个创意且描述性的提示词。"
        "然后，使用 `ImageGen` 工具使用你的提示词生成图像。"
    ),
    tools=[image_tool]
)
```

## 速览

**问题背景：** 复杂问题通常超出单个单体基于 LLM 的智能体的能力范围。单个智能体往往缺乏解决多方面任务所有部分所需的多样化专业技能或对特定工具的访问。此限制造成瓶颈，降低系统的整体效率和可扩展性。因此，处理复杂的多领域目标变得低效，并可能导致不完整或次优的结果。

**解决方案：** 多智能体协作模式通过创建多个协作智能体的系统提供了标准化解决方案。复杂问题被分解为更小、更易于管理的子问题。然后将每个子问题分配给具有解决它所需的精确工具和能力的专门智能体。这些智能体通过精心设计的通信协议和交互模型（如顺序交接、并行工作流或层次化委托）协同工作。这种分布式智能体方法创造了协同效应，使整个系统能够实现任何单个智能体都无法单独实现的成果。

**实践建议：** 当任务对于单个智能体太复杂并且可以分解为需要专业技能或工具的不同子任务时，使用此模式。它非常适合受益于多样化专业知识、并行处理或具有多个阶段的结构化工作流的问题，例如复杂的研究和分析、软件开发或创意内容生成。

**可视化摘要**

**![][image3]**

图 3：多智能体模式

## 关键要点

* 多智能体协作涉及多个智能体协同工作以实现共同目标。
* 此模式利用专业角色、分布式任务和智能体间通信。
* 协作可以采取顺序交接、并行处理、辩论或层次结构等形式。
* 此模式非常适合需要多样化专业知识或多个不同阶段的复杂问题。

## 结论

本章探讨了多智能体协作模式，展示了在系统内编排多个专门智能体的强大之处。我们研究了各种协作模型，强调该模式在跨不同领域解决复杂多方面问题中的关键作用。理解智能体间的交互自然会引出对其与外部环境交互的探究。

## 参考文献

1. Multi-Agent Collaboration Mechanisms: A Survey of LLMs, [https://arxiv.org/abs/2501.06322](https://arxiv.org/abs/2501.06322)
2. Multi-Agent System — The Power of Collaboration, [https://aravindakumar.medium.com/introducing-multi-agent-frameworks-the-power-of-collaboration-e9db31bba1b6](https://aravindakumar.medium.com/introducing-multi-agent-frameworks-the-power-of-collaboration-e9db31bba1b6)

[image1]: ../images/chapter-7/image1.png

[image2]: ../images/chapter-7/image2.png

[image3]: ../images/chapter-7/image3.png
