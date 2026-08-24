---
layout: bilingual
lang: bilingual
---

# Appendix A: Advanced Prompting Techniques

# 附录 A：高级提示技术

## Introduction to Prompting

## 提示技术简介

Prompting, the primary interface for interacting with language models, is the process of crafting inputs to guide the model towards generating a desired output. This involves structuring requests, providing relevant context, specifying the output format, and demonstrating expected response types. Well-designed prompts can maximize the potential of language models, resulting in accurate, relevant, and creative responses. In contrast, poorly designed prompts can lead to ambiguous, irrelevant, or erroneous outputs.

提示技术是与语言模型交互的核心方式，指通过精心设计输入来引导模型生成期望输出的过程。这包括构建请求结构、提供相关上下文、指定输出格式以及展示预期的响应模式。设计精良的提示能够充分发挥语言模型的潜力，产生准确、相关且富有创造性的响应。反之，设计不当的提示则可能导致模糊、不相关甚至错误的输出。

The objective of prompt engineering is to consistently elicit high-quality responses from language models. This requires understanding the capabilities and limitations of the models and effectively communicating intended goals. It involves developing expertise in communicating with AI by learning how to best instruct it.

提示工程的目标是从语言模型中持续获得高质量的输出。这需要深入理解模型的能力边界和局限性，并有效地传达预期目标。它涉及通过学习如何最优地指导 AI 来发展与 AI 沟通的专业技能。

This appendix details various prompting techniques that extend beyond basic interaction methods. It explores methodologies for structuring complex requests, enhancing the model's reasoning abilities, controlling output formats, and integrating external information. These techniques are applicable to building a range of applications, from simple chatbots to complex multi-agent systems, and can improve the performance and reliability of agentic applications.

本附录详细介绍了超越基础交互方法的各类提示技术。它探讨了构建复杂请求、增强模型推理能力、控制输出格式以及整合外部信息的方法论。这些技术适用于构建从简单聊天机器人到复杂多智能体的各类应用，能够显著提升 Agentic 应用的性能和可靠性。

Agentic patterns, the architectural structures for building intelligent systems, are detailed in the main chapters. These patterns define how agents plan, utilize tools, manage memory, and collaborate. The efficacy of these agentic systems is contingent upon their ability to interact meaningfully with language models.

Agentic 模式是构建智能系统的架构蓝图，在主要章节中已有详细阐述。这些模式定义了智能体如何规划、使用工具、管理记忆和协同工作。这些 Agentic 系统的效能最终取决于它们与语言模型进行有意义交互的能力。

## Core Prompting Principles

## 核心提示原则

Core Principles for Effective Prompting of Language Models:

与语言模型进行有效提示的核心原则：

Effective prompting rests on fundamental principles guiding communication with language models, applicable across various models and task complexities. Mastering these principles is essential for consistently generating useful and accurate responses.

有效的提示建立在与语言模型沟通的基本原则之上，这些原则适用于各种模型和任务复杂度。掌握这些原则对于持续生成有用且准确的响应至关重要。

**Clarity and Specificity**: Instructions should be unambiguous and precise. Language models interpret patterns; multiple interpretations may lead to unintended responses. Define the task, desired output format, and any limitations or requirements. Avoid vague language or assumptions. Inadequate prompts yield ambiguous and inaccurate responses, hindering meaningful output.

**清晰性与具体性**：指令应当明确无误且精确。语言模型基于模式进行推理；多重解释可能导致意外结果。需要明确定义任务、期望的输出格式以及任何限制或要求。避免使用模糊语言或做出假设。不充分的提示会产生模糊和不准确的响应，影响输出质量。

**Conciseness**: While specificity is crucial, it should not compromise conciseness. Instructions should be direct. Unnecessary wording or complex sentence structures can confuse the model or obscure the primary instruction. Prompts should be simple; what is confusing to the user is likely confusing to the model. Avoid intricate language and superfluous information. Use direct phrasing and active verbs to clearly delineate the desired action. Effective verbs include: Act, Analyze, Categorize, Classify, Contrast, Compare, Create, Describe, Define, Evaluate, Extract, Find, Generate, Identify, List, Measure, Organize, Parse, Pick, Predict, Provide, Rank, Recommend, Return, Retrieve, Rewrite, Select, Show, Sort, Summarize, Translate, Write.

**简洁性**：在确保具体性的同时，必须保持简洁。指令应当直截了当。不必要的措辞或复杂的句子结构可能混淆模型或掩盖核心指令。提示应当简单明了：对用户而言困惑的内容，对模型同样可能造成困惑。避免使用复杂语言和冗余信息。采用直接表达和主动动词来清晰界定期望操作。有效的动词包括：执行、分析、分类、归类、对比、比较、创建、描述、定义、评估、提取、查找、生成、识别、列出、测量、组织、解析、挑选、预测、提供、排序、推荐、返回、检索、重写、选择、显示、整理、总结、翻译、编写。

**Using Verbs:** Verb choice is a key prompting tool. Action verbs indicate the expected operation. Instead of "Think about summarizing this," a direct instruction like "Summarize the following text" is more effective. Precise verbs guide the model to activate relevant training data and processes for that specific task.

**善用动词**：动词选择是提示工程的关键技巧。动作动词明确指示期望的操作。与其说"考虑总结这个"，不如直接使用"总结以下文本"这样的指令更为有效。精确的动词能够引导模型激活与特定任务相关的训练数据和流程。

**Instructions Over Constraints:** Positive instructions are generally more effective than negative constraints. Specifying the desired action is preferred to outlining what not to do. While constraints have their place for safety or strict formatting, excessive reliance can cause the model to focus on avoidance rather than the objective. Frame prompts to guide the model directly. Positive instructions align with human guidance preferences and reduce confusion.

**指令优于约束**：积极指令通常比消极约束更为有效。明确指定期望操作比罗列禁止事项效果更好。虽然约束在安全控制或严格格式要求中有其价值，但过度依赖可能使模型过度关注规避而非目标达成。构建提示时应直接引导模型。积极指令更符合人类指导习惯，并能减少混淆。

**Experimentation and Iteration:** Prompt engineering is an iterative process. Identifying the most effective prompt requires multiple attempts. Begin with a draft, test it, analyze the output, identify shortcomings, and refine the prompt. Model variations, configurations (like temperature or top-p), and slight phrasing changes can yield different results. Documenting attempts is vital for learning and improvement. Experimentation and iteration are necessary to achieve the desired performance.

**实验与迭代**：提示工程是一个迭代过程。找到最有效的提示需要多次尝试。从初步设计开始，进行测试，分析输出，识别不足，然后优化提示。模型变体、配置参数（如温度或 top-p）以及细微的措辞变化都可能产生不同结果。记录实验过程对于学习和改进至关重要。实验和迭代是实现预期性能的必要手段。

These principles form the foundation of effective communication with language models. By prioritizing clarity, conciseness, action verbs, positive instructions, and iteration, a robust framework is established for applying more advanced prompting techniques.

这些原则构成了与语言模型有效沟通的基础。通过优先考虑清晰性、简洁性、善用动词、积极指令和迭代流程，为应用更高级提示技术奠定了坚实基础。

## Basic Prompting Techniques

## 基础提示技术

Building on core principles, foundational techniques provide language models with varying levels of information or examples to direct their responses. These methods serve as an initial phase in prompt engineering and are effective for a wide spectrum of applications.

基于核心原则，基础技术为语言模型提供不同层次的信息或示例来引导其响应。这些方法作为提示工程的入门阶段，适用于广泛的应用场景。

## Zero-Shot Prompting

## 零样本提示（Zero-Shot）

Zero-shot prompting is the most basic form of prompting, where the language model is provided with an instruction and input data without any examples of the desired input-output pair. It relies entirely on the model's pre-training to understand the task and generate a relevant response. Essentially, a zero-shot prompt consists of a task description and initial text to begin the process.

零样本提示是最基础的提示形式，语言模型仅接收指令和输入数据，不提供任何期望的输入-输出对示例。它完全依赖模型的预训练知识来理解任务并生成相关响应。本质上，零样本提示包含任务描述和启动过程的初始文本。

* **When to use:** Zero-shot prompting is often sufficient for tasks that the model has likely encountered extensively during its training, such as simple question answering, text completion, or basic summarization of straightforward text. It's the quickest approach to try first.  
* **Example:**  
  Translate the following English sentence to French: 'Hello, how are you?'

* **适用场景**：零样本提示通常适用于模型在训练过程中可能广泛接触的任务，例如简单问答、文本补全或基础文本摘要。这是最快捷的初步尝试方法。
* **示例**：
  将以下英文句子翻译成法语：'Hello, how are you?'

## One-Shot Prompting

## 单样本提示（One-Shot）

One-shot prompting involves providing the language model with a single example of the input and the corresponding desired output prior to presenting the actual task. This method serves as an initial demonstration to illustrate the pattern the model is expected to replicate. The purpose is to equip the model with a concrete instance that it can use as a template to effectively execute the given task.

单样本提示在呈现实际任务前，向语言模型提供一个输入及其对应期望输出的示例。这种方法作为初始演示，展示模型应遵循的模式。目的是为模型提供具体实例，使其能够作为模板有效执行给定任务。

* **When to use:** One-shot prompting is useful when the desired output format or style is specific or less common. It gives the model a concrete instance to learn from. It can improve performance compared to zero-shot for tasks requiring a particular structure or tone.  
* **Example:**  
  Translate the following English sentences to Spanish:  
  English: 'Thank you.'  
  Spanish: 'Gracias.'

  English: 'Please.'  
  Spanish:

* **适用场景**：当期望的输出格式或风格较为特殊或不常见时，单样本提示十分有用。它为模型提供了具体的学习范例。相比零样本，它能提升需要特定结构或语气任务的性能。
* **示例**：
  将以下英文句子翻译成西班牙语：
  英文：'Thank you.'
  西班牙语：'Gracias.'

  英文：'Please.'
  西班牙语：

## Few-Shot Prompting

## 少样本提示（Few-Shot）

Few-shot prompting enhances one-shot prompting by supplying several examples, typically three to five, of input-output pairs. This aims to demonstrate a clearer pattern of expected responses, improving the likelihood that the model will replicate this pattern for new inputs. This method provides multiple examples to guide the model to follow a specific output pattern.

少样本提示在单样本基础上增强，提供多个（通常三到五个）输入-输出对示例。这旨在展示更清晰的预期响应模式，提高模型为新输入复制该模式的可能性。此方法通过多个示例引导模型遵循特定输出模式。

* **When to use:** Few-shot prompting is particularly effective for tasks where the desired output requires adhering to a specific format, style, or exhibiting nuanced variations. It's excellent for tasks like classification, data extraction with specific schemas, or generating text in a particular style, especially when zero-shot or one-shot don't yield consistent results. Using at least three to five examples is a general rule of thumb, adjusting based on task complexity and model token limits.  
* **Importance of Example Quality and Diversity:** The effectiveness of few-shot prompting heavily relies on the quality and diversity of the examples provided. Examples should be accurate, representative of the task, and cover potential variations or edge cases the model might encounter. High-quality, well-written examples are crucial; even a small mistake can confuse the model and result in undesired output. Including diverse examples helps the model generalize better to unseen inputs.  
* **Mixing Up Classes in Classification Examples:** When using few-shot prompting for classification tasks (where the model needs to categorize input into predefined classes), it's a best practice to mix up the order of the examples from different classes. This prevents the model from potentially overfitting to the specific sequence of examples and ensures it learns to identify the key features of each class independently, leading to more robust and generalizable performance on unseen data.  
* **Evolution to "Many-Shot" Learning:** As modern LLMs like Gemini get stronger with long context modeling, they are becoming highly effective at utilizing "many-shot" learning. This means optimal performance for complex tasks can now be achieved by including a much larger number of examples—sometimes even hundreds—directly within the prompt, allowing the model to learn more intricate patterns.  
* **Example:**  
  Classify the sentiment of the following movie reviews as POSITIVE, NEUTRAL, or NEGATIVE:

   Review: "The acting was superb and the story was engaging."  
   Sentiment: POSITIVE

   Review: "It was okay, nothing special."  
   Sentiment: NEUTRAL

   Review: "I found the plot confusing and the characters unlikable."  
   Sentiment: NEGATIVE

   Review: "The visuals were stunning, but the dialogue was weak."  
   Sentiment:

Understanding when to apply zero-shot, one-shot, and few-shot prompting techniques, and thoughtfully crafting and organizing examples, are essential for enhancing the effectiveness of agentic systems. These basic methods serve as the groundwork for various prompting strategies.

理解何时应用零样本、单样本和少样本提示技术，并精心设计和组织示例，对于提升 Agentic 系统的效能至关重要。这些基础方法为各种提示策略奠定了根基。

## Structuring Prompts

## 提示结构设计

Beyond the basic techniques of providing examples, the way you structure your prompt plays a critical role in guiding the language model. Structuring involves using different sections or elements within the prompt to provide distinct types of information, such as instructions, context, or examples, in a clear and organized manner. This helps the model parse the prompt correctly and understand the specific role of each piece of text.

除了提供示例的基础技术外，提示的结构化方式在引导语言模型方面起着关键作用。结构化涉及在提示中使用不同部分或元素，以清晰有序的方式提供指令、上下文或示例等不同类型的信息。这有助于模型正确解析提示，理解每段文本的特定角色。

## System Prompting

## 系统提示

System prompting sets the overall context and purpose for a language model, defining its intended behavior for an interaction or session. This involves providing instructions or background information that establish rules, a persona, or overall behavior. Unlike specific user queries, a system prompt provides foundational guidelines for the model's responses. It influences the model's tone, style, and general approach throughout the interaction. For example, a system prompt can instruct the model to consistently respond concisely and helpfully or ensure responses are appropriate for a general audience. System prompts are also utilized for safety and toxicity control by including guidelines such as maintaining respectful language.

系统提示为语言模型设定整体上下文和目的，定义其在交互或会话中的预期行为。这涉及提供建立规则、角色或整体行为的指令或背景信息。与具体的用户查询不同，系统提示为模型的响应提供基础指导。它影响模型在整个交互过程中的语气、风格和总体方法。例如，系统提示可指示模型始终保持简洁有益的响应，或确保输出适合普通受众。系统提示还用于安全和内容控制，包含保持尊重语言等指导原则。

Furthermore, to maximize their effectiveness, system prompts can undergo automatic prompt optimization through LLM-based iterative refinement. Services like the Vertex AI Prompt Optimizer facilitate this by systematically improving prompts based on user-defined metrics and target data, ensuring the highest possible performance for a given task.

此外，为最大化其效果，系统提示可通过基于 LLM 的迭代改进进行自动优化。Vertex AI Prompt Optimizer 等服务通过根据用户定义的指标和目标数据系统性地优化提示来促进这一过程，确保特定任务的最佳性能。

* **Example:**  
  You are a helpful and harmless AI assistant. Respond to all queries in a polite and informative manner. Do not generate content that is harmful, biased, or inappropriate

* **示例**：
  你是一个乐于助人且无害的 AI 助手。以礼貌且信息丰富的方式回应所有查询。不要生成有害、有偏见或不适当的内容。

## Role Prompting

## 角色提示

Role prompting assigns a specific character, persona, or identity to the language model, often in conjunction with system or contextual prompting. This involves instructing the model to adopt the knowledge, tone, and communication style associated with that role. For example, prompts such as "Act as a travel guide" or "You are an expert data analyst" guide the model to reflect the perspective and expertise of that assigned role. Defining a role provides a framework for the tone, style, and focused expertise, aiming to enhance the quality and relevance of the output. The desired style within the role can also be specified, for instance, "a humorous and inspirational style."

角色提示为语言模型分配特定角色、身份或专业背景，通常与系统或上下文提示结合使用。这涉及指示模型采用与该角色相关的知识、语气和沟通风格。例如，"扮演旅游指南"或"你是一位专业数据分析师"等提示引导模型体现所分配角色的视角和专长。定义角色为语气、风格和专业焦点提供框架，旨在提升输出的质量和相关性。还可指定角色内的期望风格，如"幽默且鼓舞人心的风格"。

* **Example:**  
  Act as a seasoned travel blogger. Write a short, engaging paragraph about the best hidden gem in Rome.

* **示例**：
  扮演一位经验丰富的旅行博主。写一段简短且引人入胜的文字，介绍罗马最佳隐藏景点。

## Using Delimiters

## 使用分隔符

Effective prompting involves clear distinction of instructions, context, examples, and input for language models. Delimiters, such as triple backticks (```), XML tags (<instruction>, <context>), or markers (---), can be utilized to visually and programmatically separate these sections. This practice, widely used in prompt engineering, minimizes misinterpretation by the model, ensuring clarity regarding the role of each part of the prompt.

有效的提示需要为语言模型清晰区分指令、上下文、示例和输入。可使用分隔符，如三重反引号（```）、XML 标签（<instruction>、<context>）或标记（---），在视觉和程序上分隔这些部分。这种在提示工程中广泛采用的做法，通过明确提示各部分的角色，最小化模型的误解。

* **Example:**  
  <instruction>Summarize the following article, focusing on the main arguments presented by the author.</instruction>  
  <article>  
  [Insert the full text of the article here]  
  </article>

* **示例**：
  <instruction>总结以下文章，重点关注作者提出的主要论点。</instruction>
  <article>
  [在此插入文章全文]
  </article>

## Contextual Engineering

## 上下文工程

Context engineering, unlike static system prompts, dynamically provides background information crucial for tasks and conversations. This ever-changing information helps models grasp nuances, recall past interactions, and integrate relevant details, leading to grounded responses and smoother exchanges. Examples include previous dialogue, relevant documents (as in Retrieval Augmented Generation), or specific operational parameters. For instance, when discussing a trip to Japan, one might ask for three family-friendly activities in Tokyo, leveraging the existing conversational context. In agentic systems, context engineering is fundamental to core agent behaviors like memory persistence, decision-making, and coordination across sub-tasks. Agents with dynamic contextual pipelines can sustain goals over time, adapt strategies, and collaborate seamlessly with other agents or tools—qualities essential for long-term autonomy. This methodology posits that the quality of a model's output depends more on the richness of the provided context than on the model's architecture. It signifies a significant evolution from traditional prompt engineering, which primarily focused on optimizing the phrasing of immediate user queries. Context engineering expands its scope to include multiple layers of information.

上下文工程与静态系统提示不同，它动态提供对任务和对话至关重要的背景信息。这种持续变化的信息帮助模型理解细微差别、回忆过往交互并整合相关细节，从而产生有根据的响应和更流畅的交流。示例包括先前对话、相关文档（如在检索增强生成中）或特定操作参数。例如，在讨论日本旅行时，可请求提供东京的三个适合家庭的活动，利用现有对话上下文。在 Agentic 系统中，上下文工程是核心智能体能力（如记忆持久性、决策制定和跨子任务协调）的基础。具备动态上下文管道的智能体能够维持目标、调整策略，并与其他智能体或人类协作——这些是实现长期自主性的关键特质。该方法论认为，模型输出的质量更多取决于所提供上下文的丰富度，而非模型架构本身。它标志着从传统提示工程的重大演进，传统提示工程主要聚焦于优化直接用户查询的措辞。上下文工程将其范畴扩展至包含多层信息。

These layers include:

这些层次包括：

* **System prompts:** Foundational instructions that define the AI's operational parameters (e.g., "You are a technical writer; your tone must be formal and precise").  
* **External data:**  
  * **Retrieved documents:** Information actively fetched from a knowledge base to inform responses (e.g., pulling technical specifications).  
  * **Tool outputs:** Results from the AI using an external API for real-time data (e.g., querying a calendar for availability).  
* **Implicit data:** Critical information such as user identity, interaction history, and environmental state. Incorporating implicit context presents challenges related to privacy and ethical data management. Therefore, robust governance is essential for context engineering, especially in sectors like enterprise, healthcare, and finance.

* **系统提示**：定义 AI 操作参数的基础指令（例如，"你是技术文档作者；语气必须正式且精确"）。
* **外部数据**：
  * **检索文档**：从知识库主动获取以支撑响应的信息（例如，提取技术规格）。
  * **工具输出**：AI 使用外部 API 获取实时数据的结果（例如，查询日历获取可用性）。
* **隐式数据**：关键信息，如用户身份、交互历史和环境状态。整合隐式上下文面临与隐私和道德数据管理相关的挑战。因此，强大的治理机制对上下文工程至关重要，尤其是在企业、医疗和金融等领域。

The core principle is that even advanced models underperform with a limited or poorly constructed view of their operational environment. This practice reframes the task from merely answering a question to building a comprehensive operational picture for the agent. For example, a context-engineered agent would integrate a user's calendar availability (tool output), the professional relationship with an email recipient (implicit data), and notes from previous meetings (retrieved documents) before responding to a query. This enables the model to generate highly relevant, personalized, and pragmatically useful outputs. The "engineering" aspect involves creating robust pipelines to fetch and transform this data at runtime and establishing feedback loops to continually improve context quality.

核心原则是，即使是先进模型，若对其操作环境的认知有限或构建不当，表现也会欠佳。这种做法将任务从单纯回答问题重新定义为为智能体构建全面的操作图景。例如，一个经过上下文工程设计的智能体在回复用户查询前，会整合用户的日历可用性（工具输出）、与邮件收件人的专业关系（隐式数据）以及过往会议记录（检索文档）。这使得模型能够生成高度相关、个性化且实用的输出。"工程"方面涉及构建稳健的管道以在运行时获取和转换这些数据，并建立反馈循环以持续提升上下文质量。

To implement this, specialized tuning systems, such as Google's Vertex AI prompt optimizer, can automate the improvement process at scale. By systematically evaluating responses against sample inputs and predefined metrics, these tools can enhance model performance and adapt prompts and system instructions across different models without extensive manual rewriting. Providing an optimizer with sample prompts, system instructions, and a template allows it to programmatically refine contextual inputs, offering a structured method for implementing the necessary feedback loops for sophisticated Context Engineering.  
This structured approach differentiates a rudimentary AI tool from a more sophisticated, contextually-aware system. It treats context as a primary component, emphasizing what the agent knows, when it knows it, and how it uses that information. This practice ensures the model has a well-rounded understanding of the user's intent, history, and current environment. Ultimately, Context Engineering is a crucial methodology for transforming stateless chatbots into highly capable, situationally-aware systems.

为实现这一点，专门的调优系统（如 Google 的 Vertex AI prompt optimizer）可大规模自动化改进过程。通过基于样本输入和预定义指标系统评估响应，这些工具能提升模型性能，并在不同模型间调整提示和系统指令，无需大量手动重写。为优化器提供样本提示、系统指令和模板，使其能程序化地优化上下文输入，为实施复杂上下文工程所需的反馈循环提供结构化方法。

这种结构化方法将基础 AI 工具与更复杂的情境感知系统区分开来。它将上下文视为核心要素，强调智能体知晓什么、何时知晓以及如何运用这些信息。这种做法确保模型对用户的意图、历史和当前环境有全面理解。最终，上下文工程是将无状态聊天机器人转变为高能力情境感知系统的关键方法论。

## Structured Output

## 结构化输出

Often, the goal of prompting is not just to get a free-form text response, but to extract or generate information in a specific, machine-readable format. Requesting structured output, such as JSON, XML, CSV, or Markdown tables, is a crucial structuring technique. By explicitly asking for the output in a particular format and potentially providing a schema or example of the desired structure, you guide the model to organize its response in a way that can be easily parsed and used by other parts of your agentic system or application. Returning JSON objects for data extraction is beneficial as it forces the model to create a structure and can limit hallucinations. Experimenting with output formats is recommended, especially for non-creative tasks like extracting or categorizing data.

通常，提示的目标不仅是获得自由形式的文本响应，而是以特定机器可读格式提取或生成信息。请求结构化输出（如 JSON、XML、CSV 或 Markdown 表格）是一项关键的结构化技术。通过明确要求特定格式输出并可能提供期望结构的模式或示例，您可以引导模型以易于被 Agentic 系统或其他应用组件解析和使用的方式组织响应。返回 JSON 对象进行数据提取的优势在于强制模型创建结构，从而限制幻觉产生。建议尝试不同输出格式，特别是对于数据提取或分类等非创意任务。

* **Example:**  
  Extract the following information from the text below and return it as a JSON object with keys "name", "address", and "phone_number".

  Text: "Contact John Smith at 123 Main St, Anytown, CA or call (555) 123-4567."

* **示例**：
  从以下文本中提取信息，并以包含 "name"、"address" 和 "phone_number" 键的 JSON 对象形式返回。

  文本："联系 John Smith，地址：123 Main St, Anytown, CA，或致电 (555) 123-4567。"

Effectively utilizing system prompts, role assignments, contextual information, delimiters, and structured output significantly enhances the clarity, control, and utility of interactions with language models, providing a strong foundation for developing reliable agentic systems. Requesting structured output is crucial for creating pipelines where the language model's output serves as the input for subsequent system or processing steps.

有效利用系统提示、角色分配、上下文信息、分隔符和结构化输出，显著提升了与语言模型交互的清晰度、控制力和实用性，为构建可靠的 Agentic 系统奠定了坚实基础。请求结构化输出对于创建管道至关重要，其中语言模型的输出将作为后续系统或处理步骤的输入。

**Leveraging Pydantic for an Object-Oriented Facade:** A powerful technique for enforcing structured output and enhancing interoperability is to use the LLM's generated data to populate instances of Pydantic objects. Pydantic is a Python library for data validation and settings management using Python type annotations. By defining a Pydantic model, you create a clear and enforceable schema for your desired data structure. This approach effectively provides an object-oriented facade to the prompt's output, transforming raw text or semi-structured data into validated, type-hinted Python objects.

**利用 Pydantic 实现面向对象封装**：强制执行结构化输出和增强互操作性的强大技术是使用 LLM 生成的数据填充 Pydantic 对象实例。Pydantic 是一个使用 Python 类型注解进行数据验证和设置管理的 Python 库。通过定义 Pydantic 模型，您可以为期望的数据结构创建清晰且可强制执行的模式。这种方法有效地为提示输出提供了面向对象的封装，将原始文本或半结构化数据转换为经过验证的、类型提示的 Python 对象。

You can directly parse a JSON string from an LLM into a Pydantic object using the model_validate_json method. This is particularly useful as it combines parsing and validation in a single step.

您可以使用 model_validate_json 方法直接将来自 LLM 的 JSON 字符串解析为 Pydantic 对象。这特别高效，因为它在一个步骤中同时完成解析和验证。

```python
from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import List, Optional
from datetime import date

# --- Pydantic Model Definition (from above) ---
class User(BaseModel):
    name: str = Field(..., description="The full name of the user.")
    email: EmailStr = Field(..., description="The user's email address.")
    date_of_birth: Optional[date] = Field(None, description="The user's date of birth.")
    interests: List[str] = Field(default_factory=list, description="A list of the user's interests.")

# --- Hypothetical LLM Output ---
llm_output_json = """
{
    "name": "Alice Wonderland",
    "email": "alice.w@example.com",
    "date_of_birth": "1995-07-21",
    "interests": [
        "Natural Language Processing",
        "Python Programming",
        "Gardening"
    ]
}
"""

# --- Parsing and Validation ---
try:
    # Use the model_validate_json class method to parse the JSON string.
    # This single step parses the JSON and validates the data against the User model.
    user_object = User.model_validate_json(llm_output_json)
    # Now you can work with a clean, type-safe Python object.
    print("Successfully created User object!")
    print(f"Name: {user_object.name}")
    print(f"Email: {user_object.email}")
    print(f"Date of Birth: {user_object.date_of_birth}")
    print(f"First Interest: {user_object.interests[0]}")
    # You can access the data like any other Python object attribute.
    # Pydantic has already converted the 'date_of_birth' string to a datetime.date object.
    print(f"Type of date_of_birth: {type(user_object.date_of_birth)}")
except ValidationError as e:
    # If the JSON is malformed or the data doesn't match the model's types,
    # Pydantic will raise a ValidationError.
    print("Failed to validate JSON from LLM.")
    print(e)
```

This Python code demonstrates how to use the Pydantic library to define a data model and validate JSON data. It defines a User model with fields for name, email, date of birth, and interests, including type hints and descriptions. The code then parses a hypothetical JSON output from a Large Language Model (LLM) using the model_validate_json method of the User model. This method handles both JSON parsing and data validation according to the model's structure and types. Finally, the code accesses the validated data from the resulting Python object and includes error handling for ValidationError in case the JSON is invalid.

这段 Python 代码演示了如何使用 Pydantic 库定义数据模型并验证 JSON 数据。它定义了一个包含姓名、电子邮件、出生日期和兴趣字段的 User 模型，附带类型提示和描述。代码随后使用 User 模型的 model_validate_json 方法解析来自大型语言模型（LLM）的假设 JSON 输出。该方法根据模型结构和类型要求处理 JSON 解析和数据验证。最后，代码从生成的 Python 对象中访问已验证数据，并包含 ValidationError 的异常处理，以应对 JSON 无效的情况。

For XML data, the xmltodict library can be used to convert the XML into a dictionary, which can then be passed to a Pydantic model for parsing. By using Field aliases in your Pydantic model, you can seamlessly map the often verbose or attribute-heavy structure of XML to your object's fields.

对于 XML 数据，可使用 xmltodict 库将 XML 转换为字典，然后传递给 Pydantic 模型进行解析。通过在 Pydantic 模型中使用 Field 别名，可以无缝地将通常冗长或属性密集的 XML 结构映射到对象的字段。

This methodology is invaluable for ensuring the interoperability of LLM-based components with other parts of a larger system. When an LLM's output is encapsulated within a Pydantic object, it can be reliably passed to other functions, APIs, or data processing pipelines with the assurance that the data conforms to the expected structure and types. This practice of "parse, don't validate" at the boundaries of your system components leads to more robust and maintainable applications.

## Reasoning and Thought Process Techniques

## 推理与思维过程技术

Large language models excel at pattern recognition and text generation but often face challenges with tasks requiring complex, multi-step reasoning. This appendix focuses on techniques designed to enhance these reasoning capabilities by encouraging models to reveal their internal thought processes. Specifically, it addresses methods to improve logical deduction, mathematical computation, and planning.

大型语言模型擅长模式识别和文本生成，但在需要复杂多步骤推理的任务中常常面临挑战。本附录重点介绍旨在通过鼓励模型揭示其内部思维过程来增强推理能力的技术。具体而言，它探讨了改进逻辑推演、数学计算和规划的方法。

## Chain of Thought (CoT)

## 思维链（Chain of Thought, CoT）

The Chain of Thought (CoT) prompting technique is a powerful method for improving the reasoning abilities of language models by explicitly prompting the model to generate intermediate reasoning steps before arriving at a final answer. Instead of just asking for the result, you instruct the model to "think step by step." This process mirrors how a human might break down a problem into smaller, more manageable parts and work through them sequentially.

思维链（CoT）提示技术是一种强大方法，通过明确提示模型在得出最终答案前生成中间推理步骤来提高语言模型的推理能力。您不仅是要求结果，而是指示模型"逐步思考"。这一过程模拟了人类如何将问题分解为更小、更易管理的部分并按顺序处理。

CoT helps the LLM generate more accurate answers, particularly for tasks that require some form of calculation or logical deduction, where models might otherwise struggle and produce incorrect results. By generating these intermediate steps, the model is more likely to stay on track and perform the necessary operations correctly.

CoT 帮助 LLM 生成更准确的答案，特别是对于需要计算或逻辑推演的任务，这些任务中模型可能因直接得出结果而产生错误。通过生成中间步骤，模型更有可能保持正确方向并准确执行必要操作。

There are two main variations of CoT:

CoT 有两个主要变体：

* **Zero-Shot CoT:** This involves simply adding the phrase "Let's think step by step" (or similar phrasing) to your prompt without providing any examples of the reasoning process. Surprisingly, for many tasks, this simple addition can significantly improve the model's performance by triggering its ability to expose its internal reasoning trace.  
  * **Example (Zero-Shot CoT):**  
    If a train travels at 60 miles per hour and covers a distance of 240 miles, how long did the journey take? Let's think step by step.

* **零样本思维链（Zero-Shot CoT）**：这涉及简单地在提示中添加"让我们逐步思考"（或类似措辞）的短语，不提供任何推理过程示例。令人惊讶的是，对于许多任务，这一简单添加能通过触发模型暴露内部推理轨迹的能力，显著提升其性能。
  * **示例（Zero-Shot CoT）**：
    如果火车以每小时 60 英里的速度行驶，覆盖 240 英里的距离，旅程耗时多久？让我们逐步思考。

* **Few-Shot CoT:** This combines CoT with few-shot prompting. You provide the model with several examples where both the input, the step-by-step reasoning process, and the final output are shown. This gives the model a clearer template for how to perform the reasoning and structure its response, often leading to even better results on more complex tasks compared to zero-shot CoT.  
  * **Example (Few-Shot CoT):**  
    Q: The sum of three consecutive integers is 36. What are the integers?  
    A: Let the first integer be x. The next consecutive integer is x+1, and the third is x+2. The sum is x + (x+1) + (x+2) = 3x + 3. We know the sum is 36, so 3x + 3 = 36. Subtract 3 from both sides: 3x = 33. Divide by 3: x = 11. The integers are 11, 11+1=12, and 11+2=13. The integers are 11, 12, and 13.

    Q: Sarah has 5 apples, and she buys 8 more. She eats 3 apples. How many apples does she have left? Let's think step by step.  
    A: Let's think step by step. Sarah starts with 5 apples. She buys 8 more, so she adds 8 to her initial amount: 5 + 8 = 13 apples. Then, she eats 3 apples, so we subtract 3 from the total: 13 - 3 = 10. Sarah has 10 apples left. The answer is 10.

* **少样本思维链（Few-Shot CoT）**：这结合了 CoT 与少样本提示。您向模型提供多个示例，展示输入、逐步推理过程和最终输出。这为模型提供了更清晰的模板，指导其如何执行推理和构建响应，通常在复杂任务上比零样本 CoT 产生更好结果。
  * **示例（Few-Shot CoT）**：
    问：三个连续整数的和是 36。这些整数是什么？
    答：设第一个整数为 x。下一个连续整数是 x+1，第三个是 x+2。和为 x + (x+1) + (x+2) = 3x + 3。已知和为 36，所以 3x + 3 = 36。两边减去 3：3x = 33。除以 3：x = 11。这些整数是 11、11+1=12 和 11+2=13。这些整数是 11、12 和 13。

    问：Sarah 有 5 个苹果，她又买了 8 个。她吃了 3 个苹果。她还剩多少苹果？让我们逐步思考。
    答：让我们逐步思考。Sarah 开始有 5 个苹果。她买了 8 个，所以她在初始数量上加 8：5 + 8 = 13 个苹果。然后，她吃了 3 个苹果，所以从总数中减去 3：13 - 3 = 10。Sarah 还剩 10 个苹果。答案是 10。

CoT offers several advantages. It is relatively low-effort to implement and can be highly effective with off-the-shelf LLMs without requiring fine-tuning. A significant benefit is the increased interpretability of the model's output; you can see the reasoning steps it followed, which helps in understanding why it arrived at a particular answer and in debugging if something went wrong. Additionally, CoT appears to improve the robustness of prompts across different versions of language models, meaning the performance is less likely to degrade when a model is updated. The main disadvantage is that generating the reasoning steps increases the length of the output, leading to higher token usage, which can increase costs and response time.

CoT 具有多个优势。它相对易于实施，且能在现成 LLM 上高效运行，无需微调。一个重要好处是模型输出的可解释性增强；您可以观察其遵循的推理步骤，这有助于理解其得出特定答案的原因，并在出现问题时进行调试。此外，CoT 似乎提升了提示在不同版本语言模型间的鲁棒性，意味着模型更新时性能不易下降。主要缺点是生成推理步骤会增加输出长度，导致更高的 token 使用量，可能增加成本和响应时间。

Best practices for CoT include ensuring the final answer is presented *after* the reasoning steps, as the generation of the reasoning influences the subsequent token predictions for the answer. Also, for tasks with a single correct answer (like mathematical problems), setting the model's temperature to 0 (greedy decoding) is recommended when using CoT to ensure deterministic selection of the most probable next token at each step.

CoT 的最佳实践包括确保最终答案在推理步骤*之后*呈现，因为推理生成会影响后续答案 token 的预测。此外，对于具有单一正确答案的任务（如数学问题），建议在使用 CoT 时将模型温度设置为 0（贪婪解码），以确保在每一步确定性地选择最可能的下一个 token。

## Self-Consistency

## 自洽性（Self-Consistency）

Building on the idea of Chain of Thought, the Self-Consistency technique aims to improve the reliability of reasoning by leveraging the probabilistic nature of language models. Instead of relying on a single greedy reasoning path (as in basic CoT), Self-Consistency generates multiple diverse reasoning paths for the same problem and then selects the most consistent answer among them.

基于思维链理念，自我一致性技术旨在通过利用语言模型的概率性质来提高推理可靠性。自我一致性不依赖单一贪婪推理路径（如基本 CoT），而是为同一问题生成多个不同推理路径，然后从中选择最一致的答案。

Self-Consistency involves three main steps:

自我一致性包含三个主要步骤：

1. **Generating Diverse Reasoning Paths:** The same prompt (often a CoT prompt) is sent to the LLM multiple times. By using a higher temperature setting, the model is encouraged to explore different reasoning approaches and generate varied step-by-step explanations.  
2. **Extract the Answer:** The final answer is extracted from each of the generated reasoning paths.  
3. **Choose the Most Common Answer:** A majority vote is performed on the extracted answers. The answer that appears most frequently across the diverse reasoning paths is selected as the final, most consistent answer.

1. **生成多样化推理路径**：将同一提示（通常是 CoT 提示）多次发送给 LLM。通过使用更高温度设置，鼓励模型探索不同推理方法并生成多样化逐步解释。
2. **提取答案**：从每个生成的推理路径中提取最终答案。
3. **选择最常出现的答案**：对提取的答案进行多数投票。在不同推理路径中出现最频繁的答案被选为最终、最一致的答案。

This approach improves the accuracy and coherence of responses, particularly for tasks where multiple valid reasoning paths might exist or where the model might be prone to errors in a single attempt. The benefit is a pseudo-probability likelihood of the answer being correct, increasing overall accuracy. However, the significant cost is the need to run the model multiple times for the same query, leading to much higher computation and expense.

这种方法提高了响应的准确性和连贯性，特别适用于可能存在多个有效推理路径或模型单次尝试易出错的任务。优势在于获得答案正确的伪概率可能性，从而提升整体准确性。然而，显著代价是需要为同一查询多次运行模型，导致计算成本和费用大幅增加。

* **Example (Conceptual):**  
  * *Prompt:* "Is the statement 'All birds can fly' true or false? Explain your reasoning."  
  * *Model Run 1 (High Temp):* Reasons about most birds flying, concludes True.  
  * *Model Run 2 (High Temp):* Reasons about penguins and ostriches, concludes False.  
  * *Model Run 3 (High Temp):* Reasons about birds *in general*, mentions exceptions briefly, concludes True.  
  * *Self-Consistency Result:* Based on majority vote (True appears twice), the final answer is "True". (Note: A more sophisticated approach would weigh the reasoning quality).

* **示例（概念性）**：
  * *提示*："陈述'所有鸟类都能飞'是真还是假？解释你的推理。"
  * *模型运行 1（高温度）*：推理大多数鸟类会飞，结论为真。
  * *模型运行 2（高温度）*：考虑企鹅和鸵鸟等例外，结论为假。
  * *模型运行 3（高温度）*：讨论鸟类*一般*特性，简要提及例外，结论为真。
  * *自我一致性结果*：基于多数投票（真出现两次），最终答案为"真"。（注：更复杂的方法会权衡推理质量）。

## Step-Back Prompting

## 后退提示

Step-back prompting enhances reasoning by first asking the language model to consider a general principle or concept related to the task before addressing specific details. The response to this broader question is then used as context for solving the original problem.

后退提示通过首先要求语言模型考虑与任务相关的一般原则或概念来增强推理，然后再处理具体细节。对这一更广泛问题的响应随后用作解决原始问题的上下文。

This process allows the language model to activate relevant background knowledge and wider reasoning strategies. By focusing on underlying principles or higher-level abstractions, the model can generate more accurate and insightful answers, less influenced by superficial elements. Initially considering general factors can provide a stronger basis for generating specific creative outputs. Step-back prompting encourages critical thinking and the application of knowledge, potentially mitigating biases by emphasizing general principles.

此过程允许语言模型激活相关背景知识和更广泛的推理策略。通过关注基本原则或更高层次抽象，模型能生成更准确和富有洞察力的答案，减少受表面元素影响。初始考虑一般因素可为生成特定创意输出提供更强基础。后退提示鼓励批判性思维和知识应用，通过强调一般原则可能减轻偏见。

* **Example:**  
  * *Prompt 1 (Step-Back):* "What are the key factors that make a good detective story?"  
  * *Model Response 1:* (Lists elements like red herrings, compelling motive, flawed protagonist, logical clues, satisfying resolution).  
  * *Prompt 2 (Original Task + Step-Back Context):* "Using the key factors of a good detective story [insert Model Response 1 here], write a short plot summary for a new mystery novel set in a small town."

* **示例**：
  * *提示 1（后退）*："优秀侦探故事的关键要素是什么？"
  * *模型响应 1*：（列出如红鲱鱼、令人信服的动机、有缺陷的主角、逻辑线索、令人满意的结局等要素）。
  * *提示 2（原始任务 + 后退上下文）*："运用优秀侦探故事的关键要素[在此插入模型响应 1]，为一部设定在小镇的新神秘小说撰写简短情节摘要。"

## Tree of Thoughts (ToT)

## 思维树（Tree of Thoughts, ToT）

Tree of Thoughts (ToT) is an advanced reasoning technique that extends the Chain of Thought method. It enables a language model to explore multiple reasoning paths concurrently, instead of following a single linear progression. This technique utilizes a tree structure, where each node represents a "thought"—a coherent language sequence acting as an intermediate step. From each node, the model can branch out, exploring alternative reasoning routes.

思维树（ToT）是一种高级推理技术，扩展了思维链方法。它使语言模型能够同时探索多个推理路径，而非遵循单一线性进程。此技术采用树状结构，其中每个节点代表一个"思维"——作为中间步骤的连贯语言序列。从每个节点，模型可分支探索替代推理路线。

ToT is particularly suited for complex problems that require exploration, backtracking, or the evaluation of multiple possibilities before arriving at a solution. While more computationally demanding and intricate to implement than the linear Chain of Thought method, ToT can achieve superior results on tasks necessitating deliberate and exploratory problem-solving. It allows an agent to consider diverse perspectives and potentially recover from initial errors by investigating alternative branches within the "thought tree."

ToT 特别适合需要探索、回溯或在得出解决方案前评估多种可能性的复杂问题。虽然比线性思维链方法计算要求更高且实现更复杂，但 ToT 能在需要深思熟虑和探索性问题解决的任务上取得更优结果。它允许智能体探索不同视角，并通过调查"思维树"中的替代分支从初始错误中恢复。

* **Example (Conceptual):** For a complex creative writing task like "Develop three different possible endings for a story based on these plot points," ToT would allow the model to explore distinct narrative branches from a key turning point, rather than just generating one linear continuation.

* **示例（概念性）**：对于像"基于这些情节点为故事构思三种不同可能结局"的复杂创意写作任务，ToT 将允许模型从关键转折点探索不同叙事分支，而非仅生成单一线性延续。

These reasoning and thought process techniques are crucial for building agents capable of handling tasks that go beyond simple information retrieval or text generation. By prompting models to expose their reasoning, consider multiple perspectives, or step back to general principles, we can significantly enhance their ability to perform complex cognitive tasks within agentic systems.

这些推理和思维过程技术对于构建能处理超越简单信息检索或文本生成任务的智能体至关重要。通过提示模型暴露推理、考虑多视角或后退至一般原则，我们能显著增强其在 Agentic 系统中执行复杂认知任务的能力。

## Action and Interaction Techniques

## 行动与交互技术

Intelligent agents possess the capability to actively engage with their environment, beyond generating text. This includes utilizing tools, executing external functions, and participating in iterative cycles of observation, reasoning, and action. This section examines prompting techniques designed to enable these active behaviors.

智能体具备主动与环境交互的能力，这超越了单纯的文本生成。这包括利用工具、执行外部函数以及参与观察、推理和行动的迭代循环。本节探讨旨在实现这些主动行为的提示技术。

## Tool Use / Function Calling

## 工具使用/工具调用

A crucial ability for an agent is using external tools or calling functions to perform actions beyond its internal capabilities. These actions may include web searches, database access, sending emails, performing calculations, or interacting with external APIs. Effective prompting for tool use involves designing prompts that instruct the model on the appropriate timing and methodology for tool utilization.

Agent 的关键能力之一是使用外部工具或调用函数来执行超出其内部能力范围的操作。这些操作可能包括网络搜索、数据库访问、发送电子邮件、执行计算或与外部 API 交互。有效的工具使用提示涉及设计能够指示模型在适当时机和方法下利用工具的指令。

Modern language models often undergo fine-tuning for "function calling" or "tool use." This enables them to interpret descriptions of available tools, including their purpose and parameters. Upon receiving a user request, the model can determine the necessity of tool use, identify the appropriate tool, and format the required arguments for its invocation. The model does not execute the tool directly. Instead, it generates a structured output, typically in JSON format, specifying the tool and its parameters. An agentic system then processes this output, executes the tool, and provides the tool's result back to the model, integrating it into the ongoing interaction.

现代语言模型通常经过"工具调用"或"工具使用"的专门微调。这使得它们能够理解可用工具的描述，包括其用途和参数。在接收到用户请求后，模型可以判断是否需要使用工具，识别合适的工具，并格式化调用所需的参数。模型本身并不直接执行工具，而是生成结构化输出（通常为 JSON 格式），指定要使用的工具及其参数。随后，Agentic 系统处理此输出，执行工具，并将工具结果返回给模型，将其整合到持续交互中。

* **Example:**  
  You have access to a weather tool that can get the current weather for a specified city. The tool is called 'get_current_weather' and takes a 'city' parameter (string).

  User: What's the weather like in London right now?

  * *Expected Model Output (Function Call):*  
    {  
      "tool_code": "get_current_weather",  
      "tool_name": "get_current_weather",  
      "parameters": {  
        "city": "London"  
      }  
    }

* **示例**：
  你可以访问一个天气工具，该工具可以获取指定城市的当前天气。该工具名为 'get_current_weather'，接受一个 'city' 参数（字符串类型）。

  用户：伦敦现在的天气怎么样？

  * *预期模型输出（工具调用）*：
    {
      "tool_code": "get_current_weather",
      "tool_name": "get_current_weather",
      "parameters": {
        "city": "London"
      }
    }

## ReAct (Reason & Act)

## ReAct（推理与行动）

ReAct, short for Reason and Act, is a prompting paradigm that combines Chain of Thought-style reasoning with the ability to perform actions using tools in an interleaved manner. ReAct mimics how humans operate – we reason verbally and take actions to gather more information or make progress towards a goal.

ReAct 是"推理与行动"的缩写，是一种将思维链风格推理与使用工具执行操作交织结合的提示范式。ReAct 模拟人类的工作方式——我们通过口头推理并采取行动来收集更多信息或推进目标实现。

The ReAct pattern involves a loop:

ReAct 模式包含一个循环过程：

1. **Thought:** The model generates a thought process, explaining its current understanding and plan.  
2. **Action:** Based on the thought, the model decides to perform an action, often using a tool (e.g., Search, Calculator, API call). It outputs the name of the tool and the required input.  
3. **Observation:** The agentic system executes the tool and provides the result (Observation) back to the model.  
4. The loop continues with the model generating a new "Thought" based on the latest "Observation," leading to further "Actions" and "Observations" until the task is complete and the model outputs a "Final Answer."

1. **思考**：模型生成思维过程，阐述其当前理解和计划。
2. **行动**：基于思考，模型决定执行操作，通常涉及使用工具（如搜索、计算器、API 调用）。它输出工具名称和所需输入。
3. **观察**：Agentic 系统执行工具并将结果（观察）反馈给模型。
4. 循环继续，模型基于最新"观察"生成新的"思考"，引发进一步的"行动"和"观察"，直至任务完成，模型输出"最终答案"。

This interleaved process of thinking and acting allows the agent to dynamically gather information, react to tool outputs, and refine its approach, making it particularly effective for tasks requiring interaction with dynamic environments or external knowledge sources.

这种思考与行动的交错过程使智能体动态收集信息、响应工具输出并优化策略，特别适用于需要与动态环境或外部知识源交互的任务。

* **Example (Illustrative ReAct Trace):**  
  User: What is the capital of France and its current population?

  Thought: The user is asking for two pieces of information: the capital of France and its population. I can use a search tool to find this information. I will start by confirming the capital, although I am likely to know it.  
  Action: Search({"query": "capital of France"})  
  Observation: Paris

  Thought: Okay, the capital is Paris. Now I need to find the population of Paris.  
  Action: Search({"query": "current population of Paris"})  
  Observation: The population of Paris was estimated to be around 2.1 million people in 2023.

  Thought: I have found both pieces of information. I can now provide the final answer to the user.  
  Final Answer: The capital of France is Paris, and its estimated population in 2023 was around 2.1 million people.

* **示例（说明性 ReAct 轨迹）**：
  用户：法国的首都是什么？当前人口是多少？

  思考：用户询问两个信息：法国首都及其人口。我可以使用搜索工具查找这些信息。我将从确认首都开始，尽管我可能已经知道。
  行动：Search({"query": "capital of France"})
  观察：巴黎

  思考：好的，首都是巴黎。现在我需要查找巴黎的人口。
  行动：Search({"query": "current population of Paris"})
  观察：巴黎人口在 2023 年估计约为 210 万人。

  思考：我已找到两条信息。现在可以向用户提供最终答案。
  最终答案：法国的首都是巴黎，其 2023 年估计人口约为 210 万人。

These techniques are vital for building agents that can actively engage with the world, retrieve real-time information, and perform tasks that require interacting with external systems.

这些技术对于构建能够主动与世界互动、检索实时信息并执行需要与外部系统交互任务的智能体至关重要。

## Advanced Techniques

## 高级技术

Beyond the foundational, structural, and reasoning patterns, there are several other prompting techniques that can further enhance the capabilities and efficiency of agentic systems. These range from using AI to optimize prompts to incorporating external knowledge and tailoring responses based on user characteristics.

除了基础、结构和推理模式外，还有多种其他提示技术可以进一步提升 Agentic 系统的能力和效率。这些技术涵盖从使用 AI 优化提示到整合外部知识和基于用户特征定制响应等多个方面。

## Automatic Prompt Engineering (APE)

## 自动提示工程（APE）

Recognizing that crafting effective prompts can be a complex and iterative process, Automatic Prompt Engineering (APE) explores using language models themselves to generate, evaluate, and refine prompts. This method aims to automate the prompt writing process, potentially enhancing model performance without requiring extensive human effort in prompt design.

认识到制作有效提示可能是一个复杂且迭代的过程，自动提示工程（APE）探索使用语言模型本身来生成、评估和改进提示。这种方法旨在自动化提示编写过程，有可能在无需大量人工设计投入的情况下提升模型性能。

The general idea is to have a "meta-model" or a process that takes a task description and generates multiple candidate prompts. These prompts are then evaluated based on the quality of the output they produce on a given set of inputs (perhaps using metrics like BLEU or ROUGE, or human evaluation). The best-performing prompts can be selected, potentially refined further, and used for the target task. Using an LLM to generate variations of a user query for training a chatbot is an example of this.

基本思路是构建一个"元模型"或流程，该流程接收任务描述并生成多个候选提示。然后根据这些提示在给定输入集上产生的输出质量进行评估（可能使用 BLEU 或 ROUGE 等指标，或人工评估）。表现最佳的提示可以被选择，进一步优化后用于目标任务。使用 LLM 生成用户查询变体以训练聊天机器人就是此类应用的一个实例。

* **Example (Conceptual):** A developer provides a description: "I need a prompt that can extract the date and sender from an email." An APE system generates several candidate prompts. These are tested on sample emails, and the prompt that consistently extracts the correct information is selected.

* **示例（概念性）**：开发者提供描述："我需要一个能从电子邮件中提取日期和发件人的提示。"APE 系统生成若干候选提示。这些提示在样本电子邮件上测试，最终选择能稳定提取正确信息的提示。

Of course. Here is a rephrased and slightly expanded explanation of programmatic prompt optimization using frameworks like DSPy:

当然。以下是使用 DSPy 等框架进行程序化提示优化的重新表述和适度扩展说明：

Another powerful prompt optimization technique, notably promoted by the DSPy framework, involves treating prompts not as static text but as programmatic modules that can be automatically optimized. This approach moves beyond manual trial-and-error and into a more systematic, data-driven methodology.

另一种强大的提示优化技术，尤其以 DSPy 框架为代表，将提示视为可自动优化的程序化模块，而非静态文本。这种方法超越了手动试错，进入了更系统化、数据驱动的方法论范畴。

The core of this technique relies on two key components:

该技术的核心依赖于两个关键组件：

1. **A Goldset (or High-Quality Dataset):** This is a representative set of high-quality input-and-output pairs. It serves as the "ground truth" that defines what a successful response looks like for a given task.  
2. **An Objective Function (or Scoring Metric):** This is a function that automatically evaluates the LLM's output against the corresponding "golden" output from the dataset. It returns a score indicating the quality, accuracy, or correctness of the response.

1. **金标准集（或高质量数据集）**：这是一组具有代表性的高质量输入-输出对。它作为"真实基准"，定义了特定任务下成功响应应具备的特征。
2. **目标函数（或评分指标）**：这是一个自动评估 LLM 输出与数据集中对应"黄金"输出的函数。它返回一个分数，指示响应的质量、准确性或正确性。

Using these components, an optimizer, such as a Bayesian optimizer, systematically refines the prompt. This process typically involves two main strategies, which can be used independently or in concert:

利用这些组件，优化器（如贝叶斯优化器）系统性地改进提示。此过程通常涉及两种主要策略，可独立或协同使用：

* **Few-Shot Example Optimization:** Instead of a developer manually selecting examples for a few-shot prompt, the optimizer programmatically samples different combinations of examples from the goldset. It then tests these combinations to identify the specific set of examples that most effectively guides the model toward generating the desired outputs.

* **Few-Shot 示例优化**：优化器并非由开发者手动选择 few-shot 提示的示例，而是从金标准集中程序化地采样不同示例组合。随后测试这些组合，以识别最能有效引导模型生成期望输出的特定示例集合。

* **Instructional Prompt Optimization:** In this approach, the optimizer automatically refines the prompt's core instructions. It uses an LLM as a "meta-model" to iteratively mutate and rephrase the prompt's text—adjusting wording, tone, or structure—to discover which phrasing yields the highest scores from the objective function.

* **指令提示优化**：在此方法中，优化器自动优化提示的核心指令。它使用 LLM 作为"元模型"迭代地变异和重新表述提示文本——调整措辞、语气或结构——以发现能获得目标函数最高评分的表述方式。

The ultimate goal for both strategies is to maximize the scores from the objective function, effectively "training" the prompt to produce results that are consistently closer to the high-quality goldset. By combining these two approaches, the system can simultaneously optimize *what instructions* to give the model and *which examples* to show it, leading to a highly effective and robust prompt that is machine-optimized for the specific task.

两种策略的最终目标都是最大化目标函数的分数，实质上"训练"提示以产生与高质量金标准集持续接近的结果。通过结合这两种方法，系统能同时优化*给予模型的指令*和*展示给模型的示例*，从而获得为特定任务机器优化的高效且强大的提示。

## Iterative Prompting / Refinement

## 迭代提示/改进

This technique involves starting with a simple, basic prompt and then iteratively refining it based on the model's initial responses. If the model's output isn't quite right, you analyze the shortcomings and modify the prompt to address them. This is less about an automated process (like APE) and more about a human-driven iterative design loop.

此技术涉及从简单的基础提示开始，然后根据模型的初始响应迭代改进。如果模型输出不理想，您分析不足之处并修改提示以解决问题。这更侧重于人工驱动的迭代设计循环，而非自动化过程（如 APE）。

* **Example:**  
  * *Attempt 1:* "Write a product description for a new type of coffee maker." (Result is too generic).  
  * *Attempt 2:* "Write a product description for a new type of coffee maker. Highlight its speed and ease of cleaning." (Result is better, but lacks detail).  
  * *Attempt 3:* "Write a product description for the 'SpeedClean Coffee Pro'. Emphasize its ability to brew a pot in under 2 minutes and its self-cleaning cycle. Target busy professionals." (Result is much closer to desired).

* **示例**：
  * *尝试 1*："为新型咖啡机撰写产品描述。"（结果过于泛泛）。
  * *尝试 2*："为新型咖啡机撰写产品描述。突出其速度和清洁便利性。"（结果改善，但缺乏细节）。
  * *尝试 3*："为'SpeedClean Coffee Pro'撰写产品描述。强调其在 2 分钟内冲泡一壶咖啡的能力及自清洁循环。目标受众为忙碌的专业人士。"（结果更接近期望）。

## Providing Negative Examples

## 提供负面示例

While the principle of "Instructions over Constraints" generally holds true, there are situations where providing negative examples can be helpful, albeit used carefully. A negative example shows the model an input and an *undesired* output, or an input and an output that *should not* be generated. This can help clarify boundaries or prevent specific types of incorrect responses.

尽管"指令优于约束"的原则普遍适用，但在某些情况下谨慎使用负面示例可能有所帮助。负面示例向模型展示输入与*不期望的*输出，或输入与*不应*生成的输出。这有助于明确边界或防止特定类型的错误响应。

* **Example:**  
  Generate a list of popular tourist attractions in Paris. Do NOT include the Eiffel Tower.

  Example of what NOT to do:  
  Input: List popular landmarks in Paris.  
  Output: The Eiffel Tower, The Louvre, Notre Dame Cathedral.

* **示例**：
  生成巴黎热门旅游景点列表。不要包含埃菲尔铁塔。

  不应采取的做法示例：
  输入：列出巴黎著名地标。
  输出：埃菲尔铁塔、卢浮宫、巴黎圣母院。

## Using Analogies

## 使用类比

Framing a task using an analogy can sometimes help the model understand the desired output or process by relating it to something familiar. This can be particularly useful for creative tasks or explaining complex roles.

通过类比来框定任务，有时能通过将任务与熟悉概念关联，帮助模型理解期望的输出或过程。这对创意任务或解释复杂角色尤为有用。

* **Example:**  
  Act as a "data chef". Take the raw ingredients (data points) and prepare a "summary dish" (report) that highlights the key flavors (trends) for a business audience.

* **示例**：
  扮演"数据厨师"角色。取用原始食材（数据点），为商务受众烹制一份"摘要菜肴"（报告），突出关键风味（趋势）。

## Factored Cognition / Decomposition

## 分解式认知/任务分解（Factored Cognition / Decomposition）

For very complex tasks, it can be effective to break down the overall goal into smaller, more manageable sub-tasks and prompt the model separately on each sub-task. The results from the sub-tasks are then combined to achieve the final outcome. This is related to prompt chaining and planning but emphasizes the deliberate decomposition of the problem.

对于极其复杂的任务，将总体目标分解为更小、更易管理的子任务，并对每个子任务分别提示模型，可能是有效的方法。子任务的结果随后被组合以实现最终成果。这与提示词链和规划相关，但强调对问题的深思熟虑分解。

* **Example:** To write a research paper:  
  * Prompt 1: "Generate a detailed outline for a paper on the impact of AI on the job market."  
  * Prompt 2: "Write the introduction section based on this outline: [insert outline intro]."  
  * Prompt 3: "Write the section on 'Impact on White-Collar Jobs' based on this outline: [insert outline section]." (Repeat for other sections).  
  * Prompt N: "Combine these sections and write a conclusion."

* **示例**：撰写研究论文：
  * 提示 1："生成关于 AI 对就业市场影响的论文详细大纲。"
  * 提示 2："基于此大纲撰写引言部分：[插入大纲引言]。"
  * 提示 3："基于此大纲撰写'对白领工作的影响'部分：[插入大纲相关部分]。"（对其他部分重复此过程）。
  * 提示 N："整合这些部分并撰写结论。"

## Retrieval Augmented Generation (RAG)

## 检索增强生成（RAG）

RAG is a powerful technique that enhances language models by giving them access to external, up-to-date, or domain-specific information during the prompting process. When a user asks a question, the system first retrieves relevant documents or data from a knowledge base (e.g., a database, a set of documents, the web). This retrieved information is then included in the prompt as context, allowing the language model to generate a response grounded in that external knowledge. This mitigates issues like hallucination and provides access to information the model wasn't trained on or that is very recent. This is a key pattern for agentic systems that need to work with dynamic or proprietary information.

RAG 是一种强大技术，通过在提示过程中赋予语言模型访问外部、最新或领域特定信息的能力来增强模型。当用户提出问题时，系统首先从知识库（如数据库、文档集、网络）检索相关文档或数据。随后将此检索信息作为上下文纳入提示，使语言模型能够基于此外部知识生成响应。这有助于缓解幻觉问题，并提供模型未训练过或非常新的信息访问途径。这是需要处理动态或专有信息的 Agentic 系统的关键模式。

* **Example:**  
  * *User Query:* "What are the new features in the latest version of the Python library 'X'?"  
  * *System Action:* Search a documentation database for "Python library X latest features".  
  * *Prompt to LLM:* "Based on the following documentation snippets: [insert retrieved text], explain the new features in the latest version of Python library 'X'."

* **示例**：
  * *用户查询*："Python 库'X'最新版本有哪些新功能？"
  * *系统操作*：在文档数据库中搜索"Python 库 X 最新功能"。
  * *对 LLM 的提示*："基于以下文档片段：[插入检索到的文本]，解释 Python 库'X'最新版本的新功能。"

## Persona Pattern (User Persona):

## 用户画像模式

While role prompting assigns a persona to the *model*, the Persona Pattern involves describing the user or the target audience for the model's output. This helps the model tailor its response in terms of language, complexity, tone, and the kind of information it provides.

虽然角色提示为*模型*分配角色，用户画像模式则涉及描述用户或模型输出的目标受众。这有助于模型在语言、复杂度、语气和提供信息类型方面定制其响应。

* **Example:**  
  You are explaining quantum physics. The target audience is a high school student with no prior knowledge of the subject. Explain it simply and use analogies they might understand.

  Explain quantum physics: [Insert basic explanation request]

* **示例**：
  你正在解释量子物理。目标受众是毫无该学科基础知识的高中生。请用简单语言解释，并使用他们可能理解的类比。

  解释量子物理：[插入基础解释请求]

These advanced and supplementary techniques provide further tools for prompt engineers to optimize model behavior, integrate external information, and tailor interactions for specific users and tasks within agentic workflows.

这些高级和补充技术为提示工程师提供了额外工具，以优化模型行为、整合外部信息，并为 Agentic 工作流中的特定用户和任务定制交互。

## Using Google Gems

## 使用 Google Gems

Google's AI "Gems" (see Fig. 1) represent a user-configurable feature within its large language model architecture. Each "Gem" functions as a specialized instance of the core Gemini AI, tailored for specific, repeatable tasks. Users create a Gem by providing it with a set of explicit instructions, which establishes its operational parameters. This initial instruction set defines the Gem's designated purpose, response style, and knowledge domain. The underlying model is designed to consistently adhere to these pre-defined directives throughout a conversation.

Google 的 AI"Gems"（见图 1）代表其大型语言模型架构中的用户可配置功能。每个"Gem"作为核心 Gemini AI 的专门实例运行，为特定可重复任务量身定制。用户通过提供一组明确指令来创建 Gem，这确立了其操作参数。此初始指令集定义了 Gem 的指定目标、响应风格和知识领域。底层模型设计为在整个对话过程中始终遵循这些预定义指令。

This allows for the creation of highly specialized AI agents for focused applications. For example, a Gem can be configured to function as a code interpreter that only references specific programming libraries. Another could be instructed to analyze data sets, generating summaries without speculative commentary. A different Gem might serve as a translator adhering to a particular formal style guide. This process creates a persistent, task-specific context for the artificial intelligence.

这允许为专注应用创建高度专业化的 AI Agent。例如，可配置 Gem 作为仅引用特定编程库的代码解释器。另一个可被指示分析数据集，生成摘要而不进行推测性评论。不同的 Gem 可能作为遵守特定正式风格指南的翻译器。此过程为 AI 创建了持久且特定于任务的上下文。

Consequently, the user avoids the need to re-establish the same contextual information with each new query. This methodology reduces conversational redundancy and improves the efficiency of task execution. The resulting interactions are more focused, yielding outputs that are consistently aligned with the user's initial requirements. This framework allows for applying fine-grained, persistent user direction to a generalist AI model. Ultimately, Gems enable a shift from general-purpose interaction to specialized, pre-defined AI functionalities.

因此，用户无需在每个新查询中重新建立相同上下文信息。这种方法减少了对话冗余，提升了任务执行效率。产生的交互更加专注，输出与用户初始要求保持高度一致。此框架允许对通用 AI 模型应用细粒度、持久的用户指导。最终，Gems 实现了从通用交互向专业化、预定义 AI 功能的转变。

![][image1]
图 1：Google Gem 使用示例。

## Using LLMs to Refine Prompts (The Meta Approach)

## 使用 LLM 改进提示（元方法）

We've explored numerous techniques for crafting effective prompts, emphasizing clarity, structure, and providing context or examples. This process, however, can be iterative and sometimes challenging. What if we could leverage the very power of large language models, like Gemini, to help us *improve* our prompts? This is the essence of using LLMs for prompt refinement – a "meta" application where AI assists in optimizing the instructions given to AI.

我们已经探讨了多种制作有效提示的技术，强调清晰性、结构以及提供上下文或示例的重要性。然而，这一过程往往是迭代的，有时颇具挑战性。如果我们能利用大型语言模型（如 Gemini）的强大能力来帮助我们*优化*提示呢？这正是使用 LLM 进行提示改进的核心思想——一种"元"应用，即 AI 协助优化给 AI 的指令。

This capability is particularly "cool" because it represents a form of AI self-improvement or at least AI-assisted human improvement in interacting with AI. Instead of solely relying on human intuition and trial-and-error, we can tap into the LLM's understanding of language, patterns, and even common prompting pitfalls to get suggestions for making our prompts better. It turns the LLM into a collaborative partner in the prompt engineering process.

这种能力尤为"精妙"，因为它代表了 AI 自我改进的一种形式，或至少是 AI 辅助人类改进与 AI 交互的方式。我们不再仅仅依赖人类直觉和试错，而是能借助 LLM 对语言、模式乃至常见提示陷阱的理解，获得改进提示的建议。它将 LLM 转变为提示工程过程中的协作伙伴。

How does this work in practice? You can provide a language model with an existing prompt that you're trying to improve, along with the task you want it to accomplish and perhaps even examples of the output you're currently getting (and why it's not meeting your expectations). You then prompt the LLM to analyze the prompt and suggest improvements.

如何在实践中实现这一点？您可以为语言模型提供一个您正在尝试改进的现有提示，以及您希望它完成的任务，甚至可能包括您当前获得的输出示例（以及为什么它不符合您的期望）。然后提示 LLM 分析提示并提出改进建议。

A model like Gemini, with its strong reasoning and language generation capabilities, can analyze your existing prompt for potential areas of ambiguity, lack of specificity, or inefficient phrasing. It can suggest incorporating techniques we've discussed, such as adding delimiters, clarifying the desired output format, suggesting a more effective persona, or recommending the inclusion of few-shot examples.

像 Gemini 这样的模型，凭借其强大的推理和语言生成能力，可以分析您的现有提示，寻找潜在的歧义、缺乏具体性或措辞效率低下的区域。它可以建议结合我们讨论过的技术，例如添加分隔符、明确期望的输出格式、建议更有效的角色或推荐包含少样本示例。

The benefits of this meta-prompting approach include:

这种元级提示方法的优势包括：

* **Accelerated Iteration:** Get suggestions for improvement much faster than pure manual trial and error.  
* **Identification of Blind Spots:** An LLM might spot ambiguities or potential misinterpretations in your prompt that you overlooked.  
* **Learning Opportunity:** By seeing the types of suggestions the LLM makes, you can learn more about what makes prompts effective and improve your own prompt engineering skills.  
* **Scalability:** Potentially automate parts of the prompt optimization process, especially when dealing with a large number of prompts.

* **加速迭代**：相比纯手动试错，能更快获得改进建议。
* **识别盲点**：LLM 可能发现您忽略的提示中的歧义或潜在误解。
* **学习机会**：通过观察 LLM 提出的建议类型，您可更深入理解提示有效的要素，提升自身提示工程技能。
* **可扩展性**：可能自动化部分提示优化流程，尤其在处理大量提示时优势明显。

It's important to note that the LLM's suggestions are not always perfect and should be evaluated and tested, just like any manually engineered prompt. However, it provides a powerful starting point and can significantly streamline the refinement process.

需注意，LLM 的建议并非总是完美的，应像对待任何手动设计的提示一样进行评估和测试。然而，它提供了一个强有力的起点，能显著简化优化过程。

* **Example Prompt for Refinement:**  
  Analyze the following prompt for a language model and suggest ways to improve it to consistently extract the main topic and key entities (people, organizations, locations) from news articles. The current prompt sometimes misses entities or gets the main topic wrong.

  Existing Prompt:  
  "Summarize the main points and list important names and places from this article: [insert article text]"

  Suggestions for Improvement:

* **改进提示的示例**：
  分析以下语言模型提示，并提出改进建议，以使其能稳定地从新闻文章中提取主题和关键实体（人物、组织、地点）。当前提示有时会遗漏实体或错误判断主题。

  现有提示：
  "总结本文要点并列出重要名称和地点：[插入文章文本]"

  改进建议：

In this example, we're using the LLM to critique and enhance another prompt. This meta-level interaction demonstrates the flexibility and power of these models, allowing us to build more effective agentic systems by first optimizing the fundamental instructions they receive. It's a fascinating loop where AI helps us talk better to AI.

在此示例中，我们使用 LLM 来评审和增强另一个提示。这种元级交互展示了这些模型的灵活性与强大能力，使我们能通过首先优化给它们的基本指令来构建更有效的 Agentic 系统。这是一个迷人的循环：AI 帮助我们更有效地与 AI 对话。

## Prompting for Specific Tasks

## 特定任务的提示

While the techniques discussed so far are broadly applicable, some tasks benefit from specific prompting considerations. This is particularly relevant in the realm of code and multimodal inputs.

尽管前述技术具有广泛适用性，但某些任务仍受益于特定的提示考量。这在代码和多模态输入领域尤为相关。

## Code Prompting

## 代码提示

Language models, especially those trained on large code datasets, can be powerful assistants for developers. Prompting for code involves using LLMs to generate, explain, translate, or debug code. Various use cases exist:

语言模型，尤其是在大型代码数据集上训练的模型，可成为开发者的强大助手。代码提示涉及使用 LLM 生成、解释、翻译或调试代码。存在多种应用场景：

* **Prompts for writing code:** Asking the model to generate code snippets or functions based on a description of the desired functionality.  
  * **Example:** "Write a Python function that takes a list of numbers and returns the average."  
* **Prompts for explaining code:** Providing a code snippet and asking the model to explain what it does, line by line or in a summary.  
  * **Example:** "Explain the following JavaScript code snippet: [insert code]."  
* **Prompts for translating code:** Asking the model to translate code from one programming language to another.  
  * **Example:** "Translate the following Java code to C++: [insert code]."  
* **Prompts for debugging and reviewing code:** Providing code that has an error or could be improved and asking the model to identify issues, suggest fixes, or provide refactoring suggestions.  
  * **Example:** "The following Python code is giving a 'NameError'. What is wrong and how can I fix it? [insert code and traceback]."

* **代码编写提示**：要求模型基于功能描述生成代码片段或函数。
  * **示例**："编写一个接受数字列表并返回平均值的 Python 函数。"
* **代码解释提示**：提供代码片段并要求模型逐行或整体解释其功能。
  * **示例**："解释以下 JavaScript 代码片段：[插入代码]。"
* **代码翻译提示**：要求模型将代码从一种编程语言转换为另一种。
  * **示例**："将以下 Java 代码翻译为 C++：[插入代码]。"
* **代码调试与审查提示**：提供存在错误或可优化代码，要求模型识别问题、建议修复或提供重构意见。
  * **示例**："以下 Python 代码出现'NameError'。问题何在？如何修复？[插入代码和错误回溯]。"

Effective code prompting often requires providing sufficient context, specifying the desired language and version, and being clear about the functionality or issue.

有效的代码提示通常需要提供充分上下文、明确指定语言和版本，并清晰阐述功能需求或问题描述。

## Multimodal Prompting

## 多模态提示

While the focus of this appendix and much of current LLM interaction is text-based, the field is rapidly moving towards multimodal models that can process and generate information across different modalities (text, images, audio, video, etc.). Multimodal prompting involves using a combination of inputs to guide the model. This refers to using multiple input formats instead of just text.

尽管本附录重点及当前多数 LLM 交互基于文本，但该领域正迅速向能跨模态（文本、图像、音频、视频等）处理和生成信息的多模态模型发展。多模态提示涉及使用输入组合引导模型，即采用多种输入格式而非仅文本。

* **Example:** Providing an image of a diagram and asking the model to explain the process shown in the diagram (Image Input + Text Prompt). Or providing an image and asking the model to generate a descriptive caption (Image Input + Text Prompt -> Text Output).

* **示例**：提供图表图像并要求模型解释图中所示过程（图像输入 + 文本提示）。或提供图像并要求模型生成描述性标题（图像输入 + 文本提示 -> 文本输出）。

As multimodal capabilities become more sophisticated, prompting techniques will evolve to effectively leverage these combined inputs and outputs.

随着多模态能力日益复杂，提示技术将相应演进，以有效利用这些组合的输入与输出。

## Best Practices and Experimentation

## 最佳实践与实验

Becoming a skilled prompt engineer is an iterative process that involves continuous learning and experimentation. Several valuable best practices are worth reiterating and emphasizing:

成为熟练的提示工程师是一个需要持续学习和实验的迭代过程。值得重申和强调若干有价值的最佳实践：

* **Provide Examples:** Providing one or few-shot examples is one of the most effective ways to guide the model.  
* **Design with Simplicity:** Keep your prompts concise, clear, and easy to understand. Avoid unnecessary jargon or overly complex phrasing.  
* **Be Specific about the Output:** Clearly define the desired format, length, style, and content of the model's response.  
* **Use Instructions over Constraints:** Focus on telling the model what you want it to do rather than what you don't want it to do.  
* **Control the Max Token Length:** Use model configurations or explicit prompt instructions to manage the length of the generated output.  
* **Use Variables in Prompts:** For prompts used in applications, use variables to make them dynamic and reusable, avoiding hardcoding specific values.  
* **Experiment with Input Formats and Writing Styles:** Try different ways of phrasing your prompt (question, statement, instruction) and experiment with different tones or styles to see what yields the best results.  
* **For Few-Shot Prompting with Classification Tasks, Mix Up the Classes:** Randomize the order of examples from different categories to prevent overfitting.  
* **Adapt to Model Updates:** Language models are constantly being updated. Be prepared to test your existing prompts on new model versions and adjust them to leverage new capabilities or maintain performance.  
* **Experiment with Output Formats:** Especially for non-creative tasks, experiment with requesting structured output like JSON or XML.  
* **Experiment Together with Other Prompt Engineers:** Collaborating with others can provide different perspectives and lead to discovering more effective prompts.  
* **CoT Best Practices:** Remember specific practices for Chain of Thought, such as placing the answer after the reasoning and setting temperature to 0 for tasks with a single correct answer.  
* **Document the Various Prompt Attempts:** This is crucial for tracking what works, what doesn't, and why. Maintain a structured record of your prompts, configurations, and results.  
* **Save Prompts in Codebases:** When integrating prompts into applications, store them in separate, well-organized files for easier maintenance and version control.  
* **Rely on Automated Tests and Evaluation:** For production systems, implement automated tests and evaluation procedures to monitor prompt performance and ensure generalization to new data.

* **提供示例**：提供 one-shot 或 few-shot 示例是最有效的模型引导方法之一。
* **设计简洁**：保持提示简明、清晰且易于理解。避免不必要的专业术语或过度复杂措辞。
* **明确输出要求**：清晰定义模型响应的期望格式、长度、风格和内容。
* **指令优于约束**：聚焦于告知模型应做什么，而非不应做什么。
* **控制最大 Token 长度**：使用模型配置或明确提示指令管理生成输出的长度。
* **提示中使用变量**：对应用中使用的提示，采用变量使其动态可复用，避免硬编码特定值。
* **尝试输入格式与写作风格**：试验不同提示措辞方式（疑问、陈述、指令）并探索不同语气或风格，以寻找最佳效果。
* **Few-Shot 分类任务提示中混合类别**：随机化不同类别示例顺序，防止过拟合。
* **适应模型更新**：语言模型持续更新。准备在新模型版本上测试现有提示，并调整以利用新功能或维持性能。
* **尝试输出格式**：尤其对非创意任务，试验请求 JSON 或 XML 等结构化输出。
* **与其他提示工程师协作实验**：合作可提供不同视角，有助于发现更有效提示。
* **CoT 最佳实践**：牢记思维链特定实践，如答案置于推理后，以及对单一正确答案任务设置温度为 0。
* **记录各类提示尝试**：对追踪何者有效、无效及原因至关重要。维护提示、配置和结果的结构化记录。
* **代码库中保存提示**：集成提示至应用时，将其存储于独立、组织良好的文件中，便于维护和版本控制。
* **依赖自动化测试与评估**：对生产系统，实施自动化测试和评估流程，监控提示性能并确保对新数据的泛化能力。

Prompt engineering is a skill that improves with practice. By applying these principles and techniques, and by maintaining a systematic approach to experimentation and documentation, you can significantly enhance your ability to build effective agentic systems.

提示工程是一项通过实践持续提升的技能。应用这些原则与技术，并保持对实验和文档的系统性方法，您将显著增强构建高效 Agentic 系统的能力。

## Conclusion

## 结论

This appendix provides a comprehensive overview of prompting, reframing it as a disciplined engineering practice rather than a simple act of asking questions. Its central purpose is to demonstrate how to transform general-purpose language models into specialized, reliable, and highly capable tools for specific tasks. The journey begins with non-negotiable core principles like clarity, conciseness, and iterative experimentation, which are the bedrock of effective communication with AI. These principles are critical because they reduce the inherent ambiguity in natural language, helping to steer the model's probabilistic outputs toward a single, correct intention. Building on this foundation, basic techniques such as zero-shot, one-shot, and few-shot prompting serve as the primary methods for demonstrating expected behavior through examples. These methods provide varying levels of contextual guidance, powerfully shaping the model's response style, tone, and format. Beyond just examples, structuring prompts with explicit roles, system-level instructions, and clear delimiters provides an essential architectural layer for fine-grained control over the model.

本附录全面概述了提示工程，将其重新定位为一项有纪律的工程实践，而非简单的提问行为。其核心目标是展示如何将通用语言模型转化为针对特定任务的专业化、可靠且高度能干的工具。这一旅程始于不容妥协的核心原则：清晰性、简洁性和迭代实验，这些是与 AI 有效沟通的基石。这些原则至关重要，因其减少了自然语言固有的歧义，帮助引导模型的概率输出朝向明确正确的意图。在此基础上，基础技术（如 zero-shot、one-shot 和 few-shot 提示）作为通过示例展示预期行为的主要手段。这些方法提供不同层级的上下文指导，有力塑造模型的响应风格、语气和格式。超越示例范畴，使用明确角色、系统级指令和清晰分隔符构建提示，为精细控制模型提供了必要的架构层次。

The importance of these techniques becomes paramount in the context of building autonomous agents, where they provide the control and reliability necessary for complex, multi-step operations. For an agent to effectively create and execute a plan, it must leverage advanced reasoning patterns like Chain of Thought and Tree of Thoughts. These sophisticated methods compel the model to externalize its logical steps, systematically breaking down complex goals into a sequence of manageable sub-tasks. The operational reliability of the entire agentic system hinges on the predictability of each component's output. This is precisely why requesting structured data like JSON, and programmatically validating it with tools such as Pydantic, is not a mere convenience but an absolute necessity for robust automation. Without this discipline, the agent's internal cognitive components cannot communicate reliably, leading to catastrophic failures within an automated workflow. Ultimately, these structuring and reasoning techniques are what successfully convert a model's probabilistic text generation into a deterministic and trustworthy cognitive engine for an agent.

这些技术在构建自主智能体的背景下变得至关重要，它们为复杂多步骤操作提供了必要的控制与可靠性。为使智能体能够制定和执行计划，必须利用高级推理模式，如思维链和思维树。这些复杂方法迫使模型外化其逻辑步骤，系统地将复杂目标分解为可管理的子任务序列。整个 Agentic 系统的运营可靠性依赖于各组件输出的可预测性。这正是为何请求 JSON 等结构化数据，并使用 Pydantic 等工具进行程序化验证，不仅是一种便利，更是强大自动化的绝对必要条件。缺乏这种纪律，Agent 的内部认知组件无法可靠通信，导致自动化工作流中的灾难性故障。最终，这些结构化与推理技术成功将模型的概率文本生成转化为智能体的可靠认知引擎。

Furthermore, these prompts are what grant an agent its crucial ability to perceive and act upon its environment, bridging the gap between digital thought and real-world interaction. Action-oriented frameworks like ReAct and native function calling are the vital mechanisms that serve as the agent's hands, allowing it to use tools, query APIs, and manipulate data. In parallel, techniques like Retrieval Augmented Generation (RAG) and the broader discipline of Context Engineering function as the agent's senses. They actively retrieve relevant, real-time information from external knowledge bases, ensuring the agent's decisions are grounded in current, factual reality. This critical capability prevents the agent from operating in a vacuum, where it would be limited to its static and potentially outdated training data. Mastering this full spectrum of prompting is therefore the definitive skill that elevates a generalist language model from a simple text generator into a truly sophisticated agent, capable of performing complex tasks with autonomy, awareness, and intelligence.

此外，这些提示赋予智能体感知环境并与之交互的关键能力，弥合数字思维与现实世界行动间的鸿沟。ReAct 和原生工具调用等行动导向框架赋予智能体行动能力，使其能使用工具、查询 API 和操作数据。同时，检索增强生成（RAG）及更广泛的上下文工程学科则充当智能体的信息检索系统，使它们能主动从外部知识库检索相关实时信息，确保智能体的决策基于现实世界信息。这一关键能力防止智能体在信息真空中运作，并使其免受限于其静态且可能过时的训练数据。因此，掌握完整的提示技术谱系，是将通用语言模型从简单文本生成器提升为真正复杂智能体的决定性技能，使智能体具备自主性、情境意识和智能执行复杂任务的能力。

## References

## 参考文献

Here is a list of resources for further reading and deeper exploration of prompt engineering techniques:

以下是进一步阅读和深入探索提示工程技术的资源列表：

 1. Prompt Engineering, [https://www.kaggle.com/whitepaper-prompt-engineering](https://www.kaggle.com/whitepaper-prompt-engineering)
 2. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, [https://arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903)
 3. Self-Consistency Improves Chain of Thought Reasoning in Language Models,  [https://arxiv.org/pdf/2203.11171](https://arxiv.org/pdf/2203.11171)
 4. ReAct: Synergizing Reasoning and Acting in Language Models, [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)
 5. Tree of Thoughts: Deliberate Problem Solving with Large Language Models,  [https://arxiv.org/pdf/2305.10601](https://arxiv.org/pdf/2305.10601)
 6. Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models, [https://arxiv.org/abs/2310.06117](https://arxiv.org/abs/2310.06117)
 7. DSPy: Programming—not prompting—Foundation Models [https://github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)

[image1]: ../images/appendix-a/image1.png
