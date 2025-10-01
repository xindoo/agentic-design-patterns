# 附录 D \- 使用 AgentSpace 构建 Agent

# 概述

AgentSpace 是一个旨在通过将人工智能集成到日常工作流程中来促进"Agent 驱动型企业"的平台。其核心是在组织的整个数字足迹（包括文档、电子邮件和数据库）中提供统一的搜索能力。该系统利用先进的 AI 模型（如 Google 的 Gemini）来理解和综合来自这些不同来源的信息。

该平台支持创建和部署专门的 AI "Agent"，这些 Agent 可以执行复杂任务并自动化流程。这些 Agent 不仅仅是聊天机器人；它们可以自主地进行推理、规划和执行多步骤操作。例如，一个 Agent 可以研究某个主题，编写带有引用的报告，甚至生成音频摘要。

为了实现这一点，AgentSpace 构建了企业知识图谱，映射人员、文档和数据之间的关系。这使得 AI 能够理解上下文并提供更相关和个性化的结果。该平台还包括一个名为 Agent Designer 的无代码界面，用于创建自定义 Agent，无需深厚的技术专业知识。

此外，AgentSpace 支持多 Agent 系统，其中不同的 AI Agent 可以通过称为 Agent2Agent（A2A）协议的开放协议进行通信和协作。这种互操作性允许更复杂和协调的工作流。安全性是一个基础组件，具有基于角色的访问控制和数据加密等功能来保护敏感的企业信息。最终，AgentSpace 旨在通过将智能自主系统直接嵌入组织的运营结构来提高生产力和决策能力。

# 如何使用 AgentSpace UI 构建 Agent

图 1 说明了如何通过从 Google Cloud Console 选择 AI Applications 来访问 AgentSpace。

![][image1]  
图 1：如何使用 Google Cloud Console 访问 AgentSpace

你的 Agent 可以连接到各种服务，包括 Calendar、Google Mail、Workaday、Jira、Outlook 和 Service Now（见图 2）。

![][image2]  
图 2：与包括 Google 和第三方平台在内的各种服务集成。

然后，Agent 可以使用自己的提示词，从 Google 提供的预制提示词库中选择，如图 3 所示。

![][image3]  
图 3：Google 的预组装提示词库

或者，你可以创建自己的提示词，如图 4 所示，然后由你的 Agent 使用。  
![][image4]  
图 4：自定义 Agent 的提示词    
   
AgentSpace 提供了许多高级功能，例如与数据存储集成以存储你自己的数据、与 Google 知识图谱或你的私有知识图谱集成、用于将你的 Agent 暴露给 Web 的 Web 界面、用于监控使用情况的分析等（见图 5）。   
![][image5]  
图 5：AgentSpace 高级功能

完成后，AgentSpace 聊天界面（图 6）将可访问。

![][image6]  
图 6：用于与你的 Agent 启动聊天的 AgentSpace 用户界面。

# 结论

总之，AgentSpace 为在组织现有数字基础设施中开发和部署 AI Agent 提供了一个功能性框架。该系统的架构将复杂的后端流程（如自主推理和企业知识图谱映射）与用于 Agent 构建的图形用户界面连接起来。通过此界面，用户可以通过集成各种数据服务并通过提示词定义其操作参数来配置 Agent，从而生成定制的、上下文感知的自动化系统。

这种方法抽象了底层技术复杂性，使得无需深厚的编程专业知识即可构建专门的多 Agent 系统。主要目标是将自动化分析和操作能力直接嵌入工作流程，从而提高流程效率并增强数据驱动分析。对于实践指导，提供了实践学习模块，例如 Google Cloud Skills Boost 上的"Build a Gen AI Agent with Agentspace"实验室，该实验室为技能获取提供了结构化环境。

# 参考文献

1. Create a no-code agent with Agent Designer, [https://cloud.google.com/agentspace/agentspace-enterprise/docs/agent-designer](https://cloud.google.com/agentspace/agentspace-enterprise/docs/agent-designer)   
2. Google Cloud Skills Boost, [https://www.cloudskillsboost.google/](https://www.cloudskillsboost.google/) 

[image1]: ../images/appendix-d/image1.png

[image2]: ../images/appendix-d/image2.png

[image3]: ../images/appendix-d/image3.png

[image4]: ../images/appendix-d/image4.png

[image5]: ../images/appendix-d/image5.png

[image6]: ../images/appendix-d/image6.png