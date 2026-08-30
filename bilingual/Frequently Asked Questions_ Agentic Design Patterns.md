# **Frequently Asked Questions: Agentic Design Patterns**

# **常见问题解答：Agentic 设计模式**

**What is an "agentic design pattern"?** An agentic design pattern is a reusable, high-level solution to a common problem encountered when building intelligent, autonomous systems (agents). These patterns provide a structured framework for designing agent behaviors, much like software design patterns do for traditional programming. They help developers build more robust, predictable, and effective AI agents.

**什么是"Agentic 设计模式"？** Agentic 设计模式是可复用的高层解决方案，用于应对构建智能自主系统（智能体）时的常见挑战。这些模式为设计智能体提供结构化框架，其作用类似于传统编程中的软件设计模式。它们助力开发者构建更稳健、可预测且高效的 AI 智能体。

**What is the main goal of this guide?** The guide aims to provide a practical, hands-on introduction to designing and building agentic systems. It moves beyond theoretical discussions to offer concrete architectural blueprints that developers can use to create agents capable of complex, goal-oriented behavior in a reliable way.

**本指南的核心目标是什么？** 本指南致力于提供设计与构建 Agentic 系统的实践性指导。超越纯理论探讨，提供开发者可直接运用的具体架构蓝图，以可靠方式创建具备复杂目标导向行为能力的智能体。

**Who is the intended audience for this guide?** This guide is written for AI developers, software engineers, and system architects who are building applications with large language models (LLMs) and other AI components. It is for those who want to move from simple prompt-response interactions to creating sophisticated, autonomous agents.

**本指南面向哪些读者群体？** 本指南主要面向运用大语言模型（LLM）及其他 AI 组件构建应用的 AI 开发者、软件工程师与系统架构师。特别适合希望从简单提示-响应交互进阶至构建复杂自主智能体的技术人员。

**4\. What are some of the key agentic patterns discussed?** Based on the table of contents, the guide covers several key patterns, including:

* **Reflection:** The ability of an agent to critique its own actions and outputs to improve performance.  
* **Planning:** The process of breaking down a complex goal into smaller, manageable steps or tasks.  
* **Tool Use:** The pattern of an agent utilizing external tools (like code interpreters, search engines, or other APIs) to acquire information or perform actions it cannot do on its own.  
* **Multi-Agent Collaboration:** The architecture for having multiple specialized agents work together to solve a problem, often involving a "leader" or "orchestrator" agent.  
* **Human-in-the-Loop:** The integration of human oversight and intervention, allowing for feedback, correction, and approval of an agent's actions.

**4. 本指南涵盖哪些关键 Agentic 模式？** 依据目录结构，本指南深入探讨以下核心模式：

* **反思（Reflection）**：智能体通过批判自身行为与输出来提升性能的能力。
* **规划（Planning）**：将复杂目标分解为可管理步骤或任务序列的过程。
* **工具使用（Tool Use）**：智能体借助外部工具（如代码解释器、搜索引擎或其他 API）获取信息或执行自身无法完成操作的模式。
* **多智能体协作（Multi-Agent Collaboration）**：多个专业化智能体协同解决问题的架构，通常包含"领导者"或"协调者"智能体。
* **人机协同（Human-in-the-Loop）**：整合人类监督与干预机制，支持对智能体进行反馈、修正与审批。

**Why is "planning" an important pattern?** Planning is crucial because it allows an agent to tackle complex, multi-step tasks that cannot be solved with a single action. By creating a plan, the agent can maintain a coherent strategy, track its progress, and handle errors or unexpected obstacles in a structured manner. This prevents the agent from getting "stuck" or deviating from the user's ultimate goal.

**为何"规划"模式至关重要？** 规划模式使智能体能够处理无法通过单步操作解决的复杂多阶段任务。通过制定计划，智能体可维持连贯策略、追踪进度，并以结构化方式应对错误或意外障碍。这有效防止智能体"卡壳"或偏离用户最终目标。

**What is the difference between a "tool" and a "skill" for an agent?** While the terms are often used interchangeably, a "tool" generally refers to an external resource the agent can call upon (e.g., a weather API, a calculator). A "skill" is a more integrated capability that the agent has learned, often combining tool use with internal reasoning to perform a specific function (e.g., the skill of "booking a flight" might involve using calendar and airline APIs).

**智能体语境中"工具"与"技能"有何区别？** 虽常被混用，但"工具"通常指智能体可使用的外部资源（如天气 API、计算器）；"技能"则是智能体获得的更集成化能力，往往结合工具使用与内部推理以执行特定功能（如"航班预订"技能可能涉及日历与航空 API 的协同使用）。

**How does the "Reflection" pattern improve an agent's performance?** Reflection acts as a form of self-correction. After generating a response or completing a task, the agent can be prompted to review its work, check for errors, assess its quality against certain criteria, or consider alternative approaches. This iterative refinement process helps the agent produce more accurate, relevant, and high-quality results.

**"反思"模式如何提升智能体？** 反思机制充当自我校正功能。在生成响应或完成任务后，引导智能体检查其工作：检测错误、依据既定标准评估质量、考量替代方案。此迭代优化过程显著提升智能体输出的准确性、相关性及整体质量。

**What is the core idea of the Reflection pattern?** The Reflection pattern gives an agent the ability to step back and critique its own work. Instead of producing a final output in one go, the agent generates a draft and then "reflects" on it, identifying flaws, missing information, or areas for improvement. This self-correction process is key to enhancing the quality and accuracy of its responses.

**反思模式的核心理念是什么？** 反思模式赋予智能体进一步批判自身工作的能力。智能体并非一次性生成最终输出，而是先创建草稿后进行"反思"，识别缺陷、信息缺失或改进空间。此自我校正流程是提升响应质量与准确度的关键机制。

**Why is simple "prompt chaining" not enough for high-quality output?** Simple prompt chaining (where the output of one prompt becomes the input for the next) is often too basic. The model might just rephrase its previous output without genuinely improving it. A true Reflection pattern requires a more structured critique, prompting the agent to analyze its work against specific standards, check for logical errors, or verify facts.

**为何简单"提示词链"难以保证高质量输出？** 简单提示词链（前序提示输出作为后续提示输入）通常过于基础。模型可能仅对先前输出进行措辞重组而未实现实质性改进。真正的反思模式需引入结构化批判机制，引导智能体依据特定标准分析工作、检验逻辑错误或核实事实。

**What are the two main types of reflection mentioned in this chapter?** The chapter discusses two primary forms of reflection:

* **"Check your work" Reflection:** This is a basic form where the agent is simply asked to review and fix its previous output. It's a good starting point for catching simple errors.  
* **"Internal Critic" Reflection:** This is a more advanced form where a separate, "critic" agent (or a dedicated prompt) is used to evaluate the output of the "worker" agent. This critic can be given specific criteria to look for, leading to more rigorous and targeted improvements.

**本章阐述的两种主要反思类型是什么？** 本章详细解析两种核心反思形式：

* **"工作自查"式反思**：基础形式，仅要求智能体检查并修正前序输出。适用于捕捉简单错误的入门场景。
* **"内部评审"式反思**：进阶形式，通过独立"评审者"智能体（或专用提示）评估"执行者"智能体的输出。可为评审者设定特定检验标准，实现更严密且定向的改进。

**How does reflection help in reducing "hallucinations"?** By prompting an agent to review its work, especially by comparing its statements against a known source or by checking its own reasoning steps, the Reflection pattern can significantly reduce the likelihood of hallucinations (making up facts). The agent is forced to be more grounded in the provided context and less likely to generate unsupported information.

**反思机制如何助力减少"幻觉"现象？** 通过强制智能体检查自身工作——特别是将其陈述与已知来源比对或检验推理步骤——反思模式能显著降低幻觉（虚构事实）发生概率。智能体被迫更严格遵循给定上下文，减少生成无依据信息的可能性。

**Can the Reflection pattern be applied more than once?** Yes, reflection can be an iterative process. An agent can be made to reflect on its work multiple times, with each loop refining the output further. This is particularly useful for complex tasks where the first or second attempt may still contain subtle errors or could be substantially improved.

**反思模式可否多次迭代应用？** 可以，反思本身即为迭代过程。可引导智能体对同一工作进行多轮反思，每轮循环持续优化输出质量。这对复杂任务尤为关键，因初版或次版输出可能仍存在细微错误或具大幅提升空间。

**What is the Planning pattern in the context of AI agents?** The Planning pattern involves enabling an agent to break down a complex, high-level goal into a sequence of smaller, actionable steps. Instead of trying to solve a big problem at once, the agent first creates a "plan" and then executes each step in the plan, which is a much more reliable approach.

**AI智能体中的规划模式指什么？** 规划模式旨在使智能体将高层目标分解为系列可执行步骤序列。智能体不试图一次性解决宏观问题，而是先构建"计划"框架，随后按序执行各步骤，此方法显著提升任务可靠性。

**Why is planning necessary for complex tasks?** LLMs can struggle with tasks that require multiple steps or dependencies. Without a plan, an agent might lose track of the overall objective, miss crucial steps, or fail to handle the output of one step as the input for the next. A plan provides a clear roadmap, ensuring all requirements of the original request are met in a logical order.

**为何复杂任务必须引入规划机制？** 大语言模型在处理多步骤或具依赖关系的任务时存在局限。缺乏计划指引时，智能体易丢失整体目标脉络、遗漏关键环节或未能将前步骤输出有效传递至后续输入。计划提供清晰实施路线，确保按逻辑顺序满足原始请求全部要求。

**What is a common way to implement the Planning pattern?** A common implementation is to have the agent first generate a list of steps in a structured format (like a JSON array or a numbered list). The system can then iterate through this list, executing each step one by one and feeding the result back to the agent to inform the next action.

**实现规划模式的典型方法有哪些？** 常见实施方案是引导智能体生成结构化步骤列表（如 JSON 数组或编号清单）。系统随后遍历该列表，逐项执行步骤并将执行结果反馈至智能体以进行后续操作。

**How does the agent handle errors or changes during execution?** A robust planning pattern allows for dynamic adjustments. If a step fails or the situation changes, the agent can be prompted to "re-plan" from the current state. It can analyze the error, modify the remaining steps, or even add new ones to overcome the obstacle.

**智能体如何处理执行过程中的异常或动态变化？** 健全的规划模式支持动态调整能力。当某步骤失败或情境变更时，可触发智能体根据当前状态"重新规划"。智能体能分析错误成因、调整剩余步骤序列，甚至新增步骤以突破障碍。

**Does the user see the plan?** This is a design choice. In many cases, showing the plan to the user first for approval is a great practice. This aligns with the "Human-in-the-Loop" pattern, giving the user transparency and control over the agent's proposed actions before they are executed.

**计划内容是否对用户可见？** 此为设计决策项。多数场景下，预先向用户展示计划并获取批准是推荐实践。这与"人机协同"模式高度契合，在执行前赋予用户对智能体执行操作的透明度与控制权。

**What does the "Tool Use" pattern entail?** The Tool Use pattern allows an agent to extend its capabilities by interacting with external software or APIs. Since an LLM's knowledge is static and it can't perform real-world actions on its own, tools give it access to live information (e.g., Google Search), proprietary data (e.g., a company's database), or the ability to perform actions (e.g., send an email, book a meeting).

**"工具使用"模式的核心要素是什么？** 工具使用模式使智能体通过与外部软件或 API 交互扩展自身能力边界。鉴于 LLM 知识库的静态特性及无法自主执行现实操作的限制，工具为其提供实时信息访问（如 Google 搜索）、专有数据获取（如企业数据库）及动作执行能力（如邮件发送、会议预订）。

**How does an agent decide which tool to use?** The agent is typically given a list of available tools along with descriptions of what each tool does and what parameters it requires. When faced with a request it can't handle with its internal knowledge, the agent's reasoning ability allows it to select the most appropriate tool from the list to accomplish the task.

**智能体如何决策工具选用？** 通常会为智能体提供可用工具清单及各工具的功能描述与参数要求。当面临内部知识无法处理的请求时，智能体依托推理能力从清单中筛选最适配任务需求的工具。

**What is the "ReAct" (Reason and Act) framework mentioned in this context?** ReAct is a popular framework that integrates reasoning and acting. The agent follows a loop of **Thought** (reasoning about what it needs to do), **Action** (deciding which tool to use and with what inputs), and **Observation** (seeing the result from the tool). This loop continues until it has gathered enough information to fulfill the user's request.

**文中所提"ReAct"（推理-行动）框架是什么？** ReAct 是集成推理与行动的流行框架。智能体遵循**思考**（分析待执行任务）、**行动**（决策工具选择及输入参数）与**观察**（获取工具返回结果）的循环流程。该循环持续迭代直至收集足够信息满足用户请求。

**What are some challenges in implementing tool use?** Key challenges include:

* **Error Handling:** Tools can fail, return unexpected data, or time out. The agent needs to be able to recognize these errors and decide whether to try again, use a different tool, or ask the user for help.  
* **Security:** Giving an agent access to tools, especially those that perform actions, has security implications. It's crucial to have safeguards, permissions, and often human approval for sensitive operations.  
* **Prompting:** The agent must be prompted effectively to generate correctly formatted tool calls (e.g., the right function name and parameters).

**工具使用实施面临哪些主要挑战？** 关键挑战包括：

* **异常处理**：工具可能执行失败、返回意外数据或超时。智能体需具备异常识别能力并决策重试、切换工具或寻求用户协助。
* **安全考量**：授予智能体访问权限——特别是具现实影响的操作工具——存在安全风险。对敏感操作必须设置防护机制、权限控制及常需人工审批流程。
* **提示工程**：需通过精准提示引导智能体格式规范的工具调用（如正确函数名与参数结构）。

**What is the Human-in-the-Loop (HITL) pattern?** HITL is a pattern that integrates human oversight and interaction into the agent's workflow. Instead of being fully autonomous, the agent pauses at critical junctures to ask for human feedback, approval, clarification, or direction.

**什么是人机协同（HITL）模式？** HITL 是一种将人类监督与交互机制深度整合至智能体工作流的模式。智能体并非完全自主运行，而是在关键决策节点暂停执行，主动寻求人类反馈、审批、澄清或方向指引。

**Why is HITL important for agentic systems?** It's crucial for several reasons:

* **Safety and Control:** For high-stakes tasks (e.g., financial transactions, sending official communications), HITL ensures a human verifies the agent's proposed actions before they are executed.  
* **Improving Quality:** Humans can provide corrections or nuanced feedback that the agent can use to improve its performance, especially in subjective or ambiguous tasks.  
* **Building Trust:** Users are more likely to trust and adopt an AI system that they can guide and supervise.

**为何 HITL 对 Agentic 系统至关重要？** 其重要性体现在多个维度：

* **安全与可控性**：针对高风险任务（如金融交易、官方通讯发送），HITL 确保人类在操作执行前验证智能体的行动。
* **质量提升**：人类可提供精准修正或细致反馈，助力智能体优化输出，尤其在主观判断或模糊情境任务中。
* **信任构建**：用户更倾向于采纳具备可指导与监督特性的 AI 系统，从而建立长期信任关系。

**At what points in a workflow should you include a human?** Common points for human intervention include:

* **Plan Approval:** Before executing a multi-step plan.  
* **Tool Use Confirmation:** Before using a tool that has real-world consequences or costs money.  
* **Ambiguity Resolution:** When the agent is unsure how to proceed or needs more information from the user.  
* **Final Output Review:** Before delivering the final result to the end-user or system.

**工作流中哪些环节应引入人类干预？** 典型的人类介入节点包括：

* **计划审批环节**：多步骤计划正式执行前的确认阶段。
* **工具使用授权**：涉及现实影响或产生经济成本的工具调用前。
* **歧义消解节点**：当智能体的路径不明确或需用户补充信息时。
* **最终输出审核**：向终端用户或下游系统交付成果前的质量把关。

**Isn't constant human intervention inefficient?** It can be, which is why the key is to find the right balance. HITL should be implemented at critical checkpoints, not for every single action. The goal is to build a collaborative partnership between the human and the agent, where the agent handles the bulk of the work and the human provides strategic guidance.

**持续人工介入是否影响效率？** 确存此风险，因此关键在于精准把握平衡点。HITL 应部署于核心决策节点，而非每个操作步骤。目标是构建人机协作伙伴关系：智能体承担主体工作量，人类提供战略级指导。

**What is the Multi-Agent Collaboration pattern?** This pattern involves creating a system composed of multiple specialized agents that work together to achieve a common goal. Instead of one "generalist" agent trying to do everything, you create a team of "specialist" agents, each with a specific role or expertise.

**何为多智能体协作模式？** 该模式指构建由多个专业化智能体协同的系统，通过集体智慧达成共同目标。替代单一"全才"智能体尝试包揽所有任务的模式，转而组建各具专长的"专家"智能体团队。

**What are the benefits of a multi-agent system?**

* **Modularity and Specialization:** Each agent can be fine-tuned and prompted for its specific task (e.g., a "researcher" agent, a "writer" agent, a "code" agent), leading to higher quality results.  
* **Reduced Complexity:** Breaking a complex workflow down into specialized roles makes the overall system easier to design, debug, and maintain.  
* **Simulated Brainstorming:** Different agents can offer different perspectives on a problem, leading to more creative and robust solutions, similar to how a human team works.

**多智能体协作的优势何在？**

* **模块化与专业化**：每个智能体针对特定任务进行精细化提示调优（如"研究专员"、"文案专家"、"代码工程师"），产出质量显著提升。
* **复杂度管控**：将复杂工作流分解为专业角色，大幅降低系统整体设计、调试与维护难度。
* **群体智慧模拟**：不同智能体提供多元视角，催生更具创意与鲁棒性的解决方案，仿效人类团队协作模式。

**What is a common architecture for multi-agent systems?** A common architecture involves an **Orchestrator Agent** (sometimes called a "manager" or "conductor"). The orchestrator understands the overall goal, breaks it down, and delegates sub-tasks to the appropriate specialist agents. It then collects the results from the specialists and synthesizes them into a final output.

**多智能体协作的典型架构如何？** 常见架构核心为**协调者智能体**（亦称"管理者"或"指挥者"）。协调者把握全局目标，进行任务分解与委派，收集各专家智能体的输出进行最终合成。

**How do the agents communicate with each other?** Communication is often managed by the orchestrator. For example, the orchestrator might pass the output of the "researcher" agent to the "writer" agent as context. A shared "scratchpad" or message bus where agents can post their findings is another common communication method.

**智能体间如何实现通信协作？** 通信通常由协调者主导管理。例如，协调者可将"研究员"智能体的输出作为上下文传递给"写作"智能体。此外，支持智能体相互发现的共享"工作区"或消息总线亦是常用通信机制。

**Why is evaluating an agent more difficult than evaluating a traditional software program?** Traditional software has deterministic outputs (the same input always produces the same output). Agents, especially those using LLMs, are non-deterministic and their performance can be subjective. Evaluating them requires assessing the *quality* and *relevance* of their output, not just whether it's technically "correct."

**为何评估智能体比评估传统软件更困难？** 传统软件具备确定性输出（相同输入恒定产生相同输出）。而基于 LLM 的智能体具有不确定性特征，其性能评估常涉主观判断。评估需聚焦输出*质量*与*相关性*，而非单纯技术正确性。

**What are some common methods for evaluating agent performance?** The guide suggests a few methods:

* **Outcome-based Evaluation:** Did the agent successfully achieve the final goal? For example, if the task was "book a flight," was a flight actually booked correctly? This is the most important measure.  
* **Process-based Evaluation:** Was the agent's *process* efficient and logical? Did it use the right tools? Did it follow a sensible plan? This helps debug why an agent might be failing.  
* **Human Evaluation:** Having humans score the agent's performance on a scale (e.g., 1-5) based on criteria like helpfulness, accuracy, and coherence. This is crucial for user-facing applications.

**智能体性能评估的常用方法有哪些？** 本指南推荐以下方法：

* **结果导向评估**：智能体是否成功达成终极目标？例如任务为"航班预订"，是否实际完成正确预订？此为核心衡量指标。
* **过程质量评估**：智能体执行*流程*是否高效合理？工具选用是否恰当？计划遵循是否严谨？此有助于诊断失败根源。
* **人工评分评估**：邀请人类评估者依据帮助性、准确性、连贯性等维度进行量表评分（如1-5分）。对用户导向应用尤为关键。

**What is an "agent trajectory"?** An agent trajectory is the complete log of an agent's steps while performing a task. It includes all its thoughts, actions (tool calls), and observations. Analyzing these trajectories is a key part of debugging and understanding agent behavior.

**何为"智能体轨迹"？** 智能体轨迹是任务执行全过程的完整步骤记录，涵盖所有思考过程、操作行为（工具调用）及环境观察。分析这些轨迹是调试与理解智能体行为的核心手段。

**How can you create reliable tests for a non-deterministic system?** While you can't guarantee the exact wording of an agent's output, you can create tests that check for key elements. For example, you can write a test that verifies if the agent's final response *contains* specific information or if it successfully called a certain tool with the right parameters. This is often done using mock tools in a dedicated testing environment.

**如何为非确定性系统构建可靠测试？** 虽无法保证智能体的精确措辞，但可设计验证关键要素的测试。例如创建检测最终响应是否*包含*特定信息，或是否以正确参数成功调用某工具的测试。通常通过在专用测试环境部署模拟工具实现。

**How is prompting an agent different from a simple ChatGPT prompt?** Prompting an agent involves creating a detailed "system prompt" or constitution that acts as its operating instructions. This goes beyond a single user query; it defines the agent's role, its available tools, the patterns it should follow (like ReAct or Planning), its constraints, and its personality.

**智能体提示与简单 ChatGPT 提示有何本质区别？** 智能体需构建详尽的"系统提示"或运行章程作为操作指南。这超越单一用户查询范畴，需明确定义智能体角色、可用工具集、应遵循模式（如 ReAct 或规划）、行为约束及交互风格。

**What are the key components of a good system prompt for an agent?** A strong system prompt typically includes:

* **Role and Goal:** Clearly define who the agent is and what its primary purpose is.  
* **Tool Definitions:** A list of available tools, their descriptions, and how to use them (e.g., in a specific function-calling format).  
* **Constraints and Rules:** Explicit instructions on what the agent *should not* do (e.g., "Do not use tools without approval," "Do not provide financial advice").  
* **Process Instructions:** Guidance on which patterns to use. For example, "First, create a plan. Then, execute the plan step-by-step."  
* **Example Trajectories:** Providing a few examples of successful "thought-action-observation" loops can significantly improve the agent's reliability.

**优质智能体提示的核心构成要素有哪些？** 卓越的系统提示通常包含：

* **角色与目标界定**：清晰定义智能体标识与核心使命。
* **工具规格说明**：可用工具清单、功能描述及调用规范（如特定函数调用格式）。
* **约束与规则体系**：明确禁止行为指令（如"未经批准禁止使用工具"、"不提供金融建议"）。
* **流程执行指引**：模式应用指导，例如"首先制定计划，随后按步骤执行"。
* **示范轨迹案例**：提供若干成功"思考-行动-观察"循环实例，可大幅提升智能体可靠性。

**What is "prompt leakage"?** Prompt leakage occurs when parts of the system prompt (like tool definitions or internal instructions) are inadvertently revealed in the agent's final response to the user. This can be confusing for the user and expose underlying implementation details. Techniques like using separate prompts for reasoning and for generating the final answer can help prevent this.

**何为"提示泄漏"？** 提示泄漏指系统提示内容（如工具定义或内部指令）意外出现在智能体给用户的最终响应中。此现象可能导致用户困惑并暴露系统实现细节。采用推理与最终答案生成分离的提示策略等技术可有效防范。

**What are some future trends in agentic systems?** The guide points towards a future with:

* **More Autonomous Agents:** Agents that require less human intervention and can learn and adapt on their own.  
* **Highly Specialized Agents:** An ecosystem of agents that can be hired or subscribed to for specific tasks (e.g., a travel agent, a research agent).  
* **Better Tools and Platforms:** The development of more sophisticated frameworks and platforms that make it easier to build, test, and deploy robust multi-agent systems.

**Agentic 系统未来发展趋势如何？** 本指南展望以下方向：

* **增强自主能力**：需更少人工干预且具备自学习与自适应能力的智能体。
* **深度专业分化**：形成可按需雇佣或订阅的专项任务智能体系统（如旅行顾问、研究助手）。
* **工具平台演进**：开发更复杂精密的框架与平台，显著降低构建、测试与部署健壮多智能体系统的技术门槛。
