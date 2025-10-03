# 第 4 章：反思

## 反思模式概述

在前面的章节中，我们探讨了基础的 Agent 模式：顺序执行的链式、动态路径选择的路由以及并发任务执行的并行化。这些模式使 Agent 能够更高效、更灵活地执行复杂任务。然而，即使采用复杂的工作流，Agent 的初始输出或计划也可能并非最优、准确或完整。这正是**反思**模式发挥关键作用之处。

反思模式涉及 Agent 评估其自身工作、输出或内部状态，并利用该评估来提升性能或优化响应。这是一种自我纠正或自我改进机制，允许 Agent 基于反馈、内部评审或与预期标准的对比，迭代优化其输出或调整策略。反思有时可由专门的 Agent 来促进，其特定职责是分析初始 Agent 的输出。

与简单顺序链（输出直接传递至下一步）或路径选择的路由不同，反思引入了反馈循环。Agent 不仅产生输出，还会检查该输出（或其生成过程），识别潜在问题或改进空间，并运用这些洞察生成更好的版本或调整后续行动。

该过程通常包含以下步骤：

1. **执行：** Agent 执行任务或生成初始输出
2. **评估/评审：** Agent（通常通过另一个 LLM 调用或规则集）分析上一步结果。此评估可能涉及事实准确性、连贯性、风格、完整性、指令遵循度或其他相关标准
3. **反思/优化：** 基于评审意见，Agent 确定改进方向。这可能包括生成优化后的输出、调整后续步骤参数，甚至修改整体计划
4. **迭代（可选但常见）：** 优化后的输出或调整后的方法可继续执行，反思过程可重复进行，直至获得满意结果或达到停止条件

反思模式的一个关键且高效的实现是将流程分离为两个不同的逻辑角色：生产者和评审者。这通常被称为"生成器-评审者"或"生产者-审查者"模型。虽然单个 Agent 可执行自我反思，但使用两个专门 Agent（或两个具有不同系统提示的独立 LLM 调用）通常能产生更稳健和客观的结果。

1. 生产者 Agent：此 Agent 的主要职责是执行任务的初始工作。它完全专注于内容生成，无论是编写代码、起草博客文章还是制定计划。它接收初始提示并生成输出的第一版

2. 评审者 Agent：此 Agent 的唯一目的是评估生产者生成的输出。它被赋予不同的指令集，通常承担特定角色（如"高级软件工程师"、"严谨的事实核查员"）。评审者的指令引导其根据特定标准分析生产者工作，包括事实准确性、代码质量、风格要求或完整性。其设计目标是发现缺陷、提出改进建议并提供结构化反馈

这种关注点分离非常有效，因为它避免了 Agent 审查自身工作时可能产生的"认知偏差"。评审者 Agent 以全新视角处理输出，完全专注于发现错误和改进空间。评审者的反馈随后传回生产者 Agent，生产者 Agent 以此为指南生成新的优化版本。提供的 LangChain 和 ADK 代码示例均实现了这种双 Agent 模型：LangChain 示例使用特定的"reflector_prompt"创建评审者角色，而 ADK 示例明确定义了生产者和审查者 Agent。

实现反思通常需要在 Agent 工作流中构建这些反馈循环。这可通过代码中的迭代循环实现，或使用支持基于评估结果进行状态管理和条件转换的框架。虽然单步评估和优化可在 LangChain/LangGraph、ADK 或 Crew.AI 链中实现，但真正的迭代反思通常涉及更复杂的编排。

反思模式对于构建能够产出高质量输出、处理精细任务并展现一定自我意识和适应性的 Agent 至关重要。它推动 Agent 从单纯执行指令转向更复杂的问题解决和内容生成形式。

值得注意的是反思与目标设定和监控（见第 11 章）的交叉点。目标为 Agent 的自我评估提供最终基准，而监控跟踪其进展。在许多实际案例中，反思可能充当纠正引擎，利用监控反馈分析偏差并调整策略。这种协同作用将 Agent 从被动执行者转变为有目的地自适应工作以实现目标。

此外，当 LLM 保持对话记忆（见第 8 章）时，反思模式的有效性显著增强。对话历史为评估阶段提供关键上下文，使 Agent 不仅能孤立评估输出，还能在先前交互、用户反馈和演进目标的背景下进行评估。这使 Agent 能从过去的评审中学习并避免重复错误。没有记忆时，每次反思都是独立事件；有了记忆，反思成为累积过程，每个周期都基于前一个周期，从而实现更智能和上下文感知的优化。

## 实际应用与用例

反思模式在输出质量、准确性或复杂约束遵循度至关重要的场景中极具价值：

1. 创意写作与内容生成：
优化生成的文本、故事、诗歌或营销文案

* **用例：** 博客文章撰写 Agent
  * **反思：** 生成草稿，评审其流畅度、语气和清晰度，然后基于评审重写。重复直至内容达到质量标准
  * **优势：** 产出更精炼有效的内容

2. 代码生成与调试：
编写代码、识别错误并进行修复

* **用例：** Python 函数编写 Agent
  * **反思：** 编写初始代码，运行测试或静态分析，识别错误或低效环节，然后基于发现修改代码
  * **优势：** 生成更健壮和功能完善的代码

3. 复杂问题解决：
评估多步推理任务中的中间步骤或建议方案

* **用例：** 逻辑谜题求解 Agent
  * **反思：** 提出步骤，评估其是否接近解决方案或引入矛盾，必要时回溯或选择不同步骤
  * **优势：** 提升 Agent 在复杂问题空间中的导航能力

4. 摘要与信息综合：
优化摘要的准确性、完整性和简洁性

* **用例：** 长文档摘要 Agent
  * **反思：** 生成初始摘要，与原始文档关键点对比，优化摘要以补全缺失信息或提升准确性
  * **优势：** 创建更准确全面的摘要

5. 规划与策略：
评估提议计划并识别潜在缺陷或改进点

* **用例：** 目标达成行动规划 Agent
  * **反思：** 生成计划，模拟执行或根据约束评估可行性，基于评估修订计划
  * **优势：** 制定更有效和现实的计划

6. 对话 Agent：
审查对话历史轮次以保持上下文、纠正误解或提升响应质量

* **用例：** 客户支持聊天机器人
  * **反思：** 用户响应后，审查对话历史和最后生成消息，确保连贯性并准确回应用户最新输入
  * **优势：** 促成更自然有效的对话

反思为 Agent 系统增加了元认知层，使其能从自身输出和过程中学习，从而产生更智能、可靠和高质量的结果

## 实操代码示例（LangChain）

实现完整的迭代反思过程需要状态管理和循环执行机制。虽然这些在基于图的框架（如 LangGraph）中内置处理或通过自定义程序代码实现，但单个反思周期的基本原理可通过 LCEL（LangChain 表达式语言）的组合语法有效演示。

此示例使用 Langchain 库和 OpenAI 的 GPT-4o 模型实现反思循环，迭代生成并优化计算数字阶乘的 Python 函数。该过程从任务提示开始，生成初始代码，然后基于模拟高级软件工程师角色的评审反复反思代码，在每次迭代中优化代码，直至评审阶段确认代码完美或达到最大迭代次数。最后打印优化后的代码。

首先确保安装必要库：

```bash
pip install langchain langchain-community langchain-openai
```

您还需要使用所选语言模型的 API 密钥配置环境（如 OpenAI、Google Gemini、Anthropic）

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

## --- 配置 ---
## 从 .env 文件加载环境变量（用于 OPENAI_API_KEY）
load_dotenv()

## 检查是否设置了 API 密钥
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("在 .env 文件中未找到 OPENAI_API_KEY。请添加它。")

## 初始化聊天 LLM。我们使用 gpt-4o 以获得更好的推理。
## 使用较低的温度以获得更确定性的输出。
llm = ChatOpenAI(model="gpt-4o", temperature=0.1)

def run_reflection_loop():
    """
    演示多步 AI 反思循环以逐步改进 Python 函数。
    """
    # --- 核心任务 ---
    task_prompt = """
    你的任务是创建一个名为 `calculate_factorial` 的 Python 函数。
    此函数应执行以下操作：
    1. 接受单个整数 `n` 作为输入。
    2. 计算其阶乘 (n!)。
    3. 包含清楚解释函数功能的文档字符串。
    4. 处理边缘情况：0 的阶乘是 1。
    5. 处理无效输入：如果输入是负数，则引发 ValueError。
    """
    
    # --- 反思循环 ---
    max_iterations = 3
    current_code = ""
    
    # 我们将构建对话历史以在每一步中提供上下文。
    message_history = [HumanMessage(content=task_prompt)]
    
    for i in range(max_iterations):
        print("\n" + "="*25 + f" 反思循环：迭代 {i + 1} " + "="*25)
        
        # --- 1. 生成/完善阶段 ---
        # 在第一次迭代中，它生成。在后续迭代中，它完善。
        if i == 0:
            print("\n>>> 阶段 1：生成初始代码...")
            # 第一条消息只是任务提示词。
            response = llm.invoke(message_history)
            current_code = response.content
        else:
            print("\n>>> 阶段 1：基于先前批评完善代码...")
            # 消息历史现在包含任务、
            # 最后一个代码和最后一个批评。
            # 我们指示模型应用批评。
            message_history.append(HumanMessage(content="请使用提供的批评完善代码。"))
            response = llm.invoke(message_history)
            current_code = response.content
        
        print("\n--- 生成的代码 (v" + str(i + 1) + ") ---\n" + current_code)
        message_history.append(response) # 将生成的代码添加到历史记录
        
        # --- 2. 反思阶段 ---
        print("\n>>> 阶段 2：对生成的代码进行反思...")
        # 为反思 Agent 创建特定提示词。
        # 这要求模型充当高级代码审查员。
        reflector_prompt = [
            SystemMessage(content="""
                你是一名高级软件工程师和 Python 专家。
                你的角色是执行细致的代码审查。
                根据原始任务要求批判性地评估提供的 Python 代码。
                查找错误、风格问题、缺失的边缘情况和改进领域。
                如果代码完美并满足所有要求，
                用单一短语 'CODE_IS_PERFECT' 响应。
                否则，提供批评的项目符号列表。
            """),
            HumanMessage(content=f"原始任务：\n{task_prompt}\n\n要审查的代码：\n{current_code}")
        ]
        
        critique_response = llm.invoke(reflector_prompt)
        critique = critique_response.content
        
        # --- 3. 停止条件 ---
        if "CODE_IS_PERFECT" in critique:
            print("\n--- 批评 ---\n未发现进一步批评。代码令人满意。")
            break
        
        print("\n--- 批评 ---\n" + critique)
        
        # 将批评添加到历史记录以用于下一个完善循环。
        message_history.append(HumanMessage(content=f"对先前代码的批评：\n{critique}"))
    
    print("\n" + "="*30 + " 最终结果 " + "="*30)
    print("\n反思过程后的最终精炼代码：\n")
    print(current_code)

if __name__ == "__main__":
    run_reflection_loop()
```

代码首先设置环境，加载 API 密钥，并使用低温度初始化强大的语言模型（如 GPT-4o）以获得专注输出。核心任务由提示定义，要求创建计算数字阶乘的 Python 函数，包括文档字符串、边界情况（0 的阶乘）和负输入错误处理的特定要求。run_reflection_loop 函数协调迭代优化过程。在循环中，第一次迭代时语言模型根据任务提示生成初始代码，后续迭代中则基于前一步的评审优化代码。单独的"反思者"角色（同样由语言模型扮演但使用不同系统提示）充当高级软件工程师，根据原始任务要求评审生成的代码。此评审以问题项目符号列表或短语 'CODE_IS_PERFECT'（如无问题）形式提供。循环持续至评审指示代码完美或达到最大迭代次数。对话历史被维护并在每一步传递给语言模型，为生成/优化和反思阶段提供上下文。最后，脚本在循环结束后打印最终生成的代码版本

## 实操代码示例（ADK）

现在让我们看一个使用 Google ADK 实现的概念性代码示例。具体而言，代码通过采用生成器-评审者结构来展示，其中一个组件（生成器）产生初始结果或计划，另一个组件（评审者）提供批判性反馈或评审，引导生成器朝向更优化或准确的最终输出

```python
from google.adk.agents import SequentialAgent, LlmAgent

## 第一个 Agent 生成初始草稿。
generator = LlmAgent(
    name="DraftWriter",
    description="生成关于给定主题的初始草稿内容。",
    instruction="撰写关于用户主题的简短、信息丰富的段落。",
    output_key="draft_text" # 输出保存到此状态键。
)

## 第二个 Agent 批评第一个 Agent 的草稿。
reviewer = LlmAgent(
    name="FactChecker",
    description="审查给定文本的事实准确性并提供结构化批评。",
    instruction="""
    你是一个细致的事实核查员。
    1. 阅读状态键 'draft_text' 中提供的文本。
    2. 仔细验证所有声明的事实准确性。
    3. 你的最终输出必须是包含两个键的字典：
       - "status": 字符串，"ACCURATE" 或 "INACCURATE"。
       - "reasoning": 字符串，提供对你的状态的清楚解释，如果发现任何问题则引用具体问题。
    """,
    output_key="review_output" # 结构化字典保存在这里。
)

## SequentialAgent 确保生成器在审查者之前运行。
review_pipeline = SequentialAgent(
    name="WriteAndReview_Pipeline",
    sub_agents=[generator, reviewer]
)

## 执行流程：
## 1. generator 运行 -> 将其段落保存到 state['draft_text']。
## 2. reviewer 运行 -> 读取 state['draft_text'] 并将其字典输出保存到 state['review_output']。
```

此代码演示了在 Google ADK 中使用顺序 Agent 管道生成和审查文本。它定义了两个 LlmAgent 实例：generator 和 reviewer。generator Agent 设计用于创建关于给定主题的初始草稿段落，被指示撰写简短信息丰富的文章，并将其输出保存至状态键 draft_text。reviewer Agent 作为生成器产出文本的事实核查员，被指示从 draft_text 读取文本并验证其事实准确性。审查者的输出是包含两个键的结构化字典：status 和 reasoning。status 指示文本为"ACCURATE"或"INACCURATE"，reasoning 则提供状态解释。此字典保存至状态键 review_output。创建名为 review_pipeline 的 SequentialAgent 来管理两个 Agent 的执行顺序，确保生成器先运行，然后是审查者。整体执行流程为：生成器产出文本并保存至状态，随后审查者从状态读取文本，执行事实核查，并将其发现（状态和推理）保存回状态。此管道允许使用独立 Agent 进行结构化内容创建和审查过程。**注意：** 对于感兴趣者，还提供了利用 ADK 的 LoopAgent 的替代实现。

结束前需考虑，虽然反思模式显著提升输出质量，但也带来重要权衡。迭代过程虽强大，但可能导致更高成本和延迟，因为每个优化循环可能需要新的 LLM 调用，使其对时间敏感应用并非最优选择。此外，该模式内存密集；随着每次迭代，对话历史扩展，包含初始输出、评审和后续优化

## 概览

**什么：** Agent 的初始输出通常次优，存在不准确、不完整或未满足复杂要求的问题。基础 Agent 工作流缺乏 Agent 识别和修复自身错误的内置流程。这通过让 Agent 评估自身工作，或更稳健地引入独立逻辑 Agent 充当评审者来解决，防止无论质量如何初始响应都成为最终结果

**为什么：** 反思模式通过引入自我纠正和优化机制提供解决方案。它建立反馈循环，其中"生产者" Agent 生成输出，然后"评审者" Agent（或生产者自身）根据预定义标准进行评估。随后使用此评审生成改进版本。这种生成、评估和优化的迭代过程逐步提升最终结果质量，从而产生更准确、连贯和可靠的结果

**经验法则：** 当最终输出的质量、准确性和细节比速度和成本更重要时使用反思模式。它对生成精炼长篇内容、编写调试代码以及创建详细计划等任务特别有效。当任务需要通用生产者 Agent 可能遗漏的高客观性或专门评估时，使用独立评审者 Agent

**视觉摘要**

**![][image1]**

图 1：反思设计模式，自我反思

**![][image2]**

图 2：反思设计模式，生产者和批评者 Agent

## 关键要点

* 反思模式的主要优势在于其迭代自我纠正和优化输出的能力，带来显著更高的质量、准确性和复杂指令遵循度
* 它涉及执行、评估/评审和优化的反馈循环。反思对需要高质量、准确或精细输出的任务至关重要
* 一个强大的实现是生产者-评审者模型，其中独立 Agent（或提示角色）评估初始输出。这种关注点分离增强客观性，并支持更专业、结构化的反馈
* 然而，这些优势以增加的延迟和计算成本为代价，同时伴随超出模型上下文窗口或被 API 服务限制的更高风险
* 虽然完整迭代反思通常需要状态化工作流（如 LangGraph），但单个反思步骤可在 LangChain 中使用 LCEL 实现，以传递输出进行评审和后续优化
* Google ADK 可通过顺序工作流促进反思，其中一个 Agent 的输出被另一个 Agent 评审，允许后续优化步骤
* 此模式使 Agent 能够执行自我纠正并随时间提升性能

## 结论

反思模式为 Agent 工作流中的自我纠正提供关键机制，实现超越单次执行的迭代改进。这是通过创建循环实现的：系统生成输出，根据特定标准评估，然后使用该评估产生优化结果。此评估可由 Agent 自身（自我反思）执行，或通常更有效地由不同评审者 Agent 执行，这代表了模式内的关键架构选择

虽然完全自主的多步反思过程需要强大的状态管理架构，但其核心原理可在单个生成-评审-优化周期中有效演示。作为控制结构，反思可与其他基础模式集成，以构建更健壮和功能更复杂的 Agent 系统

## 参考文献

以下是有关反思模式和相关概念的一些进一步阅读资源：

1. Training Language Models to Self-Correct via Reinforcement Learning, [https://arxiv.org/abs/2409.12917](https://arxiv.org/abs/2409.12917)
2. LangChain Expression Language (LCEL) Documentation: [https://python.langchain.com/docs/introduction/](https://python.langchain.com/docs/introduction/)
3. LangGraph Documentation:[https://www.langchain.com/langgraph](https://www.langchain.com/langgraph)
4. Google Agent Developer Kit (ADK) Documentation (Multi-Agent Systems): [https://google.github.io/adk-docs/agents/multi-agents/](https://google.github.io/adk-docs/agents/multi-agents/)

[image1]: ../images/chapter-4/image1.png

[image2]: ../images/chapter-4/image2.png