# 第 4 章：反思

## 反思模式概述

在前面的章节中，我们探讨了基本的 Agent 模式：用于顺序执行的链接、用于动态路径选择的路由以及用于并发任务执行的并行化。这些模式使 Agent 能够更高效、更灵活地执行复杂任务。然而，即使使用复杂的工作流，Agent 的初始输出或计划可能也不是最优的、准确的或完整的。这就是**反思**模式发挥作用的地方。

反思模式涉及 Agent 评估其自身的工作、输出或内部状态，并使用该评估来改进其性能或完善其响应。这是一种自我纠正或自我改进的形式，允许 Agent 根据反馈、内部批评或与期望标准的比较，迭代地完善其输出或调整其方法。反思有时可以由一个单独的 Agent 促进，其特定角色是分析初始 Agent 的输出。

与简单的顺序链（其中输出直接传递到下一步）或选择路径的路由不同，反思引入了反馈循环。Agent 不仅仅产生输出；它然后检查该输出（或生成它的过程），识别潜在问题或改进领域，并使用这些见解生成更好的版本或修改其未来行动。

该过程通常包括：

1. **执行：** Agent 执行任务或生成初始输出。
2. **评估/批评：** Agent（通常使用另一个 LLM 调用或一组规则）分析前一步的结果。此评估可能检查事实准确性、连贯性、风格、完整性、对指令的遵守或其他相关标准。
3. **反思/完善：** 基于批评，Agent 确定如何改进。这可能涉及生成精炼的输出、调整后续步骤的参数，甚至修改总体计划。
4. **迭代（可选但常见）：** 然后可以执行精炼的输出或调整的方法，反思过程可以重复，直到达到满意的结果或满足停止条件。

反思模式的一个关键且高效的实现是将过程分离为两个不同的逻辑角色：生产者和批评者。这通常被称为"生成器-批评者"或"生产者-审查者"模型。虽然单个 Agent 可以执行自我反思，但使用两个专门的 Agent（或两个具有不同系统提示词的单独 LLM 调用）通常会产生更稳健和无偏见的结果。

1. 生产者 Agent：此 Agent 的主要责任是执行任务的初始执行。它完全专注于生成内容，无论是编写代码、起草博客文章还是创建计划。它接受初始提示词并产生输出的第一个版本。

2. 批评者 Agent：此 Agent 的唯一目的是评估生产者生成的输出。它被赋予一组不同的指令，通常是不同的角色（例如，"你是一名高级软件工程师"，"你是一个细致的事实核查员"）。批评者的指令引导它根据特定标准分析生产者的工作，例如事实准确性、代码质量、风格要求或完整性。它旨在发现缺陷、提出改进建议并提供结构化反馈。

这种关注点分离非常强大，因为它防止了 Agent 审查其自己工作的"认知偏差"。批评者 Agent 以全新的视角处理输出，完全致力于发现错误和改进领域。批评者的反馈然后传递回生产者 Agent，生产者 Agent 使用它作为指南生成新的、精炼的输出版本。提供的 LangChain 和 ADK 代码示例都实现了这种双 Agent 模型：LangChain 示例使用特定的"reflector_prompt"创建批评者角色，而 ADK 示例明确定义了生产者和审查者 Agent。

实现反思通常需要构建 Agent 的工作流以包括这些反馈循环。这可以通过代码中的迭代循环实现，或使用支持基于评估结果的状态管理和条件转换的框架。虽然单步评估和完善可以在 LangChain/LangGraph、ADK 或 Crew.AI 链中实现，但真正的迭代反思通常涉及更复杂的编排。

反思模式对于构建能够产生高质量输出、处理细微任务并展现一定程度的自我意识和适应性的 Agent 至关重要。它使 Agent 从简单地执行指令转向更复杂的问题解决和内容生成形式。

值得注意的是反思与目标设定和监控（见第 11 章）的交集。目标为 Agent 的自我评估提供了最终基准，而监控跟踪其进度。在许多实际案例中，反思可能充当纠正引擎，使用监控反馈来分析偏差并调整其策略。这种协同作用将 Agent 从被动执行者转变为自适应地工作以实现其目标的有目的系统。

此外，当 LLM 保留对话记忆（见第 8 章）时，反思模式的有效性会显著增强。这种对话历史为评估阶段提供了关键上下文，使 Agent 能够不仅孤立地评估其输出，而且能够在先前交互、用户反馈和不断发展的目标的背景下进行评估。它使 Agent 能够从过去的批评中学习并避免重复错误。没有记忆，每次反思都是一个独立的事件；有了记忆，反思成为一个累积过程，其中每个周期都建立在上一个周期的基础上，导致更智能和上下文感知的完善。

## 实际应用与用例

反思模式在输出质量、准确性或对复杂约束的遵守至关重要的场景中很有价值：

1. 创意写作和内容生成：  
完善生成的文本、故事、诗歌或营销文案。

* **用例：** 撰写博客文章的 Agent。
  * **反思：** 生成草稿，批评其流畅性、语气和清晰度，然后根据批评重写。重复直到帖子满足质量标准。
  * **好处：** 产生更精致和有效的内容。

2. 代码生成和调试：  
编写代码、识别错误并修复它们。

* **用例：** 编写 Python 函数的 Agent。
  * **反思：** 编写初始代码，运行测试或静态分析，识别错误或低效之处，然后根据发现修改代码。
  * **好处：** 生成更稳健和功能性的代码。

3. 复杂问题解决：  
评估多步推理任务中的中间步骤或提出的解决方案。

* **用例：** 解决逻辑谜题的 Agent。
  * **反思：** 提出一个步骤，评估它是否更接近解决方案或引入矛盾，如果需要则回溯或选择不同的步骤。
  * **好处：** 提高 Agent 导航复杂问题空间的能力。

4. 总结和信息综合：  
完善摘要的准确性、完整性和简洁性。

* **用例：** 总结长文档的 Agent。
  * **反思：** 生成初始摘要，将其与原始文档中的关键点进行比较，完善摘要以包含缺失信息或提高准确性。
  * **好处：** 创建更准确和全面的摘要。

5. 规划和策略：  
评估提出的计划并识别潜在缺陷或改进。

* **用例：** 规划一系列行动以实现目标的 Agent。
  * **反思：** 生成计划，模拟其执行或根据约束评估其可行性，根据评估修订计划。
  * **好处：** 开发更有效和现实的计划。

6. 对话 Agent：  
审查对话中的先前轮次以保持上下文、纠正误解或提高响应质量。

* **用例：** 客户支持聊天机器人。
  * **反思：** 在用户响应后，审查对话历史和最后生成的消息，以确保连贯性并准确解决用户的最新输入。
  * **好处：** 导致更自然和有效的对话。

反思为 Agent 系统增加了一层元认知，使它们能够从自己的输出和过程中学习，从而产生更智能、更可靠和更高质量的结果。

## 实操代码示例（LangChain）

实现完整的迭代反思过程需要状态管理和循环执行的机制。虽然这些在基于图的框架（如 LangGraph）中本地处理或通过自定义程序代码处理，但单个反思周期的基本原理可以使用 LCEL（LangChain 表达式语言）的组合语法有效地演示。

此示例使用 Langchain 库和 OpenAI 的 GPT-4o 模型实现反思循环，以迭代生成和完善计算数字阶乘的 Python 函数。该过程从任务提示词开始，生成初始代码，然后根据来自模拟高级软件工程师角色的批评反复反思代码，在每次迭代中完善代码，直到批评阶段确定代码完美或达到最大迭代次数。最后，它打印生成的精炼代码。

首先，确保您已安装必要的库：

```bash
pip install langchain langchain-community langchain-openai
```

您还需要使用您选择的语言模型的 API 密钥设置环境（例如，OpenAI、Google Gemini、Anthropic）。

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

代码首先设置环境，加载 API 密钥，并使用低温度初始化强大的语言模型（如 GPT-4o）以获得聚焦的输出。核心任务由提示词定义，要求创建一个计算数字阶乘的 Python 函数，包括文档字符串、边缘情况（0 的阶乘）和负输入的错误处理的特定要求。run_reflection_loop 函数协调迭代完善过程。在循环中，在第一次迭代中，语言模型根据任务提示词生成初始代码。在后续迭代中，它根据前一步的批评完善代码。一个单独的"反思者"角色，也由语言模型扮演但使用不同的系统提示词，充当高级软件工程师来根据原始任务要求批评生成的代码。此批评以问题的项目符号列表或短语 'CODE_IS_PERFECT'（如果未发现问题）的形式提供。循环继续，直到批评指示代码完美或达到最大迭代次数。对话历史被维护并在每一步传递给语言模型，为生成/完善和反思阶段提供上下文。最后，脚本在循环结束后打印最后生成的代码版本。

## 实操代码示例（ADK）

现在让我们看一个使用 Google ADK 实现的概念性代码示例。具体来说，代码通过采用生成器-批评者结构来展示这一点，其中一个组件（生成器）产生初始结果或计划，另一个组件（批评者）提供批判性反馈或批评，引导生成器朝向更精炼或准确的最终输出。

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

此代码演示了在 Google ADK 中使用顺序 Agent 管道生成和审查文本。它定义了两个 LlmAgent 实例：generator 和 reviewer。generator Agent 设计用于创建关于给定主题的初始草稿段落。它被指示撰写简短而信息丰富的文章，并将其输出保存到状态键 draft_text。reviewer Agent 充当生成器产生的文本的事实核查员。它被指示从 draft_text 读取文本并验证其事实准确性。审查者的输出是一个包含两个键的结构化字典：status 和 reasoning。status 指示文本是"ACCURATE"还是"INACCURATE"，而 reasoning 提供对状态的解释。此字典保存到状态键 review_output。创建了一个名为 review_pipeline 的 SequentialAgent 来管理两个 Agent 的执行顺序。它确保生成器首先运行，然后是审查者。整体执行流程是生成器产生文本，然后保存到状态。随后，审查者从状态读取此文本，执行其事实核查，并将其发现（状态和推理）保存回状态。此管道允许使用单独的 Agent 进行结构化的内容创建和审查过程。**注意：** 对于感兴趣的人，还提供了利用 ADK 的 LoopAgent 的替代实现。

在结束之前，重要的是要考虑，虽然反思模式显著提高了输出质量，但它带来了重要的权衡。迭代过程虽然强大，但可能导致更高的成本和延迟，因为每个完善循环可能需要新的 LLM 调用，使其对时间敏感的应用程序不是最优的。此外，该模式是内存密集型的；随着每次迭代，对话历史扩展，包括初始输出、批评和后续完善。

## 概览

**什么：** Agent 的初始输出通常是次优的，存在不准确、不完整或未能满足复杂要求的问题。基本的 Agent 工作流缺乏 Agent 识别和修复自身错误的内置过程。这通过让 Agent 评估自己的工作，或更稳健地通过引入单独的逻辑 Agent 充当批评者来解决，防止初始响应无论质量如何都成为最终响应。

**为什么：** 反思模式通过引入自我纠正和完善机制提供了解决方案。它建立了一个反馈循环，其中"生产者" Agent 生成输出，然后"批评者" Agent（或生产者本身）根据预定义标准对其进行评估。然后使用此批评生成改进的版本。这种生成、评估和完善的迭代过程逐步提高最终结果的质量，从而导致更准确、连贯和可靠的结果。

**经验法则：** 当最终输出的质量、准确性和细节比速度和成本更重要时，使用反思模式。它对于生成精致的长篇内容、编写和调试代码以及创建详细计划等任务特别有效。当任务需要通用生产者 Agent 可能错过的高客观性或专门评估时，使用单独的批评者 Agent。

**视觉摘要**

**![][image1]**

图 1：反思设计模式，自我反思

**![][image2]**

图 2：反思设计模式，生产者和批评者 Agent

## 关键要点

* 反思模式的主要优势是其迭代自我纠正和完善输出的能力，导致显著更高的质量、准确性和对复杂指令的遵守。
* 它涉及执行、评估/批评和完善的反馈循环。反思对于需要高质量、准确或细微输出的任务至关重要。
* 一个强大的实现是生产者-批评者模型，其中单独的 Agent（或提示的角色）评估初始输出。这种关注点分离增强了客观性，并允许更专业、结构化的反馈。
* 然而，这些好处是以增加的延迟和计算费用为代价的，以及超过模型上下文窗口或被 API 服务限制的更高风险。
* 虽然完整的迭代反思通常需要有状态工作流（如 LangGraph），但单个反思步骤可以在 LangChain 中使用 LCEL 实现，以传递输出进行批评和后续完善。
* Google ADK 可以通过顺序工作流促进反思，其中一个 Agent 的输出被另一个 Agent 批评，允许后续完善步骤。
* 此模式使 Agent 能够执行自我纠正并随时间提高其性能。

## 结论

反思模式为 Agent 工作流中的自我纠正提供了关键机制，实现了超越单次执行的迭代改进。这是通过创建一个循环来实现的，其中系统生成输出，根据特定标准对其进行评估，然后使用该评估来产生精炼的结果。此评估可以由 Agent 本身（自我反思）执行，或者通常更有效地由不同的批评者 Agent 执行，这代表了模式内的关键架构选择。

虽然完全自主的多步反思过程需要强大的状态管理架构，但其核心原理可以在单个生成-批评-完善周期中有效演示。作为控制结构，反思可以与其他基础模式集成，以构建更稳健和功能更复杂的 Agent 系统。

## 参考文献

以下是有关反思模式和相关概念的一些进一步阅读资源：

1. Training Language Models to Self-Correct via Reinforcement Learning, [https://arxiv.org/abs/2409.12917](https://arxiv.org/abs/2409.12917)
2. LangChain Expression Language (LCEL) Documentation: [https://python.langchain.com/docs/introduction/](https://python.langchain.com/docs/introduction/)
3. LangGraph Documentation:[https://www.langchain.com/langgraph](https://www.langchain.com/langgraph)
4. Google Agent Developer Kit (ADK) Documentation (Multi-Agent Systems): [https://google.github.io/adk-docs/agents/multi-agents/](https://google.github.io/adk-docs/agents/multi-agents/)

[image1]: ../images/chapter-4/image1.png

[image2]: ../images/chapter-4/image2.png