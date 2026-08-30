# 术语索引

## 基本概念

**提示词（Prompt）：** 提示词是用户提供给 AI 模型的输入，通常以问题、指令或陈述的形式出现，用于引发响应。提示词的质量和结构极大地影响模型的输出，使提示词工程成为有效使用 AI 的关键技能。


**上下文窗口（Context Window）：** 上下文窗口是 AI 模型一次可以处理的最大 token 数量，包括输入和生成的输出。这个固定大小是一个关键限制，因为窗口外的信息会被忽略，而更大的窗口可以实现更复杂的对话和文档分析。


**上下文学习（In-Context Learning）：** 上下文学习是 AI 直接从提示词中提供的示例学习新任务的能力，无需任何重新训练。这个强大的功能允许单个通用模型即时适应无数特定任务。


**零样本、单样本和少样本提示（Zero-Shot, One-Shot, & Few-Shot Prompting）：** 这些是提示技术，其中向模型提供零个、一个或几个任务示例来指导其响应。提供更多示例通常有助于模型更好地理解用户意图，并提高特定任务的准确性。


**多模态（Multimodality）：** 多模态是 AI 理解和处理多种数据类型（如文本、图像和音频）信息的能力。这允许更多样化和类人的交互，例如描述图像或回答口头问题。


**基础化（Grounding）：** 基础化是将模型输出连接到可验证的真实世界信息源的过程，以确保事实准确性并减少幻觉。这通常通过 RAG 等技术实现，使 AI 系统更值得信赖。

## 核心 AI 模型架构

**Transformers：** Transformer 是大多数现代 LLM 的基础神经网络架构。其关键创新是自注意力机制，可以高效处理长文本序列并捕获单词之间的复杂关系。


**循环神经网络（Recurrent Neural Network, RNN）：** 循环神经网络是 Transformer 之前的基础架构。RNN 按顺序处理信息，使用循环来维护先前输入的"记忆"，这使它们适合文本和语音处理等任务。


**专家混合（Mixture of Experts, MoE）：** 专家混合是一种高效的模型架构，其中"路由器"网络动态选择一小部分"专家"网络来处理任何给定的输入。这允许模型拥有大量参数，同时保持可管理的计算成本。


**扩散模型（Diffusion Models）：** 扩散模型是擅长创建高质量图像的生成模型。它们通过向数据添加随机噪声，然后训练模型精确地逆转该过程来工作，允许它们从随机起点生成新颖的数据。


**Mamba：** Mamba 是一种最新的 AI 架构，使用选择性状态空间模型（SSM）以高效率处理序列，特别是对于非常长的上下文。其选择性机制允许它专注于相关信息同时过滤噪声，使其成为 Transformer 的潜在替代方案。

## LLM 开发生命周期

强大语言模型的开发遵循明确的顺序。它始于预训练（Pre-training），在大量通用互联网文本数据集上训练大规模基础模型，以学习语言、推理和世界知识。接下来是微调（Fine-tuning），这是一个专业化阶段，在较小的特定任务数据集上进一步训练通用模型，以使其能力适应特定目的。最后阶段是对齐（Alignment），调整专业化模型的行为，以确保其输出有帮助、无害且与人类价值观保持一致。


**预训练技术：** 预训练是模型从大量数据中学习通用知识的初始阶段。这方面的顶级技术涉及模型学习的不同目标。最常见的是因果语言建模（CLM），其中模型预测句子中的下一个单词。另一种是掩码语言建模（MLM），其中模型填充文本中故意隐藏的单词。其他重要方法包括去噪目标，其中模型学习将损坏的输入恢复到其原始状态，对比学习，其中它学习区分相似和不相似的数据片段，以及下一句预测（NSP），其中它确定两个句子是否在逻辑上相互跟随。


**微调技术：** 微调是使用较小的专业化数据集将通用预训练模型适应特定任务的过程。最常见的方法是监督微调（SFT），其中模型在标记的正确输入输出对示例上进行训练。一个流行的变体是指令调优，专注于训练模型更好地遵循用户命令。为了使此过程更高效，使用参数高效微调（PEFT）方法，顶级技术包括 LoRA（低秩适应），仅更新少量参数，以及其内存优化版本 QLoRA。另一种技术，检索增强生成（RAG），通过在微调或推理阶段将模型连接到外部知识源来增强模型。


**对齐和安全技术：** 对齐是确保 AI 模型行为与人类价值观和期望保持一致的过程，使其有帮助且无害。最突出的技术是基于人类反馈的强化学习（RLHF），其中在人类偏好上训练的"奖励模型"指导 AI 的学习过程，通常使用近端策略优化（PPO）等算法来保持稳定性。已经出现了更简单的替代方案，例如直接偏好优化（DPO），它绕过了对单独奖励模型的需求，以及 Kahneman-Tversky 优化（KTO），它进一步简化了数据收集。为确保安全部署，实施护栏作为最终安全层，以实时过滤输出并阻止有害行为。

## 增强 AI 智能体

AI 智能体是能够感知其环境并采取自主行动以实现目标的系统。它们的有效性通过强大的推理框架得到增强。


**思维链（Chain of Thought, CoT）：** 这种提示技术鼓励模型在给出最终答案之前逐步解释其推理。这种"大声思考"的过程通常会在复杂推理任务上产生更准确的结果。


**思维树（Tree of Thoughts, ToT）：** 思维树是一种高级推理框架，其中智能体探索多个推理路径，就像树上的分支一样。它允许智能体探索不同的思路并选择最有希望的路径，使其在复杂问题解决方面更有效。


**ReAct（推理与行动，Reason and Act）：** ReAct 是一个智能体，在循环中结合推理和行动。Agent 首先"思考"要做什么，然后使用工具采取"行动"，并使用结果观察来通知其下一个想法，使其在解决复杂任务方面非常有效。


**规划（Planning）：** 这是智能体将高级目标分解为一系列较小的、可管理的子任务的能力。然后智能体使用计划来按顺序执行这些步骤，使其能够处理复杂的多步骤任务。


**深度研究（Deep Research）：** 深度研究是指智能体迭代搜索信息、综合发现和识别新问题来自主深入探索主题的能力。这允许智能体获得对主题的全面理解，远超单个搜索查询。


**评判模型（Critique Model）：** 评判模型是一种专门的 AI 模型，经过训练可以审查、评估和提供关于另一个 AI 模型输出的反馈。它充当自动评审者，有助于识别错误、改进推理并确保最终输出符合期望的质量标准。

## 术语索引

此术语索引使用 Gemini Pro 2.5 生成。提示词和推理步骤包含在末尾，以展示 AI 辅助索引创建的效率优势并用于教育目的。

**A**

* A/B 测试(A/B Testing) - 第 3 章：并行化
* 行动选择(Action Selection) - 第 20 章：优先级排序
* 适应(Adaptation) - 第 9 章：学习与适应
* 自适应任务分配(Adaptive Task Allocation) - 第 16 章：资源感知优化
* 自适应工具使用与选择(Adaptive Tool Use &amp; Selection) - 第 16 章：资源感知优化
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

* 行为约束(Behavioral Constraints) - 第 18 章：护栏/安全模式
* 浏览器使用(Browser Use) - 附录 B

**C**

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
* 上下文修剪与摘要(Contextual Pruning &amp; Summarization) - 第 16 章：资源感知优化
* 上下文提示(Contextual Prompting) - 附录 A
* 承包商模型(Contractor Model) - 第 19 章：评估与监控
* ConversationBufferMemory(ConversationBufferMemory) - 第 8 章：记忆管理
* 对话式 Agent(Conversational Agents) - 第 1 章：提示词链，第 4 章：反思
* 成本敏感探索(Cost-Sensitive Exploration) - 第 16 章：资源感知优化
* CrewAI(CrewAI) - 第 3 章：并行化，第 5 章：工具使用，第 6 章：规划，第 7 章：多智能体协作，第 18 章：护栏/安全模式，附录 C
* 批评智能体(Critique Agent) - 第 16 章：资源感知优化
* 评判模型(Critique Model) - 术语表
* 客户支持(Customer Support) - 第 13 章：人机协同

**D**

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

* 分解式认知/任务分解(Factored Cognition) - 附录 A
* FastMCP(FastMCP) - 第 10 章：模型上下文协议（MCP）
* 容错(Fault Tolerance) - 第 18 章：护栏/安全模式
* 少样本学习(Few-Shot Learning) - 第 9 章：学习与适应
* 少样本提示(Few-Shot Prompting) - 附录 A
* 微调(Fine-tuning) - 术语表
* 正式化合同(Formalized Contract) - 第 19 章：评估与监控
* 工具调用(Tool Calling) - 第 5 章：工具使用，附录 A

**G**

* Gemini Live(Gemini Live) - 附录 B
* Gems(Gems) - 附录 A
* 生成媒体编排(Generative Media Orchestration) - 第 10 章：模型上下文协议（MCP）
* 目标设定(Goal Setting) - 第 11 章：目标设定与监控
* GoD（辩论图）(GoD, Graph of Debates) - 第 17 章：推理技术
* Google 智能体开发工具包(Google Agent Development Kit, ADK) - 第 2 章：路由，第 3 章：并行化，第 4 章：反思，第 5 章：工具使用，第 7 章：多智能体协作，第 8 章：记忆管理，第 12 章：异常处理与恢复，第 13 章：人机协同，第 15 章：Agent 间通信（A2A），第 16 章：资源感知优化，第 19 章：评估与监控，附录 C
* Google 联合科学家(Google Co-Scientist) - 第 21 章：探索与发现
* Google DeepResearch(Google DeepResearch) - 第 6 章：规划
* 辩论图(Graph of Debates, GoD) - 第 17 章：推理技术
* Google Project Mariner(Google Project Mariner) - 附录 B
* 优雅降级(Graceful Degradation) - 第 12 章：异常处理与恢复，第 16 章：资源感知优化
* 基础化(Grounding) - 术语表
* 护栏(Guardrails) - 第 18 章：护栏/安全模式

**H**

* Haystack(Haystack) - 附录 C
* 层次化分解(Hierarchical Decomposition) - 第 19 章：评估与监控
* 层次化结构(Hierarchical Structures) - 第 7 章：多智能体协作
* HITL（人机协同）(HITL, Human-in-the-Loop) - 第 13 章：人机协同
* 人机协同(Human-in-the-Loop, HITL) - 第 13 章：人机协同
* 人在环路上(Human-on-the-loop) - 第 13 章：人机协同
* 人类监督(Human Oversight) - 第 13 章：人机协同，第 18 章：护栏/安全模式

**I**

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

* 越狱(Jailbreaking) - 第 18 章：护栏/安全模式

**K**

* Kahneman-Tversky 优化(Kahneman-Tversky Optimization, KTO) - 术语表
* 知识检索(Knowledge Retrieval, RAG) - 第 14 章：知识检索（RAG）

**L**

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

* 负面示例(Negative Examples) - 附录 A
* 下一句预测(Next Sentence Prediction, NSP) - 术语表

**O**

* 可观察性(Observability) - 第 18 章：护栏/安全模式
* 单样本提示(One-Shot Prompting) - 附录 A
* 在线学习(Online Learning) - 第 9 章：学习与适应
* OpenAI Deep Research API(OpenAI Deep Research API) - 第 6 章：规划
* OpenEvolve(OpenEvolve) - 第 9 章：学习与适应
* OpenRouter(OpenRouter) - 第 16 章：资源感知优化
* 输出过滤/后处理(Output Filtering/Post-processing) - 第 18 章：护栏/安全模式

**P**

* PAL（程序辅助语言模型）(PAL, Program-Aided Language Models) - 第 17 章：推理技术
* 并行化(Parallelization) - 第 3 章：并行化
* 并行化与分布式计算感知(Parallelization &amp; Distributed Computing Awareness) - 第 16 章：资源感知优化
* 参数高效微调(Parameter-Efficient Fine-Tuning, PEFT) - 术语表
* PEFT（参数高效微调）(PEFT, Parameter-Efficient Fine-Tuning) - 术语表
* 性能跟踪(Performance Tracking) - 第 19 章：评估与监控
* 角色模式(Persona Pattern) - 附录 A
* 个性化(Personalization) - 什么使 AI 系统成为 Agent？
* 规划(Planning) - 第 6 章：规划，术语表
* 优先级排序(Prioritization) - 第 20 章：优先级排序
* 最小权限原则(Principle of Least Privilege) - 附录 B
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

* QLoRA(QLoRA) - 术语表
* 质量导向迭代执行(Quality-Focused Iterative Execution) - 第 19 章：评估与监控

**R**

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
* 路由器智能体(Router Agent) - 第 16 章：资源感知优化
* 路由(Routing) - 第 2 章：路由

**S**

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

* 任务评估(Task Evaluation) - 第 20 章：优先级排序
* 文本相似性(Text Similarity) - 第 14 章：知识检索（RAG）
* Token 使用(Token Usage) - 第 19 章：评估与监控
* 工具使用(Tool Use) - 第 5 章：工具使用，附录 A
* 工具使用限制(Tool Use Restrictions) - 第 18 章：护栏/安全模式
* ToT（思维树）(ToT, Tree of Thoughts) - 第 17 章：推理技术，附录 A，术语表
* Transformers(Transformers) - 术语表
* 思维树(Tree of Thoughts, ToT) - 第 17 章：推理技术，附录 A，术语表

**U**

* 无监督学习(Unsupervised Learning) - 第 9 章：学习与适应
* 用户角色(User Persona) - 附录 A

**V**

* 验证(Validation) - 第 3 章：并行化
* 向量搜索(Vector Search) - 第 14 章：知识检索（RAG）
* VertexAiRagMemoryService(VertexAiRagMemoryService) - 第 8 章：记忆管理
* VertexAiSessionService(VertexAiSessionService) - 第 8 章：记忆管理
* Vibe 编码(Vibe Coding) - 附录 B
* 视觉感知(Visual Perception) - 附录 B

**W**

* Webhooks(Webhooks) - 第 15 章：Agent 间通信（A2A）

**Z**

* 零样本学习(Zero-Shot Learning) - 第 9 章：学习与适应
* 零样本提示(Zero-Shot Prompting) - 附录 A


## 提示词

以下是用于创建此术语索引的提示词。

| *请阅读 https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0 及第一页中的所有相关文档。请提取各章节的所有标题并打印出来。然后处理所有独立章节的内容，创建一个用于出版的详细索引，包含单词或短语列表（"标题"）以及指向文档或文档集合中相关有用材料位置的指针（"定位符"）。我不需要示例索引，而是要求完整的索引，包含 100 个索引术语* |
| :---- |

## Gemini 2.5：推理步骤

**开始创建索引**

我已启动索引创建流程，首先阅读了提供的 Google 文档。目前，我专注于理解用户需求：提取章节标题以构建详细索引。正在仔细审查文档内容，寻找能够标识章节分隔的清晰结构元素，期望能够识别出一致的格式模式或关键词来指导索引过程。

**定义索引提取流程**

现在已完全投入到此任务中。已将用户请求分解为可执行的步骤：初始阶段使用 Workspaces 访问主 Google 文档，接着解析文档以定位并检索相关文档（同样使用 Workspaces 工具），最后从所有文档中提取章节标题并创建全面索引。已规划完整的详细流程。

**完善提取策略**

用户指令明确：阅读 Google 文档及其相关文档，构建章节标题的详细索引。已制定多步骤计划：Workspaces 首先访问主文档，然后解析并检索相关文档，同样使用 Workspaces。当前专注于提取标题并使用所需术语构建详细索引，优先确保准确性以满足用户对综合索引的特定要求。

**1. 确定用户意图**

已明确用户需求：获取来自 Google 文档及相关文档的章节标题列表和综合索引。现在需要确定最有效的提取和索引方法，正在探索潜在的 API 功能来简化此任务，并评估处理不同文档结构的最佳策略。

**3. 考虑工具使用**

已使用正则表达式从主文档中提取了章节 URL。现在准备利用 Workspaces 检索各章节的实际内容。一旦获得各章节文本，将立即开始索引工作。

**访问章节内容**

已成功从主文档中识别出各章节 URL，现在可使用 Workspaces。下一步是从这些 URL 检索内容，以便生成索引。专注于效率优化，旨在快速处理这些信息。

**获取章节内容**

已成功从主文档中识别出章节 URL，准备使用 Workspaces。计划包括提取这些 URL、批量处理调用以提高效率，然后处理检索内容以创建所需索引。这确保捕获所有相关信息，为全面准确的结果奠定基础。

**启动 URL 检索**

现已成功从主文档中提取章节 URL。目前正在设置对 Workspaces 工具的调用，准备获取各章节内容。目标是获取索引所需的文本内容，进而促进创建包含至少 100 个术语的索引。

**启动章节提取**

已成功从主文档中识别并提取章节 URL（如上所列）。现在继续为每个 URL 使用 Workspaces 以获取章节内容。目标是获取索引所需的文本，进而促进创建包含至少 100 个术语的索引。已开始检索相关信息。

**编排章节检索**

已提取章节 URL 并发起对 Workspaces 的调用。目前正在检索各章节内容。为确保流程顺畅，正在进行批量调用处理以防止速率限制问题。这应能高效编译索引所需文本。

**解码用户请求**

已明确用户需求：两个主要交付成果——从 Google 文档提取的章节标题综合列表，以及包含至少一百个关键术语的详细索引。提取标题的过程相对直接，而策划索引则需要更细致的分析工作。

**提取标题和索引**

已成功识别用户需求：从提供文档中提取章节标题并编制综合索引。已获取 31 个 Google 文档的内容，包括主文档及其各章节。确认无需额外工具。计划包含两个步骤：首先从文档文件名中提取章节标题，其次精心处理文本内容，使用关键术语和章节定位符构建索引。

**制定提取计划**

已完善处理用户请求的方法。现制定精确计划：首先从 31 个已获取文档的文件名中编制章节标题，其次（更复杂的部分）精心分析内容以创建超过 100 个条目的综合、按字母顺序排列的索引。已最终确定提取和索引策略，现在可以开始执行。

**制定提取策略**

方法已明确定义：从 31 个已获取文档的文件名中编制章节标题，随后精心分析内容以构建按字母顺序组织、超过 100 个条目的索引。已最终确定提取和索引策略，现在可以开始实施。用户获取详细索引的目标——涵盖 Agentic 设计模式系列中各个章节和附录的内容——现已触手可及。将专注于提供全面响应，超越简单的示例索引。

**定义方法**

已明确用户需求：从文档文件名中提取章节标题，随后精心创建超过 100 个条目的索引，按字母顺序排列并注明章节位置。准备开始索引和提取过程。