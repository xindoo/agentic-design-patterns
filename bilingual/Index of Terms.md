# Glossary

# 术语索引

## Fundamental Concepts

## 基本概念

**Prompt:** A prompt is the input, typically in the form of a question, instruction, or statement, that a user provides to an AI model to elicit a response. The quality and structure of the prompt heavily influence the model's output, making prompt engineering a key skill for effectively using AI.

**提示词（Prompt）：** 提示词是用户提供给 AI 模型的输入，通常以问题、指令或陈述的形式出现，用于引发响应。提示词的质量和结构极大地影响模型的输出，使提示词工程成为有效使用 AI 的关键技能。

**Context Window:** The context window is the maximum number of tokens an AI model can process at once, including both the input and its generated output. This fixed size is a critical limitation, as information outside the window is ignored, while larger windows enable more complex conversations and document analysis.

**上下文窗口（Context Window）：** 上下文窗口是 AI 模型一次可以处理的最大 token 数量，包括输入和生成的输出。这个固定大小是一个关键限制，因为窗口外的信息会被忽略，而更大的窗口可以实现更复杂的对话和文档分析。

**In-Context Learning:** In-context learning is an AI's ability to learn a new task from examples provided directly in the prompt, without requiring any retraining. This powerful feature allows a single, general-purpose model to be adapted to countless specific tasks on the fly.

**上下文学习（In-Context Learning）：** 上下文学习是 AI 直接从提示词中提供的示例学习新任务的能力，无需任何重新训练。这个强大的功能允许单个通用模型即时适应无数特定任务。

**Zero-Shot, One-Shot, & Few-Shot Prompting:** These are prompting techniques where a model is given zero, one, or a few examples of a task to guide its response. Providing more examples generally helps the model better understand the user's intent and improves its accuracy for the specific task.

**零样本、单样本和少样本提示（Zero-Shot, One-Shot, & Few-Shot Prompting）：** 这些是提示技术，其中向模型提供零个、一个或几个任务示例来指导其响应。提供更多示例通常有助于模型更好地理解用户意图，并提高特定任务的准确性。

**Multimodality:** Multimodality is an AI's ability to understand and process information across multiple data types like text, images, and audio. This allows for more versatile and human-like interactions, such as describing an image or answering a spoken question.

**多模态（Multimodality）：** 多模态是 AI 理解和处理多种数据类型（如文本、图像和音频）信息的能力。这允许更多样化和类人的交互，例如描述图像或回答口头问题。

**Grounding:** Grounding is the process of connecting a model's outputs to verifiable, real-world information sources to ensure factual accuracy and reduce hallucinations. This is often achieved with techniques like RAG to make AI systems more trustworthy.

**基础化（Grounding）：** 基础化是将模型输出连接到可验证的真实世界信息源的过程，以确保事实准确性并减少幻觉。这通常通过 RAG 等技术实现，使 AI 系统更值得信赖。

## Core AI Model Architectures

## 核心 AI 模型架构

**Transformers:** The Transformer is the foundational neural network architecture for most modern LLMs. Its key innovation is the self-attention mechanism, which efficiently processes long sequences of text and captures complex relationships between words.

**Transformers：** Transformer 是大多数现代 LLM 的基础神经网络架构。其关键创新是自注意力机制，可以高效处理长文本序列并捕获单词之间的复杂关系。

**Recurrent Neural Network (RNN):** The Recurrent Neural Network is a foundational architecture that preceded the Transformer. RNNs process information sequentially, using loops to maintain a "memory" of previous inputs, which made them suitable for tasks like text and speech processing.

**循环神经网络（Recurrent Neural Network, RNN）：** 循环神经网络是 Transformer 之前的基础架构。RNN 按顺序处理信息，使用循环来维护先前输入的"记忆"，这使它们适合文本和语音处理等任务。

**Mixture of Experts (MoE):** Mixture of Experts is an efficient model architecture where a "router" network dynamically selects a small subset of "expert" networks to handle any given input. This allows models to have a massive number of parameters while keeping computational costs manageable.

**专家混合（Mixture of Experts, MoE）：** 专家混合是一种高效的模型架构，其中"路由器"网络动态选择一小部分"专家"网络来处理任何给定的输入。这允许模型拥有大量参数，同时保持可管理的计算成本。

**Diffusion Models:** Diffusion models are generative models that excel at creating high-quality images. They work by adding random noise to data and then training a model to meticulously reverse the process, allowing them to generate novel data from a random starting point.

**扩散模型（Diffusion Models）：** 扩散模型是擅长创建高质量图像的生成模型。它们通过向数据添加随机噪声，然后训练模型精确地逆转该过程来工作，允许它们从随机起点生成新颖的数据。

**Mamba:** Mamba is a recent AI architecture using a Selective State Space Model (SSM) to process sequences with high efficiency, especially for very long contexts. Its selective mechanism allows it to focus on relevant information while filtering out noise, making it a potential alternative to the Transformer.

**Mamba：** Mamba 是一种最新的 AI 架构，使用选择性状态空间模型（SSM）以高效率处理序列，特别是对于非常长的上下文。其选择性机制允许它专注于相关信息同时过滤噪声，使其成为 Transformer 的潜在替代方案。

## The LLM Development Lifecycle

## LLM 开发生命周期

The development of a powerful language model follows a distinct sequence. It begins with Pre-training, where a massive base model is built by training it on a vast dataset of general internet text to learn language, reasoning, and world knowledge. Next is Fine-tuning, a specialization phase where the general model is further trained on smaller, task-specific datasets to adapt its capabilities for a particular purpose. The final stage is Alignment, where the specialized model's behavior is adjusted to ensure its outputs are helpful, harmless, and aligned with human values.

强大语言模型的开发遵循明确的顺序。它始于预训练（Pre-training），在大量通用互联网文本数据集上训练大规模基础模型，以学习语言、推理和世界知识。接下来是微调（Fine-tuning），这是一个专业化阶段，在较小的特定任务数据集上进一步训练通用模型，以使其能力适应特定目的。最后阶段是对齐（Alignment），调整专业化模型的行为，以确保其输出有帮助、无害且与人类价值观保持一致。

**Pre-training Techniques:** Pre-training is the initial phase where a model learns general knowledge from vast amounts of data. The top techniques for this involve different objectives for the model to learn from. The most common is Causal Language Modeling (CLM), where the model predicts the next word in a sentence. Another is Masked Language Modeling (MLM), where the model fills in intentionally hidden words in a text. Other important methods include Denoising Objectives, where the model learns to restore a corrupted input to its original state, Contrastive Learning, where it learns to distinguish between similar and dissimilar pieces of data, and Next Sentence Prediction (NSP), where it determines if two sentences logically follow each other.

**预训练技术：** 预训练是模型从大量数据中学习通用知识的初始阶段。这方面的顶级技术涉及模型学习的不同目标。最常见的是因果语言建模（CLM），其中模型预测句子中的下一个单词。另一种是掩码语言建模（MLM），其中模型填充文本中故意隐藏的单词。其他重要方法包括去噪目标，其中模型学习将损坏的输入恢复到其原始状态，对比学习，其中它学习区分相似和不相似的数据片段，以及下一句预测（NSP），其中它确定两个句子是否在逻辑上相互跟随。

**Fine-tuning Techniques:** Fine-tuning is the process of adapting a general pre-trained model to a specific task using a smaller, specialized dataset. The most common approach is Supervised Fine-Tuning (SFT), where the model is trained on labeled examples of correct input-output pairs. A popular variant is Instruction Tuning, which focuses on training the model to better follow user commands. To make this process more efficient, Parameter-Efficient Fine-Tuning (PEFT) methods are used, with top techniques including LoRA (Low-Rank Adaptation), which only updates a small number of parameters, and its memory-optimized version, QLoRA. Another technique, Retrieval-Augmented Generation (RAG), enhances the model by connecting it to an external knowledge source during the fine-tuning or inference stage.

**微调技术：** 微调是使用较小的专业化数据集将通用预训练模型适应特定任务的过程。最常见的方法是监督微调（SFT），其中模型在标记的正确输入输出对示例上进行训练。一个流行的变体是指令调优，专注于训练模型更好地遵循用户命令。为了使此过程更高效，使用参数高效微调（PEFT）方法，顶级技术包括 LoRA（低秩适应），仅更新少量参数，以及其内存优化版本 QLoRA。另一种技术，检索增强生成（RAG），通过在微调或推理阶段将模型连接到外部知识源来增强模型。

**Alignment & Safety Techniques:** Alignment is the process of ensuring an AI model's behavior aligns with human values and expectations, making it helpful and harmless. The most prominent technique is Reinforcement Learning from Human Feedback (RLHF), where a "reward model" trained on human preferences guides the AI's learning process, often using an algorithm like Proximal Policy Optimization (PPO) for stability. Simpler alternatives have emerged, such as Direct Preference Optimization (DPO), which bypasses the need for a separate reward model, and Kahneman-Tversky Optimization (KTO), which simplifies data collection further. To ensure safe deployment, Guardrails are implemented as a final safety layer to filter outputs and block harmful actions in real-time.

**对齐和安全技术：** 对齐是确保 AI 模型行为与人类价值观和期望保持一致的过程，使其有帮助且无害。最突出的技术是基于人类反馈的强化学习（RLHF），其中在人类偏好上训练的"奖励模型"指导 AI 的学习过程，通常使用近端策略优化（PPO）等算法来保持稳定性。已经出现了更简单的替代方案，例如直接偏好优化（DPO），它绕过了对单独奖励模型的需求，以及 Kahneman-Tversky 优化（KTO），它进一步简化了数据收集。为确保安全部署，实施护栏作为最终安全层，以实时过滤输出并阻止有害行为。

## Enhancing AI Agent Capabilities

## 增强 AI 智能体

AI agents are systems that can perceive their environment and take autonomous actions to achieve goals. Their effectiveness is enhanced by robust reasoning frameworks.

AI 智能体是能够感知其环境并采取自主行动以实现目标的系统。它们的有效性通过强大的推理框架得到增强。

**Chain of Thought (CoT):** This prompting technique encourages a model to explain its reasoning step-by-step before giving a final answer. This process of "thinking out loud" often leads to more accurate results on complex reasoning tasks.

**思维链（Chain of Thought, CoT）：** 这种提示技术鼓励模型在给出最终答案之前逐步解释其推理。这种"大声思考"的过程通常会在复杂推理任务上产生更准确的结果。

**Tree of Thoughts (ToT):** Tree of Thoughts is an advanced reasoning framework where an agent explores multiple reasoning paths simultaneously, like branches on a tree. It allows the agent to self-evaluate different lines of thought and choose the most promising one to pursue, making it more effective at complex problem-solving.

**思维树（Tree of Thoughts, ToT）：** 思维树是一种高级推理框架，其中智能体探索多个推理路径，就像树上的分支一样。它允许智能体探索不同的思路并选择最有希望的路径，使其在复杂问题解决方面更有效。

**ReAct (Reason and Act):** ReAct is an agent framework that combines reasoning and acting in a loop. The agent first "thinks" about what to do, then takes an "action" using a tool, and uses the resulting observation to inform its next thought, making it highly effective at solving complex tasks.

**ReAct（推理与行动，Reason and Act）：** ReAct 是一个智能体框架，在循环中结合推理和行动。Agent 首先"思考"要做什么，然后使用工具采取"行动"，并使用结果观察来通知其下一个想法，使其在解决复杂任务方面非常有效。

**Planning:** This is an agent's ability to break down a high-level goal into a sequence of smaller, manageable sub-tasks. The agent then creates a plan to execute these steps in order, allowing it to handle complex, multi-step assignments.

**规划（Planning）：** 这是智能体将高级目标分解为一系列较小的、可管理的子任务的能力。然后智能体使用计划来按顺序执行这些步骤，使其能够处理复杂的多步骤任务。

**Deep Research:** Deep research refers to an agent's capability to autonomously explore a topic in-depth by iteratively searching for information, synthesizing findings, and identifying new questions. This allows the agent to build a comprehensive understanding of a subject far beyond a single search query.

**深度研究（Deep Research）：** 深度研究是指智能体迭代搜索信息、综合发现和识别新问题来自主深入探索主题的能力。这允许智能体获得对主题的全面理解，远超单个搜索查询。

**Critique Model:** A critique model is a specialized AI model trained to review, evaluate, and provide feedback on the output of another AI model. It acts as an automated critic, helping to identify errors, improve reasoning, and ensure the final output meets a desired quality standard.

**批评模型（Critique Model）：** 批评模型是一种专门的 AI 模型，经过训练可以审查、评估和提供关于另一个 AI 模型输出的反馈。它充当自动批评者，有助于识别错误、改进推理并确保最终输出符合期望的质量标准。

## Index of Terms

## 术语索引

This index of terms was generated using Gemini Pro 2.5. The prompt and reasoning steps are included at the end to demonstrate the time-saving benefits and for educational purposes.

此术语索引使用 Gemini Pro 2.5 生成。提示词和推理步骤包含在末尾，以展示 AI 辅助索引创建的效率优势并用于教育目的。

**A**

* A/B Testing \- Chapter 3: Parallelization  
* Action Selection \- Chapter 20: Prioritization  
* Adaptation \- Chapter 9: Learning and Adaptation  
* Adaptive Task Allocation \- Chapter 16: Resource-Aware Optimization  
* Adaptive Tool Use & Selection \- Chapter 16: Resource-Aware Optimization  
* Agent \- What makes an AI system an Agent?  
* Agent-Computer Interfaces (ACIs) \- Appendix B  
* Agent-Driven Economy \- What makes an AI system an Agent?  
* Agent as a Tool \- Chapter 7: Multi-Agent Collaboration  
* Agent Cards \- Chapter 15: Inter-Agent Communication (A2A)  
* Agent Development Kit (ADK) \- Chapter 2: Routing, Chapter 3: Parallelization, Chapter 4: Reflection, Chapter 5: Tool Use, Chapter 7: Multi-Agent Collaboration, Chapter 8: Memory Management, Chapter 12: Exception Handling and Recovery, Chapter 13: Human-in-the-Loop, Chapter 15: Inter-Agent Communication (A2A), Chapter 16: Resource-Aware Optimization, Chapter 19: Evaluation and Monitoring, Appendix C  
* Agent Discovery \- Chapter 15: Inter-Agent Communication (A2A)  
* Agent Trajectories \- Chapter 19: Evaluation and Monitoring  
* Agentic Design Patterns \- Introduction  
* Agentic RAG \- Chapter 14: Knowledge Retrieval (RAG)  
* Agentic Systems \- Introduction  
* AI Co-scientist \- Chapter 21: Exploration and Discovery  
* Alignment \- Glossary  
* AlphaEvolve \- Chapter 9: Learning and Adaptation  
* Analogies \- Appendix A  
* Anomaly Detection \- Chapter 19: Evaluation and Monitoring  
* Anthropic's Claude 4 Series \- Appendix B  
* Anthropic's Computer Use \- Appendix B  
* API Interaction \- Chapter 10: Model Context Protocol (MCP)  
* Artifacts \- Chapter 15: Inter-Agent Communication (A2A)  
* Asynchronous Polling \- Chapter 15: Inter-Agent Communication (A2A)  
* Audit Logs \- Chapter 15: Inter-Agent Communication (A2A)  
* Automated Metrics \- Chapter 19: Evaluation and Monitoring  
* Automatic Prompt Engineering (APE) \- Appendix A  
* Autonomy \- Introduction  
* A2A (Agent-to-Agent) \- Chapter 15: Inter-Agent Communication (A2A)

* A/B 测试(A/B Testing) - 第 3 章：并行化
* 行动选择(Action Selection) - 第 20 章：优先级排序
* 适应(Adaptation) - 第 9 章：学习与适应
* 自适应任务分配(Adaptive Task Allocation) - 第 16 章：资源感知优化
* 自适应工具使用与选择(Adaptive Tool Use & Selection) - 第 16 章：资源感知优化
* 智能体(Agent) - 什么使 AI 系统成为 Agent？
* Agent-计算机接口(Agent-Computer Interfaces, ACIs) - 附录 B
* Agent 驱动型经济(Agent-Driven Economy) - 什么使 AI 系统成为 Agent？
* Agent 作为工具(Agent as a Tool) - 第 7 章：多智能体协作
* Agent 卡片(Agent Cards) - 第 15 章：Agent 间通信（A2A）
* 智能体开发工具包(Agent Development Kit, ADK) - 第 2 章：路由，第 3 章：并行化，第 4 章：反思，第 5 章：工具使用，第 7 章：多智能体协作，第 8 章：记忆管理，第 12 章：异常处理与恢复，第 13 章：人机协同，第 15 章：Agent 间通信（A2A），第 16 章：资源感知优化，第 19 章：评估与监控，附录 C
* Agent 发现(Agent Discovery) - 第 15 章：Agent 间通信（A2A）
* Agent 轨迹(Agent Trajectories) - 第 19 章：评估与监控
* Agentic 设计模式(Agentic Design Patterns) - 引言
* Agentic RAG(Agentic RAG) - 第 14 章：知识检索（RAG）
* Agentic 系统(Agentic Systems) - 引言
* AI 联合科学家(AI Co-scientist) - 第 21 章：探索与发现
* 对齐(Alignment) - 术语表
* AlphaEvolve(AlphaEvolve) - 第 9 章：学习与适应
* 类比(Analogies) - 附录 A
* 异常检测(Anomaly Detection) - 第 19 章：评估与监控
* Anthropic's Claude 4 系列(Anthropic's Claude 4 Series) - 附录 B
* Anthropic's 计算机使用(Anthropic's Computer Use) - 附录 B
* API 交互(API Interaction) - 第 10 章：模型上下文协议（MCP）
* 工件(Artifacts) - 第 15 章：Agent 间通信（A2A）
* 异步轮询(Asynchronous Polling) - 第 15 章：Agent 间通信（A2A）
* 审计日志(Audit Logs) - 第 15 章：Agent 间通信（A2A）
* 自动化指标(Automated Metrics) - 第 19 章：评估与监控
* 自动提示工程(Automatic Prompt Engineering, APE) - 附录 A
* 自主性(Autonomy) - 引言
* A2A（Agent 间通信）(A2A, Agent-to-Agent) - 第 15 章：Agent 间通信（A2A）

**B**

* Behavioral Constraints \- Chapter 18: Guardrails/Safety Patterns  
* Browser Use \- Appendix B

* 行为约束(Behavioral Constraints) - 第 18 章：护栏/安全模式
* 浏览器使用(Browser Use) - 附录 B

**C**

* Callbacks \- Chapter 18: Guardrails/Safety Patterns  
* Causal Language Modeling (CLM) \- Glossary  
* Chain of Debates (CoD) \- Chapter 17: Reasoning Techniques  
* Chain-of-Thought (CoT) \- Chapter 17: Reasoning Techniques, Appendix A  
* Chatbots \- Chapter 8: Memory Management  
* ChatMessageHistory \- Chapter 8: Memory Management  
* Checkpoint and Rollback \- Chapter 18: Guardrails/Safety Patterns  
* Chunking \- Chapter 14: Knowledge Retrieval (RAG)  
* Clarity and Specificity \- Appendix A  
* Client Agent \- Chapter 15: Inter-Agent Communication (A2A)  
* Code Generation \- Chapter 1: Prompt Chaining, Chapter 4: Reflection  
* Code Prompting \- Appendix A  
* CoD (Chain of Debates) \- Chapter 17: Reasoning Techniques  
* CoT (Chain of Thought) \- Chapter 17: Reasoning Techniques, Appendix A  
* Collaboration \- Chapter 7: Multi-Agent Collaboration  
* Compliance \- Chapter 19: Evaluation and Monitoring  
* Conciseness \- Appendix A  
* Content Generation \- Chapter 1: Prompt Chaining, Chapter 4: Reflection  
* Context Engineering \- Chapter 1: Prompt Chaining  
* Context Window \- Glossary  
* Contextual Pruning & Summarization \- Chapter 16: Resource-Aware Optimization  
* Contextual Prompting \- Appendix A  
* Contractor Model \- Chapter 19: Evaluation and Monitoring  
* ConversationBufferMemory \- Chapter 8: Memory Management  
* Conversational Agents \- Chapter 1: Prompt Chaining, Chapter 4: Reflection  
* Cost-Sensitive Exploration \- Chapter 16: Resource-Aware Optimization  
* CrewAI \- Chapter 3: Parallelization, Chapter 5: Tool Use, Chapter 6: Planning, Chapter 7: Multi-Agent Collaboration, Chapter 18: Guardrails/Safety Patterns, Appendix C  
* Critique Agent \- Chapter 16: Resource-Aware Optimization  
* Critique Model \- Glossary  
* Customer Support \- Chapter 13: Human-in-the-Loop

* 回调(Callbacks) - 第 18 章：护栏/安全模式
* 因果语言建模(Causal Language Modeling, CLM) - 术语表
* 辩论链(Chain of Debates, CoD) - 第 17 章：推理技术
* 思维链(Chain-of-Thought, CoT) - 第 17 章：推理技术，附录 A
* 聊天机器人(Chatbots) - 第 8 章：记忆管理
* ChatMessageHistory(ChatMessageHistory) - 第 8 章：记忆管理
* 检查点与回滚(Checkpoint and Rollback) - 第 18 章：护栏/安全模式
* 分块(Chunking) - 第 14 章：知识检索（RAG）
* 清晰性和具体性(Clarity and Specificity) - 附录 A
* 客户端 Agent(Client Agent) - 第 15 章：Agent 间通信（A2A）
* 代码生成(Code Generation) - 第 1 章：提示词链，第 4 章：反思
* 代码提示(Code Prompting) - 附录 A
* CoD（辩论链）(CoD, Chain of Debates) - 第 17 章：推理技术
* CoT（思维链）(CoT, Chain of Thought) - 第 17 章：推理技术，附录 A
* 协作(Collaboration) - 第 7 章：多智能体协作
* 合规性(Compliance) - 第 19 章：评估与监控
* 简洁性(Conciseness) - 附录 A
* 内容生成(Content Generation) - 第 1 章：提示词链，第 4 章：反思
* 上下文工程(Context Engineering) - 第 1 章：提示词链
* 上下文窗口(Context Window) - 术语表
* 上下文修剪与摘要(Contextual Pruning & Summarization) - 第 16 章：资源感知优化
* 上下文提示(Contextual Prompting) - 附录 A
* 承包商模型(Contractor Model) - 第 19 章：评估与监控
* ConversationBufferMemory(ConversationBufferMemory) - 第 8 章：记忆管理
* 对话式 Agent(Conversational Agents) - 第 1 章：提示词链，第 4 章：反思
* 成本敏感探索(Cost-Sensitive Exploration) - 第 16 章：资源感知优化
* CrewAI(CrewAI) - 第 3 章：并行化，第 5 章：工具使用，第 6 章：规划，第 7 章：多智能体协作，第 18 章：护栏/安全模式，附录 C
* 批评 Agent(Critique Agent) - 第 16 章：资源感知优化
* 批评模型(Critique Model) - 术语表
* 客户支持(Customer Support) - 第 13 章：人机协同

**D**

* Data Extraction \- Chapter 1: Prompt Chaining  
* Data Labeling \- Chapter 13: Human-in-the-Loop  
* Database Integration \- Chapter 10: Model Context Protocol (MCP)  
* DatabaseSessionService \- Chapter 8: Memory Management  
* Debate and Consensus \- Chapter 7: Multi-Agent Collaboration  
* Decision Augmentation \- Chapter 13: Human-in-the-Loop  
* Decomposition \- Appendix A  
* Deep Research \- Chapter 6: Planning, Chapter 17: Reasoning Techniques, Glossary  
* Delimiters \- Appendix A  
* Denoising Objectives \- Glossary  
* Dependencies \- Chapter 20: Prioritization  
* Diffusion Models \- Glossary  
* Direct Preference Optimization (DPO) \- Chapter 9: Learning and Adaptation  
* Discoverability \- Chapter 10: Model Context Protocol (MCP)  
* Drift Detection \- Chapter 19: Evaluation and Monitoring  
* Dynamic Model Switching \- Chapter 16: Resource-Aware Optimization  
* Dynamic Re-prioritization \- Chapter 20: Prioritization

* 数据提取(Data Extraction) - 第 1 章：提示词链
* 数据标注(Data Labeling) - 第 13 章：人机协同
* 数据库集成(Database Integration) - 第 10 章：模型上下文协议（MCP）
* DatabaseSessionService(DatabaseSessionService) - 第 8 章：记忆管理
* 辩论与共识(Debate and Consensus) - 第 7 章：多智能体协作
* 决策增强(Decision Augmentation) - 第 13 章：人机协同
* 分解(Decomposition) - 附录 A
* 深度研究(Deep Research) - 第 6 章：规划，第 17 章：推理技术，术语表
* 分隔符(Delimiters) - 附录 A
* 去噪目标(Denoising Objectives) - 术语表
* 依赖关系(Dependencies) - 第 20 章：优先级排序
* 扩散模型(Diffusion Models) - 术语表
* 直接偏好优化(Direct Preference Optimization, DPO) - 第 9 章：学习与适应
* 可发现性(Discoverability) - 第 10 章：模型上下文协议（MCP）
* 漂移检测(Drift Detection) - 第 19 章：评估与监控
* 动态模型切换(Dynamic Model Switching) - 第 16 章：资源感知优化
* 动态重新优先级排序(Dynamic Re-prioritization) - 第 20 章：优先级排序

**E**

* Embeddings \- Chapter 14: Knowledge Retrieval (RAG)  
* Embodiment \- What makes an AI system an Agent?  
* Energy-Efficient Deployment \- Chapter 16: Resource-Aware Optimization  
* Episodic Memory \- Chapter 8: Memory Management  
* Error Detection \- Chapter 12: Exception Handling and Recovery  
* Error Handling \- Chapter 12: Exception Handling and Recovery  
* Escalation Policies \- Chapter 13: Human-in-the-Loop  
* Evaluation \- Chapter 19: Evaluation and Monitoring  
* Exception Handling \- Chapter 12: Exception Handling and Recovery  
* Expert Teams \- Chapter 7: Multi-Agent Collaboration  
* Exploration and Discovery \- Chapter 21: Exploration and Discovery  
* External Moderation APIs \- Chapter 18: Guardrails/Safety Patterns

* 嵌入(Embeddings) - 第 14 章：知识检索（RAG）
* 具身化(Embodiment) - 什么使 AI 系统成为 Agent？
* 节能部署(Energy-Efficient Deployment) - 第 16 章：资源感知优化
* 情景记忆(Episodic Memory) - 第 8 章：记忆管理
* 错误检测(Error Detection) - 第 12 章：异常处理与恢复
* 错误处理(Error Handling) - 第 12 章：异常处理与恢复
* 升级策略(Escalation Policies) - 第 13 章：人机协同
* 评估(Evaluation) - 第 19 章：评估与监控
* 异常处理(Exception Handling) - 第 12 章：异常处理与恢复
* 专家团队(Expert Teams) - 第 7 章：多智能体协作
* 探索与发现(Exploration and Discovery) - 第 21 章：探索与发现
* 外部审核 API(External Moderation APIs) - 第 18 章：护栏/安全模式

**F**

* Factored Cognition \- Appendix A  
* FastMCP \- Chapter 10: Model Context Protocol (MCP)  
* Fault Tolerance \- Chapter 18: Guardrails/Safety Patterns  
* Few-Shot Learning \- Chapter 9: Learning and Adaptation  
* Few-Shot Prompting \- Appendix A  
* Fine-tuning \- Glossary  
* Formalized Contract \- Chapter 19: Evaluation and Monitoring  
* Function Calling \- Chapter 5: Tool Use, Appendix A

* 因子化认知(Factored Cognition) - 附录 A
* FastMCP(FastMCP) - 第 10 章：模型上下文协议（MCP）
* 容错(Fault Tolerance) - 第 18 章：护栏/安全模式
* 少样本学习(Few-Shot Learning) - 第 9 章：学习与适应
* 少样本提示(Few-Shot Prompting) - 附录 A
* 微调(Fine-tuning) - 术语表
* 正式化合同(Formalized Contract) - 第 19 章：评估与监控
* 工具调用(Tool Calling) - 第 5 章：工具使用，附录 A

**G**

* Gemini Live \- Appendix B  
* Gems \- Appendix A  
* Generative Media Orchestration \- Chapter 10: Model Context Protocol (MCP)  
* Goal Setting \- Chapter 11: Goal Setting and Monitoring  
* GoD (Graph of Debates) \- Chapter 17: Reasoning Techniques  
* Google Agent Development Kit (ADK) \- Chapter 2: Routing, Chapter 3: Parallelization, Chapter 4: Reflection, Chapter 5: Tool Use, Chapter 7: Multi-Agent Collaboration, Chapter 8: Memory Management, Chapter 12: Exception Handling and Recovery, Chapter 13: Human-in-the-Loop, Chapter 15: Inter-Agent Communication (A2A), Chapter 16: Resource-Aware Optimization, Chapter 19: Evaluation and Monitoring, Appendix C  
* Google Co-scientist \- Chapter 21: Exploration and Discovery  
* Google DeepResearch \- Chapter 6: Planning  
* Google Project Mariner \- Appendix B  
* Graceful Degradation \- Chapter 12: Exception Handling and Recovery, Chapter 16: Resource-Aware Optimization  
* Grounding \- Glossary  
* Guardrails \- Chapter 18: Guardrails/Safety Patterns

* Gemini Live(Gemini Live) - 附录 B
* Gems(Gems) - 附录 A
* 生成媒体编排(Generative Media Orchestration) - 第 10 章：模型上下文协议（MCP）
* 目标设定(Goal Setting) - 第 11 章：目标设定与监控
* GoD（辩论图）(GoD, Graph of Debates) - 第 17 章：推理技术
* Google 智能体开发工具包(Google Agent Development Kit, ADK) - 第 2 章：路由，第 3 章：并行化，第 4 章：反思，第 5 章：工具使用，第 7 章：多智能体协作，第 8 章：记忆管理，第 12 章：异常处理与恢复，第 13 章：人机协同，第 15 章：Agent 间通信（A2A），第 16 章：资源感知优化，第 19 章：评估与监控，附录 C
* Google 联合科学家(Google Co-scientist) - 第 21 章：探索与发现
* Google DeepResearch(Google DeepResearch) - 第 6 章：规划
* Google Project Mariner(Google Project Mariner) - 附录 B
* 优雅降级(Graceful Degradation) - 第 12 章：异常处理与恢复，第 16 章：资源感知优化
* 基础化(Grounding) - 术语表
* 护栏(Guardrails) - 第 18 章：护栏/安全模式

**H**

* Haystack \- Appendix C  
* Hierarchical Decomposition \- Chapter 19: Evaluation and Monitoring  
* Hierarchical Structures \- Chapter 7: Multi-Agent Collaboration  
* HITL (Human-in-the-Loop) \- Chapter 13: Human-in-the-Loop  
* Human-in-the-Loop (HITL) \- Chapter 13: Human-in-the-Loop  
* Human-on-the-loop \- Chapter 13: Human-in-the-Loop  
* Human Oversight \- Chapter 13: Human-in-the-Loop, Chapter 18: Guardrails/Safety Patterns

* Haystack(Haystack) - 附录 C
* 层次化分解(Hierarchical Decomposition) - 第 19 章：评估与监控
* 层次化结构(Hierarchical Structures) - 第 7 章：多智能体协作
* HITL（人机协同）(HITL, Human-in-the-Loop) - 第 13 章：人机协同
* 人机协同(Human-in-the-Loop, HITL) - 第 13 章：人机协同
* 人在环路上(Human-on-the-loop) - 第 13 章：人机协同
* 人类监督(Human Oversight) - 第 13 章：人机协同，第 18 章：护栏/安全模式

**I**

* In-Context Learning \- Glossary  
* InMemoryMemoryService \- Chapter 8: Memory Management  
* InMemorySessionService \- Chapter 8: Memory Management  
* Input Validation/Sanitization \- Chapter 18: Guardrails/Safety Patterns  
* Instructions Over Constraints \- Appendix A  
* Inter-Agent Communication (A2A) \- Chapter 15: Inter-Agent Communication (A2A)  
* Intervention and Correction \- Chapter 13: Human-in-the-Loop  
* IoT Device Control \- Chapter 10: Model Context Protocol (MCP)  
* Iterative Prompting / Refinement \- Appendix A

* 上下文学习(In-Context Learning) - 术语表
* InMemoryMemoryService(InMemoryMemoryService) - 第 8 章：记忆管理
* InMemorySessionService(InMemorySessionService) - 第 8 章：记忆管理
* 输入验证/清理(Input Validation/Sanitization) - 第 18 章：护栏/安全模式
* 指令优先于约束(Instructions Over Constraints) - 附录 A
* Agent 间通信(Inter-Agent Communication, A2A) - 第 15 章：Agent 间通信（A2A）
* 干预与纠正(Intervention and Correction) - 第 13 章：人机协同
* IoT 设备控制(IoT Device Control) - 第 10 章：模型上下文协议（MCP）
* 迭代提示/细化(Iterative Prompting / Refinement) - 附录 A

**J**

* Jailbreaking \- Chapter 18: Guardrails/Safety Patterns

* 越狱(Jailbreaking) - 第 18 章：护栏/安全模式

**K**

* Kahneman-Tversky Optimization (KTO) \- Glossary  
* Knowledge Retrieval (RAG) \- Chapter 14: Knowledge Retrieval (RAG)

* Kahneman-Tversky 优化(Kahneman-Tversky Optimization, KTO) - 术语表
* 知识检索(Knowledge Retrieval, RAG) - 第 14 章：知识检索（RAG）

**L**

* LangChain \- Chapter 1: Prompt Chaining, Chapter 2: Routing, Chapter 3: Parallelization, Chapter 4: Reflection, Chapter 5: Tool Use, Chapter 8: Memory Management, Chapter 20: Prioritization, Appendix C  
* LangGraph \- Chapter 1: Prompt Chaining, Chapter 2: Routing, Chapter 3: Parallelization, Chapter 4: Reflection, Chapter 5: Tool Use, Chapter 8: Memory Management, Appendix C  
* Latency Monitoring \- Chapter 19: Evaluation and Monitoring  
* Learned Resource Allocation Policies \- Chapter 16: Resource-Aware Optimization  
* Learning and Adaptation \- Chapter 9: Learning and Adaptation  
* LLM-as-a-Judge \- Chapter 19: Evaluation and Monitoring  
* LlamaIndex \- Appendix C  
* LoRA (Low-Rank Adaptation) \- Glossary  
* Low-Rank Adaptation (LoRA) \- Glossary

* LangChain(LangChain) - 第 1 章：提示词链，第 2 章：路由，第 3 章：并行化，第 4 章：反思，第 5 章：工具使用，第 8 章：记忆管理，第 20 章：优先级排序，附录 C
* LangGraph(LangGraph) - 第 1 章：提示词链，第 2 章：路由，第 3 章：并行化，第 4 章：反思，第 5 章：工具使用，第 8 章：记忆管理，附录 C
* 延迟监控(Latency Monitoring) - 第 19 章：评估与监控
* 学习资源分配策略(Learned Resource Allocation Policies) - 第 16 章：资源感知优化
* 学习与适应(Learning and Adaptation) - 第 9 章：学习与适应
* LLM 作为裁判(LLM-as-a-Judge) - 第 19 章：评估与监控
* LlamaIndex(LlamaIndex) - 附录 C
* LoRA（低秩适应）(LoRA, Low-Rank Adaptation) - 术语表
* 低秩适应(Low-Rank Adaptation, LoRA) - 术语表

**M**

* Mamba \- Glossary  
* Masked Language Modeling (MLM) \- Glossary  
* MASS (Multi-Agent System Search) \- Chapter 17: Reasoning Techniques  
* MCP (Model Context Protocol) \- Chapter 10: Model Context Protocol (MCP)  
* Memory Management \- Chapter 8: Memory Management  
* Memory-Based Learning \- Chapter 9: Learning and Adaptation  
* MetaGPT \- Appendix C  
* Microsoft AutoGen \- Appendix C  
* Mixture of Experts (MoE) \- Glossary  
* Model Context Protocol (MCP) \- Chapter 10: Model Context Protocol (MCP)  
* Modularity \- Chapter 18: Guardrails/Safety Patterns  
* Monitoring \- Chapter 11: Goal Setting and Monitoring, Chapter 19: Evaluation and Monitoring  
* Multi-Agent Collaboration \- Chapter 7: Multi-Agent Collaboration  
* Multi-Agent System Search (MASS) \- Chapter 17: Reasoning Techniques  
* Multimodality \- Glossary  
* Multimodal Prompting \- Appendix A

* Mamba(Mamba) - 术语表
* 掩码语言建模(Masked Language Modeling, MLM) - 术语表
* MASS（多智能体搜索）(MASS, Multi-Agent System Search) - 第 17 章：推理技术
* MCP（模型上下文协议）(MCP, Model Context Protocol) - 第 10 章：模型上下文协议（MCP）
* 记忆管理(Memory Management) - 第 8 章：记忆管理
* 基于内存的学习(Memory-Based Learning) - 第 9 章：学习与适应
* MetaGPT(MetaGPT) - 附录 C
* Microsoft AutoGen(Microsoft AutoGen) - 附录 C
* 专家混合(Mixture of Experts, MoE) - 术语表
* 模型上下文协议(Model Context Protocol, MCP) - 第 10 章：模型上下文协议（MCP）
* 模块化(Modularity) - 第 18 章：护栏/安全模式
* 监控(Monitoring) - 第 11 章：目标设定与监控，第 19 章：评估与监控
* 多智能体协作(Multi-Agent Collaboration) - 第 7 章：多智能体协作
* 多智能体搜索(Multi-Agent System Search, MASS) - 第 17 章：推理技术
* 多模态(Multimodality) - 术语表
* 多模态提示(Multimodal Prompting) - 附录 A

**N**

* Negative Examples \- Appendix A  
* Next Sentence Prediction (NSP) \- Glossary

* 负面示例(Negative Examples) - 附录 A
* 下一句预测(Next Sentence Prediction, NSP) - 术语表

**O**

* Observability \- Chapter 18: Guardrails/Safety Patterns  
* One-Shot Prompting \- Appendix A  
* Online Learning \- Chapter 9: Learning and Adaptation  
* OpenAI Deep Research API \- Chapter 6: Planning  
* OpenEvolve \- Chapter 9: Learning and Adaptation  
* OpenRouter \- Chapter 16: Resource-Aware Optimization  
* Output Filtering/Post-processing \- Chapter 18: Guardrails/Safety Patterns

* 可观察性(Observability) - 第 18 章：护栏/安全模式
* 单样本提示(One-Shot Prompting) - 附录 A
* 在线学习(Online Learning) - 第 9 章：学习与适应
* OpenAI Deep Research API(OpenAI Deep Research API) - 第 6 章：规划
* OpenEvolve(OpenEvolve) - 第 9 章：学习与适应
* OpenRouter(OpenRouter) - 第 16 章：资源感知优化
* 输出过滤/后处理(Output Filtering/Post-processing) - 第 18 章：护栏/安全模式

**P**

* PAL (Program-Aided Language Models) \- Chapter 17: Reasoning Techniques  
* Parallelization \- Chapter 3: Parallelization  
* Parallelization & Distributed Computing Awareness \- Chapter 16: Resource-Aware Optimization  
* Parameter-Efficient Fine-Tuning (PEFT) \- Glossary  
* PEFT (Parameter-Efficient Fine-Tuning) \- Glossary  
* Performance Tracking \- Chapter 19: Evaluation and Monitoring  
* Persona Pattern \- Appendix A  
* Personalization \- What makes an AI system an Agent?  
* Planning \- Chapter 6: Planning, Glossary  
* Prioritization \- Chapter 20: Prioritization  
* Principle of Least Privilege \- Chapter 18: Guardrails/Safety Patterns  
* Proactive Resource Prediction \- Chapter 16: Resource-Aware Optimization  
* Procedural Memory \- Chapter 8: Memory Management  
* Program-Aided Language Models (PAL) \- Chapter 17: Reasoning Techniques  
* Proximal Policy Optimization (PPO) \- Chapter 9: Learning and Adaptation  
* Project Astra \- Appendix B  
* Prompt \- Glossary  
* Prompt Chaining \- Chapter 1: Prompt Chaining  
* Prompt Engineering \- Appendix A  
* Push Notifications \- Chapter 15: Inter-Agent Communication (A2A)

* PAL（程序辅助语言模型）(PAL, Program-Aided Language Models) - 第 17 章：推理技术
* 并行化(Parallelization) - 第 3 章：并行化
* 并行化与分布式计算感知(Parallelization & Distributed Computing Awareness) - 第 16 章：资源感知优化
* 参数高效微调(Parameter-Efficient Fine-Tuning, PEFT) - 术语表
* PEFT（参数高效微调）(PEFT, Parameter-Efficient Fine-Tuning) - 术语表
* 性能跟踪(Performance Tracking) - 第 19 章：评估与监控
* 角色模式(Persona Pattern) - 附录 A
* 个性化(Personalization) - 什么使 AI 系统成为 Agent？
* 规划(Planning) - 第 6 章：规划，术语表
* 优先级排序(Prioritization) - 第 20 章：优先级排序
* 最小权限原则(Principle of Least Privilege) - 第 18 章：护栏/安全模式
* 主动资源预测(Proactive Resource Prediction) - 第 16 章：资源感知优化
* 过程记忆(Procedural Memory) - 第 8 章：记忆管理
* 程序辅助语言模型(Program-Aided Language Models, PAL) - 第 17 章：推理技术
* 近端策略优化(Proximal Policy Optimization, PPO) - 第 9 章：学习与适应
* Project Astra(Project Astra) - 附录 B
* 提示词(Prompt) - 术语表
* 提示词链(Prompt Chaining) - 第 1 章：提示词链
* 提示工程(Prompt Engineering) - 附录 A
* 推送通知(Push Notifications) - 第 15 章：Agent 间通信（A2A）

**Q**

* QLoRA \- Glossary  
* Quality-Focused Iterative Execution \- Chapter 19: Evaluation and Monitoring

* QLoRA(QLoRA) - 术语表
* 质量导向迭代执行(Quality-Focused Iterative Execution) - 第 19 章：评估与监控

**R**

* RAG (Retrieval-Augmented Generation) \- Chapter 8: Memory Management, Chapter 14: Knowledge Retrieval (RAG), Appendix A  
* ReAct (Reason and Act) \- Chapter 17: Reasoning Techniques, Appendix A, Glossary  
* Reasoning \- Chapter 17: Reasoning Techniques  
* Reasoning-Based Information Extraction \- Chapter 10: Model Context Protocol (MCP)  
* Recovery \- Chapter 12: Exception Handling and Recovery  
* Recurrent Neural Network (RNN) \- Glossary  
* Reflection \- Chapter 4: Reflection  
* Reinforcement Learning \- Chapter 9: Learning and Adaptation  
* Reinforcement Learning from Human Feedback (RLHF) \- Glossary  
* Reinforcement Learning with Verifiable Rewards (RLVR) \- Chapter 17: Reasoning Techniques  
* Remote Agent \- Chapter 15: Inter-Agent Communication (A2A)  
* Request/Response (Polling) \- Chapter 15: Inter-Agent Communication (A2A)  
* Resource-Aware Optimization \- Chapter 16: Resource-Aware Optimization  
* Retrieval-Augmented Generation (RAG) \- Chapter 8: Memory Management, Chapter 14: Knowledge Retrieval (RAG), Appendix A  
* RLHF (Reinforcement Learning from Human Feedback) \- Glossary  
* RLVR (Reinforcement Learning with Verifiable Rewards) \- Chapter 17: Reasoning Techniques  
* RNN (Recurrent Neural Network) \- Glossary  
* Role Prompting \- Appendix A  
* Router Agent \- Chapter 16: Resource-Aware Optimization  
* Routing \- Chapter 2: Routing

* RAG（检索增强生成）(RAG, Retrieval-Augmented Generation) - 第 8 章：记忆管理，第 14 章：知识检索（RAG），附录 A
* ReAct（推理与行动）(ReAct, Reason and Act) - 第 17 章：推理技术，附录 A，术语表
* 推理(Reasoning) - 第 17 章：推理技术
* 基于推理的信息提取(Reasoning-Based Information Extraction) - 第 10 章：模型上下文协议（MCP）
* 恢复(Recovery) - 第 12 章：异常处理与恢复
* 循环神经网络(Recurrent Neural Network, RNN) - 术语表
* 反思(Reflection) - 第 4 章：反思
* 强化学习(Reinforcement Learning) - 第 9 章：学习与适应
* 基于人类反馈的强化学习(Reinforcement Learning from Human Feedback, RLHF) - 术语表
* 可验证奖励的强化学习(Reinforcement Learning with Verifiable Rewards, RLVR) - 第 17 章：推理技术
* 远程 Agent(Remote Agent) - 第 15 章：Agent 间通信（A2A）
* 请求/响应（轮询）(Request/Response, Polling) - 第 15 章：Agent 间通信（A2A）
* 资源感知优化(Resource-Aware Optimization) - 第 16 章：资源感知优化
* 检索增强生成(Retrieval-Augmented Generation, RAG) - 第 8 章：记忆管理，第 14 章：知识检索（RAG），附录 A
* RLHF（基于人类反馈的强化学习）(RLHF, Reinforcement Learning from Human Feedback) - 术语表
* RLVR（可验证奖励的强化学习）(RLVR, Reinforcement Learning with Verifiable Rewards) - 第 17 章：推理技术
* RNN（循环神经网络）(RNN, Recurrent Neural Network) - 术语表
* 角色提示(Role Prompting) - 附录 A
* 路由器 Agent(Router Agent) - 第 16 章：资源感知优化
* 路由(Routing) - 第 2 章：路由

**S**

* Safety \- Chapter 18: Guardrails/Safety Patterns  
* Scaling Inference Law \- Chapter 17: Reasoning Techniques  
* Scheduling \- Chapter 20: Prioritization  
* Self-Consistency \- Appendix A  
* Self-Correction \- Chapter 4: Reflection, Chapter 17: Reasoning Techniques  
* Self-Improving Coding Agent (SICA) \- Chapter 9: Learning and Adaptation  
* Self-Refinement \- Chapter 17: Reasoning Techniques  
* Semantic Kernel \- Appendix C  
* Semantic Memory \- Chapter 8: Memory Management  
* Semantic Similarity \- Chapter 14: Knowledge Retrieval (RAG)  
* Separation of Concerns \- Chapter 18: Guardrails/Safety Patterns  
* Sequential Handoffs \- Chapter 7: Multi-Agent Collaboration  
* Server-Sent Events (SSE) \- Chapter 15: Inter-Agent Communication (A2A)  
* Session \- Chapter 8: Memory Management  
* SICA (Self-Improving Coding Agent) \- Chapter 9: Learning and Adaptation  
* SMART Goals \- Chapter 11: Goal Setting and Monitoring  
* State \- Chapter 8: Memory Management  
* State Rollback \- Chapter 12: Exception Handling and Recovery  
* Step-Back Prompting \- Appendix A  
* Streaming Updates \- Chapter 15: Inter-Agent Communication (A2A)  
* Structured Logging \- Chapter 18: Guardrails/Safety Patterns  
* Structured Output \- Chapter 1: Prompt Chaining, Appendix A  
* SuperAGI \- Appendix C  
* Supervised Fine-Tuning (SFT) \- Glossary  
* Supervised Learning \- Chapter 9: Learning and Adaptation  
* System Prompting \- Appendix A

* 安全(Safety) - 第 18 章：护栏/安全模式
* 扩展推理法则(Scaling Inference Law) - 第 17 章：推理技术
* 调度(Scheduling) - 第 20 章：优先级排序
* 自一致性(Self-Consistency) - 附录 A
* 自我纠正(Self-Correction) - 第 4 章：反思，第 17 章：推理技术
* 自我改进编码 Agent(Self-Improving Coding Agent, SICA) - 第 9 章：学习与适应
* 自我细化(Self-Refinement) - 第 17 章：推理技术
* Semantic Kernel(Semantic Kernel) - 附录 C
* 语义记忆(Semantic Memory) - 第 8 章：记忆管理
* 语义相似性(Semantic Similarity) - 第 14 章：知识检索（RAG）
* 关注点分离(Separation of Concerns) - 第 18 章：护栏/安全模式
* 顺序交接(Sequential Handoffs) - 第 7 章：多智能体协作
* 服务器发送事件(Server-Sent Events, SSE) - 第 15 章：Agent 间通信（A2A）
* 会话(Session) - 第 8 章：记忆管理
* SICA（自我改进编码 Agent）(SICA, Self-Improving Coding Agent) - 第 9 章：学习与适应
* SMART 目标(SMART Goals) - 第 11 章：目标设定与监控
* 状态(State) - 第 8 章：记忆管理
* 状态回滚(State Rollback) - 第 12 章：异常处理与恢复
* 后退提示(Step-Back Prompting) - 附录 A
* 流式更新(Streaming Updates) - 第 15 章：Agent 间通信（A2A）
* 结构化日志(Structured Logging) - 第 18 章：护栏/安全模式
* 结构化输出(Structured Output) - 第 1 章：提示词链，附录 A
* SuperAGI(SuperAGI) - 附录 C
* 监督微调(Supervised Fine-Tuning, SFT) - 术语表
* 监督学习(Supervised Learning) - 第 9 章：学习与适应
* 系统提示(System Prompting) - 附录 A

**T**

* Task Evaluation \- Chapter 20: Prioritization  
* Text Similarity \- Chapter 14: Knowledge Retrieval (RAG)  
* Token Usage \- Chapter 19: Evaluation and Monitoring  
* Tool Use \- Chapter 5: Tool Use, Appendix A  
* Tool Use Restrictions \- Chapter 18: Guardrails/Safety Patterns  
* ToT (Tree of Thoughts) \- Chapter 17: Reasoning Techniques, Appendix A, Glossary  
* Transformers \- Glossary  
* Tree of Thoughts (ToT) \- Chapter 17: Reasoning Techniques, Appendix A, Glossary

* 任务评估(Task Evaluation) - 第 20 章：优先级排序
* 文本相似性(Text Similarity) - 第 14 章：知识检索（RAG）
* Token 使用(Token Usage) - 第 19 章：评估与监控
* 工具使用(Tool Use) - 第 5 章：工具使用，附录 A
* 工具使用限制(Tool Use Restrictions) - 第 18 章：护栏/安全模式
* ToT（思维树）(ToT, Tree of Thoughts) - 第 17 章：推理技术，附录 A，术语表
* Transformers(Transformers) - 术语表
* 思维树(Tree of Thoughts, ToT) - 第 17 章：推理技术，附录 A，术语表

**U**

* Unsupervised Learning \- Chapter 9: Learning and Adaptation  
* User Persona \- Appendix A

* 无监督学习(Unsupervised Learning) - 第 9 章：学习与适应
* 用户角色(User Persona) - 附录 A

**V**

* Validation \- Chapter 3: Parallelization  
* Vector Search \- Chapter 14: Knowledge Retrieval (RAG)  
* VertexAiRagMemoryService \- Chapter 8: Memory Management  
* VertexAiSessionService \- Chapter 8: Memory Management  
* Vibe Coding \- Appendix B  
* Visual Perception \- Appendix B

* 验证(Validation) - 第 3 章：并行化
* 向量搜索(Vector Search) - 第 14 章：知识检索（RAG）
* VertexAiRagMemoryService(VertexAiRagMemoryService) - 第 8 章：记忆管理
* VertexAiSessionService(VertexAiSessionService) - 第 8 章：记忆管理
* Vibe 编码(Vibe Coding) - 附录 B
* 视觉感知(Visual Perception) - 附录 B

**W**

* Webhooks \- Chapter 15: Inter-Agent Communication (A2A)

* Webhooks(Webhooks) - 第 15 章：Agent 间通信（A2A）

**Z**

* Zero-Shot Learning \- Chapter 9: Learning and Adaptation  
* Zero-Shot Prompting \- Appendix A

* 零样本学习(Zero-Shot Learning) - 第 9 章：学习与适应
* 零样本提示(Zero-Shot Prompting) - 附录 A

## Prompt

## 提示词

Below is the prompt that was utilized to create this index of terms.

以下是用于创建此术语索引的提示词。

| *do you read https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0 and all the related documents in the first page Please extract all the titles for each chapter. and print them. Then process the content of all the individual chapters, and create a detailed index used for publishing, a list of words or phrases ('headings') and associated pointers ('locators') to where useful material relating to that heading can be found in a document or collection of documents. I don't want a sample index. I want the full index, with 100 index terms* |
| :---- |

| *请阅读 https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0 及第一页中的所有相关文档。请提取各章节的所有标题并打印出来。然后处理所有独立章节的内容，创建一个用于出版的详细索引，包含单词或短语列表（"标题"）以及指向文档或文档集合中相关有用材料位置的指针（"定位符"）。我不需要示例索引，而是要求完整的索引，包含 100 个索引术语* |
| :---- |

## Gemini 2.5: Reasoning Steps

## Gemini 2.5：推理步骤

**Beginning Index Creation**

**开始创建索引**

I've initiated the process by reading the Google Doc provided. Currently, I'm focusing on understanding the user's request: extracting chapter titles to build a detailed index. I'm carefully reviewing the document, looking for clear structural elements that would indicate chapter breaks. I'm hoping to identify consistent formatting or keywords that will guide the indexing process.

我已启动索引创建流程，首先阅读了提供的 Google 文档。目前，我专注于理解用户需求：提取章节标题以构建详细索引。正在仔细审查文档内容，寻找能够标识章节分隔的清晰结构元素，期望能够识别出一致的格式模式或关键词来指导索引过程。
