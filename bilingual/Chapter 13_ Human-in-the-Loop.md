# Chapter 13: Human-in-the-Loop

# 第 13 章：人机协同

The Human-in-the-Loop (HITL) pattern represents a pivotal strategy in the development and deployment of Agents. It deliberately interweaves the unique strengths of human cognition—such as judgment, creativity, and nuanced understanding—with the computational power and efficiency of AI. This strategic integration is not merely an option but often a necessity, especially as AI systems become increasingly embedded in critical decision-making processes.

人机协同（Human-in-the-Loop，HITL）模式是智能体开发和部署中的关键策略。它有意识地将人类认知的独特优势——如判断力、创造力和对细微差别的理解——与 AI 的计算能力和效率相结合。这种战略性整合不仅是一种选择，在许多情况下更是一种必然，尤其是随着 AI 系统越来越深入地嵌入关键决策流程中。

The core principle of HITL is to ensure that AI operates within ethical boundaries, adheres to safety protocols, and achieves its objectives with optimal effectiveness. These concerns are particularly acute in domains characterized by complexity, ambiguity, or significant risk, where the implications of AI errors or misinterpretations can be substantial. In such scenarios, full autonomy—where AI systems function independently without any human intervention—may prove to be imprudent. HITL acknowledges this reality and emphasizes that even with rapidly advancing AI technologies, human oversight, strategic input, and collaborative interactions remain indispensable.

HITL 的核心原则是确保 AI 在道德边界内运行，遵守安全协议，并以最佳效率实现其目标。在具有复杂性、模糊性或重大风险的领域中，这些担忧尤为突出，因为 AI 错误或误解的后果可能非常严重。在这种情况下，完全自主——即 AI 系统在没有任何人工干预的情况下独立运行——可能是不明智的。HITL 承认这一现实，并强调即使 AI 技术飞速发展，人类监督、战略投入和协作互动仍然不可或缺。

The HITL approach fundamentally revolves around the idea of synergy between artificial and human intelligence. Rather than viewing AI as a replacement for human workers, HITL positions AI as a tool that augments and enhances human capabilities. This augmentation can take various forms, from automating routine tasks to providing data-driven insights that inform human decisions. The end goal is to create a collaborative ecosystem where both humans and AI Agents can leverage their distinct strengths to achieve outcomes that neither could accomplish alone.

HITL 方法从根本上围绕人工智能与人类智能之间的协同理念展开。HITL 不是将 AI 视为人类工作者的替代品，而是将 AI 定位为增强和提升人类能力的工具。这种增强可以采取多种形式，从自动化常规任务到提供数据驱动的见解来为人类决策提供信息。最终目标是创建一个协作生态系统，让人类和 AI 智能体都能利用各自的独特优势，实现任何一方都无法单独完成的成果。

In practice, HITL can be implemented in diverse ways. One common approach involves humans acting as validators or reviewers, examining AI outputs to ensure accuracy and identify potential errors. Another implementation involves humans actively guiding AI behavior, providing feedback or making corrections in real-time. In more complex setups, humans may collaborate with AI as partners, jointly solving problems or making decisions through interactive dialog or shared interfaces. Regardless of the specific implementation, the HITL pattern underscores the importance of maintaining human control and oversight, ensuring that AI systems remain aligned with human ethics, values, goals, and societal expectations.

在实践中，HITL 可以通过多种方式实施。一种常见的方法是让人类充当验证者或审查者，检查 AI 输出以确保准确性并识别潜在错误。另一种实施方式是让人类主动引导 AI 行为，实时提供反馈或进行纠正。在更复杂的设置中，人类可能与 AI 作为合作伙伴协作，通过交互式对话或共享界面共同解决问题或做出决策。无论具体实施方式如何，HITL 模式都强调保持人类控制和监督的重要性，确保 AI 系统始终与人类道德、价值观、目标和社会期望保持一致。

## Human-in-the-Loop Pattern Overview

## 人机协同速览

The Human-in-the-Loop (HITL) pattern integrates artificial intelligence with human input to enhance Agent capabilities. This approach acknowledges that optimal AI performance frequently requires a combination of automated processing and human insight, especially in scenarios with high complexity or ethical considerations. Rather than replacing human input, HITL aims to augment human abilities by ensuring that critical judgments and decisions are informed by human understanding.

人机协同（HITL）模式将人工智能与人类输入相结合，以增强智能体能力。这种方法承认，最佳的 AI 性能通常需要自动化处理和人类洞察的结合，特别是在高度复杂或涉及道德考量的场景中。HITL 的目标不是取代人类输入，而是通过确保关键判断和决策基于人类理解来增强人类能力。

HITL encompasses several key aspects: Human Oversight, which involves monitoring AI agent performance and output (e.g., via log reviews or real-time dashboards) to ensure adherence to guidelines and prevent undesirable outcomes. Intervention and Correction occurs when an AI agent encounters errors or ambiguous scenarios and may request human intervention; human operators can rectify errors, supply missing data, or guide the agent, which also informs future agent improvements. Human Feedback for Learning is collected and used to refine AI models, prominently in methodologies like reinforcement learning with human feedback, where human preferences directly influence the agent's learning trajectory. Decision Augmentation is where an AI agent provides analyses and recommendations to a human, who then makes the final decision, enhancing human decision-making through AI-generated insights rather than full autonomy. Human-Agent Collaboration is a cooperative interaction where humans and AI agents contribute their respective strengths; routine data processing may be handled by the agent, while creative problem-solving or complex negotiations are managed by the human. Finally, Escalation Policies are established protocols that dictate when and how an agent should escalate tasks to human operators, preventing errors in situations beyond the agent's capability.

HITL 包含几个关键方面：**人类监督**涉及监控 AI 智能体性能和输出（例如通过日志审查或实时仪表板），以确保遵循指南并防止不良结果。**干预和纠正**发生在 AI 智能体遇到错误或模糊场景并可能请求人工干预时；人类操作员可以纠正错误、提供缺失数据或指导智能体，这也有助于未来智能体的改进。**用于学习的人类反馈**被收集并用于完善 AI 模型，在带有人类反馈的强化学习等方法中尤为突出，其中人类偏好直接影响智能体的学习轨迹。**决策增强**是指 AI 智能体向人类提供分析和建议，由人类做出最终决定，通过 AI 生成的见解而非完全自主来增强人类决策。**人机协作**是一种合作互动，人类和 AI 智能体贡献各自的优势；常规数据处理可能由智能体处理，而创造性问题解决或复杂谈判则由人类管理。最后，**升级策略**是建立的协议，规定智能体何时以及如何将任务升级给人类操作员，以防止在超出智能体能力范围的情况下出现错误。

Implementing HITL patterns enables the use of Agents in sensitive sectors where full autonomy is not feasible or permitted. It also provides a mechanism for ongoing improvement through feedback loops. For example, in finance, the final approval of a large corporate loan requires a human loan officer to assess qualitative factors like leadership character. Similarly, in the legal field, core principles of justice and accountability demand that a human judge retain final authority over critical decisions like sentencing, which involve complex moral reasoning.

实施 HITL 模式使得在完全自主不可行或不被允许的敏感行业中使用智能体成为可能。它还通过反馈循环提供了持续改进的机制。例如在金融领域，大型企业贷款的最终批准需要人类贷款官员评估诸如领导层品格等定性因素。同样在法律领域，正义和问责制的核心原则要求人类法官保留对关键决定（如量刑）的最终权威，这些决定涉及复杂的道德推理。

**Caveats:** Despite its benefits, the HITL pattern has significant caveats, chief among them being a lack of scalability. While human oversight provides high accuracy, operators cannot manage millions of tasks, creating a fundamental trade-off that often requires a hybrid approach combining automation for scale and HITL for accuracy. Furthermore, the effectiveness of this pattern is heavily dependent on the expertise of the human operators; for example, while an AI can generate software code, only a skilled developer can accurately identify subtle errors and provide the correct guidance to fix them. This need for expertise also applies when using HITL to generate training data, as human annotators may require special training to learn how to correct an AI in a way that produces high-quality data. Lastly, implementing HITL raises significant privacy concerns, as sensitive information must often be rigorously anonymized before it can be exposed to a human operator, adding another layer of process complexity.

**注意事项**：尽管 HITL 模式具有诸多优势，但也存在重要的注意事项，其中最主要的是可扩展性不足。虽然人类监督提供了高精度，但操作员无法管理数百万个任务，这造成了基本权衡，通常需要采用混合方法，结合自动化实现规模化和 HITL 实现准确性。此外，此模式的有效性在很大程度上依赖于人类操作员的专业知识；例如虽然 AI 可以生成软件代码，但只有熟练的开发人员才能准确识别细微错误并提供正确的修复指导。这种对专业知识的需求同样适用于使用 HITL 生成训练数据时，因为人类标注员可能需要特殊培训才能学会如何以产生高质量数据的方式纠正 AI。最后，实施 HITL 会引发重大隐私问题，因为敏感信息在暴露给人类操作员之前通常必须严格匿名化，这增加了另一层流程复杂性。

## Practical Applications & Use Cases

## 实际应用和用例

The Human-in-the-Loop pattern is vital across a wide range of industries and applications, particularly where accuracy, safety, ethics, or nuanced understanding are paramount.

人机协同模式在广泛的行业和应用中至关重要，特别是在准确性、安全性、道德考量或细微理解至关重要的领域。

* **Content Moderation:** AI agents can rapidly filter vast amounts of online content for violations (e.g., hate speech, spam). However, ambiguous cases or borderline content are escalated to human moderators for review and final decision, ensuring nuanced judgment and adherence to complex policies.  

* **内容审核**：AI 智能体可以快速过滤大量在线内容以查找违规内容（如仇恨言论、垃圾邮件）。然而，模糊案例或边界内容会升级给人类审核员进行审查和最终决定，确保细致入微的判断并遵循复杂政策。  

* **Autonomous Driving:** While self-driving cars handle most driving tasks autonomously, they are designed to hand over control to a human driver in complex, unpredictable, or dangerous situations that the AI cannot confidently navigate (e.g., extreme weather, unusual road conditions).  

* **自动驾驶**：虽然自动驾驶汽车自主处理大多数驾驶任务，但它们被设计为在 AI 无法自信导航的复杂、不可预测或危险情况下（如极端天气、异常道路条件）将控制权交还给人类驾驶员。  

* **Financial Fraud Detection:** AI systems can flag suspicious transactions based on patterns. However, high-risk or ambiguous alerts are often sent to human analysts who investigate further, contact customers, and make the final determination on whether a transaction is fraudulent.  

* **金融欺诈检测**：AI 系统可以根据模式标记可疑交易。然而，高风险或模糊的警报通常会发送给人类分析师，他们进一步调查、联系客户，并对交易是否欺诈做出最终决定。  

* **Legal Document Review:** AI can quickly scan and categorize thousands of legal documents to identify relevant clauses or evidence. Human legal professionals then review the AI's findings for accuracy, context, and legal implications, especially for critical cases.  

* **法律文件审查**：AI 可快速扫描和分类数千份法律文件以识别相关条款或证据。然后，人类法律专业人员审查 AI 的发现以确保准确性、上下文和法律含义，特别是对于关键案例。  

* **Customer Support (Complex Queries):** A chatbot might handle routine customer inquiries. If the user's problem is too complex, emotionally charged, or requires empathy that the AI cannot provide, the conversation is seamlessly handed over to a human support agent.  

* **客户支持（复杂查询）**：聊天机器人可能处理常规客户查询。如果用户问题过于复杂、情绪激动或需要 AI 无法提供的同理心，对话将无缝交接给人类支持人员。  

* **Data Labeling and Annotation:** AI models often require large datasets of labeled data for training. Humans are put in the loop to accurately label images, text, or audio, providing the ground truth that the AI learns from. This is a continuous process as models evolve.  

* **数据标注和注释**：AI 模型通常需要大量标注数据集进行训练。人类被纳入循环以准确标注图像、文本或音频，为 AI 学习提供基本事实。随着模型发展，这是一个持续过程。  

* **Generative AI Refinement:** When an LLM generates creative content (e.g., marketing copy, design ideas), human editors or designers review and refine the output, ensuring it meets brand guidelines, resonates with the target audience, and maintains quality.  

* **生成 AI 完善**：当 LLM 生成创意内容（如营销文案、设计理念）时，人类编辑或设计师审查和完善输出，确保其符合品牌指南、与目标受众产生共鸣并保持质量。  

* **Autonomous Networks:** AI systems are capable of analyzing alerts and forecasting network issues and traffic anomalies by leveraging key performance indicators (KPIs) and identified patterns. Nevertheless, crucial decisions—such as addressing high-risk alerts—are frequently escalated to human analysts. These analysts conduct further investigation and make the ultimate determination regarding the approval of network changes.

* **自主网络**：AI 系统能够通过利用关键性能指标（KPI）和识别模式来分析警报并预测网络问题和流量异常。然而，关键决策——如处理高风险警报——经常升级给人类分析师。这些分析师进行进一步调查，并对网络更改的批准做出最终决定。

This pattern exemplifies a practical method for AI implementation. It harnesses AI for enhanced scalability and efficiency, while maintaining human oversight to ensure quality, safety, and ethical compliance.

此模式体现了 AI 实施的实用方法。它利用 AI 实现增强的可扩展性和效率，同时保持人类监督以确保质量、安全性和道德合规性。

"Human-on-the-loop" is a variation of this pattern where human experts define the overarching policy, and the AI then handles immediate actions to ensure compliance. Let's consider two examples:

"人在循环外"（Human-on-the-loop）是此模式的一个变体，其中人类专家定义总体策略，然后 AI 处理即时操作以确保合规性。让我们考虑两个例子：

* **Automated financial trading system**: In this scenario, a human financial expert sets the overarching investment strategy and rules. For instance, the human might define the policy as: "Maintain a portfolio of 70% tech stocks and 30% bonds, do not invest more than 5% in any single company, and automatically sell any stock that falls 10% below its purchase price." The AI then monitors the stock market in real-time, executing trades instantly when these predefined conditions are met. The AI is handling the immediate, high-speed actions based on the slower, more strategic policy set by the human operator.  

* **自动金融交易系统**：在此场景中，人类金融专家设定总体投资策略和规则。例如，人类可能将策略定义为："维持 70% 科技股和 30% 债券的投资组合，不要在任何单一公司投资超过 5%，并自动出售任何跌幅低于购买价格 10% 的股票。"然后，AI 实时监控股票市场，在满足这些预定义条件时立即执行交易。AI 正在根据人类操作员设定的较慢、更具战略性的策略处理即时、高速的操作。  

* **Modern call center**:  In this setup, a human manager establishes high-level policies for customer interactions. For instance, the manager might set rules such as "any call mentioning 'service outage' should be immediately routed to a technical support specialist," or "if a customer's tone of voice indicates high frustration, the system should offer to connect them directly to a human agent." The AI system then handles the initial customer interactions, listening to and interpreting their needs in real-time. It autonomously executes the manager's policies by instantly routing the calls or offering escalations without needing human intervention for each individual case. This allows the AI to manage the high volume of immediate actions according to the slower, strategic guidance provided by the human operator.

* **现代呼叫中心**：在此设置中，人类经理为客户互动建立高级策略。例如，经理可能设置规则，如"任何提到'服务中断'的呼叫应立即转接给技术支持专家"，或"如果客户的语调表明高度沮丧，系统应提供直接连接到人类支持人员"。然后，AI 系统处理初始客户互动，实时倾听和解释他们的需求。它通过立即转接呼叫或提供升级来自主执行经理的策略，无需对每个单独案例进行人工干预。这允许 AI 根据人类操作员提供的较慢、战略性的指导管理大量即时操作。

## Hands-On Code Example

## 实践代码示例

To demonstrate the Human-in-the-Loop pattern, an ADK agent can identify scenarios requiring human review and initiate an escalation process . This allows for human intervention in situations where the agent's autonomous decision-making capabilities are limited or when complex judgments are required. This is not an isolated feature; other popular frameworks have adopted similar capabilities. LangChain, for instance, also provides tools to implement these types of interactions.

为演示人机协同模式，ADK 智能体可识别需要人工审查的场景并启动升级过程。这允许在智能体的自主决策能力有限或需要复杂判断时进行人工干预。此功能并非孤立存在；其他流行框架也采用了类似能力。例如，LangChain 同样提供了实现此类交互的工具。

```python
from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext
from google.adk.callbacks import CallbackContext
from google.adk.models.llm import LlmRequest
from google.genai import types
from typing import Optional

## Placeholder for tools (replace with actual implementations if needed)
def troubleshoot_issue(issue: str) -> dict:
    return {"status": "success", "report": f"Troubleshooting steps for {issue}."}

def create_ticket(issue_type: str, details: str) -> dict:
    return {"status": "success", "ticket_id": "TICKET123"}

def escalate_to_human(issue_type: str) -> dict:
    # This would typically transfer to a human queue in a real system
    return {"status": "success", "message": f"Escalated {issue_type} to a human specialist."}

technical_support_agent = Agent(
    name="technical_support_specialist",
    model="gemini-2.0-flash-exp",
    instruction="""
You are a technical support specialist for our electronics company.
FIRST, check if the user has a support history in state["customer_info"]["support_history"].
If they do, reference this history in your responses.

For technical issues:
1. Use the troubleshoot_issue tool to analyze the problem.
2. Guide the user through basic troubleshooting steps.
3. If the issue persists, use create_ticket to log the issue.

For complex issues beyond basic troubleshooting:
1. Use escalate_to_human to transfer to a human specialist.

Maintain a professional but empathetic tone. Acknowledge the frustration technical issues can cause,
while providing clear steps toward resolution.
""",
    tools=[troubleshoot_issue, create_ticket, escalate_to_human]
)

def personalization_callback(
    callback_context: CallbackContext, llm_request: LlmRequest
) -> Optional[LlmRequest]:
    """Adds personalization information to the LLM request."""
    # Get customer info from state
    customer_info = callback_context.state.get("customer_info")
    if customer_info:
        customer_name = customer_info.get("name", "valued customer")
        customer_tier = customer_info.get("tier", "standard")
        recent_purchases = customer_info.get("recent_purchases", [])
        personalization_note = (
            f"\nIMPORTANT PERSONALIZATION:\n"
            f"Customer Name: {customer_name}\n"
            f"Customer Tier: {customer_tier}\n"
        )
        if recent_purchases:
            personalization_note += f"Recent Purchases: {', '.join(recent_purchases)}\n"

        if llm_request.contents:
            # Add as a system message before the first content
            system_content = types.Content(
                role="system", parts=[types.Part(text=personalization_note)]
            )
            llm_request.contents.insert(0, system_content)

    # Return None to continue with the modified request
    return None
```

This code offers a blueprint for creating a technical support agent using Google's ADK, designed around a HITL framework. The agent acts as an intelligent first line of support, configured with specific instructions and equipped with tools like troubleshoot\_issue, create\_ticket, and escalate\_to\_human to manage a complete support workflow. The escalation tool is a core part of the HITL design, ensuring complex or sensitive cases are passed to human specialists.

此代码提供了使用 Google ADK 创建技术支持智能体的蓝图，围绕 HITL 框架设计。智能体充当智能第一线支持，配置了特定指令，并配备了 troubleshoot_issue、create_ticket 和 escalate_to_human 等工具来管理完整的支持工作流。升级工具是 HITL 设计的核心部分，确保复杂或敏感案例传递给人类专家。

A key feature of this architecture is its capacity for deep personalization, achieved through a dedicated callback function. Before contacting the LLM, this function dynamically retrieves customer-specific data—such as their name, tier, and purchase history—from the agent's state. This context is then injected into the prompt as a system message, enabling the agent to provide highly tailored and informed responses that reference the user's history. By combining a structured workflow with essential human oversight and dynamic personalization, this code serves as a practical example of how the ADK facilitates the development of sophisticated and robust AI support solutions.

此架构的一个关键特性是其深度个性化能力，通过专用回调函数实现。在联系 LLM 之前，此函数从智能体状态中动态检索客户特定数据——如姓名、等级和购买历史。然后将此上下文作为系统消息注入提示词中，使智能体能够提供高度定制和知情的响应，引用用户历史记录。通过将结构化工作流与基本人类监督和动态个性化相结合，此代码展示了 ADK 如何促进开发复杂且强大的 AI 支持解决方案。

## At a Glance

## 速览

**What:** AI systems, including advanced LLMs, often struggle with tasks that require nuanced judgment, ethical reasoning, or a deep understanding of complex, ambiguous contexts. Deploying fully autonomous AI in high-stakes environments carries significant risks, as errors can lead to severe safety, financial, or ethical consequences. These systems lack the inherent creativity and common-sense reasoning that humans possess. Consequently, relying solely on automation in critical decision-making processes is often imprudent and can undermine the system's overall effectiveness and trustworthiness.

**问题背景：** AI 系统（包括高级 LLM）通常在需要细致入微判断、道德推理或对复杂模糊上下文深刻理解的任务中表现不佳。在高风险环境中部署完全自主的 AI 具有重大风险，因为错误可能导致严重的安全、财务或道德后果。这些系统缺乏人类固有的创造力和常识推理能力。因此，在关键决策过程中仅依赖自动化通常是不明智的，并可能损害系统的整体有效性和可信度。

**Why:** The Human-in-the-Loop (HITL) pattern provides a standardized solution by strategically integrating human oversight into AI workflows. This agentic approach creates a symbiotic partnership where AI handles computational heavy-lifting and data processing, while humans provide critical validation, feedback, and intervention. By doing so, HITL ensures that AI actions align with human values and safety protocols. This collaborative framework not only mitigates the risks of full automation but also enhances the system's capabilities through continuous learning from human input. Ultimately, this leads to more robust, accurate, and ethical outcomes that neither human nor AI could achieve alone.

**解决方案：** 人机协同（HITL）模式通过战略性地将人类监督整合到 AI 工作流中提供了标准化解决方案。这种智能体方法创建了共生伙伴关系，AI 处理计算繁重工作和数据处理，而人类提供关键验证、反馈和干预。通过这样做，HITL 确保 AI 行动与人类价值观和安全协议保持一致。这种协作框架不仅降低了完全自动化的风险，还通过从人类输入中持续学习来增强系统能力。最终，这带来了更强大、准确和道德的结果，这些结果是人类或 AI 单独无法实现的。

**Rule of thumb:** Use this pattern when deploying AI in domains where errors have significant safety, ethical, or financial consequences, such as in healthcare, finance, or autonomous systems. It is essential for tasks involving ambiguity and nuance that LLMs cannot reliably handle, like content moderation or complex customer support escalations. Employ HITL when the goal is to continuously improve an AI model with high-quality, human-labeled data or to refine generative AI outputs to meet specific quality standards.

**实践建议：** 在部署 AI 到错误会产生重大安全、道德或财务后果的领域时使用此模式，例如医疗保健、金融或自主系统。对于涉及 LLM 无法可靠处理的模糊性和细微差别的任务（如内容审核或复杂客户支持升级），它至关重要。当目标是使用高质量人类标注数据持续改进 AI 模型或完善生成 AI 输出以满足特定质量标准时，采用 HITL。

**Visual summary:**

**可视化摘要**：

**![][image1]**

Fig.1: Human in the loop design pattern

图 1：人机协同设计模式

[image1]: ../images/chapter-13/image1.png

## Key Takeaways

## 关键要点

Key takeaways include: 

关键要点包括： 

* Human-in-the-Loop (HITL) integrates human intelligence and judgment into AI workflows.  

* 人机协同（HITL）将人类智能和判断整合到 AI 工作流中。  

* It's crucial for safety, ethics, and effectiveness in complex or high-stakes scenarios.  

* 它在复杂或高风险场景中对安全性、道德和有效性至关重要。  

* Key aspects include human oversight, intervention, feedback for learning, and decision augmentation.  

* 关键方面包括人类监督、干预、学习反馈和决策增强。  

* Escalation policies are essential for agents to know when to hand off to a human.  

* 升级策略对于智能体何时交接给人类至关重要。  

* HITL allows for responsible AI deployment and continuous improvement.  

* HITL 允许负责任的 AI 部署和持续改进。  

* The primary drawbacks of Human-in-the-Loop are its inherent lack of scalability, creating a trade-off between accuracy and volume, and its dependence on highly skilled domain experts for effective intervention.   

* 人机协同的主要缺点是其固有的可扩展性不足，在准确性和数量之间造成权衡，以及对高技能领域专家进行有效干预的依赖性。   

* Its implementation presents operational challenges, including the need to train human operators for data generation and to address privacy concerns by anonymizing sensitive information.

* 其实施带来了操作挑战，包括需要培训人类操作员进行数据生成，以及通过匿名化敏感信息来解决隐私问题。

## Conclusion

## 结论

This chapter explored the vital Human-in-the-Loop (HITL) pattern, emphasizing its role in creating robust, safe, and ethical AI systems. We discussed how integrating human oversight, intervention, and feedback into agent workflows can significantly enhance their performance and trustworthiness, especially in complex and sensitive domains. The practical applications demonstrated HITL's widespread utility, from content moderation and medical diagnosis to autonomous driving and customer support. The conceptual code example provided a glimpse into how ADK can facilitate these human-agent interactions through escalation mechanisms. As AI capabilities continue to advance, HITL remains a cornerstone for responsible AI development, ensuring that human values and expertise remain central to intelligent system design.

本章探讨了至关重要的人机协同（HITL）模式，强调了其在创建强大、安全和道德的 AI 系统中的作用。我们讨论了如何将人类监督、干预和反馈整合到智能体工作流中可以显著增强其性能和可信度，特别是在复杂和敏感的领域中。实际应用展示了 HITL 的广泛实用性，从内容审核和医疗诊断到自动驾驶和客户支持。概念性代码示例提供了 ADK 如何通过升级机制促进这些人机交互的一瞥。随着 AI 能力不断进步，HITL 仍然是负责任的 AI 开发的基石，确保人类价值观和专业知识在智能系统设计中保持核心地位。

## References

## 参考文献

1. A Survey of Human-in-the-loop for Machine Learning, Xingjiao Wu, Luwei Xiao, Yixuan Sun, Junhang Zhang, Tianlong Ma, Liang He, [https://arxiv.org/abs/2108.00941](https://arxiv.org/abs/2108.00941)
