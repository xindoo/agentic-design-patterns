# Chapter 12: Exception Handling and Recovery

# 第 12 章：异常处理和恢复

For AI agents to operate reliably in diverse real-world environments, they must be able to manage unforeseen situations, errors, and malfunctions. Just as humans adapt to unexpected obstacles, intelligent agents need robust systems to detect problems, initiate recovery procedures, or at least ensure controlled failure. This essential requirement forms the basis of the Exception Handling and Recovery pattern.

要使 AI 智能体在各种现实世界环境中可靠运行，它们必须能够管理不可预见的情况、错误和故障。正如人类能够适应意外障碍一样，智能体也需要强大的系统来检测问题、启动恢复程序，或至少确保受控失败。这一基本需求构成了异常处理和恢复模式的基础。

This pattern focuses on developing exceptionally durable and resilient agents that can maintain uninterrupted functionality and operational integrity despite various difficulties and anomalies. It emphasizes the importance of both proactive preparation and reactive strategies to ensure continuous operation, even when facing challenges. This adaptability is critical for agents to function successfully in complex and unpredictable settings, ultimately boosting their overall effectiveness and trustworthiness.

此模式专注于开发极其耐用且有弹性的智能体，即使面临各种困难和异常情况，也能保持不间断的功能和操作完整性。它强调主动准备和响应策略的重要性，以确保在面临挑战时也能持续运行。这种适应性对于智能体在复杂和不可预测的环境中成功运作至关重要，最终提升其整体有效性和可信度。

The capacity to handle unexpected events ensures these AI systems are not only intelligent but also stable and reliable, which fosters greater confidence in their deployment and performance. Integrating comprehensive monitoring and diagnostic tools further strengthens an agent's ability to quickly identify and address issues, preventing potential disruptions and ensuring smoother operation in evolving conditions. These advanced systems are crucial for maintaining the integrity and efficiency of AI operations, reinforcing their ability to manage complexity and unpredictability.

处理意外事件的能力确保这些 AI 系统不仅智能，而且稳定可靠，从而增强对其部署和性能的信心。集成全面的监控和诊断工具进一步强化了智能体快速识别和解决问题的能力，防止潜在中断并确保在不断变化的条件下更顺畅地运行。这些先进系统对于维护 AI 操作的完整性和效率至关重要，增强了其管理复杂性和不可预测性的能力。

This pattern may sometimes be used with reflection. For example, if an initial attempt fails and raises an exception, a reflective process can analyze the failure and reattempt the task with a refined approach, such as an improved prompt, to resolve the error.

此模式有时可能与反思模式结合使用。例如，如果初始尝试失败并引发异常，反思过程可以分析失败原因，并使用改进的方法（如优化提示词）重新尝试任务，以解决错误。

## Exception Handling and Recovery Pattern Overview

## 异常处理和恢复模式速览

The Exception Handling and Recovery pattern addresses the need for AI agents to manage operational failures. This pattern involves anticipating potential issues, such as tool errors or service unavailability, and developing strategies to mitigate them. These strategies may include error logging, retries, fallbacks, graceful degradation, and notifications. Additionally, the pattern emphasizes recovery mechanisms like state rollback, diagnosis, self-correction, and escalation, to restore agents to stable operation. Implementing this pattern enhances the reliability and robustness of AI agents, allowing them to function in unpredictable environments. Examples of practical applications include chatbots managing database errors, trading bots handling financial errors, and smart home agents addressing device malfunctions. The pattern ensures that agents can continue to operate effectively despite encountering complexities and failures.

异常处理和恢复模式解决了 AI 智能体应对操作失败的需求。此模式涉及预测潜在问题，例如工具错误或服务不可用，并制定相应的缓解策略。这些策略可能包括错误日志记录、重试机制、回退方案、优雅降级和通知机制。此外，该模式强调恢复机制，如状态回滚、诊断分析、自我纠正和问题升级，以将智能体恢复到稳定运行状态。实施此模式增强了 AI 智能体的可靠性和鲁棒性，使它们能够在不可预测的环境中有效运作。实际应用示例包括管理数据库错误的聊天机器人、处理金融错误的交易机器人以及解决设备故障的智能家居智能体。该模式确保智能体在遇到失败时能够继续有效运行。

![][image1]

Fig.1: Key components of exception handling and recovery for AI agents

图 1：AI 智能体异常处理和恢复的关键组件

**Error Detection:** This involves meticulously identifying operational issues as they arise. This could manifest as invalid or malformed tool outputs, specific API errors such as 404 (Not Found) or 500 (Internal Server Error) codes, unusually long response times from services or APIs, or incoherent and nonsensical responses that deviate from expected formats. Additionally, monitoring by other agents or specialized monitoring systems might be implemented for more proactive anomaly detection, enabling the system to catch potential issues before they escalate.

**错误检测**：这涉及仔细识别出现的操作问题。这可能表现为无效或格式错误的工具输出、特定的 API 错误（如 404（未找到）或 500（内部服务器错误）代码）、来自服务或 API 的异常长响应时间，或偏离预期格式的不连贯和无意义响应。此外，可以实施其他智能体或专门监控系统的监控，以实现更主动的异常检测，使系统能够在潜在问题升级之前捕获它们。

**Error Handling**: Once an error is detected, a carefully thought-out response plan is essential. This includes recording error details meticulously in logs for later debugging and analysis (logging). Retrying the action or request, sometimes with slightly adjusted parameters, may be a viable strategy, especially for transient errors (retries). Utilizing alternative strategies or methods (fallbacks) can ensure that some functionality is maintained. Where complete recovery is not immediately possible, the agent can maintain partial functionality to provide at least some value (graceful degradation). Finally, alerting human operators or other agents might be crucial for situations that require human intervention or collaboration (notification).

**错误处理**：一旦检测到错误，就需要一个经过深思熟虑的响应计划。这包括在日志中仔细记录错误详细信息，以便后续调试和分析（日志记录）。重试操作或请求（有时使用略微调整的参数）可能是一种可行的策略，特别是对于瞬态错误（重试）。使用替代策略或方法（回退）可以确保维持某些功能。在无法立即完全恢复的情况下，智能体可以维持部分功能以至少提供一些价值（优雅降级）。最后，向人类操作员或其他智能体发送警报可能对需要人工干预或协作的情况至关重要（通知）。

**Recovery:** This stage is about restoring the agent or system to a stable and operational state after an error. It could involve reversing recent changes or transactions to undo the effects of the error (state rollback). A thorough investigation into the cause of the error is vital for preventing recurrence. Adjusting the agent's plan, logic, or parameters through a self-correction mechanism or replanning process may be needed to avoid the same error in the future. In complex or severe cases, delegating the issue to a human operator or a higher-level system (escalation) might be the best course of action.

**恢复**：这个阶段是关于在错误后将智能体或系统恢复到稳定和可操作的状态。它可能涉及撤销最近的更改或事务以撤消错误的影响（状态回滚）。对错误原因进行彻底调查对于防止复发至关重要。通过自我纠正机制或重新规划过程调整智能体的计划、逻辑或参数可能需要避免将来出现相同的错误。在复杂或严重的情况下，将问题委托给人类操作员或更高级别的系统（升级）可能是最佳行动方案。

Implementation of this robust exception handling and recovery pattern can transform AI agents from fragile and unreliable systems into robust, dependable components capable of operating effectively and resiliently in challenging and highly unpredictable environments. This ensures that the agents maintain functionality, minimize downtime, and provide a seamless and reliable experience even when faced with unexpected issues.

实施这种强大的异常处理和恢复模式可以将 AI 智能体从脆弱和不可靠的系统转变为能够在具有挑战性和高度不可预测的环境中有效且有弹性运行的强大、可靠组件。这确保了智能体保持功能、最小化停机时间，并在面临意外问题时提供无缝和可靠的体验。

## Practical Applications & Use Cases

## 实际应用和用例

Exception Handling and Recovery is critical for any agent deployed in a real-world scenario where perfect conditions cannot be guaranteed.

异常处理和恢复对于在无法保证完美条件的现实场景中部署的任何智能体都至关重要。

* **Customer Service Chatbots:** If a chatbot tries to access a customer database and the database is temporarily down, it shouldn't crash. Instead, it should detect the API error, inform the user about the temporary issue, perhaps suggest trying again later, or escalate the query to a human agent.  

* **客户服务聊天机器人**：如果聊天机器人尝试访问客户数据库而数据库暂时停机，它不应该崩溃。相反，它应该检测 API 错误，通知用户临时问题，可能建议稍后再试，或将查询升级给人工客服。

* **Automated Financial Trading:** A trading bot attempting to execute a trade might encounter an "insufficient funds" error or a "market closed" error. It needs to handle these exceptions by logging the error, not repeatedly trying the same invalid trade, and potentially notifying the user or adjusting its strategy.  

* **自动金融交易**：尝试执行交易的交易机器人可能会遇到"资金不足"错误或"市场关闭"错误。它需要通过记录错误、避免重复尝试相同的无效交易以及可能通知用户或调整策略来处理这些异常。

* **Smart Home Automation:** An agent controlling smart lights might fail to turn on a light due to a network issue or a device malfunction. It should detect this failure, perhaps retry, and if still unsuccessful, notify the user that the light could not be turned on and suggest manual intervention.  

* **智能家居自动化**：控制智能灯的智能体由于网络问题或设备故障而无法打开灯。它应该检测到这个失败，可能重试，如果仍然不成功，通知用户无法打开灯并建议手动干预。

* **Data Processing Agents:** An agent tasked with processing a batch of documents might encounter a corrupted file. It should skip the corrupted file, log the error, continue processing other files, and report the skipped files at the end rather than halting the entire process.  

* **数据处理智能体**：负责处理一批文档的智能体会遇到损坏的文件。它应该跳过损坏的文件，记录错误，继续处理其他文件，并在结束时报告跳过的文件，而不是停止整个过程。

* **Web Scraping Agents:** When a web scraping agent encounters a CAPTCHA, a changed website structure, or a server error (e.g., 404 Not Found, 503 Service Unavailable), it needs to handle these gracefully. This could involve pausing, using a proxy, or reporting the specific URL that failed.  

* **网络爬虫智能体**：当网络爬虫智能体遇到验证码、网站结构更改或服务器错误（例如，404 未找到、503 服务不可用）时，它需要优雅地处理这些问题。这可能涉及暂停、使用代理或报告失败的特定 URL。

* **Robotics and Manufacturing:** A robotic arm performing an assembly task might fail to pick up a component due to misalignment. It needs to detect this failure (e.g., via sensor feedback), attempt to readjust, retry the pickup, and if persistent, alert a human operator or switch to a different component.

* **机器人和制造**：执行装配任务的机器人手臂可能由于未对齐而无法拾取组件。它需要检测到这个失败（例如，通过传感器反馈），尝试重新调整，重试拾取，如果持续存在，则警告人类操作员或切换到不同的组件。

In short, this pattern is fundamental for building agents that are not only intelligent but also reliable, resilient, and user-friendly in the face of real-world complexities.

简而言之，此模式对于构建不仅智能而且在面对现实世界复杂性时可靠、有弹性且用户友好的智能体非常重要。

## Hands-On Code Example (ADK)

## 实践代码示例（ADK）

Exception handling and recovery are vital for system robustness and reliability. Consider, for instance, an agent's response to a failed tool call. Such failures can stem from incorrect tool input or issues with an external service that the tool depends on.

异常处理和恢复对于系统的鲁棒性和可靠性至关重要。例如，考虑智能体对失败的工具调用的响应。这种失败可能源于不正确的工具输入或工具所依赖的外部服务的问题。

```python
from google.adk.agents import Agent, SequentialAgent

## Agent 1: Tries the primary tool. Its focus is narrow and clear.
primary_handler = Agent(
    name="primary_handler",
    model="gemini-2.0-flash-exp",
    instruction="""
Your job is to get precise location information. Use the get_precise_location_info tool with the user's provided address.
    """,
    tools=[get_precise_location_info]
)

## Agent 2: Acts as the fallback handler, checking state to decide its action.
fallback_handler = Agent(
    name="fallback_handler",
    model="gemini-2.0-flash-exp",
    instruction="""
Check if the primary location lookup failed by looking at state["primary_location_failed"].
- If it is True, extract the city from the user's original query and use the get_general_area_info tool.
- If it is False, do nothing.
    """,
    tools=[get_general_area_info]
)

## Agent 3: Presents the final result from the state.
response_agent = Agent(
    name="response_agent",
    model="gemini-2.0-flash-exp",
    instruction="""
Review the location information stored in state["location_result"]. Present this information clearly and concisely to the user.
If state["location_result"] does not exist or is empty, apologize that you could not retrieve the location.
    """,
    tools=[]  # This agent only reasons over the final state.
)

## The SequentialAgent ensures the handlers run in a guaranteed order.
robust_location_agent = SequentialAgent(
    name="robust_location_agent",
    sub_agents=[primary_handler, fallback_handler, response_agent]
)
```

This code defines a robust location retrieval system using a ADK's SequentialAgent with three sub-agents. The primary_handler is the first agent, attempting to get precise location information using the get_precise_location_info tool. The fallback_handler acts as a backup, checking if the primary lookup failed by inspecting a state variable. If the primary lookup failed, the fallback agent extracts the city from the user's query and uses the get_general_area_info tool. The response_agent is the final agent in the sequence. It reviews the location information stored in the state. This agent is designed to present the final result to the user. If no location information was found, it apologizes. The SequentialAgent ensures that these three agents execute in a predefined order. This structure allows for a layered approach to location information retrieval.

此代码使用 ADK 的 SequentialAgent 和三个子智能体定义了一个强大的位置检索系统。primary_handler 是第一个智能体，尝试使用 get_precise_location_info 工具获取精确的位置信息。fallback_handler 充当备份，通过检查状态变量来检查主要查找是否失败。如果主要查找失败，回退智能体从用户的查询中提取城市并使用 get_general_area_info 工具。response_agent 是序列中的最终智能体。它查看存储在状态中的位置信息。此智能体旨在向用户呈现最终结果。如果没有找到位置信息，它会道歉。SequentialAgent 确保这三个智能体按预定义的顺序执行。这种结构允许采用分层方法进行位置信息检索。

## At a Glance

## 速览

**What:** AI agents operating in real-world environments inevitably encounter unforeseen situations, errors, and system malfunctions. These disruptions can range from tool failures and network issues to invalid data, threatening the agent's ability to complete its tasks. Without a structured way to manage these problems, agents can be fragile, unreliable, and prone to complete failure when faced with unexpected hurdles. This unreliability makes it difficult to deploy them in critical or complex applications where consistent performance is essential.

**问题背景**：在现实世界环境中运行的 AI 智能体不可避免地会遇到不可预见的情况、错误和系统故障。这些中断可能从工具故障、网络问题到无效数据不等，威胁着智能体完成任务的能力。如果没有结构化的方法来管理这些问题，智能体可能会变得脆弱、不可靠，并且在面对意外障碍时容易完全失败。这种不可靠性使得难以在一致性能至关重要的关键或复杂应用程序中部署它们。

**Why**: The Exception Handling and Recovery pattern provides a standardized solution for building robust and resilient AI agents. It equips them with the agentic capability to anticipate, manage, and recover from operational failures. The pattern involves proactive error detection, such as monitoring tool outputs and API responses, and reactive handling strategies like logging for diagnostics, retrying transient failures, or using fallback mechanisms. For more severe issues, it defines recovery protocols, including reverting to a stable state, self-correction by adjusting its plan, or escalating the problem to a human operator. This systematic approach ensures agents can maintain operational integrity, learn from failures, and function dependably in unpredictable settings.

**解决方案**：异常处理和恢复模式为构建强大和有弹性的 AI 智能体提供了标准化的解决方案。它为它们配备了预测、管理和从操作失败中恢复的智能体能力。此模式涉及主动错误检测，例如监控工具输出和 API 响应，以及响应处理策略，如用于诊断的日志记录、重试瞬态故障或使用回退机制。对于更严重的问题，它定义了恢复协议，包括恢复到稳定状态、通过调整其计划进行自我纠正或将问题升级给人类操作员。这种系统方法确保智能体保持操作完整性，从失败中学习，并在不可预测的环境中可靠地运作。

**Rule of thumb:** Use this pattern for any AI agent deployed in a dynamic, real-world environment where system failures, tool errors, network issues, or unpredictable inputs are possible and operational reliability is a key requirement.

**实践建议**：对于在动态的现实世界环境中部署的任何 AI 智能体，当系统故障、工具错误、网络问题或不可预测的输入可能发生且操作可靠性是关键要求时，使用此模式。

**Visual summary**

**可视化摘要**

![][image2]

Fig.2: Exception handling pattern

图 2：异常处理模式

## Key Takeaways

## 关键要点

Essential points to remember:

需要记住的要点：

* Exception Handling and Recovery is essential for building robust and reliable Agents.  

* 异常处理和恢复对于构建强大和可靠的智能体非常重要。

* This pattern involves detecting errors, handling them gracefully, and implementing strategies to recover.  

* 此模式涉及检测错误、优雅地处理错误以及实施恢复策略。

* Error detection can involve validating tool outputs, checking API error codes, and using timeouts.  

* 错误检测可能涉及验证工具输出、检查 API 错误代码以及使用超时。

* Handling strategies include logging, retries, fallbacks, graceful degradation, and notifications.  

* 处理策略包括日志记录、重试、回退、优雅降级和通知。

* Recovery focuses on restoring stable operation through diagnosis, self-correction, or escalation.  

* 恢复侧重于通过诊断、自我纠正或升级恢复稳定运行。

* This pattern ensures agents can operate effectively even in unpredictable real-world environments.

* 此模式确保智能体在不可预测的现实世界环境中也能有效运行。

## Conclusion

## 结论

This chapter explores the Exception Handling and Recovery pattern, which is essential for developing robust and dependable AI agents. This pattern addresses how AI agents can identify and manage unexpected issues, implement appropriate responses, and recover to a stable operational state. The chapter discusses various aspects of this pattern, including the detection of errors, the handling of these errors through mechanisms such as logging, retries, and fallbacks, and the strategies used to restore the agent or system to proper function. Practical applications of the Exception Handling and Recovery pattern are illustrated across several domains to demonstrate its relevance in handling real-world complexities and potential failures. These applications show how equipping AI agents with exception handling capabilities contributes to their reliability and adaptability in dynamic environments.

本章探讨了异常处理和恢复模式，这对于开发强大和可靠的 AI 智能体非常重要。此模式解决了 AI 智能体如何识别和管理意外问题、实施适当的响应以及恢复到稳定操作状态的需求。本章讨论了此模式的各个方面，包括错误的检测、通过日志记录、重试和回退等机制处理这些错误，以及用于将智能体或系统恢复到正常功能的策略。异常处理和恢复模式的实际应用在多个领域中得到说明，展示了其在处理现实世界复杂性和潜在失败方面的相关性。这些应用展示了为 AI 智能体配备异常处理能力如何有助于它们在动态环境中的可靠性和适应性。

## References

## 参考文献

1. McConnell, S. (2004). *Code Complete (2nd ed.)*. Microsoft Press.
2. Shi, Y., Pei, H., Feng, L., Zhang, Y., & Yao, D. (2024). *Towards Fault Tolerance in Multi-Agent Reinforcement Learning*. arXiv preprint arXiv:2412.00534.
3. O'Neill, V. (2022). *Improving Fault Tolerance and Reliability of Heterogeneous Multi-Agent IoT Systems Using Intelligence Transfer*. Electronics, 11(17), 2724.

[image1]: ../images/chapter-12/image1.png
[image2]: ../images/chapter-12/image2.png
