# Chapter 17: Reasoning Techniques
# 第 17 章：推理技术

This chapter delves into advanced reasoning methodologies for intelligent agents, focusing on multi-step logical inferences and problem-solving. These techniques go beyond simple sequential operations, making the agent's internal reasoning explicit. This allows agents to break down problems, consider intermediate steps, and reach more robust and accurate conclusions.  A core principle among these advanced methods is the allocation of increased computational resources during inference. This means granting the agent, or the underlying LLM, more processing time or steps to process a query and generate a response. Rather than a quick, single pass, the agent can engage in iterative refinement, explore multiple solution paths, or utilize external tools. This extended processing time during inference often significantly enhances accuracy, coherence, and robustness, especially for complex problems requiring deeper analysis and deliberation.

本章深入探讨智能体的高级推理方法，重点关注多步骤逻辑推理和复杂问题解决。这些技术超越了简单的顺序操作，使智能体的内部推理过程变得透明可见。通过这种方式，智能体能够将复杂问题分解为更小的子问题、考虑中间推理步骤，并得出更加可靠和准确的结论。这些高级方法的核心原则是在推理过程中分配更多的计算资源。这意味着给予智能体或底层 LLM 更多的处理时间或推理步骤来处理查询并生成响应。与快速单次处理不同，智能体可以进行迭代改进、探索多种解决方案或利用外部工具。这种延长推理时间的方法通常能显著提升准确性、连贯性和鲁棒性，特别是在处理需要深入分析和仔细审议的复杂问题时。

## Practical Applications & Use Cases
## 实际应用和用例

Practical applications include:

这些推理技术的实际应用场景包括：

* **Complex Question Answering:** Facilitating the resolution of multi-hop queries, which necessitate the integration of data from diverse sources and the execution of logical deductions, potentially involving the examination of multiple reasoning paths, and benefiting from extended inference time to synthesize information.  

* **复杂问答**：支持解决多跳查询，这类查询需要整合不同来源的数据并进行逻辑推理，可能涉及检查多条推理路径，通过延长推理时间来综合信息。

* **Mathematical Problem Solving:** Enabling the division of mathematical problems into smaller, solvable components, illustrating the step-by-step process, and employing code execution for precise computations, where prolonged inference enables more intricate code generation and validation.  

* **数学问题解决**：能够将复杂数学问题分解为更小、可解决的组件，展示逐步解题过程，并使用代码执行进行精确计算，延长的推理时间使得更复杂的代码生成和验证成为可能。

* **Code Debugging and Generation:** Supporting an agent's explanation of its rationale for generating or correcting code, pinpointing potential issues sequentially, and iteratively refining the code based on test results (Self-Correction), leveraging extended inference time for thorough debugging cycles.  

* **代码调试和生成**：支持智能体解释其生成或修改代码的理由，按顺序识别潜在问题，并根据测试结果迭代改进代码（自我纠正），利用延长的推理时间进行彻底的调试。

* **Strategic Planning:** Assisting in the development of comprehensive plans through reasoning across various options, consequences, and preconditions, and adjusting plans based on real-time feedback (ReAct), where extended deliberation can lead to more effective and reliable plans.  

* **战略规划**：通过对各种选项、后果和前提条件进行推理，协助制定全面计划，并根据实时反馈调整策略（ReAct），延长的审议时间可以带来更有效和可靠的规划。

* **Medical Diagnosis:** Aiding an agent in systematically assessing symptoms, test outcomes, and patient histories to reach a diagnosis, articulating its reasoning at each phase, and potentially utilizing external instruments for data retrieval (ReAct). Increased inference time allows for a more comprehensive differential diagnosis.

* **医疗诊断**：帮助智能体评估症状、检查结果和患者病史以达成诊断，在每个阶段阐明推理过程，并可能利用外部工具检索数据（ReAct）。增加的推理时间允许进行更全面的鉴别诊断。

* **Legal Analysis:** Supporting the analysis of legal documents and precedents to formulate arguments or provide guidance, detailing the logical steps taken, and ensuring logical consistency through self-correction. Increased inference time allows for more in-depth legal research and argument construction.

* **法律分析**：支持分析法律文件和先例以构建论点或提供指导，详细说明所采取的逻辑步骤，并通过自我纠正确保逻辑一致性。增加的推理时间允许进行更深入的法律研究和论证构建。

## Reasoning techniques
## 推理技术

To start, let's delve into the core reasoning techniques used to enhance the problem-solving abilities of AI models.

首先，让我们深入了解用于增强 AI 模型问题解决能力的核心推理技术。

**Chain-of-Thought (CoT)** prompting significantly enhances LLMs complex reasoning abilities by mimicking a step-by-step thought process (see Fig. 1). Instead of providing a direct answer, CoT prompts guide the model to generate a sequence of intermediate reasoning steps. This explicit breakdown allows LLMs to tackle complex problems by decomposing them into smaller, more manageable sub-problems. This technique markedly improves the model's performance on tasks requiring multi-step reasoning, such as arithmetic, common sense reasoning, and symbolic manipulation. A primary advantage of CoT is its ability to transform a difficult, single-step problem into a series of simpler steps, thereby increasing the transparency of the LLM's reasoning process. This approach not only boosts accuracy but also offers valuable insights into the model's decision-making, aiding in debugging and comprehension.  CoT can be implemented using various strategies, including offering few-shot examples that demonstrate step-by-step reasoning or simply instructing the model to "think step by step." Its effectiveness stems from its ability to guide the model's internal processing toward a more deliberate and logical progression. As a result, Chain-of-Thought has become a cornerstone technique for enabling advanced reasoning capabilities in contemporary LLMs. This enhanced transparency and breakdown of complex problems into manageable sub-problems is particularly important for autonomous agents, as it enables them to perform more reliable and auditable actions in complex environments.  

**思维链（Chain-of-Thought，CoT）**提示词通过模拟逐步思考过程，显著增强了 LLM 的复杂推理能力（见图 1）。CoT 提示词不是要求模型直接给出答案，而是引导其生成一系列中间推理步骤。这种显式的分解使 LLM 能够将复杂问题拆分为更小、更易管理的子问题来逐步解决。该技术显著提升了模型在需要多步推理任务上的表现，例如算术计算、常识推理和符号操作。CoT 的主要优势在于能够将困难的单步问题转化为一系列更简单的步骤，从而提高 LLM 推理过程的透明度。这种方法不仅提高了准确性，还为理解模型决策过程提供了宝贵见解，有助于调试和分析。CoT 可以通过多种策略实现，包括提供展示逐步推理的少样本示例，或简单地指示模型"逐步思考"。其有效性源于它能够引导模型的内部处理过程朝着更审慎和逻辑化的方向发展。因此，思维链已成为在当代 LLM 中实现高级推理能力的基石技术。这种增强的透明度和复杂问题分解能力对于自主智能体尤为重要，使它们能够在复杂环境中执行更可靠和可审计的动作。

![][image1]  
Fig. 1: CoT prompt alongside the detailed, step-by-step response generated by the agent.

图 1：CoT 提示词以及智能体的详细的、逐步的响应。

Let's see an example.  It begins with a set of instructions that tell the AI how to think, defining its persona and a clear five-step process to follow. This is the prompt that initiates structured thinking.

让我们看一个例子。它以一组指令开始，告诉 AI 如何思考，定义其角色和要遵循的清晰五步流程。这是启动结构化思维的提示词。

Following that, the example shows the CoT process in action. The section labeled "Agent's Thought Process" is the internal monologue where the model executes the instructed steps. This is the literal "chain of thought." Finally, the "Agent's Final Answer" is the polished, comprehensive output generated as a result of that careful, step-by-step reasoning process

接下来，示例展示了 CoT 过程的实际应用。标记为"智能体的思考过程"的部分是模型执行指示步骤的内部独白。这是字面上的"思维链"。最后，"智能体的最终答案"是由于仔细的、逐步推理过程而生成的精炼的、全面的输出。

```markdown
You are an Information Retrieval Agent. Your goal is to answer the user's question comprehensively and accurately by thinking step-by-step. Here's the process you must follow:
1.  **Analyze the Query:** Understand the core subject and specific requirements of the user's question. Identify key entities, keywords, and the type of information being sought.
2.  **Formulate Search Queries (for Knowledge Base):** Based on your analysis, generate a list of precise search queries that you would use to retrieve relevant information from a knowledge base or external tools.
3.  **Simulate Information Retrieval (Self-Correction/Reasoning):** For each search query, mentally consider what kind of information you expect to find. If you were to retrieve the content, what would be the most relevant snippets? Think about potential ambiguities or missing pieces.
4.  **Synthesize Information:** Based on the simulated retrieval and your understanding of the user's original query, synthesize the gathered information into a coherent and complete answer. Ensure all aspects of the query are addressed.
5.  **Review and Refine:** Before finalizing, critically evaluate your answer. Is it accurate? Is it comprehensive? Is it easy to understand? Is it concise? If not, identify what needs to be improved and how.

**User Query:** "Explain the main differences between classical computers and quantum computers, and briefly describe a potential application of quantum computing."

**Agent's Thought Process (Internal CoT Output - encouraged by the prompt):**
**Thought 1 (Analyze Query):** The user wants two things: 1.  Main differences between classical and quantum computers. 2.  One potential application of quantum computing. Keywords: classical computers, quantum computers, differences, potential application.
**Thought 2 (Formulate Search Queries):**
- "differences classical vs quantum computers"
- "how quantum computers work"
- "how classical computers work"
- "applications of quantum computing"
**Thought 3 (Simulate Information Retrieval & Identify Key Concepts):**
- From "differences": Expect concepts like bits vs. qubits, superposition, entanglement, probabilistic nature, computational power for specific problems.
- From "how they work": Classical uses transistors/binary. Quantum uses quantum mechanics.
- From "applications": Expect drug discovery, material science, cryptography, optimization.
**Thought 4 (Synthesize Information):** Classical computers use bits (0 or 1), processing information sequentially. Quantum computers use qubits, which can be 0, 1, or both simultaneously (superposition), and can be entangled, allowing for vastly different computational approaches. This enables them to solve certain problems (like factoring large numbers or simulating complex molecules) far more efficiently than classical computers. A potential application is in drug discovery, where quantum computers could simulate molecular interactions with unprecedented accuracy, accelerating the development of new medicines.
**Thought 5 (Review and Refine):**
- Differences are covered (bits vs qubits, superposition, entanglement, processing).
- Application is given (drug discovery).
- Is it brief? Yes.
- Is it clear? Yes.
- Looks good.

**Agent's Final Answer (Output to User):**
Classical computers process information using bits, which can be either a 0 or a 1 at any given time, performing operations sequentially. In contrast, quantum computers utilize qubits, which can exist in multiple states simultaneously through superposition and can be linked through entanglement, allowing for exponentially more complex computations. This fundamental difference enables quantum machines to tackle certain problems, such as simulating molecular structures or breaking complex encryption, that are intractable for even the most powerful classical supercomputers. A significant potential application of quantum computing lies in drug discovery, where its ability to precisely model molecular behavior could revolutionize the development of new pharmaceuticals.
```

**Tree-of-Thought (ToT)** is a reasoning technique that builds upon Chain-of-Thought (CoT). It allows large language models to explore multiple reasoning paths by branching into different intermediate steps, forming a tree structure (see Fig. 2) This approach supports complex problem-solving by enabling backtracking, self-correction, and exploration of alternative solutions. Maintaining a tree of possibilities allows the model to evaluate various reasoning trajectories before finalizing an answer. This iterative process enhances the model's ability to handle challenging tasks that require strategic planning and decision-making.  

**思维树（Tree-of-Thought，ToT）**是一种建立在思维链（CoT）基础上的推理技术。它允许 LLM 通过分支到不同的中间步骤来探索多个推理路径，形成树状结构（见图 2）。这种方法通过支持回溯、自我纠正和探索替代解决方案来应对复杂的问题解决。维护可能性树使得模型能够在最终确定答案之前评估各种推理轨迹。这种迭代过程增强了模型处理需要战略规划和决策的挑战性任务的能力。

![][image2]  
Fig.2: Example of Tree of Thoughts

图 2：思维树示例

**Self-correction**, also known as self-refinement, is a crucial aspect of an agent's reasoning process, particularly within Chain-of-Thought prompting. It involves the agent's internal evaluation of its generated content and intermediate thought processes. This critical review enables the agent to identify ambiguities, information gaps, or inaccuracies in its understanding or solutions. This iterative cycle of reviewing and refining allows the agent to adjust its approach, improve response quality, and ensure accuracy and thoroughness before delivering a final output. This internal critique enhances the agent's capacity to produce reliable and high-quality results, as demonstrated in examples within the dedicated Chapter 4. 

**自我纠正**，也称为自我精炼，是智能体推理过程的一个关键方面，特别是在思维链提示词中。它涉及智能体对生成内容和中间思考过程的内部评估。这种批判性审查使智能体能够识别其理解或解决方案中的模糊性、信息缺口或不准确性。通过审查和改进的迭代循环，智能体可以调整方法、提升响应质量，并在提供最终输出前确保准确性和完整性。这种内部批评机制增强了智能体产生可靠和高质量结果的能力，如第 4 章的专门示例所示。

This example demonstrates a systematic process of self-correction, crucial for refining AI-generated content. It involves an iterative loop of drafting, reviewing against original requirements, and implementing specific improvements. The illustration begins by outlining the AI's function as a "Self-Correction Agent" with a defined five-step analytical and revision workflow. Following this, a subpar "Initial Draft" of a social media post is presented. The "Self-Correction Agent's Thought Process" forms the core of the demonstration. Here, the Agent critically evaluates the draft according to its instructions, pinpointing weaknesses such as low engagement and a vague call to action. It then suggests concrete enhancements, including the use of more impactful verbs and emojis. The process concludes with the "Final Revised Content," a polished and notably improved version that integrates the self-identified adjustments.

这个示例展示了自我纠正的系统过程，这对于改进 AI 生成内容至关重要。它涉及起草、根据原始要求进行审查以及实施具体改进的迭代循环。示例首先概述了 AI 作为"自我纠正智能体"的功能，并定义了五步分析和修订工作流程。然后，展示了社交媒体帖子的"初稿"。"自我纠正智能体的思考过程"构成了演示的核心部分。在这里，智能体根据其指令批判性地评估草稿，指出诸如低参与度和模糊的号召性用语等弱点。随后提出具体的改进建议，包括使用更有影响力的动词和表情符号。整个过程以"最终修订内容"结束，这是一个整合了自我识别调整的精炼和显著改进的版本。

```markdown
You are a highly critical and detail-oriented Self-Correction Agent. Your task is to review a previously generated piece of content against its original requirements and identify areas for improvement. Your goal is to refine the content to be more accurate, comprehensive, engaging, and aligned with the prompt.

Here's the process you must follow for self-correction:
1.  **Understand Original Requirements:** Review the initial prompt/requirements that led to the content's creation. What was the *original intent*? What were the key constraints or goals?
2.  **Analyze Current Content:** Read the provided content carefully.
3.  **Identify Discrepancies/Weaknesses:** Compare the current content against the original requirements. Look for:
   * **Accuracy Issues:** Are there any factual errors or misleading statements?
   * **Completeness Gaps:** Does it fully address all aspects of the original prompt? Is anything missing?
   * **Clarity & Coherence:** Is the language clear, concise, and easy to understand? Does it flow logically?
   * **Tone & Style:** Does it match the desired tone and style (e.g., professional, engaging, concise)?
   * **Engagement:** Is it captivating? Does it hold the reader's attention?
   * **Redundancy/Verbosity:** Can any parts be condensed or removed without losing meaning?
4.  **Propose Specific Improvements:** For each identified weakness, suggest concrete and actionable changes. Do not just state the problem; propose a solution.
5.  **Generate Revised Content:** Based on your proposed improvements, rewrite the original content to incorporate all the necessary changes. Ensure the revised content is polished and ready for final use.

**Original Prompt/Requirements:** "Write a short, engaging social media post (max 150 characters) announcing a new eco-friendly product line: 'GreenTech Gadgets'."

**Initial Draft (Content to be corrected):**
"We have new products. They are green and techy. Buy GreenTech Gadgets now!" (64 characters)

**Self-Correction Agent's Thought Process (Internal CoT Output - encouraged by the prompt):**
**Thought 1 (Understand Original Requirements):**
- Short, engaging social media post.
- Max 150 characters.
- Announce "GreenTech Gadgets" - a new eco-friendly product line.

**Thought 2 (Analyze Current Content):**
"We have new products. They are green and techy. Buy GreenTech Gadgets now!" (64 characters)

**Thought 3 (Identify Discrepancies/Weaknesses):**
- **Engaging:** Not very engaging. Sounds generic.
- **Eco-friendly:** Implied by "green," but not explicitly highlighted as a benefit.
- **Call to Action:** "Buy now!" is okay, but could be more compelling.
- **Conciseness:** It's short, but could use stronger verbs/phrasing.
- **Impact:** Lacks excitement for a new product launch.

**Thought 4 (Propose Specific Improvements):**
- Make it more dynamic and exciting.
- Emphasize "eco-friendly" and "innovation."
- Use stronger verbs and more active voice.
- Add a clear, engaging call to action.
- Ensure it stays under 150 characters.

**Thought 5 (Generate Revised Content):**
Original: "We have new products. They are green and techy. Buy GreenTech Gadgets now!"
Revised idea 1: "🌱 Discover GreenTech Gadgets! Our new eco-friendly line blends innovation with sustainability. Go green, go smart! Shop now! #EcoFriendly #GreenTech" (148 characters)

This revision directly addresses eco-friendliness, uses emojis for engagement, adds a stronger call to action, and includes relevant hashtags while staying within the character limit.

**Self-Correction Agent's Final Revised Content (Output to User):**
🌱 Discover GreenTech Gadgets! Our new eco-friendly line blends innovation with sustainability. Go green, go smart! Shop now! #EcoFriendly #GreenTech
```

Fundamentally, this technique integrates a quality control measure directly into the Agent's content generation, yielding more refined, precise, and superior results that more effectively meet intricate user demands.

从根本上说，这种技术将质量控制措施直接集成到智能体的内容生成过程中，产生更精炼、准确和优质的结果，从而更有效地满足复杂的用户需求。

**Program-Aided Language Models (PALMs)** integrate LLMs with symbolic reasoning capabilities. This integration allows the LLM to generate and execute code, such as Python, as part of its problem-solving process. PALMs offload complex calculations, logical operations, and data manipulation to a deterministic programming environment. This approach utilizes the strengths of traditional programming for tasks where LLMs might exhibit limitations in accuracy or consistency. When faced with symbolic challenges, the model can produce code, execute it, and convert the results into natural language. This hybrid methodology combines the LLM's understanding and generation abilities with precise computation, enabling the model to address a wider range of complex problems with potentially increased reliability and accuracy. This is important for agents as it allows them to perform more accurate and reliable actions by leveraging precise computation alongside their understanding and generation capabilities. An example is the use of external tools within Google's ADK for generating code.

**程序辅助语言模型（Program-Aided Language Models，PALMs）**将 LLM 与符号推理能力相结合。这种集成允许 LLM 在问题解决过程中生成和执行代码，例如 Python。PALMs 将复杂的计算、逻辑操作和数据操作卸载到确定性编程环境中。这种方法利用传统编程的优势来处理 LLM 在准确性或一致性方面可能存在局限的任务。当面对符号推理挑战时，模型可以生成代码、执行代码，并将结果转换为自然语言。这种混合方法结合了 LLM 的理解和生成能力与精确计算，使模型能够以更高的可靠性和准确性解决更广泛的复杂问题。这对智能体很重要，因为它允许它们通过在理解和生成能力之外利用精确计算来执行更准确和可靠的动作。一个例子是在 Google 的 ADK 中使用外部工具生成代码。

```python
from google.adk.tools import agent_tool
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.code_executors import BuiltInCodeExecutor

search_agent = Agent(
    model='gemini-2.0-flash',
    name='SearchAgent',
    instruction="""
    You're a specialist in Google Search
    """,
    tools=[google_search],
)

coding_agent = Agent(
    model='gemini-2.0-flash',
    name='CodeAgent',
    instruction="""
    You're a specialist in Code Execution
    """,
    code_executor=[BuiltInCodeExecutor],
)

root_agent = Agent(
    name="RootAgent",
    model="gemini-2.0-flash",
    description="Root Agent",
    tools=[
        agent_tool.AgentTool(agent=search_agent),
        agent_tool.AgentTool(agent=coding_agent)
    ],
)
```

**Reinforcement Learning with Verifiable Rewards (RLVR):** While effective, the standard Chain-of-Thought (CoT) prompting used by many LLMs is a somewhat basic approach to reasoning. It generates a single, predetermined line of thought without adapting to the complexity of the problem. To overcome these limitations, a new class of specialized "reasoning models" has been developed. These models operate differently by dedicating a variable amount of "thinking" time before providing an answer. This "thinking" process produces a more extensive and dynamic Chain-of-Thought that can be thousands of tokens long. This extended reasoning allows for more complex behaviors like self-correction and backtracking, with the model dedicating more effort to harder problems. The key innovation enabling these models is a training strategy called Reinforcement Learning from Verifiable Rewards (RLVR). By training the model on problems with known correct answers (like math or code), it learns through trial and error to generate effective, long-form reasoning. This allows the model to evolve its problem-solving abilities without direct human supervision. Ultimately, these reasoning models don't just produce an answer; they generate a "reasoning trajectory" that demonstrates advanced skills like planning, monitoring, and evaluation. This enhanced ability to reason and strategize is fundamental to the development of autonomous AI agents, which can break down and solve complex tasks with minimal human intervention.

**可验证奖励强化学习（Reinforcement Learning with Verifiable Rewards，RLVR）**：虽然有效，但许多 LLM 使用的标准思维链（CoT）提示词是一种相对基础的推理方法。它生成单一的、预定的思路，而无法适应问题的复杂性。为了克服这些限制，开发了一类新的专门"推理模型"。这些模型的运行方式有所不同，在提供答案之前专门花费可变量的"思考"时间。这个"思考"过程产生更广泛和动态的思维链，可能长达数千个 token。这种扩展推理允许更复杂的行为，如自我纠正和回溯，模型在更困难的问题上投入更多计算资源。实现这些模型的关键创新是一种称为可验证奖励强化学习（RLVR）的训练策略。通过在具有已知正确答案的问题（如数学或代码）上训练模型，它通过试错学习生成有效的长篇推理。这使得模型能够在没有直接人类监督的情况下发展其问题解决能力。最终，这些推理模型不仅产生答案，还生成展示规划、监控和评估等高级技能的"推理轨迹"。这种增强的推理和策略能力是开发自主 AI 智能体的基础，使它们能够在最少人类干预的情况下分解和解决复杂任务。

**ReAct** (Reasoning and Acting, see Fig. 3, where KB stands for Knowledge Base) is a paradigm that integrates Chain-of-Thought (CoT) prompting with an agent's ability to interact with external environments through tools. Unlike generative models that produce a final answer, a ReAct agent reasons about which actions to take. This reasoning phase involves an internal planning process, similar to CoT, where the agent determines its next steps, considers available tools, and anticipates outcomes. Following this, the agent acts by executing a tool or function call, such as querying a database, performing a calculation, or interacting with an API. 

**ReAct**（推理与行动，见图 3，其中 KB 代表知识库）是一种将思维链（CoT）提示词与智能体通过工具与外部环境交互的能力相结合的范式。与直接生成最终答案的生成模型不同，ReAct 智能体对采取哪些行动进行推理。这个推理阶段涉及内部规划过程，类似于 CoT，智能体确定下一步行动，考虑可用工具并预测可能的结果。然后，智能体通过执行工具或工具调用来行动，例如查询数据库、执行计算或与 API 交互。

![][image3]

Fig.3: Reasoning and Act

图 3：推理和行动

ReAct operates in an interleaved manner: the agent executes an action, observes the outcome, and incorporates this observation into subsequent reasoning. This iterative loop of "Thought, Action, Observation, Thought..." allows the agent to dynamically adapt its plan, correct errors, and achieve goals requiring multiple interactions with the environment. This provides a more robust and flexible problem-solving approach compared to linear CoT, as the agent responds to real-time feedback. By combining language model understanding and generation with the capability to use tools, ReAct enables agents to perform complex tasks requiring both reasoning and practical execution. This approach is crucial for agents as it allows them to not only reason but also to practically execute steps and interact with dynamic environments.

ReAct 以交错的方式运行：智能体执行一个动作，观察结果，并将此观察纳入后续推理。这种"思考、行动、观察、思考..."的迭代循环允许智能体调整计划、纠正错误并实现需要与环境进行多次交互的目标。与线性 CoT 相比，这提供了更强大和灵活的问题解决方法，因为智能体能够响应实时反馈。通过结合语言模型的理解和生成能力与使用工具的能力，ReAct 使智能体能够执行需要推理和实际执行的复杂任务。这种方法对智能体至关重要，因为它允许它们不仅进行推理，还可以实际执行步骤并与动态环境交互。

**CoD** (Chain of Debates) is a formal AI framework proposed by Microsoft where multiple, diverse models collaborate and argue to solve a problem, moving beyond a single AI's "chain of thought." This system operates like an AI council meeting, where different models present initial ideas, critique each other's reasoning, and exchange counterarguments. The primary goal is to enhance accuracy, reduce bias, and improve the overall quality of the final answer by leveraging collective intelligence. Functioning as an AI version of peer review, this method creates a transparent and trustworthy record of the reasoning process. Ultimately, it represents a shift from a solitary Agent providing an answer to a collaborative team of Agents working together to find a more robust and validated solution.

**CoD**（辩论链，Chain of Debates）是微软提出的一种正式 AI 框架，其中多个不同的模型协作和争论以解决问题，超越了单个 AI 的"思维链"。该系统运作类似于 AI 委员会会议，不同的模型提出初步想法，批评彼此的推理，并交换反驳论点。主要目标是通过利用集体智慧来提高准确性、减少偏见并改善最终答案的整体质量。作为 AI 版本的同行评审，这种方法创建了推理过程的透明和可信记录。最终，它代表了从单独智能体提供答案到协作智能体团队共同寻找更可靠和验证的解决方案的转变。

**GoD** (Graph of Debates)  is an advanced Agentic framework that reimagines discussion as a dynamic, non-linear network rather than a simple chain. In this model, arguments are individual nodes connected by edges that signify relationships like 'supports' or 'refutes,' reflecting the multi-threaded nature of real debate. This structure allows new lines of inquiry to dynamically branch off, evolve independently, and even merge over time. A conclusion is reached not at the end of a sequence, but by identifying the most robust and well-supported cluster of arguments within the entire graph. In this context, "well-supported" refers to knowledge that is firmly established and verifiable. This can include information considered to be ground truth, which means it is inherently correct and widely accepted as fact. Additionally, it encompasses factual evidence obtained through search grounding, where information is validated against external sources and real-world data. Finally, it also pertains to a consensus reached by multiple models during a debate, indicating a high degree of agreement and confidence in the information presented. This comprehensive approach ensures a more robust and reliable foundation for the information being discussed. This approach provides a more holistic and realistic model for complex, collaborative AI reasoning.

**GoD**（辩论图，Graph of Debates）是一个高级 Agentic 框架，它将讨论重新构想为动态的、非线性网络，而不是简单的链式结构。在这个模型中，论点是由表示"支持"或"反驳"等关系的边连接的各个节点，反映了真实辩论的多线程性质。这种结构允许新的探究线索动态分支、独立演化，甚至随时间合并。结论不是在序列的末尾达成，而是通过识别整个图中最稳健和得到良好支持的论点集群来达成。在这种情况下，"得到良好支持"是指已牢固建立和可验证的知识。这包括被认为是基本事实的信息，即本质上是正确的并被广泛接受为事实的内容。此外，它包括通过搜索基础获得的事实证据，其中信息针对外部来源和现实世界数据进行验证。最后，它还涉及在辩论期间由多个模型达成的共识，表明对所呈现信息的高度一致和信心。这种全面的方法确保了所讨论信息的更稳健和可靠的基础。这种方法为复杂的、协作的 AI 推理提供了更全面和现实的模型。

**MASS (optional advanced topic):** An in-depth analysis of the design of multi-agent systems reveals that their effectiveness is critically dependent on both the quality of the prompts used to program individual agents and the topology that dictates their interactions. The complexity of designing these systems is significant, as it involves a vast and intricate search space. To address this challenge, a novel framework called Multi-Agent System Search (MASS) was developed to automate and optimize the design of MAS.

**MASS（可选高级主题）**：对多智能体设计的深入分析表明，其有效性严重依赖于各个智能体的提示词质量以及决定其交互的拓扑结构。设计这些系统的复杂性非常显著，因为它涉及一个庞大而复杂的搜索空间。为了应对这一挑战，开发了一个名为多智能体系统搜索（Multi-Agent System Search，MASS）的新框架来自动化和优化多智能体系统的设计。

MASS employs a multi-stage optimization strategy that systematically navigates the complex design space by interleaving prompt and topology optimization (see Fig. 4)

MASS 采用多阶段优化策略，通过交错进行提示词和拓扑优化来系统地导航复杂的设计空间（见图 4）

**1\. Block-Level Prompt Optimization:** The process begins with a local optimization of prompts for individual agent types, or "blocks," to ensure each component performs its role effectively before being integrated into a larger system. This initial step is crucial as it ensures that the subsequent topology optimization builds upon well-performing agents, rather than suffering from the compounding impact of poorly configured ones. For example, when optimizing for the HotpotQA dataset, the prompt for a "Debator" agent is creatively framed to instruct it to act as an "expert fact-checker for a major publication". Its optimized task is to meticulously review proposed answers from other agents, cross-reference them with provided context passages, and identify any inconsistencies or unsupported claims. This specialized role-playing prompt, discovered during block-level optimization, aims to make the debator agent highly effective at synthesizing information before it's even placed into a larger workflow.

**1. 块级提示词优化**：该过程从对各个智能体类型或"块"的提示词进行局部优化开始，以确保每个组件在集成到更大系统之前能够有效执行其角色。这个初始步骤至关重要，因为它确保后续的拓扑优化建立在性能良好的智能体基础上，而不是受到配置不当的智能体的复合影响。例如，在针对 HotpotQA 数据集进行优化时，"Debator"智能体的提示词被创造性地构建为指示它充当"主要出版物的专家事实核查员"。其优化的任务是仔细审查来自其他智能体的建议答案，与提供的上下文段落交叉引用，并识别任何不一致或不受支持的声明。这种在块级优化期间发现的专门角色扮演提示词旨在使辩论者智能体在被放入更大工作流之前在综合信息方面非常有效。

**2\. Workflow Topology Optimization:** Following local optimization, MASS optimizes the workflow topology by selecting and arranging different agent interactions from a customizable design space. To make this search efficient, MASS employs an influence-weighted method. This method calculates the "incremental influence" of each topology by measuring its performance gain relative to a baseline agent and uses these scores to guide the search toward more promising combinations. For instance, when optimizing for the MBPP coding task, the topology search discovers that a specific hybrid workflow is most effective. The best-found topology is not a simple structure but a combination of an iterative refinement process with external tool use. Specifically, it consists of one predictor agent that engages in several rounds of reflection, with its code being verified by one executor agent that runs the code against test cases. This discovered workflow shows that for coding, a structure that combines iterative self-correction with external verification is superior to simpler MAS designs.

**2. 工作流拓扑优化**：在局部优化之后，MASS 通过从可自定义的设计空间中选择和安排不同的智能体交互来优化工作流拓扑。为了使这种搜索有效，MASS 采用影响加权方法。该方法通过测量每个拓扑相对于基线智能体的性能增益来计算其"增量影响"，并使用这些分数来引导搜索朝向更有前途的组合。例如，在针对 MBPP 编码任务进行优化时，拓扑搜索发现特定的混合工作流最有效。找到的最佳拓扑不是简单的结构，而是迭代改进过程与外部工具使用的组合。具体来说，它由一个进行多轮反思的预测器智能体组成，其代码由一个针对测试用例运行代码的执行器智能体验证。这个发现的工作流表明，对于编码任务，结合迭代自我纠正和外部验证的结构优于更简单的多智能体系统设计。

![][image4]

Fig. 4: (Courtesy of the Authors): The Multi-Agent System Search (MASS) Framework is a three-stage optimization process that navigates a search space encompassing optimizable prompts (instructions and demonstrations) and configurable agent building blocks (Aggregate, Reflect, Debate, Summarize, and Tool-use). The first stage, Block-level Prompt Optimization, independently optimizes prompts for each agent module. Stage two, Workflow Topology Optimization, samples valid system configurations from an influence-weighted design space, integrating the optimized prompts. The final stage, Workflow-level Prompt Optimization, involves a second round of prompt optimization for the entire multi-agent system after the optimal workflow from Stage two has been identified.

图 4：（由作者提供）：多智能体搜索（MASS）框架是一个三阶段优化过程，导航包含可优化提示词（指令和演示）和可配置智能体构建块（聚合、反思、辩论、总结和工具使用）的搜索空间。第一阶段，块级提示词优化，独立优化每个智能体模块的提示词。第二阶段，工作流拓扑优化，从影响加权的设计空间中采样有效的系统配置，集成优化的提示词。最后阶段，工作流级提示词优化，在从第二阶段识别出最优工作流后，对整个多智能体系统进行第二轮提示词优化。

**3\. Workflow-Level Prompt Optimization:** The final stage involves a global optimization of the entire system's prompts. After identifying the best-performing topology, the prompts are fine-tuned as a single, integrated entity to ensure they are tailored for orchestration and that agent interdependencies are optimized. As an example, after finding the best topology for the DROP dataset, the final optimization stage refines the "Predictor" agent's prompt. The final, optimized prompt is highly detailed, beginning by providing the agent with a summary of the dataset itself, noting its focus on "extractive question answering" and "numerical information". It then includes few-shot examples of correct question-answering behavior and frames the core instruction as a high-stakes scenario: "You are a highly specialized AI tasked with extracting critical numerical information for an urgent news report. A live broadcast is relying on your accuracy and speed". This multi-faceted prompt, combining meta-knowledge, examples, and role-playing, is tuned specifically for the final workflow to maximize accuracy.

**3. 工作流级提示词优化**：最后阶段涉及对整个系统提示词的全局优化。在识别出性能最佳的拓扑之后，提示词作为单一的集成实体进行微调，以确保它们针对编排进行定制，并优化智能体的相互依赖性。例如，在找到 DROP 数据集的最佳拓扑后，最终优化阶段改进"Predictor"智能体的提示词。最终优化的提示词非常详细，首先向智能体提供数据集本身的摘要，指出其重点是"抽取式问答"和"数字信息"。然后包括正确问答行为的少样本示例，并将核心指令框架为高风险场景："您是一个高度专业的 AI，负责为紧急新闻报道提取关键数字信息。现场直播依赖于您的准确性和速度"。这个多方面的提示词，结合元知识、示例和角色扮演，专门针对最终工作流进行调优以最大化准确性。

Key Findings and Principles: Experiments demonstrate that MAS optimized by MASS significantly outperform existing manually designed systems and other automated design methods across a range of tasks. The key design principles for effective MAS, as derived from this research, are threefold:

关键发现和原则：实验表明，经 MASS 优化的多智能体在一系列任务中显著优于现有的手动设计系统和其他自动设计方法。从这项研究中得出的有效多智能体的关键设计原则有三个方面：

* Optimize individual agents with high-quality prompts before composing them.  

* 在组合智能体之前，使用高质量提示词优化各个智能体。

* Construct MAS by composing influential topologies rather than exploring an unconstrained search space.  

* 通过组合有影响力的拓扑而不是探索无约束的搜索空间来构建多智能体系统。

* Model and optimize the interdependencies between agents through a final, workflow-level joint optimization.

* 通过最终的工作流级联合优化来建模和优化智能体的相互依赖性。

Building on our discussion of key reasoning techniques, let's first examine a core performance principle: the Scaling Inference Law for LLMs. This law states that a model's performance predictably improves as the computational resources allocated to it increase. We can see this principle in action in complex systems like Deep Research, where an AI agent leverages these resources to autonomously investigate a topic by breaking it down into sub-questions, using Web search as a tool, and synthesizing its findings.

在讨论了关键推理技术的基础上，让我们研究一个核心性能原则：LLM 的推理扩展定律。该定律指出，模型的性能可预测地随着分配给它的计算资源的增加而提高。我们可以在 Deep Research 等复杂系统中看到这一原则的实际应用，其中 AI 智能体利用这些资源通过将主题分解为子问题、使用网络搜索作为工具并综合其发现来自主调查主题。

**Deep Research.** The term "Deep Research" describes a category of AI Agentic tools designed to act as tireless, methodical research assistants. Major platforms in this space include Perplexity AI, Google's Gemini research capabilities, and OpenAI's advanced functions within ChatGPT (see Fig.5).

**Deep Research**：术语"Deep Research"描述了一类旨在充当不知疲倦、有条不紊的研究助手的 AI Agentic 工具。这一领域的主要平台包括 Perplexity AI、Google 的 Gemini 研究能力和 OpenAI 的 ChatGPT 高级功能（见图 5）。

![][image5]

Fig. 5: Google Deep Research for Information Gathering

图 5：Google Deep Research 用于信息收集

A fundamental shift introduced by these tools is the change in the search process itself. A standard search provides immediate links, leaving the work of synthesis to you. Deep Research operates on a different model. Here, you task an AI with a complex query and grant it a "time budget"—usually a few minutes. In return for this patience, you receive a detailed report.

这些工具引入的一个基本转变是搜索过程本身的变化。标准搜索提供即时链接，将综合工作留给用户。Deep Research 采用不同的工作模式。在这里，用户为 AI 分配一个复杂的查询并授予它一个"时间预算"——通常是几分钟。作为这种耐心的回报，用户会收到详细的报告。

During this time, the AI works on your behalf in an agentic way. It autonomously performs a series of sophisticated steps that would be incredibly time-consuming for a person:

在此期间，AI 以 agentic 方式代表用户工作。它自主执行一系列复杂的步骤，这些步骤对于人类来说将是非常耗时的：

1. Initial Exploration: It runs multiple, targeted searches based on your initial prompt.  

1. 初始探索：根据用户的初始提示词运行多个有针对性的搜索。

2. Reasoning and Refinement: It reads and analyzes the first wave of results, synthesizes the findings, and critically identifies gaps, contradictions, or areas that require more detail.  

2. 推理和改进：阅读和分析第一波结果，综合发现，并批判性地识别差距、矛盾或需要更多细节的领域。

3. Follow-up Inquiry: Based on its internal reasoning, it conducts new, more nuanced searches to fill those gaps and deepen its understanding.  

3. 后续查询：基于内部推理，进行新的、更细致的搜索以填补这些差距并加深理解。

4. Final Synthesis: After several rounds of this iterative searching and reasoning, it compiles all the validated information into a single, cohesive, and structured summary.

4. 最终综合：经过几轮这种迭代搜索和推理，将所有验证的信息编译成一个单一的、连贯的、结构化的摘要。

This systematic approach ensures a comprehensive and well-reasoned response, significantly enhancing the efficiency and depth of information gathering, thereby facilitating more agentic decision-making.

这种系统方法确保了全面和合理的响应，显著提高了信息收集的效率和深度，从而促进更 agentic 的决策过程。

## Scaling Inference Law

**推理扩展定律**

This critical principle dictates the relationship between an LLM's performance and the computational resources allocated during its operational phase, known as inference. The Inference Scaling Law differs from the more familiar scaling laws for training, which focus on how model quality improves with increased data volume and computational power during a model's creation. Instead, this law specifically examines the dynamic trade-offs that occur when an LLM is actively generating an output or answer.

这个关键原则决定了 LLM 性能与其运营阶段（称为推理）期间分配的计算资源之间的关系。推理扩展定律不同于更熟悉的训练扩展定律，后者关注模型质量如何随着模型创建期间数据量和计算能力的增加而提高。相反，该定律专门研究 LLM 主动生成输出或答案时发生的动态权衡。

A cornerstone of this law is the revelation that superior results can frequently be achieved from a comparatively smaller LLM by augmenting the computational investment at inference time. This doesn't necessarily mean using a more powerful GPU, but rather employing more sophisticated or resource-intensive inference strategies. A prime example of such a strategy is instructing the model to generate multiple potential answers—perhaps through techniques like diverse beam search or self-consistency methods—and then employing a selection mechanism to identify the most optimal output. This iterative refinement or multiple-candidate generation process demands more computational cycles but can significantly elevate the quality of the final response.

该定律的基石是揭示，通过增加推理时间的计算投资，通常可以从相对较小的 LLM 获得优越的结果。这并不一定意味着使用更强大的 GPU，而是采用更复杂或资源密集型的推理策略。这种策略的一个主要例子是指示模型生成多个潜在答案——可能通过多样化束搜索或自一致性方法等技术——然后使用选择机制来识别最优输出。这种迭代改进或多候选生成过程需要更多的计算周期，但可以显著提高最终响应的质量。

This principle offers a crucial framework for informed and economically sound decision-making in the deployment of Agents systems. It challenges the intuitive notion that a larger model will always yield better performance. The law posits that a smaller model, when granted a more substantial "thinking budget" during inference, can occasionally surpass the performance of a much larger model that relies on a simpler, less computationally intensive generation process. The "thinking budget" here refers to the additional computational steps or complex algorithms applied during inference, allowing the smaller model to explore a wider range of possibilities or apply more rigorous internal checks before settling on an answer.

这个原则为智能体部署中明智和经济合理的决策提供了关键框架。它挑战了更大模型总是产生更好性能的直观概念。该定律认为，当在推理期间被授予更充足的"思考预算"时，较小的模型有时可以超越依赖更简单、计算密集度较低的生成过程的更大模型。这里的"思考预算"是指在推理期间应用的额外计算步骤或复杂算法，允许较小的模型探索更广泛的可能性范围或在确定答案之前应用更严格的内部检查。

Consequently, the Scaling Inference Law becomes fundamental to constructing efficient and cost-effective Agentic systems. It provides a methodology for meticulously balancing several interconnected factors:

因此，推理扩展定律成为构建高效和具有成本效益的 Agentic 系统的基础。它提供了一种方法来仔细平衡几个相互关联的因素：

* **Model Size:** Smaller models are inherently less demanding in terms of memory and storage.  

* **模型大小**：较小的模型在内存和存储方面本质上要求较低。

* **Response Latency:** While increased inference-time computation can add to latency, the law helps identify the point at which the performance gains outweigh this increase, or how to strategically apply computation to avoid excessive delays.  

* **响应延迟**：虽然增加的推理时间计算可能会增加延迟，但该定律有助于识别性能增益超过这种增加的点，或如何战略性地应用计算以避免过度延迟。

* **Operational Cost:** Deploying and running larger models typically incurs higher ongoing operational costs due to increased power consumption and infrastructure requirements. The law demonstrates how to optimize performance without unnecessarily escalating these costs.

* **运营成本**：部署和运行更大的模型通常会因增加的功耗和基础设施要求而产生更高的持续运营成本。该定律演示了如何在不必要地提高这些成本的情况下优化性能。

By understanding and applying the Scaling Inference Law, developers and organizations can make strategic choices that lead to optimal performance for specific agentic applications, ensuring that computational resources are allocated where they will have the most significant impact on the quality and utility of the LLM's output. This allows for more nuanced and economically viable approaches to AI deployment, moving beyond a simple "bigger is better" paradigm.

通过理解和应用推理扩展定律，开发人员和组织可以做出战略选择，从而为特定的 agentic 应用实现最佳性能，确保计算资源分配到它们对 LLM 输出的质量和效用产生最显著影响的地方。这允许更细致和经济可行的 AI 部署方法，超越简单的"更大就是更好"的范式。

## Hands-On Code Example
## 实践代码示例

The DeepSearch code, open-sourced by Google, is available through the gemini-fullstack-langgraph-quickstart repository (Fig. 6). This repository provides a template for developers to construct full-stack AI agents using Gemini 2.5 and the LangGraph orchestration framework. This open-source stack facilitates experimentation with agent-based architectures and can be integrated with local LLLMs such as Gemma. It utilizes Docker and modular project scaffolding for rapid prototyping. It should be noted that this release serves as a well-structured demonstration and is not intended as a production-ready backend.

Google 开源的 DeepSearch 代码可通过 gemini-fullstack-langgraph-quickstart 存储库获得（图 6）。该存储库为开发人员提供了使用 Gemini 2.5 和 LangGraph 编排框架构建全栈 AI 智能体的模板。这个开源堆栈促进了基于智能体的架构实验，并可以与本地 LLM（如 Gemma）集成。它利用 Docker 和模块化项目脚手架进行快速原型设计。需要注意的是，此版本作为一个结构良好的演示，并不打算作为生产就绪的后端。

![][image6]

Fig. 6: (Courtesy of authors) Example of DeepSearch with multiple Reflection steps

图 6：（由作者提供）具有多个反思步骤的 DeepSearch 示例

This project provides a full-stack application featuring a React frontend and a LangGraph backend, designed for advanced research and conversational AI. A LangGraph agent dynamically generates search queries using Google Gemini models and integrates web research via the Google Search API. The system employs reflective reasoning to identify knowledge gaps, refine searches iteratively, and synthesize answers with citations. The frontend and backend support hot-reloading. The project's structure includes separate frontend/ and backend/ directories. Requirements for setup include Node.js, npm, Python 3.8+, and a Google Gemini API key. After configuring the API key in the backend's .env file, dependencies for both the backend (using pip install .) and frontend (npm install) can be installed. Development servers can be run concurrently with make dev or individually. The backend agent, defined in backend/src/agent/graph.py, generates initial search queries, conducts web research, performs knowledge gap analysis, refines queries iteratively, and synthesizes a cited answer using a Gemini model. Production deployment involves the backend server delivering a static frontend build and requires Redis for streaming real-time output and a Postgres database for managing data. A Docker image can be built and run using docker-compose up, which also requires a LangSmith API key for the docker-compose.yml example. The application uses React with Vite, Tailwind CSS, Shadcn UI, LangGraph, and Google Gemini. The project is licensed under the Apache License 2.0.

该项目提供了一个具有 React 前端和 LangGraph 后端的全栈应用程序，专为高级研究和对话式 AI 而设计。LangGraph 智能体使用 Google Gemini 模型动态生成搜索查询，并通过 Google Search API 集成网络研究。系统采用反思推理来识别知识差距、迭代改进搜索并综合带引用的答案。前端和后端支持热重载。项目结构包括单独的 frontend/ 和 backend/ 目录。设置要求包括 Node.js、npm、Python 3.8+ 和 Google Gemini API 密钥。在后端的 .env 文件中配置 API 密钥后，可以为后端（使用 pip install .）和前端（npm install）安装依赖项。开发服务器可以使用 make dev 同时运行或单独运行。在 backend/src/agent/graph.py 中定义的后端智能体生成初始搜索查询、进行网络研究、执行知识差距分析、迭代改进查询并使用 Gemini 模型综合带引用的答案。生产部署涉及后端服务器提供静态前端构建，并需要 Redis 用于流式实时输出和 Postgres 数据库用于管理数据。可以使用 docker-compose up 构建和运行 Docker 镜像，这也需要 docker-compose.yml 示例的 LangSmith API 密钥。该应用使用带 Vite 的 React、Tailwind CSS、Shadcn UI、LangGraph 和 Google Gemini。该项目在 Apache License 2.0 下授权。

```python
## Create our Agent Graph
builder = StateGraph(OverallState, config_schema=Configuration)

## Define the nodes we will cycle between
builder.add_node("generate_query", generate_query)
builder.add_node("web_research", web_research)
builder.add_node("reflection", reflection)
builder.add_node("finalize_answer", finalize_answer)

## Set the entrypoint as `generate_query`
## This means that this node is the first one called
builder.add_edge(START, "generate_query")

## Add conditional edge to continue with search queries in a parallel branch
builder.add_conditional_edges(
    "generate_query",
    continue_to_web_research,
    ["web_research"]
)

## Reflect on the web research
builder.add_edge("web_research", "reflection")

## Evaluate the research
builder.add_conditional_edges(
    "reflection",
    evaluate_research,
    ["web_research", "finalize_answer"]
)

## Finalize the answer
builder.add_edge("finalize_answer", END)

graph = builder.compile(name="pro-search-agent")
```

Fig. 6: Example of DeepSearch with LangGraph (code from backend/src/agent/graph.py)

图 6：使用 LangGraph 的 DeepSearch 示例（来自 backend/src/agent/graph.py 的代码）

## So, what do agents think?
## 智能体的思考过程

In summary, an agent's thinking process is a structured approach that combines reasoning and acting to solve problems. This method allows an agent to explicitly plan its steps, monitor its progress, and interact with external tools to gather information.

总之，智能体的思考过程是一种结合推理和行动来解决问题的结构化方法。这种方法允许智能体规划其步骤、监控其进展并与外部工具交互以收集信息。

At its core, the agent's "thinking" is facilitated by a powerful LLM. This LLM generates a series of thoughts that guide the agent's subsequent actions. The process typically follows a thought-action-observation loop:

其核心是，智能体的"思考"由强大的 LLM 驱动。这个 LLM 生成一系列指导智能体行动的思考。该过程通常遵循思考-行动-观察循环：

1. **Thought:** The agent first generates a textual thought that breaks down the problem, formulates a plan, or analyzes the current situation. This internal monologue makes the agent's reasoning process transparent and steerable.  

1. **思考**：智能体首先生成分解问题、制定计划或分析当前情况的文本思考。这种内部独白使智能体的推理过程透明且可引导。

2. **Action:** Based on the thought, the agent selects an action from a predefined, discrete set of options. For example, in a question-answering scenario, the action space might include searching online, retrieving information from a specific webpage, or providing a final answer.  

2. **行动**：基于思考，智能体从预定义的离散选项集中选择一个行动。例如，在问答场景中，行动空间可能包括在线搜索、从特定网页检索信息或提供最终答案。

3. **Observation:** The agent then receives feedback from its environment based on the action taken. This could be the results of a web search or the content of a webpage.

3. **观察**：智能体然后根据所采取的行动从其环境接收反馈。这可能是网络搜索的结果或网页的内容。

This cycle repeats, with each observation informing the next thought, until the agent determines that it has reached a final solution and performs a "finish" action.

这个循环重复进行，每个观察通知下一个思考，直到智能体确定它已达到最终解决方案并执行"完成"行动。

The effectiveness of this approach relies on the advanced reasoning and planning capabilities of the underlying LLM. To guide the agent, the ReAct framework often employs few-shot learning, where the LLM is provided with examples of human-like problem-solving trajectories. These examples demonstrate how to effectively combine thoughts and actions to solve similar tasks.

这种方法的有效性依赖于底层 LLM 的高级推理和规划能力。为了指导智能体，ReAct 框架通常采用少样本学习，其中向 LLM 提供类似人类问题解决轨迹的示例。这些示例演示了如何有效地结合思考和行动来解决类似任务。

The frequency of an agent's thoughts can be adjusted depending on the task. For knowledge-intensive reasoning tasks like fact-checking, thoughts are typically interleaved with every action to ensure a logical flow of information gathering and reasoning. In contrast, for decision-making tasks that require many actions, such as navigating a simulated environment, thoughts may be used more sparingly, allowing the agent to decide when thinking is necessary

智能体思考的频率可以根据任务进行调整。对于知识密集型推理任务（如事实核查），思考通常与每个行动交错，以确保信息收集和推理的逻辑流动。相比之下，对于需要许多行动的决策任务（例如在模拟环境中导航），思考可能更谨慎地使用，允许智能体决定何时需要思考。

## At a Glance
## 速览

**What**: Complex problem-solving often requires more than a single, direct answer, posing a significant challenge for AI. The core problem is enabling AI agents to tackle multi-step tasks that demand logical inference, decomposition, and strategic planning. Without a structured approach, agents may fail to handle intricacies, leading to inaccurate or incomplete conclusions. These advanced reasoning methodologies aim to make an agent's internal "thought" process explicit, allowing it to systematically work through challenges.

**问题背景**：复杂的问题解决通常需要的不仅仅是单一的、直接的答案，这对 AI 构成了重大挑战。核心问题是使 AI 智能体能够处理需要逻辑推理、分解和战略规划的多步骤任务。如果没有结构化的方法，智能体可能无法处理复杂性，导致不准确或不完整的结论。这些高级推理方法旨在使智能体的内部"思考"过程明确，使其能够系统地处理挑战。

**Why:** The standardized solution is a suite of reasoning techniques that provide a structured framework for an agent's problem-solving process. Methodologies like Chain-of-Thought (CoT) and Tree-of-Thought (ToT) guide LLMs to break down problems and explore multiple solution paths. Self-Correction allows for the iterative refinement of answers, ensuring higher accuracy. Agentic frameworks like ReAct integrate reasoning with action, enabling agents to interact with external tools and environments to gather information and adapt their plans. This combination of explicit reasoning, exploration, refinement, and tool use creates more robust, transparent, and capable AI systems.

**解决方案**：标准化解决方案是一套为智能体的问题解决过程提供结构化框架的推理技术。像思维链（CoT）和思维树（ToT）这样的方法指导 LLM 分解问题并探索多个解决路径。自我纠正允许答案的迭代改进，确保更高的准确性。像 ReAct 这样的 Agentic 框架将推理与行动集成，使智能体能够与外部工具和环境交互以收集信息并调整其计划。这种明确推理、探索、改进和工具使用的组合创建了更强大、透明和有能力的 AI 系统。

**Rule of thumb:** Use these reasoning techniques when a problem is too complex for a single-pass answer and requires decomposition, multi-step logic, interaction with external data sources or tools, or strategic planning and adaptation. They are ideal for tasks where showing the "work" or thought process is as important as the final answer.

**实践建议**：当问题对于单次通过的答案过于复杂并需要分解、多步骤逻辑、与外部数据源或工具的交互或战略规划和适应时，使用这些推理技术。它们非常适合展示"工作"或思考过程与最终答案同样重要的任务。

**Visual summary**

**可视化摘要**

![][image7]

Fig. 7: Reasoning design pattern

图 7：推理设计模式

## Key Takeaways
## 关键要点

* By making their reasoning explicit, agents can formulate transparent, multi-step plans, which is the foundational capability for autonomous action and user trust.  

* 通过使推理明确，智能体可以制定透明的、多步骤的计划，这是自主行动和用户信任的基础能力。

* The ReAct framework provides agents with their core operational loop, empowering them to move beyond mere reasoning and interact with external tools to dynamically act and adapt within an environment.  

* ReAct 框架为智能体提供了其核心操作循环，使它们能够超越单纯的推理并与外部工具交互，以在环境中动态行动和适应。

* The Scaling Inference Law implies an agent's performance is not just about its underlying model size, but its allocated "thinking time," allowing for more deliberate and higher-quality autonomous actions.  

* 推理扩展定律意味着智能体的性能不仅关乎其底层模型大小，还关乎其分配的"思考时间"，允许更审慎和更高质量的自主行动。

* Chain-of-Thought (CoT) serves as an agent's internal monologue, providing a structured way to formulate a plan by breaking a complex goal into a sequence of manageable actions.  

* 思维链（CoT）作为智能体的内部独白，提供了一种通过将复杂目标分解为一系列可管理的行动来制定计划的结构化方法。

* Tree-of-Thought and Self-Correction give agents the crucial ability to deliberate, allowing them to evaluate multiple strategies, backtrack from errors, and improve their own plans before execution.  

* 思维树和自我纠正赋予智能体关键的审议能力，允许它们评估多个策略、从错误中回溯并在执行前改进自己的计划。

* Collaborative frameworks like Chain of Debates (CoD) signal the shift from solitary agents to multi-agent systems, where teams of agents can reason together to tackle more complex problems and reduce individual biases.  

* 像辩论链（CoD）这样的协作框架标志着从单独智能体到多智能体系统的转变，其中智能体团队可以共同推理以解决更复杂的问题并减少个体偏见。

* Applications like Deep Research demonstrate how these techniques culminate in agents that can execute complex, long-running tasks, such as in-depth investigation, completely autonomously on a user's behalf.  

* 像 Deep Research 这样的应用程序展示了这些技术如何在智能体中达到高潮，这些智能体能够完全自主地代表用户执行复杂的、长期运行的任务，例如深入调查。

* To build effective teams of agents, frameworks like MASS automate the optimization of how individual agents are instructed and how they interact, ensuring the entire multi-agent system performs optimally.  

* 为了构建有效的智能体团队，像 MASS 这样的框架自动化优化各个智能体的指令方式以及它们如何交互，确保整个多智能体系统以最优方式执行。

* By integrating these reasoning techniques, we build agents that are not just automated but truly autonomous, capable of being trusted to plan, act, and solve complex problems without direct supervision.

* 通过集成这些推理技术，我们构建的智能体不仅是自动化的，而且是真正自主的，能够被信任去规划、行动和解决复杂问题而无需直接监督。

## Conclusions
## 结论

Modern AI is evolving from passive tools into autonomous agents, capable of tackling complex goals through structured reasoning. This agentic behavior begins with an internal monologue, powered by techniques like Chain-of-Thought (CoT), which allows an agent to formulate a coherent plan before acting. True autonomy requires deliberation, which agents achieve through Self-Correction and Tree-of-Thought (ToT), enabling them to evaluate multiple strategies and independently improve their own work. The pivotal leap to fully agentic systems comes from the ReAct framework, which empowers an agent to move beyond thinking and start acting by using external tools. This establishes the core agentic loop of thought, action, and observation, allowing the agent to dynamically adapt its strategy based on environmental feedback.

现代 AI 正在从被动工具演变为自主智能体，能够通过结构化推理解决复杂目标。这种 agentic 行为始于由思维链（CoT）等技术驱动的内部独白，允许智能体在行动前制定连贯的计划。真正的自主需要审议，智能体通过自我纠正和思维树（ToT）实现这一点，使它们能够评估多个策略并独立改进自己的工作。向完全 agentic 系统的关键飞跃来自 ReAct 框架，它使智能体能够超越思考并开始通过使用外部工具来行动。这建立了思考、行动和观察的核心 agentic 循环，允许智能体根据环境反馈动态调整其策略。

An agent's capacity for deep deliberation is fueled by the Scaling Inference Law, where more computational "thinking time" directly translates into more robust autonomous actions. The next frontier is the multi-agent system, where frameworks like Chain of Debates (CoD) create collaborative agent societies that reason together to achieve a common goal. This is not theoretical; agentic applications like Deep Research already demonstrate how autonomous agents can execute complex, multi-step investigations on a user's behalf. The overarching goal is to engineer reliable and transparent autonomous agents that can be trusted to independently manage and solve intricate problems. Ultimately, by combining explicit reasoning with the power to act, these methodologies are completing the transformation of AI into truly agentic problem-solvers.

智能体的深度审议能力由推理扩展定律推动，其中更多的计算"思考时间"直接转化为更稳健的自主行动。下一个前沿是多智能体系统，其中像辩论链（CoD）这样的框架创建协作智能体群体，它们一起推理以实现共同目标。这不是理论性的；像 Deep Research 这样的 agentic 应用程序已经展示了自主智能体如何能够代表用户执行复杂的、多步骤的调查。总体目标是设计可靠和透明的自主智能体，可以被信任独立管理和解决复杂问题。最终，通过将明确推理与行动能力相结合，这些方法正在完成 AI 向真正 agentic 问题解决者的转变。

## References
## 参考文献

Relevant research includes:

相关研究包括：

1. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" by Wei et al. (2022)  

2. "Tree of Thoughts: Deliberate Problem Solving with Large Language Models" by Yao et al. (2023)  

3. "Program-Aided Language Models" by Gao et al. (2023)  

4. "ReAct: Synergizing Reasoning and Acting in Language Models" by Yao et al. (2023)  

5. Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving, 2024  

6. Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies, [https://arxiv.org/abs/2502.02533](https://arxiv.org/abs/2502.02533) 

[image1]: ../images/chapter-17/image1.png

[image2]: ../images/chapter-17/image2.png

[image3]: ../images/chapter-17/image3.png

[image4]: ../images/chapter-17/image4.png

[image5]: ../images/chapter-17/image5.png

[image6]: ../images/chapter-17/image6.png

[image7]: ../images/chapter-17/image7.png
