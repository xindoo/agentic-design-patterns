# Appendix B - AI Agentic Interactions: From GUI to Real World environment

# 附录 B - AI 智能体交互：从图形用户界面到真实世界环境

AI agents are increasingly performing complex tasks by interacting with digital interfaces and the physical world. Their ability to perceive, process, and act within these varied environments is fundamentally transforming automation, human-computer interaction, and intelligent systems. This appendix explores how agents interact with computers and their environments, highlighting advancements and projects.

AI 智能体正日益通过与数字界面和物理世界的交互来执行复杂任务。它们在这些多样化环境中感知、处理和行动的能力，正在从根本上重塑自动化、人机交互和智能系统的格局。本附录深入探讨智能体如何与计算机及其环境交互，并重点介绍相关技术进展与代表性项目。

## Interaction: Agents with Computers

## 交互：智能体与计算机

The evolution of AI from conversational partners to active, task-oriented agents is being driven by Agent-Computer Interfaces (ACIs). These interfaces allow AI to interact directly with a computer's Graphical User Interface (GUI), enabling it to perceive and manipulate visual elements like icons and buttons just as a human would. This new method moves beyond the rigid, developer-dependent scripts of traditional automation that relied on APIs and system calls. By using the visual "front door" of software, AI can now automate complex digital tasks in a more flexible and powerful way, a process that involves several key stages:

AI 从对话伙伴向主动式任务导向型智能体演进，正由智能体-计算机界面（Agent-Computer Interfaces，ACIs）技术驱动。这些界面使 AI 能够直接与计算机的图形用户界面（Graphical User Interface，GUI）交互，使其能像人类一样感知并操作图标、按钮等视觉元素。这种新范式超越了依赖 API 和系统调用的传统自动化方法——后者往往受限于僵化的、依赖开发人员编写的脚本。通过利用软件的视觉"前门"，AI 现能以更灵活、更强大的方式自动化复杂数字任务，该过程涉及以下关键阶段：

* **Visual Perception:** The agent first captures a visual representation of the screen, essentially taking a screenshot.  
* **GUI Element Recognition:** It then analyzes this image to distinguish between various GUI elements. It must learn to "see" the screen not as a mere collection of pixels, but as a structured layout with interactive components, discerning a clickable "Submit" button from a static banner image or an editable text field from a simple label.  
* **Contextual Interpretation:** The ACI module, acting as a bridge between the visual data and the agent's core intelligence (often a Large Language Model or LLM), interprets these elements within the context of the task. It understands that a magnifying glass icon typically means "search" or that a series of radio buttons represents a choice. This module is crucial for enhancing the LLM's reasoning, allowing it to form a plan based on visual evidence.  
* **Dynamic Action and Response:** The agent then programmatically controls the mouse and keyboard to execute its plan—clicking, typing, scrolling, and dragging. Critically, it must constantly monitor the screen for visual feedback, dynamically responding to changes, loading screens, pop-up notifications, or errors to successfully navigate multi-step workflows.

* **视觉感知**：智能体首先捕获屏幕的视觉呈现，本质上相当于截屏操作。
* **GUI 元素识别**：随后分析该图像以区分各类 GUI 元素。它必须学会将屏幕"解读"为具有交互组件的结构化布局，而非单纯的像素集合，能够辨别可点击的"提交"按钮与静态横幅广告，或区分可编辑文本框与普通标签。
* **上下文理解**：ACI 模块作为视觉数据与智能体核心智能（通常为大型语言模型 LLM）间的桥梁，在任务背景下解析这些元素。它能理解放大镜图标通常代表"搜索"，或一组单选按钮表示选项。此模块对增强 LLM 推理能力至关重要，使其能基于视觉证据制定行动计划。
* **动态执行与响应**：智能体随后通过程序化控制鼠标和键盘执行计划——包括点击、输入、滚动和拖拽。关键在于，它必须持续监控屏幕以获取视觉反馈，动态响应界面变化、加载状态、弹窗通知或错误信息，从而成功驾驭多步骤工作流。

This technology is no longer theoretical. Several leading AI labs have developed functional agents that demonstrate the power of GUI interaction:

这项技术已不再停留在理论层面。多家领先 AI 实验室已开发出功能性智能体，充分展示了 GUI 交互的强大潜力：

**ChatGPT Operator (OpenAI):** Envisioned as a digital partner, ChatGPT Operator is designed to automate tasks across a wide range of applications directly from the desktop. It understands on-screen elements, enabling it to perform actions like transferring data from a spreadsheet into a customer relationship management (CRM) platform, booking a complex travel itinerary across airline and hotel websites, or filling out detailed online forms without needing specialized API access for each service. This makes it a universally adaptable tool aimed at boosting both personal and enterprise productivity by taking over repetitive digital chores.

**ChatGPT Operator（OpenAI）**：ChatGPT Operator 被构想为数字协作伙伴，旨在直接从桌面端自动化多种应用程序的任务。它能理解屏幕元素，从而执行诸如将电子表格数据导入客户关系管理（CRM）系统、在航空公司和酒店网站间规划复杂行程，或填写详尽在线表单等操作，无需为每个服务配置专用 API 访问权限。这使其成为通用性工具，旨在通过接管重复性数字任务提升个人与企业效率。

**Google Project Mariner:** As a research prototype, Project Mariner operates as an agent within the Chrome browser (see Fig. 1). Its purpose is to understand a user's intent and autonomously carry out web-based tasks on their behalf. For example, a user could ask it to find three apartments for rent within a specific budget and neighborhood; Mariner would then navigate to real estate websites, apply the filters, browse the listings, and extract the relevant information into a document. This project represents Google's exploration into creating a truly helpful and "agentive" web experience where the browser actively works for the user.

**Google Project Mariner**：作为研究原型，Project Mariner 作为智能体在 Chrome 浏览器内运行（见图 1）。其核心目标是理解用户意图并自主执行基于网络的任务。例如，用户可指令其在特定预算和区域内寻找三套出租公寓；Mariner 便会导航至房产网站，应用筛选条件，浏览房源列表，并将相关信息提取至文档中。该项目体现了 Google 对构建真正实用且具"代理性"网络体验的探索——让浏览器主动为用户服务。

![][image1]

Fig.1: Interaction between and Agent and the Web Browser

图 1：智能体与网络浏览器的交互示意图

**Anthropic's Computer Use:** This feature empowers Anthropic's AI model, Claude, to become a direct user of a computer's desktop environment. By capturing screenshots to perceive the screen and programmatically controlling the mouse and keyboard, Claude can orchestrate workflows that span multiple, unconnected applications. A user could ask it to analyze data in a PDF report, open a spreadsheet application to perform calculations on that data, generate a chart, and then paste that chart into an email draft—a sequence of tasks that previously required constant human input.

**Anthropic 的计算机使用功能**：该特性使 Anthropic 的 AI 模型 Claude 能够成为计算机桌面环境的直接操作用户。通过截屏感知界面并以程序化方式控制鼠标键盘，Claude 可编排跨多个独立应用的工作流。用户可要求其分析 PDF 报告中的数据，打开电子表格程序进行相关计算，生成图表，并将图表插入邮件草稿——这一系列任务以往需要持续的人工介入。

**Browser Use**: This is an open-source library that provides a high-level API for programmatic browser automation. It enables AI agents to interface with web pages by granting them access to and control over the Document Object Model (DOM). The API abstracts the intricate, low-level commands of browser control protocols, into a more simplified and intuitive set of functions. This allows an agent to perform complex sequences of actions, including data extraction from nested elements, form submissions, and automated navigation across multiple pages. As a result, the library facilitates the transformation of unstructured web data into a structured format that an AI agent can systematically process and utilize for analysis or decision-making.

**Browser Use**：这是一个提供程序化浏览器自动化高级 API 的开源库。它使 AI 智能体通过访问和控制文档对象模型（Document Object Model，DOM）与网页交互。该 API 将浏览器控制协议的复杂底层指令抽象为更简洁直观的函数集。这使得智能体能够执行复杂操作序列，包括从嵌套元素提取数据、提交表单以及跨页面自动导航。因此，该库助力将非结构化网络数据转化为 AI 智能体可以用于分析或决策的结构化格式。

## Interaction: Agents with the Environment

## 交互：智能体与环境

Beyond the confines of a computer screen, AI agents are increasingly designed to interact with complex, dynamic environments, often mirroring the real world. This requires sophisticated perception, reasoning, and actuation capabilities.

超越计算机屏幕的局限，AI 智能体正越来越多地被设计用于与复杂、动态的环境交互，这些环境往往模拟现实世界。这要求智能体具备复杂的感知、推理和执行能力。

Google's **Project Astra** is a prime example of an initiative pushing the boundaries of agent interaction with the environment. Astra aims to create a universal AI agent that is helpful in everyday life, leveraging multimodal inputs (sight, sound, voice) and outputs to understand and interact with the world contextually. This project focuses on rapid understanding, reasoning, and response, allowing the agent to "see" and "hear" its surroundings through cameras and microphones and engage in natural conversation while providing real-time assistance. Astra's vision is an agent that can seamlessly assist users with tasks ranging from finding lost items to debugging code, by understanding the environment it observes. This moves beyond simple voice commands to a truly embodied understanding of the user's immediate physical context.

Google 的 **Project Astra** 是推动智能体与环境交互边界的一个典范。Astra 致力于打造一个在日常生活中实用的通用 AI 智能体，它利用多模态输入（视觉、听觉、语音）和输出来理解世界并进行上下文交互。该项目聚焦于快速理解、推理与响应，使智能体通过摄像头和麦克风"看见"和"听见"周遭环境，并在提供实时协助的同时进行自然对话。Astra 的愿景是打造一个能无缝帮助用户完成从寻找失物到调试代码等各种任务的智能体，其核心在于理解所观察的环境。这超越了简单的语音指令，实现了对用户即时物理情境的真正具身化理解。

Google's **Gemini Live**, transforms standard AI interactions into a fluid and dynamic conversation. Users can speak to the AI and receive responses in a natural-sounding voice with minimal delay, and can even interrupt or change topics mid-sentence, prompting the AI to adapt immediately. The interface expands beyond voice, allowing users to incorporate visual information by using their phone's camera, sharing their screen, or uploading files for a more context-aware discussion. More advanced versions can even perceive a user's tone of voice and intelligently filter out irrelevant background noise to better understand the conversation. These capabilities combine to create rich interactions, such as receiving live instructions on a task by simply pointing a camera at it.

Google 的 **Gemini Live** 将标准 AI 交互转化为流畅且动态的对话体验。用户可与 AI 交谈，并以极低延迟收到自然语音回复，甚至能在语句中途打断或切换话题，AI 会立即适应。交互界面不限于语音，用户还可通过手机摄像头、屏幕共享或文件上传融入视觉信息，进行更具情境感知的讨论。更高级版本甚至能感知用户语调，并智能滤除无关背景噪音以提升对话理解。这些能力共同创造了丰富的交互场景，例如仅需将摄像头对准某物即可获得该任务的实时指导。

OpenAI's **GPT-4o model** is an alternative designed for "omni" interaction, meaning it can reason across voice, vision, and text. It processes these inputs with low latency that mirrors human response times, which allows for real-time conversations. For example, users can show the AI a live video feed to ask questions about what is happening, or use it for language translation. OpenAI provides developers with a "Realtime API" to build applications requiring low-latency, speech-to-speech interactions.

OpenAI 的 **GPT-4o 模型** 是专为"全向"交互设计的另一选择，意指其能跨语音、视觉和文本进行推理。该模型以接近人类响应速度的低延迟处理这些输入，从而实现实时对话。例如，用户可向 AI 展示实时视频流并询问画面内容，或用于语言翻译。OpenAI 为开发者提供了"实时 API"，用于构建需要低延迟、语音到语音交互的应用。

OpenAI's **ChatGPT Agent** represents a significant architectural advancement over its predecessors, featuring an integrated framework of new capabilities. Its design incorporates several key functional modalities: the capacity for autonomous navigation of the live internet for real-time data extraction, the ability to dynamically generate and execute computational code for tasks like data analysis, and the functionality to interface directly with third-party software applications. The synthesis of these functions allows the agent to orchestrate and complete complex, sequential workflows from a singular user directive. It can therefore autonomously manage entire processes, such as performing market analysis and generating a corresponding presentation, or planning logistical arrangements and executing the necessary transactions. In parallel with the launch, OpenAI has proactively addressed the emergent safety considerations inherent in such a system. An accompanying "System Card" delineates the potential operational hazards associated with an AI capable of performing actions online, acknowledging the new vectors for misuse. To mitigate these risks, the agent's architecture includes engineered safeguards, such as requiring explicit user authorization for certain classes of actions and deploying robust content filtering mechanisms. The company is now engaging its initial user base to further refine these safety protocols through a feedback-driven, iterative process.

OpenAI 的 **ChatGPT Agent** 代表了相较于前代产品的重大架构升级，集成了新功能框架。其设计包含多项核心功能模式：自主浏览实时互联网以提取实时数据的能力、动态生成并执行计算代码以完成数据分析等任务的能力，以及直接与第三方软件应用交互的功能。这些能力的融合使智能体从单一用户指令出发，编排并完成复杂、有序的工作流。因此，它能自主管理整个流程，例如执行市场分析并生成对应演示文稿，或规划物流安排并执行必要交易。在发布同时，OpenAI 主动应对了此类系统固有的新兴安全问题。随附的"系统卡"文件阐明了具备在线操作能力的 AI 可能带来的潜在风险，承认了新的滥用途径。为降低这些风险，智能体架构内置了工程化保障措施，如要求特定操作类别需获得用户明确授权，并部署了强健的内容过滤机制。公司现正通过反馈驱动的迭代流程，邀请初期用户群体共同完善这些安全协议。

**Seeing AI,** a complimentary mobile application from Microsoft, empowers individuals who are blind or have low vision by offering real-time narration of their surroundings. The app leverages artificial intelligence through the device's camera to identify and describe various elements, including objects, text, and even people. Its core functionalities encompass reading documents, recognizing currency, identifying products through barcodes, and describing scenes and colors. By providing enhanced access to visual information, Seeing AI ultimately fosters greater independence for visually impaired users.

**Seeing AI** 是 Microsoft 推出的一款免费移动应用，它通过实时描述周围环境，为盲人或视力障碍人士赋能。该应用借助设备摄像头运用人工智能技术，识别并描述各类元素，包括物体、文字乃至人物。其核心功能涵盖文档阅读、货币识别、条形码产品辨识以及场景和颜色描述。通过增强对视觉信息的可及性，Seeing AI 最终提升了视障用户的独立生活能力。

**Anthropic's Claude 4 Series**: Anthropic's Claude 4 is another alternative with capabilities for advanced reasoning and analysis. Though historically focused on text, Claude 4 includes robust vision capabilities, allowing it to process information from images, charts, and documents. The model is suited for handling complex, multi-step tasks and providing detailed analysis. While the real-time conversational aspect is not its primary focus compared to other models, its underlying intelligence is designed for building highly capable AI agents.

**Anthropic 的 Claude 4 系列**：Anthropic 的 Claude 4 是另一款具备高级推理与分析能力的替代选择。尽管其传统强项在于文本处理，但 Claude 4 也包含了强大的视觉功能，能处理来自图像、图表和文档的信息。该模型适用于处理复杂的多步骤任务并提供详尽分析。虽然其实时对话特性并非主要焦点（相较于其他模型），但其底层智能专为构建高能力 AI 智能体而设计。

## Vibe Coding: Intuitive Development with AI

## Vibe 编码：使用 AI 的直观开发范式

Beyond direct interaction with GUIs and the physical world, a new paradigm is emerging in how developers build software with AI: "vibe coding." This approach moves away from precise, step-by-step instructions and instead relies on a more intuitive, conversational, and iterative interaction between the developer and an AI coding assistant. The developer provides a high-level goal, a desired "vibe," or a general direction, and the AI generates code to match.

除了与 GUI 和物理环境的直接交互外，开发人员使用 AI 构建软件的方式也涌现出新范式："vibe 编码"。这种方法摒弃了精确的、逐步的指令，转而依赖开发者与 AI 编码助手之间更直观、对话式和迭代的协作。开发者提供高层次目标、期望的"氛围"或大致方向，AI 则生成与之匹配的代码。

This process is characterized by:

该过程具有以下特征：

* **Conversational Prompts:** Instead of writing detailed specifications, a developer might say, "Create a simple, modern-looking landing page for a new app," or, "Refactor this function to be more Pythonic and readable." The AI interprets the "vibe" of "modern" or "Pythonic" and generates the corresponding code.
* **Iterative Refinement:** The initial output from the AI is often a starting point. The developer then provides feedback in natural language, such as, "That's a good start, but can you make the buttons blue?" or, "Add some error handling to that." This back-and-forth continues until the code meets the developer's expectations.
* **Creative Partnership:** In vibe coding, the AI acts as a creative partner, suggesting ideas and solutions that the developer may not have considered. This can accelerate the development process and lead to more innovative outcomes.
* **Focus on "What" not "How":** The developer focuses on the desired outcome (the "what") and leaves the implementation details (the "how") to the AI. This allows for rapid prototyping and exploration of different approaches without getting bogged down in boilerplate code.
* **Optional Memory Banks:** To maintain context across longer interactions, developers can use "memory banks" to store key information, preferences, or constraints. For example, a developer might save a specific coding style or a set of project requirements to the AI's memory, ensuring that future code generations remain consistent with the established "vibe" without needing to repeat the instructions.

* **对话式提示**：开发者不再编写详细规格说明，而是用自然语言表达，如"为新应用创建一个简洁现代风格的登录页面"，或"重构此函数使其更符合 Pythonic 风格并提升可读性"。AI 会解读"现代"或"Pythonic"的"氛围"内涵，生成相应代码。
* **迭代精炼**：AI 的初始输出通常只是起点。开发者随后以自然语言提供反馈，如"这个开头不错，但能把按钮改成蓝色吗？"或"为那段代码添加错误处理机制。"如此往复，直至代码符合预期。
* **创意伙伴关系**：在 vibe 编码中，AI 扮演创意伙伴角色，提出开发者可能未曾考虑的创意和解决方案。这能加速开发进程并催生更具创新性的成果。
* **聚焦"目标"而非"方法"**：开发者专注于期望成果（"目标"），将实现细节（"方法"）交由 AI 处理。这使得快速原型设计和多方案探索成为可能，避免陷入样板代码的繁琐。
* **可选记忆库**：为在长对话中保持上下文连贯，开发者可使用"记忆库"存储关键信息、偏好或约束条件。例如，开发者可将特定编码风格或项目需求集保存至 AI 记忆库，确保后续代码生成与既定"氛围"保持一致，无需重复指令。

Vibe coding is becoming increasingly popular with the rise of powerful AI models like GPT-4, Claude, and Gemini, which are integrated into development environments. These tools are not just auto-completing code; they are actively participating in the creative process of software development, making it more accessible and efficient. This new way of working is changing the nature of software engineering, emphasizing creativity and high-level thinking over rote memorization of syntax and APIs.

随着 GPT-4、Claude 和 Gemini 等强大 AI 模型集成至开发环境，Vibe 编码日益流行。这些工具不仅是代码自动补全器；它们正积极参与软件开发的创意过程，使其更易用、更高效。这种新型工作方式正在改变软件工程的性质，强调创造力与高阶思维，而非对语法和 API 的死记硬背。

## Key takeaways

## 关键要点

* AI agents are evolving from simple automation to visually controlling software through graphical user interfaces, much like a human would.  
* The next frontier is real-world interaction, with projects like Google's Astra using cameras and microphones to see, hear, and understand their physical surroundings.  
* Leading technology companies are converging these digital and physical capabilities to create universal AI assistants that operate seamlessly across both domains.  
* This shift is creating a new class of proactive, context-aware AI companions capable of assisting with a vast range of tasks in users' daily lives.

* AI 智能体正从简单自动化演进为通过图形用户界面视觉控制软件，操作方式类人化。
* 下一前沿是真实世界交互，如 Google Astra 等项目利用摄像头和麦克风感知、聆听并理解物理环境。
* 领先科技公司正融合这些数字与物理能力，打造跨域无缝运行的通用 AI 助手。
* 这一转变催生了新型主动式、情境感知型 AI 伙伴，能协助用户处理日常生活中的大量任务。

## Conclusion

## 结论

Agents are undergoing a significant transformation, moving from basic automation to sophisticated interaction with both digital and physical environments. By leveraging visual perception to operate Graphical User Interfaces, these agents can now manipulate software just as a human would, bypassing the need for traditional APIs. Major technology labs are pioneering this space with agents capable of automating complex, multi-application workflows directly on a user's desktop. Simultaneously, the next frontier is expanding into the physical world, with initiatives like Google's Project Astra using cameras and microphones to contextually engage with their surroundings. These advanced systems are designed for multimodal, real-time understanding that mirrors human interaction.

智能体正经历重大转型，从基础自动化迈向与数字及物理环境的复杂交互。借助视觉感知操作图形用户界面，这些智能体能像人类一样操控软件，绕过了对传统 API 的依赖。主要技术实验室正引领这一领域，其开发的智能体可在桌面直接自动化复杂的多应用工作流。与此同时，下一前沿已扩展至物理世界，如 Google Project Astra 等项目利用摄像头和麦克风与周边环境进行情境化互动。这些先进系统旨在实现媲美人类交互的多模态实时理解。

The ultimate vision is a convergence of these digital and physical capabilities, creating universal AI assistants that operate seamlessly across all of a user's environments. This evolution is also reshaping software creation itself through "vibe coding," a more intuitive and conversational partnership between developers and AI. This new method prioritizes high-level goals and creative intent, allowing developers to focus on the desired outcome rather than implementation details. This shift accelerates development and fosters innovation by treating AI as a creative partner. Ultimately, these advancements are paving the way for a new era of proactive, context-aware AI companions capable of assisting with a vast array of tasks in our daily lives.

终极愿景是融合这些数字与物理能力，创建跨用户所有环境无缝运作的通用 AI 助手。这一演进也通过"vibe 编码"重塑了软件创作本身，形成开发者与 AI 间更直观、对话式的伙伴关系。该新方法优先考虑高层次目标与创意意图，让开发者聚焦于期望成果而非实现细节。通过将 AI 视为创意合作伙伴，这一转变加速了开发进程并激发了创新。最终，这些进步正为主动式、情境感知型 AI 伙伴的新时代铺平道路，使其能够协助我们应对日常生活中的大量任务。

## References

## 参考文献

 1. Open AI Operator, [https://openai.com/index/introducing-operator/](https://openai.com/index/introducing-operator/)
 2. Open AI ChatGPT Agent: [https://openai.com/index/introducing-chatgpt-agent/](https://openai.com/index/introducing-chatgpt-agent/)
 3. Browser Use: [https://docs.browser-use.com/introduction](https://docs.browser-use.com/introduction)
 4. Project Mariner, [https://deepmind.google/models/project-mariner/](https://deepmind.google/models/project-mariner/)
 5. Anthropic Computer use: [https://docs.anthropic.com/en/docs/build-with-claude/computer-use](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)
 6. Project Astra, [https://deepmind.google/models/project-astra/](https://deepmind.google/models/project-astra/)
 7. Gemini Live, [https://gemini.google/overview/gemini-live/?hl=en](https://gemini.google/overview/gemini-live/?hl=en)
 8. OpenAI's GPT-4,  [https://openai.com/index/gpt-4-research/](https://openai.com/index/gpt-4-research/)
 9. Claude 4, [https://www.anthropic.com/news/claude-4](https://www.anthropic.com/news/claude-4)

[image1]: ../images/appendix-b/image1.png
