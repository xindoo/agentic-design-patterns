# Glossary

# Fundamental Concepts

# Prompt: A prompt is the input, typically in the form of a question, instruction, or statement, that a user provides to an AI model to elicit a response. The quality and structure of the prompt heavily influence the model's output, making prompt engineering a key skill for effectively using AI.

# 

# Context Window: The context window is the maximum number of tokens an AI model can process at once, including both the input and its generated output. This fixed size is a critical limitation, as information outside the window is ignored, while larger windows enable more complex conversations and document analysis.

# 

# In-Context Learning: In-context learning is an AI's ability to learn a new task from examples provided directly in the prompt, without requiring any retraining. This powerful feature allows a single, general-purpose model to be adapted to countless specific tasks on the fly.

# 

# Zero-Shot, One-Shot, & Few-Shot Prompting: These are prompting techniques where a model is given zero, one, or a few examples of a task to guide its response. Providing more examples generally helps the model better understand the user's intent and improves its accuracy for the specific task.

# 

# Multimodality: Multimodality is an AI's ability to understand and process information across multiple data types like text, images, and audio. This allows for more versatile and human-like interactions, such as describing an image or answering a spoken question.

# 

# Grounding: Grounding is the process of connecting a model's outputs to verifiable, real-world information sources to ensure factual accuracy and reduce hallucinations. This is often achieved with techniques like RAG to make AI systems more trustworthy.

# Core AI Model Architectures

# Transformers: The Transformer is the foundational neural network architecture for most modern LLMs. Its key innovation is the self-attention mechanism, which efficiently processes long sequences of text and captures complex relationships between words.

# 

# Recurrent Neural Network (RNN): The Recurrent Neural Network is a foundational architecture that preceded the Transformer. RNNs process information sequentially, using loops to maintain a "memory" of previous inputs, which made them suitable for tasks like text and speech processing.

# 

# Mixture of Experts (MoE): Mixture of Experts is an efficient model architecture where a "router" network dynamically selects a small subset of "expert" networks to handle any given input. This allows models to have a massive number of parameters while keeping computational costs manageable.

# 

# Diffusion Models: Diffusion models are generative models that excel at creating high-quality images. They work by adding random noise to data and then training a model to meticulously reverse the process, allowing them to generate novel data from a random starting point.

# 

# Mamba: Mamba is a recent AI architecture using a Selective State Space Model (SSM) to process sequences with high efficiency, especially for very long contexts. Its selective mechanism allows it to focus on relevant information while filtering out noise, making it a potential alternative to the Transformer.

# The LLM Development Lifecycle

# The development of a powerful language model follows a distinct sequence. It begins with Pre-training, where a massive base model is built by training it on a vast dataset of general internet text to learn language, reasoning, and world knowledge. Next is Fine-tuning, a specialization phase where the general model is further trained on smaller, task-specific datasets to adapt its capabilities for a particular purpose. The final stage is Alignment, where the specialized model's behavior is adjusted to ensure its outputs are helpful, harmless, and aligned with human values.

# 

# Pre-training Techniques: Pre-training is the initial phase where a model learns general knowledge from vast amounts of data. The top techniques for this involve different objectives for the model to learn from. The most common is Causal Language Modeling (CLM), where the model predicts the next word in a sentence. Another is Masked Language Modeling (MLM), where the model fills in intentionally hidden words in a text. Other important methods include Denoising Objectives, where the model learns to restore a corrupted input to its original state, Contrastive Learning, where it learns to distinguish between similar and dissimilar pieces of data, and Next Sentence Prediction (NSP), where it determines if two sentences logically follow each other.

# 

# Fine-tuning Techniques: Fine-tuning is the process of adapting a general pre-trained model to a specific task using a smaller, specialized dataset. The most common approach is Supervised Fine-Tuning (SFT), where the model is trained on labeled examples of correct input-output pairs. A popular variant is Instruction Tuning, which focuses on training the model to better follow user commands. To make this process more efficient, Parameter-Efficient Fine-Tuning (PEFT) methods are used, with top techniques including LoRA (Low-Rank Adaptation), which only updates a small number of parameters, and its memory-optimized version, QLoRA. Another technique, Retrieval-Augmented Generation (RAG), enhances the model by connecting it to an external knowledge source during the fine-tuning or inference stage.

# 

# Alignment & Safety Techniques: Alignment is the process of ensuring an AI model's behavior aligns with human values and expectations, making it helpful and harmless. The most prominent technique is Reinforcement Learning from Human Feedback (RLHF), where a "reward model" trained on human preferences guides the AI's learning process, often using an algorithm like Proximal Policy Optimization (PPO) for stability. Simpler alternatives have emerged, such as Direct Preference Optimization (DPO), which bypasses the need for a separate reward model, and Kahneman-Tversky Optimization (KTO), which simplifies data collection further. To ensure safe deployment, Guardrails are implemented as a final safety layer to filter outputs and block harmful actions in real-time.

# Enhancing AI Agent Capabilities

# AI agents are systems that can perceive their environment and take autonomous actions to achieve goals. Their effectiveness is enhanced by robust reasoning frameworks.

# 

# Chain of Thought (CoT): This prompting technique encourages a model to explain its reasoning step-by-step before giving a final answer. This process of "thinking out loud" often leads to more accurate results on complex reasoning tasks.

# 

# Tree of Thoughts (ToT): Tree of Thoughts is an advanced reasoning framework where an agent explores multiple reasoning paths simultaneously, like branches on a tree. It allows the agent to self-evaluate different lines of thought and choose the most promising one to pursue, making it more effective at complex problem-solving.

# 

# ReAct (Reason and Act): ReAct is an agent framework that combines reasoning and acting in a loop. The agent first "thinks" about what to do, then takes an "action" using a tool, and uses the resulting observation to inform its next thought, making it highly effective at solving complex tasks.

# 

# Planning: This is an agent's ability to break down a high-level goal into a sequence of smaller, manageable sub-tasks. The agent then creates a plan to execute these steps in order, allowing it to handle complex, multi-step assignments.

# 

# Deep Research: Deep research refers to an agent's capability to autonomously explore a topic in-depth by iteratively searching for information, synthesizing findings, and identifying new questions. This allows the agent to build a comprehensive understanding of a subject far beyond a single search query.

# 

# Critique Model: A critique model is a specialized AI model trained to review, evaluate, and provide feedback on the output of another AI model. It acts as an automated critic, helping to identify errors, improve reasoning, and ensure the final output meets a desired quality standard.

# Index of Terms

This index of terms was generated using Gemini Pro 2.5. The prompt and reasoning steps are included at the end to demonstrate the time-saving benefits and for educational purposes.

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

**B**

* Behavioral Constraints \- Chapter 18: Guardrails/Safety Patterns  
* Browser Use \- Appendix B

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

**F**

* Factored Cognition \- Appendix A  
* FastMCP \- Chapter 10: Model Context Protocol (MCP)  
* Fault Tolerance \- Chapter 18: Guardrails/Safety Patterns  
* Few-Shot Learning \- Chapter 9: Learning and Adaptation  
* Few-Shot Prompting \- Appendix A  
* Fine-tuning \- Glossary  
* Formalized Contract \- Chapter 19: Evaluation and Monitoring  
* Function Calling \- Chapter 5: Tool Use, Appendix A

**G**

* Gemini Live \- Appendix B  
* Gems \- Appendix A  
* Generative Media Orchestration \- Chapter 10: Model Context Protocol (MCP)  
* Goal Setting \- Chapter 11: Goal Setting and Monitoring  
* GoD (Graph of Debates) \- Chapter 17: Reasoning Techniques  
* Google Agent Development Kit (ADK) \- Chapter 2: Routing, Chapter 3: Parallelization, Chapter 4: Reflection, Chapter 5: Tool Use, Chapter 7: Multi-Agent Collaboration, Chapter 8: Memory Management, Chapter 12: Exception Handling and Recovery, Chapter 13: Human-in-the-Loop, Chapter 15: Inter-Agent Communication (A2A), Chapter 16: Resource-Aware Optimization, Chapter 19: Evaluation and Monitoring, Appendix C  
* Google Co-Scientist \- Chapter 21: Exploration and Discovery  
* Google DeepResearch \- Chapter 6: Planning  
* Google Project Mariner \- Appendix B  
* Graceful Degradation \- Chapter 12: Exception Handling and Recovery, Chapter 16: Resource-Aware Optimization  
* Graph of Debates (GoD) \- Chapter 17: Reasoning Techniques  
* Grounding \- Glossary  
* Guardrails \- Chapter 18: Guardrails/Safety Patterns

**H**

* Haystack \- Appendix C  
* Hierarchical Decomposition \- Chapter 19: Evaluation and Monitoring  
* Hierarchical Structures \- Chapter 7: Multi-Agent Collaboration  
* HITL (Human-in-the-Loop) \- Chapter 13: Human-in-the-Loop  
* Human-in-the-Loop (HITL) \- Chapter 13: Human-in-the-Loop  
* Human-on-the-loop \- Chapter 13: Human-in-the-Loop  
* Human Oversight \- Chapter 13: Human-in-the-Loop, Chapter 18: Guardrails/Safety Patterns

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

**J**

* Jailbreaking \- Chapter 18: Guardrails/Safety Patterns

**K**

* Kahneman-Tversky Optimization (KTO) \- Glossary  
* Knowledge Retrieval (RAG) \- Chapter 14: Knowledge Retrieval (RAG)

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

**N**

* Negative Examples \- Appendix A  
* Next Sentence Prediction (NSP) \- Glossary

**O**

* Observability \- Chapter 18: Guardrails/Safety Patterns  
* One-Shot Prompting \- Appendix A  
* Online Learning \- Chapter 9: Learning and Adaptation  
* OpenAI Deep Research API \- Chapter 6: Planning  
* OpenEvolve \- Chapter 9: Learning and Adaptation  
* OpenRouter \- Chapter 16: Resource-Aware Optimization  
* Output Filtering/Post-processing \- Chapter 18: Guardrails/Safety Patterns

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
* Project Astra \- Appendix B  
* Prompt \- Glossary  
* Prompt Chaining \- Chapter 1: Prompt Chaining  
* Prompt Engineering \- Appendix A  
* Proximal Policy Optimization (PPO) \- Chapter 9: Learning and Adaptation  
* Push Notifications \- Chapter 15: Inter-Agent Communication (A2A)

**Q**

* QLoRA \- Glossary  
* Quality-Focused Iterative Execution \- Chapter 19: Evaluation and Monitoring

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

**T**

* Task Evaluation \- Chapter 20: Prioritization  
* Text Similarity \- Chapter 14: Knowledge Retrieval (RAG)  
* Token Usage \- Chapter 19: Evaluation and Monitoring  
* Tool Use \- Chapter 5: Tool Use, Appendix A  
* Tool Use Restrictions \- Chapter 18: Guardrails/Safety Patterns  
* ToT (Tree of Thoughts) \- Chapter 17: Reasoning Techniques, Appendix A, Glossary  
* Transformers \- Glossary  
* Tree of Thoughts (ToT) \- Chapter 17: Reasoning Techniques, Appendix A, Glossary

**U**

* Unsupervised Learning \- Chapter 9: Learning and Adaptation  
* User Persona \- Appendix A

**V**

* Validation \- Chapter 3: Parallelization  
* Vector Search \- Chapter 14: Knowledge Retrieval (RAG)  
* VertexAiRagMemoryService \- Chapter 8: Memory Management  
* VertexAiSessionService \- Chapter 8: Memory Management  
* Vibe Coding \- Appendix B  
* Visual Perception \- Appendix B

**W**

* Webhooks \- Chapter 15: Inter-Agent Communication (A2A)

**Z**

* Zero-Shot Learning \- Chapter 9: Learning and Adaptation  
* Zero-Shot Prompting \- Appendix A

# 

# Prompt

Below is the prompt that was utilized to create this index of terms.

| *do you read https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0 and all the related documents in the first page Please extract all the titles for each chapter. and print them. Then process the content of all the individual chapters, and create a detailed index used for publishing, a list of words or phrases ('headings') and associated pointers ('locators') to where useful material relating to that heading can be found in a document or collection of documents. I don't want a sample index. I want the full index, with 100 index terms* |
| :---- |

## Gemini 2.5: Reasoning Steps

**Beginning Index Creation**

I've initiated the process by reading the Google Doc provided. Currently, I'm focusing on understanding the user's request: extracting chapter titles to build a detailed index. I'm carefully reviewing the document, looking for clear structural elements that would indicate chapter breaks. I'm hoping to identify consistent formatting or keywords that will guide the indexing process.

**Defining Index Extraction Process**

I'm now fully immersed in the task. I've broken down the user's request into actionable steps. My initial focus is using Workspaces to access the main Google Doc. Following this, I'll parse the document to locate and retrieve related documents, which will also be accessed using the same tool. Finally, I will extract all chapter titles from all the documents, and create a comprehensive index. I've planned the detailed process.

**Refining the Extraction Strategy**

The user's instructions are clear: read a Google Doc, its related documents, and build a detailed index of chapter titles. I've devised a multi-step plan. First, Workspaces will access the main Google Doc. Then, I'll parse it to find and read related documents, also using Workspaces. I'm now focusing on extracting titles and forming the detailed index with the required terms. I'm prioritizing accuracy to meet the user's specific demands for a comprehensive index.

**1 . Establish user intent:**

I've determined the user wants a chapter title list and comprehensive index from the Google Doc and related documents. Now I need to figure out the most effective method for this extraction and indexing process. I'm exploring potential API functionalities to streamline this task, and will need to assess the best strategy for handling different document structures.

**3\. Considering Tool Use**

I've extracted the chapter URLs from the main document using a regular expression. Now, I'm ready to utilize Workspaces to retrieve the actual content of each chapter. Once I have the text for each chapter, I'll proceed with indexing.

**Accessing chapter content:**

I've successfully identified the URLs for each chapter from the main document, which I can now use with Workspaces. My next step is to retrieve the content from these URLs, which will then allow me to generate the index. I'm focusing on efficiency, aiming to process this information quickly.

**Fetching Chapter Content**

I've successfully identified the chapter URLs from the main document and am ready to utilize Workspaces. My plan involves extracting these URLs, batching the calls for efficiency, and then processing the retrieved content to create the desired index. This ensures all relevant information is captured, paving the way for a comprehensive and accurate result.

**Initiating URL Retrieval**

I've now successfully extracted the chapter URLs from the main document. Currently, I'm setting up calls to the Workspaces tool, preparing to fetch the content of each chapter. The goal is to obtain the necessary text for indexing. This information will then facilitate the creation of the index with at least 100 terms as requested.

**Initiating Chapter Extraction**

I've successfully identified and extracted the chapter URLs from the main document, which I've included above. I am now proceeding to use Workspaces for each URL to obtain the chapter content. The goal is to obtain the necessary text for indexing. This information will then facilitate the creation of the index with at least 100 terms as requested. I've begun to retrieve this information.

**Orchestrating Chapter Retrieval**

I've extracted the chapter URLs and initiated a call to Workspaces. I'm currently retrieving the content for each chapter. To ensure a smooth process, I'm batching the calls to prevent any rate-limiting issues. This should enable me to efficiently compile the text needed for the index.

**Decoding User Request**

I've determined the user's need. They require two primary deliverables: first, a comprehensive list of chapter titles extracted from Google Docs, and second, a detailed index containing a minimum of one hundred key terms. The process of extracting titles seems straightforward, while curating the index will involve more nuanced analysis.

**Extracting Titles and Indexing**

I've successfully identified the user's need: extracting chapter titles from the provided documents and compiling a comprehensive index. I've fetched the content of 31 Google Docs, including the main document and its chapters. I've confirmed that no additional tools are needed. My plan involves two steps: first, extracting chapter titles from the document filenames, and second, meticulously processing the text to build the index with key terms and chapter locators.

**Developing an Extraction Plan**

I've refined my approach to tackle the user's request. I've now formulated a precise plan. Firstly, I will compile the chapter titles from the filenames of the 31 fetched documents. Secondly, and more complexly, I will meticulously analyze the content to create a comprehensive, alphabetically ordered index exceeding 100 entries. I have finalized my extraction and indexing strategy and can now commence execution.

**Crafting the Extraction Strategy**

My approach is well-defined. I will compile chapter titles from the filenames of the 31 fetched documents. Subsequently, I'll analyze the content meticulously to construct an alphabetically organized index exceeding 100 entries. I've finalized the extraction and indexing strategy and can now commence implementation. The user's goal of a detailed index, covering content from diverse chapters and appendices within the Agentic Design Patterns series, is now within reach. I'll focus on delivering a thorough response, going beyond a mere sample index.

**Defining the Approach**

I've clarified the user's need. I will extract chapter titles from the document filenames. Following that, I will carefully create an index exceeding 100 entries, arranging them alphabetically and noting their chapter locations. I am prepared to begin the indexing and extraction process.

