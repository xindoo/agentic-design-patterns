# 第 21 章：探索和发现

本章探讨了使智能 Agent 能够主动寻求新信息、发现新可能性并识别其操作环境中未知的未知因素的模式。探索和发现不同于被动行为或在预定义解决方案空间内的优化。相反，它们侧重于 Agent 主动进入陌生领域、尝试新方法并生成新知识或理解。这种模式对于在开放式、复杂或快速演变的领域中运行的 Agent 至关重要，在这些领域中，静态知识或预编程的解决方案是不够的。它强调 Agent 扩展其理解和能力的能力。

## 实际应用和用例

AI Agent 具有智能优先级排序和探索的能力，这导致了跨各个领域的应用。通过自主评估和排序潜在行动，这些 Agent 可以导航复杂环境、发现隐藏的洞察并推动创新。这种优先探索的能力使它们能够优化流程、发现新知识并生成内容。

示例：

* **科学研究自动化**：Agent 设计和运行实验、分析结果并制定新假设，以发现新材料、候选药物或科学原理。
* **游戏玩法和策略生成**：Agent 探索游戏状态，发现新兴策略或识别游戏环境中的漏洞（例如 AlphaGo）。
* **市场研究和趋势发现**：Agent 扫描非结构化数据（社交媒体、新闻、报告）以识别趋势、消费者行为或市场机会。
* **安全漏洞发现**：Agent 探测系统或代码库以查找安全漏洞或攻击向量。
* **创意内容生成**：Agent 探索风格、主题或数据的组合，以生成艺术作品、音乐作品或文学作品。
* **个性化教育和培训**：AI 导师根据学生的进度、学习风格和需要改进的领域来优先处理学习路径和内容交付。

Google Co-Scientist

AI 协同科学家是由 Google Research 开发的 AI 系统，被设计为计算科学合作者。它在假设生成、提案改进和实验设计等研究方面协助人类科学家。该系统基于 Gemini LLM 运行。

AI 协同科学家的开发解决了科学研究中的挑战。这些挑战包括处理大量信息、生成可测试的假设以及管理实验规划。AI 协同科学家通过执行涉及大规模信息处理和综合的任务来支持研究人员，可能揭示数据中的关系。其目的是通过处理早期阶段研究中计算密集型方面来增强人类认知过程。

**系统架构和方法论：** AI 协同科学家的架构基于多 Agent 框架，结构化以模拟协作和迭代过程。这种设计集成了专门的 AI Agent，每个 Agent 在为研究目标做出贡献方面都有特定的角色。一个主管 Agent 管理和协调这些单独 Agent 在异步任务执行框架内的活动，该框架允许计算资源的灵活扩展。

核心 Agent 及其功能包括（见图 1）：

* **生成 Agent**：通过文献探索和模拟科学辩论来生成初始假设，从而启动流程。
* **反思 Agent**：作为同行评审员，批判性地评估生成假设的正确性、新颖性和质量。
* **排名 Agent**：采用基于 Elo 的锦标赛，通过模拟科学辩论来比较、排名和优先处理假设。
* **进化 Agent**：通过简化概念、综合想法和探索非常规推理，不断完善排名靠前的假设。
* **接近度 Agent**：计算接近度图以聚类相似想法并协助探索假设景观。
* **元审查 Agent**：综合所有审查和辩论的见解，以识别共同模式并提供反馈，使系统能够持续改进。

该系统的运营基础依赖于 Gemini，它提供语言理解、推理和生成能力。该系统包含"测试时计算扩展"，这是一种分配增加的计算资源以迭代推理和增强输出的机制。该系统处理和综合来自不同来源的信息，包括学术文献、基于网络的数据和数据库。

![][image1]图 1：（由作者提供）AI 协同科学家：从构思到验证

该系统遵循反映科学方法的迭代"生成、辩论和进化"方法。在从人类科学家那里接收科学问题的输入后，系统参与假设生成、评估和改进的自我改进循环。假设经过系统评估，包括 Agent 之间的内部评估和基于锦标赛的排名机制。

**验证和结果：** AI 协同科学家的效用已在几项验证研究中得到证明，特别是在生物医学领域，通过自动化基准、专家评审和端到端湿实验室实验来评估其性能。

**自动化和专家评估：** 在具有挑战性的 GPQA 基准上，该系统的内部 Elo 评级被证明与其结果的准确性一致，在困难的"钻石集"上实现了 78.4% 的 top-1 准确率。对超过 200 个研究目标的分析表明，扩展测试时计算可持续提高假设的质量，通过 Elo 评级来衡量。在精心策划的 15 个挑战性问题集上，AI 协同科学家的表现优于其他最先进的 AI 模型和人类专家提供的"最佳猜测"解决方案。在小规模评估中，生物医学专家将协同科学家的输出评为比其他基线模型更新颖、更有影响力。该系统针对药物再利用的提案（格式化为 NIH 特定目标页面）也被六位专家肿瘤学家小组评判为高质量。

**端到端实验验证：**

药物再利用：对于急性髓系白血病（AML），该系统提出了新的候选药物。其中一些，如 KIRA6，是完全新颖的建议，之前没有在 AML 中使用的临床前证据。随后的体外实验证实，KIRA6 和其他建议的药物在多个 AML 细胞系中以临床相关浓度抑制肿瘤细胞活力。

新靶点发现：该系统识别了肝纤维化的新表观遗传靶点。使用人类肝脏类器官的实验室实验验证了这些发现，表明针对建议的表观遗传修饰剂的药物具有显著的抗纤维化活性。其中一种已识别的药物已被 FDA 批准用于另一种疾病，为再利用提供了机会。

抗微生物耐药性：AI 协同科学家独立重现了未发表的实验发现。它被要求解释为什么某些移动遗传元件（cf-PICIs）在许多细�菌种中被发现。在两天内，该系统排名最高的假设是 cf-PICIs 与不同的噬菌体尾部相互作用以扩展其宿主范围。这反映了一个独立研究小组在十多年的研究后达到的新颖的、经实验验证的发现。

**增强和局限性：** AI 协同科学家背后的设计理念强调增强而不是完全自动化人类研究。研究人员通过自然语言与系统交互并指导系统，提供反馈、贡献自己的想法，并在"科学家在环"的协作范式中指导 AI 的探索过程。然而，该系统有一些局限性。其知识受到对开放获取文献的依赖的限制，可能会遗漏付费墙后的关键先前工作。它对负面实验结果的访问也有限，这些结果很少发表，但对经验丰富的科学家至关重要。此外，该系统继承了底层 LLM 的局限性，包括事实不准确或"幻觉"的潜力。

**安全性：** 安全性是一个关键考虑因素，系统包含多个保障措施。所有研究目标在输入时都会进行安全审查，生成的假设也会被检查，以防止系统被用于不安全或不道德的研究。使用 1,200 个对抗性研究目标进行的初步安全评估发现，该系统可以稳健地拒绝危险输入。为确保负责任的开发，该系统正通过可信测试者计划向更多科学家提供，以收集实际反馈。

## 实践代码示例

让我们看一个探索和发现中 Agentic AI 的具体示例：Agent Laboratory，这是 Samuel Schmidgall 在 MIT 许可下开发的项目。

"Agent Laboratory"是一个自主研究工作流框架，旨在增强而不是取代人类科学努力。该系统利用专门的 LLM 来自动化科学研究过程的各个阶段，从而使人类研究人员能够将更多认知资源用于概念化和批判性分析。

该框架集成了"AgentRxiv"，这是一个用于自主研究 Agent 的去中心化存储库。AgentRxiv 促进研究输出的存储、检索和开发。

Agent Laboratory 通过不同的阶段指导研究过程：

1. **文献综述**：在这个初始阶段，专门的 LLM 驱动的 Agent 负责自主收集和批判性分析相关学术文献。这涉及利用 arXiv 等外部数据库来识别、综合和分类相关研究，有效地为后续阶段建立全面的知识库。
2. **实验**：此阶段包括实验设计的协作制定、数据准备、实验执行和结果分析。Agent 利用集成工具（如用于代码生成和执行的 Python，以及用于模型访问的 Hugging Face）来进行自动化实验。该系统设计用于迭代改进，Agent 可以根据实时结果调整和优化实验程序。
3. **报告撰写**：在最后阶段，系统自动生成全面的研究报告。这涉及将实验阶段的发现与文献综述的见解相结合，根据学术惯例构建文档，并集成外部工具（如用于专业格式化和图形生成的 LaTeX）。
4. **知识共享**：AgentRxiv 是一个平台，使自主研究 Agent 能够共享、访问和协作推进科学发现。它允许 Agent 在先前发现的基础上构建，促进累积的研究进展。

Agent Laboratory 的模块化架构确保了计算灵活性。目标是通过自动化任务来提高研究生产力，同时保持人类研究人员的参与。

**代码分析：** 虽然全面的代码分析超出了本书的范围，但我想为您提供一些关键见解，并鼓励您自己深入研究代码。

**判断：** 为了模拟人类评估过程，系统采用三方 Agentic 判断机制来评估输出。这涉及部署三个不同的自主 Agent，每个 Agent 配置为从特定角度评估产出，从而共同模仿人类判断的细致和多方面性质。这种方法允许更稳健和全面的评估，超越单一指标以捕获更丰富的定性评估。

```python
class ReviewersAgent:
    def __init__(self, model="gpt-4o-mini", notes=None, openai_api_key=None):
        if notes is None:
            self.notes = []
        else:
            self.notes = notes
        self.model = model
        self.openai_api_key = openai_api_key

    def inference(self, plan, report):
        reviewer_1 = "你是一个严格但公平的审稿人，期望能够为研究主题带来见解的良好实验。"
        review_1 = get_score(outlined_plan=plan, latex=report, reward_model_llm=self.model, reviewer_type=reviewer_1, openai_api_key=self.openai_api_key)
        reviewer_2 = "你是一个严格、挑剔但公平的审稿人，正在寻找一个在该领域具有影响力的想法。"
        review_2 = get_score(outlined_plan=plan, latex=report, reward_model_llm=self.model, reviewer_type=reviewer_2, openai_api_key=self.openai_api_key)
        reviewer_3 = "你是一个严格但公平、思想开放的审稿人，正在寻找以前未曾提出过的新颖想法。"
        review_3 = get_score(outlined_plan=plan, latex=report, reward_model_llm=self.model, reviewer_type=reviewer_3, openai_api_key=self.openai_api_key)
        return f"审稿人 #1:\n{review_1}, \n审稿人 #2:\n{review_2}, \n审稿人 #3:\n{review_3}"
```

判断 Agent 的设计采用了特定的提示词，该提示词密切模拟了人类审稿人通常采用的认知框架和评估标准。此提示词指导 Agent 通过类似于人类专家的方式分析输出，考虑相关性、连贯性、事实准确性和整体质量等因素。通过精心设计这些提示词以反映人类审查协议，该系统旨在实现接近人类判断力的评估复杂性水平。

| ````def get_score(outlined_plan, latex, reward_model_llm, reviewer_type=None, attempts=3, openai_api_key=None):    e = str()    for _attempt in range(attempts):        try:                       template_instructions = """            按以下格式响应：            思考：            <思考>            审查 JSON：            ```json            <JSON>            ```            在 <思考> 中，首先简要讨论您对评估的直觉和推理。            详细说明您的高层次论点、必要的选择和审查的预期结果。            不要在这里做出泛泛的评论，而是针对您当前的论文具体说明。            将此视为审查的笔记阶段。            在 <JSON> 中，以 JSON 格式提供审查，字段按以下顺序排列：            - "Summary"：论文内容及其贡献的摘要。            - "Strengths"：论文的优点列表。            - "Weaknesses"：论文的缺点列表。            - "Originality"：从 1 到 4 的评级（低、中、高、非常高）。            - "Quality"：从 1 到 4 的评级（低、中、高、非常高）。            - "Clarity"：从 1 到 4 的评级（低、中、高、非常高）。            - "Significance"：从 1 到 4 的评级（低、中、高、非常高）。            - "Questions"：论文作者需要回答的一组澄清性问题。            - "Limitations"：工作的一组局限性和潜在的负面社会影响。            - "Ethical Concerns"：一个布尔值，指示是否存在道德问题。            - "Soundness"：从 1 到 4 的评级（差、一般、好、优秀）。            - "Presentation"：从 1 到 4 的评级（差、一般、好、优秀）。            - "Contribution"：从 1 到 4 的评级（差、一般、好、优秀）。            - "Overall"：从 1 到 10 的评级（非常强烈拒绝到获奖质量）。            - "Confidence"：从 1 到 5 的评级（低、中、高、非常高、绝对）。            - "Decision"：必须是以下之一的决定：Accept、Reject。            对于 "Decision" 字段，不要使用 Weak Accept、Borderline Accept、Borderline Reject 或 Strong Reject。              相反，只使用 Accept 或 Reject。            此 JSON 将被自动解析，因此请确保格式精确。            """```` |
| :---- |

在这个多 Agent 系统中，研究过程围绕专门角色构建，反映了典型的学术层次结构，以简化工作流程并优化输出。

**教授 Agent：** 教授 Agent 充当主要研究主管，负责建立研究议程、定义研究问题并将任务委托给其他 Agent。该 Agent 设定战略方向并确保与项目目标保持一致。

```python
class ProfessorAgent(BaseAgent):
    def __init__(self, model="gpt4omini", notes=None, max_steps=100, openai_api_key=None):
        super().__init__(model, notes, max_steps, openai_api_key)
        self.phases = ["report writing"]

    def generate_readme(self):
        sys_prompt = f"""您是 {self.role_description()} \n 这是撰写的论文 \n{self.report}。任务说明：您的目标是整合提供给您的所有知识、代码、报告和笔记，并为 github 存储库生成 readme.md。"""
        history_str = "\n".join([_[1] for _ in self.history])
        prompt = (
            f"""历史记录：{history_str}\n{'~' * 10}\n"""
            f"请在下面以 markdown 格式生成 readme：\n")
        model_resp = query_model(model_str=self.model, system_prompt=sys_prompt, prompt=prompt, openai_api_key=self.openai_api_key)
        return model_resp.replace("```markdown", "")
```

**博士后 Agent：** 博士后 Agent 的角色是执行研究。这包括进行文献综述、设计和实施实验以及生成研究输出（如论文）。重要的是，博士后 Agent 具有编写和执行代码的能力，使实验协议和数据分析的实际实施成为可能。该 Agent 是研究成果的主要生产者。

```python
class PostdocAgent(BaseAgent):
    def __init__(self, model="gpt4omini", notes=None, max_steps=100, openai_api_key=None):
        super().__init__(model, notes, max_steps, openai_api_key)
        self.phases = ["plan formulation", "results interpretation"]

    def context(self, phase):
        sr_str = str()
        if self.second_round:
            sr_str = (
                f"以下是先前实验的结果\n",
                f"先前的实验代码：{self.prev_results_code}\n"
                f"先前的结果：{self.prev_exp_results}\n"
                f"先前对结果的解释：{self.prev_interpretation}\n"
                f"先前的报告：{self.prev_report}\n"
                f"{self.reviewer_response}\n\n\n"
            )
        if phase == "plan formulation":
            return (
                sr_str,
                f"当前文献综述：{self.lit_review_sum}",
            )
        elif phase == "results interpretation":
            return (
                sr_str,
                f"当前文献综述：{self.lit_review_sum}\n"
                f"当前计划：{self.plan}\n"
                f"当前数据集代码：{self.dataset_code}\n"
                f"当前实验代码：{self.results_code}\n"
                f"当前结果：{self.exp_results}"
            )
        return ""
```

**审稿人 Agent：** 审稿人 Agent 对博士后 Agent 的研究输出进行批判性评估，评估论文和实验结果的质量、有效性和科学严谨性。这个评估阶段模拟学术环境中的同行评审过程，以确保在最终确定之前研究输出的高标准。

**机器学习工程 Agent：** 机器学习工程 Agent 充当机器学习工程师，与博士生进行对话式协作以开发代码。他们的核心功能是为数据预处理生成简单的代码，整合从提供的文献综述和实验协议中得出的见解。这确保数据被适当格式化并为指定的实验做好准备。

```python
"您是一位机器学习工程师，由一位博士生指导，他将帮助您编写代码，您可以通过对话与他们互动。\n"
"您的目标是生成为提供的实验准备数据的代码。您应该追求简单的代码来准备数据，而不是复杂的代码。您应该整合提供的文献综述和计划，并为此实验准备数据的代码。\n"
```

**软件工程 Agent：** 软件工程 Agent 指导机器学习工程 Agent。他们的主要目的是协助机器学习工程 Agent 为特定实验创建简单的数据准备代码。软件工程 Agent 整合提供的文献综述和实验计划，确保生成的代码简单明了，并与研究目标直接相关。

```python
"您是一位软件工程师，正在指导一位机器学习工程师，机器学习工程师将编写代码，您可以通过对话与他们互动。\n"
"您的目标是帮助机器学习工程师生成为提供的实验准备数据的代码。您应该追求非常简单的代码来准备数据，而不是复杂的代码。您应该整合提供的文献综述和计划，并为此实验准备数据的代码。\n"
```

总之，"Agent Laboratory"代表了自主科学研究的复杂框架。它旨在通过自动化关键研究阶段和促进 AI 驱动的知识生成来增强人类研究能力。该系统旨在通过管理日常任务来提高研究效率，同时保持人类监督。

## 概览

**定义（What）：** AI Agent 通常在预定义的知识范围内运行，限制了它们处理新情况或开放式问题的能力。在复杂和动态的环境中，这种静态的、预编程的信息不足以实现真正的创新或发现。根本挑战是使 Agent 能够超越简单的优化，主动寻求新信息并识别"未知的未知因素"。这需要从纯粹的被动行为转变为扩展系统自身理解和能力的主动 Agentic 探索。

**原因（Why）：** 标准化的解决方案是构建专门用于自主探索和发现的 Agentic AI 系统。这些系统通常利用多 Agent 框架，其中专门的 LLM 协作以模拟科学方法等过程。例如，可以为不同的 Agent 分配生成假设、批判性审查它们以及发展最有前途的概念的任务。这种结构化的协作方法允许系统智能地导航庞大的信息景观、设计和执行实验并生成真正的新知识。通过自动化探索的劳动密集型方面，这些系统增强了人类智力并显著加速了发现的步伐。

**经验法则（Rule of thumb）：** 当在开放式、复杂或快速演变的领域中运行时，使用探索和发现模式，在这些领域中解决方案空间没有完全定义。它非常适合需要生成新假设、策略或见解的任务，例如科学研究、市场分析和创意内容生成。当目标是发现"未知的未知因素"而不仅仅是优化已知过程时，此模式至关重要。

**视觉总结**

**![][image2]**

图 2：探索和发现设计模式

## 关键要点

* AI 中的探索和发现使 Agent 能够主动追求新信息和可能性，这对于导航复杂和不断演变的环境至关重要。
* Google Co-Scientist 等系统展示了 Agent 如何自主生成假设和设计实验，补充人类科学研究。
* 多 Agent 框架（例如 Agent Laboratory 的专门角色）通过自动化文献综述、实验和报告撰写来改进研究。
* 最终，这些 Agent 旨在通过管理计算密集型任务来增强人类创造力和问题解决能力，从而加速创新和发现。

## 结论

总之，探索和发现模式是真正 Agentic 系统的本质，定义了其超越被动指令跟随来主动探索其环境的能力。这种与生俱来的 Agentic 驱动力使 AI 能够在复杂领域中自主运行，不仅执行任务，而且独立设定子目标以发现新信息。这种高级 Agentic 行为通过多 Agent 框架最有力地实现，其中每个 Agent 在更大的协作过程中体现特定的主动角色。例如，Google Co-scientist 的高度 Agentic 系统具有自主生成、辩论和发展科学假设的 Agent。

像 Agent Laboratory 这样的框架通过创建模仿人类研究团队的 Agentic 层次结构进一步构建这一点，使系统能够自我管理整个发现生命周期。该模式的核心在于编排新兴的 Agentic 行为，允许系统以最少的人工干预来追求长期的、开放式的目标。这提升了人机合作关系，将 AI 定位为真正的 Agentic 协作者，处理探索性任务的自主执行。通过将这种主动发现工作委托给 Agentic 系统，人类智力得到显著增强，创新得以加速。开发这种强大的 Agentic 能力也需要对安全性和道德监督做出强有力的承诺。最终，这种模式提供了创建真正 Agentic AI 的蓝图，将计算工具转变为追求知识的独立的、目标寻求的伙伴。

## 参考文献

1. Exploration-Exploitation Dilemma**：** 强化学习和不确定性下决策的一个基本问题。[https://en.wikipedia.org/wiki/Exploration%E2%80%93exploitation\_dilemma](https://en.wikipedia.org/wiki/Exploration%E2%80%93exploitation_dilemma)   
2. Google Co-Scientist: [https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)   
3. Agent Laboratory: Using LLM Agents as Research Assistants [https://github.com/SamuelSchmidgall/AgentLaboratory](https://github.com/SamuelSchmidgall/AgentLaboratory)   
4. AgentRxiv: Towards Collaborative Autonomous Research: [https://agentrxiv.github.io/](https://agentrxiv.github.io/) 

[image1]: ../images/chapter-21/image1.png

[image2]: ../images/chapter-21/image2.png