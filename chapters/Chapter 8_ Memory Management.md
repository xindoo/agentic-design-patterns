# 第 8 章：内存管理

有效的内存管理对于智能 Agent 保留信息至关重要。Agent 需要不同类型的内存，就像人类一样，才能高效运行。本章深入探讨内存管理，特别是解决 Agent 的即时（短期）和持久（长期）内存需求。

在 Agent 系统中，内存是指 Agent 保留和利用过去交互、观察和学习经验中的信息的能力。这种能力使 Agent 能够做出明智的决策、维护对话上下文并随时间改进。Agent 内存通常分为两种主要类型：

* **短期内存（上下文内存）：** 类似于工作记忆，它保存当前正在处理或最近访问的信息。对于使用大语言模型（LLM）的 Agent，短期内存主要存在于上下文窗口中。此窗口包含最近的消息、Agent 回复、工具使用结果以及当前交互中的 Agent 反思，所有这些都会为 LLM 的后续响应和操作提供信息。上下文窗口具有有限的容量，限制了 Agent 可以直接访问的最近信息量。高效的短期内存管理涉及在这个有限空间内保留最相关的信息，可能通过总结旧的对话片段或强调关键细节等技术。具有"长上下文"窗口的模型的出现只是扩展了这种短期内存的大小，允许在单次交互中保存更多信息。然而，这个上下文仍然是临时的，一旦会话结束就会丢失，并且每次处理都可能成本高昂且效率低下。因此，Agent 需要单独的内存类型来实现真正的持久性、从过去交互中调用信息并建立持久的知识库。
* **长期内存（持久内存）：** 这充当 Agent 需要跨各种交互、任务或延长期间保留的信息的存储库，类似于长期知识库。数据通常存储在 Agent 的即时处理环境之外，通常存储在数据库、知识图谱或向量数据库中。在向量数据库中，信息被转换为数字向量并存储，使 Agent 能够基于语义相似性而不是精确关键字匹配来检索数据，这个过程称为语义搜索。当 Agent 需要来自长期内存的信息时，它查询外部存储，检索相关数据，并将其集成到短期上下文中以供即时使用，从而将先前的知识与当前交互结合起来。

# 实际应用与用例

内存管理对于 Agent 跟踪信息并随时间智能执行至关重要。这对于 Agent 超越基本问答能力是必不可少的。应用包括：

* **聊天机器人和对话式 AI：** 维护对话流程依赖于短期内存。聊天机器人需要记住先前的用户输入以提供连贯的响应。长期内存使聊天机器人能够回忆用户偏好、过去的问题或先前的讨论，提供个性化和持续的交互。
* **面向任务的 Agent：** 管理多步骤任务的 Agent 需要短期内存来跟踪先前的步骤、当前进度和总体目标。这些信息可能驻留在任务的上下文或临时存储中。长期内存对于访问不在即时上下文中的特定用户相关数据至关重要。
* **个性化体验：** 提供定制交互的 Agent 利用长期内存存储和检索用户偏好、过去的行为和个人信息。这使 Agent 能够调整其响应和建议。
* **学习和改进：** Agent 可以通过从过去的交互中学习来改进其性能。成功的策略、错误和新信息存储在长期内存中，促进未来的适应。强化学习 Agent 以这种方式存储学习的策略或知识。
* **信息检索（RAG）：** 设计用于回答问题的 Agent 访问知识库，即它们的长期内存，通常在检索增强生成（RAG）中实现。Agent 检索相关文档或数据以告知其响应。
* **自主系统：** 机器人或自动驾驶汽车需要内存来存储地图、路线、对象位置和学习的行为。这涉及用于即时周围环境的短期内存和用于一般环境知识的长期内存。

内存使 Agent 能够维护历史、学习、个性化交互并管理复杂的、时间依赖的问题。

# 实操代码：Google Agent Developer Kit (ADK) 中的内存管理

Google Agent Developer Kit（ADK）提供了一种结构化的方法来管理上下文和内存，包括用于实际应用的组件。深入理解 ADK 的 Session、State 和 Memory 对于构建需要保留信息的 Agent 至关重要。

就像在人类交互中一样，Agent 需要能够回忆先前的交流才能进行连贯和自然的对话。ADK 通过三个核心概念及其相关服务简化了上下文管理。

与 Agent 的每次交互都可以被视为一个独特的对话线程。Agent 可能需要访问早期交互的数据。ADK 将其结构化如下：

* **Session（会话）：** 一个单独的聊天线程，记录该特定交互的消息和操作（Events），还存储与该对话相关的临时数据（State）。
* **State（状态）（session.state）：** 存储在 Session 中的数据，包含仅与当前活动聊天线程相关的信息。
* **Memory（内存）：** 来自各种过去聊天或外部来源的信息的可搜索存储库，作为超出即时对话的数据检索资源。

ADK 为管理构建复杂、有状态和上下文感知 Agent 所必需的关键组件提供专用服务。SessionService 通过处理 Session 对象的启动、记录和终止来管理聊天线程，而 MemoryService 监督长期知识（Memory）的存储和检索。

SessionService 和 MemoryService 都提供各种配置选项，允许用户根据应用程序需求选择存储方法。内存选项可用于测试目的，尽管数据不会在重启后保持。对于持久存储和可扩展性，ADK 还支持数据库和基于云的服务。

## Session：跟踪每次聊天

ADK 中的 Session 对象旨在跟踪和管理单个聊天线程。在与 Agent 开始对话时，SessionService 生成一个 Session 对象，表示为 `google.adk.sessions.Session`。此对象封装了与特定对话线程相关的所有数据，包括唯一标识符（id、app_name、user_id）、作为 Event 对象的事件的时间顺序记录、用于会话特定临时数据的存储区域（称为 state）以及指示最后更新的时间戳（last_update_time）。开发人员通常通过 SessionService 间接与 Session 对象交互。SessionService 负责管理对话会话的生命周期，包括启动新会话、恢复先前的会话、记录会话活动（包括状态更新）、识别活动会话以及管理会话数据的删除。ADK 提供几种具有不同存储机制的 SessionService 实现，用于会话历史和临时数据，例如 InMemorySessionService，适合测试但不提供跨应用程序重启的数据持久性。

```python
# 示例：使用 InMemorySessionService
# 这适用于不需要跨应用程序重启的数据持久性的本地开发和测试。
from google.adk.sessions import InMemorySessionService

session_service = InMemorySessionService()
```

然后是 DatabaseSessionService，如果您想可靠地保存到您管理的数据库。

```python
# 示例：使用 DatabaseSessionService
# 这适用于需要持久存储的生产或开发。
# 您需要配置数据库 URL（例如，用于 SQLite、PostgreSQL 等）。
# 需要：pip install google-adk[sqlalchemy] 和数据库驱动程序（例如，PostgreSQL 的 psycopg2）
from google.adk.sessions import DatabaseSessionService

# 示例使用本地 SQLite 文件：
db_url = "sqlite:///./my_agent_data.db"
session_service = DatabaseSessionService(db_url=db_url)
```

此外，还有 VertexAiSessionService，它使用 Vertex AI 基础设施在 Google Cloud 上进行可扩展的生产。

```python
# 示例：使用 VertexAiSessionService
# 这适用于 Google Cloud Platform 上的可扩展生产，利用
# Vertex AI 基础设施进行会话管理。
# 需要：pip install google-adk[vertexai] 和 GCP 设置/身份验证
from google.adk.sessions import VertexAiSessionService

PROJECT_ID = "your-gcp-project-id" # 替换为您的 GCP 项目 ID
LOCATION = "us-central1" # 替换为您想要的 GCP 位置

# 与此服务一起使用的 app_name 应对应于 Reasoning Engine ID 或名称
REASONING_ENGINE_APP_NAME = "projects/your-gcp-project-id/locations/us-central1/reasoningEngines/your-engine-id" # 替换为您的 Reasoning Engine 资源名称

session_service = VertexAiSessionService(project=PROJECT_ID, location=LOCATION)

# 使用此服务时，将 REASONING_ENGINE_APP_NAME 传递给服务方法：
# session_service.create_session(app_name=REASONING_ENGINE_APP_NAME, ...)
# session_service.get_session(app_name=REASONING_ENGINE_APP_NAME, ...)
# session_service.append_event(session, event, app_name=REASONING_ENGINE_APP_NAME)
# session_service.delete_session(app_name=REASONING_ENGINE_APP_NAME, ...)
```

选择适当的 SessionService 至关重要，因为它决定了 Agent 的交互历史和临时数据的存储方式及其持久性。

每次消息交换都涉及一个循环过程：接收消息，Runner 使用 SessionService 检索或建立 Session，Agent 使用 Session 的上下文（状态和历史交互）处理消息，Agent 生成响应并可能更新状态，Runner 将其封装为 Event，session_service.append_event 方法记录新事件并更新存储中的状态。然后 Session 等待下一条消息。理想情况下，当交互结束时使用 delete_session 方法终止会话。此过程说明了 SessionService 如何通过管理特定于 Session 的历史和临时数据来维护连续性。

## State：Session 的草稿本

在 ADK 中，每个代表聊天线程的 Session 都包含一个 state 组件，类似于 Agent 在该特定对话期间的临时工作记忆。虽然 session.events 记录整个聊天历史，但 session.state 存储和更新与活动聊天相关的动态数据点。

从根本上说，session.state 作为字典运行，将数据存储为键值对。其核心功能是使 Agent 能够保留和管理对于连贯对话至关重要的详细信息，例如用户偏好、任务进度、增量数据收集或影响后续 Agent 操作的条件标志。

状态的结构包括字符串键与可序列化 Python 类型的值配对，包括字符串、数字、布尔值、列表和包含这些基本类型的字典。State 是动态的，在整个对话中不断演变。这些更改的持久性取决于配置的 SessionService。

可以使用键前缀来定义数据范围和持久性来组织状态。没有前缀的键是特定于会话的。

* user: 前缀将数据与跨所有会话的用户 ID 关联。
* app: 前缀指定在应用程序的所有用户之间共享的数据。
* temp: 前缀指示仅对当前处理轮次有效且不会持久存储的数据。

Agent 通过单个 session.state 字典访问所有状态数据。SessionService 处理数据检索、合并和持久性。应在通过 session_service.append_event() 向会话历史添加 Event 时更新状态。这确保了准确的跟踪、在持久服务中的正确保存以及状态更改的安全处理。

1. **简单方法：使用 output_key（用于 Agent 文本回复）：** 如果您只想将 Agent 的最终文本响应直接保存到状态中，这是最简单的方法。设置 LlmAgent 时，只需告诉它要使用的 output_key。Runner 看到这一点并在追加事件时自动创建必要的操作以将响应保存到状态。让我们看一个通过 output_key 演示状态更新的代码示例。

```python
# 从 Google Agent Developer Kit (ADK) 导入必要的类
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService, Session
from google.adk.runners import Runner
from google.genai.types import Content, Part

# 定义带有 output_key 的 LlmAgent。
greeting_agent = LlmAgent(
   name="Greeter",
   model="gemini-2.0-flash",
   instruction="生成一个简短、友好的问候语。",
   output_key="last_greeting"
)

# --- 设置 Runner 和 Session ---
app_name, user_id, session_id = "state_app", "user1", "session1"
session_service = InMemorySessionService()
runner = Runner(
   agent=greeting_agent,
   app_name=app_name,
   session_service=session_service
)

session = session_service.create_session(
   app_name=app_name,
   user_id=user_id,
   session_id=session_id
)

print(f"初始状态：{session.state}")

# --- 运行 Agent ---
user_message = Content(parts=[Part(text="你好")])
print("\n--- 运行 agent ---")
for event in runner.run(
   user_id=user_id,
   session_id=session_id,
   new_message=user_message
):
   if event.is_final_response():
     print("Agent 已响应。")

# --- 检查更新的状态 ---
# 在 runner 完成处理所有事件*之后*正确检查状态。
updated_session = session_service.get_session(app_name, user_id, session_id)
print(f"\nAgent 运行后的状态：{updated_session.state}")
```

在幕后，Runner 看到您的 output_key，并在调用 append_event 时自动创建具有 state_delta 的必要操作。

2. **标准方法：使用 EventActions.state_delta（用于更复杂的更新）：** 对于需要执行更复杂操作的时候——例如一次更新多个键、保存不只是文本的内容、针对特定范围（如 user: 或 app:）或进行与 Agent 最终文本回复无关的更新——您将手动构建状态更改的字典（state_delta）并将其包含在要追加的 Event 的 EventActions 中。让我们看一个例子：

```python
import time
from google.adk.tools.tool_context import ToolContext
from google.adk.sessions import InMemorySessionService

# --- 定义推荐的基于工具的方法 ---
def log_user_login(tool_context: ToolContext) -> dict:
   """
   在用户登录事件时更新会话状态。
   此工具封装了与用户登录相关的所有状态更改。
   参数：
       tool_context：由 ADK 自动提供，提供对会话状态的访问。
   返回：
       确认操作成功的字典。
   """
   # 通过提供的上下文直接访问状态。
   state = tool_context.state
   
   # 获取当前值或默认值，然后更新状态。
   # 这更加清晰并将逻辑共置。
   login_count = state.get("user:login_count", 0) + 1
   state["user:login_count"] = login_count
   state["task_status"] = "active"
   state["user:last_login_ts"] = time.time()
   state["temp:validation_needed"] = True
   
   print("从 `log_user_login` 工具内部更新了状态。")
   
   return {
       "status": "success",
       "message": f"已跟踪用户登录。总登录次数：{login_count}。"
   }

# --- 使用演示 ---
# 在真实应用程序中，LLM Agent 会决定调用此工具。
# 在这里，我们模拟直接调用以进行演示。

# 1. 设置
session_service = InMemorySessionService()
app_name, user_id, session_id = "state_app_tool", "user3", "session3"
session = session_service.create_session(
   app_name=app_name,
   user_id=user_id,
   session_id=session_id,
   state={"user:login_count": 0, "task_status": "idle"}
)

print(f"初始状态：{session.state}")

# 2. 模拟工具调用（在真实应用中，ADK Runner 会执行此操作）
# 我们仅为此独立示例手动创建 ToolContext。
from google.adk.tools.tool_context import InvocationContext
mock_context = ToolContext(
   invocation_context=InvocationContext(
       app_name=app_name, user_id=user_id, session_id=session_id,
       session=session, session_service=session_service
   )
)

# 3. 执行工具
log_user_login(mock_context)

# 4. 检查更新的状态
updated_session = session_service.get_session(app_name, user_id, session_id)
print(f"工具执行后的状态：{updated_session.state}")

# 预期输出将显示与"之前"情况相同的状态更改，
# 但代码组织明显更清晰
# 且更健壮。
```

此代码演示了一种基于工具的方法来管理应用程序中的用户会话状态。它定义了一个函数 *log_user_login*，充当工具。此工具负责在用户登录时更新会话状态。  
该函数接受由 ADK 提供的 ToolContext 对象，以访问和修改会话的状态字典。在工具内部，它递增 *user:login_count*，将 *task_status* 设置为"active"，记录 *user:last_login_ts（时间戳）*，并添加临时标志 temp:validation_needed。

代码的演示部分模拟了如何使用此工具。它设置了内存会话服务并创建了具有一些预定义状态的初始会话。然后手动创建 ToolContext 以模拟 ADK Runner 执行工具的环境。使用此模拟上下文调用 log_user_login 函数。最后，代码再次检索会话以显示状态已通过工具的执行更新。目标是展示将状态更改封装在工具中如何使代码比直接在工具外部操作状态更清晰、更有组织。

请注意，强烈不建议在检索会话后直接修改 `session.state` 字典，因为它会绕过标准事件处理机制。这种直接更改不会记录在会话的事件历史中，可能不会被选定的 `SessionService` 持久化，可能导致并发问题，并且不会更新时间戳等基本元数据。更新会话状态的推荐方法是在 `LlmAgent` 上使用 `output_key` 参数（专门用于 Agent 的最终文本响应）或在通过 `session_service.append_event()` 追加事件时在 `EventActions.state_delta` 中包含状态更改。`session.state` 应主要用于读取现有数据。

总而言之，在设计状态时，保持简单，使用基本数据类型，为键提供清晰的名称并正确使用前缀，避免深度嵌套，并始终使用 append_event 过程更新状态。

## Memory：使用 MemoryService 的长期知识

在 Agent 系统中，Session 组件维护当前聊天历史（events）和特定于单个对话的临时数据（state）的记录。然而，为了使 Agent 在多次交互中保留信息或访问外部数据，需要长期知识管理。这由 MemoryService 促进。

```python
# 示例：使用 InMemoryMemoryService
# 这适用于不需要跨应用程序重启的数据持久性的本地开发和测试。
# 应用停止时内存内容会丢失。
from google.adk.memory import InMemoryMemoryService

memory_service = InMemoryMemoryService()
```

Session 和 State 可以概念化为单个聊天会话的短期内存，而由 MemoryService 管理的长期知识则充当持久且可搜索的存储库。此存储库可能包含来自多个过去交互或外部来源的信息。由 BaseMemoryService 接口定义的 MemoryService 为管理这个可搜索的长期知识建立了标准。其主要功能包括添加信息，涉及从会话中提取内容并使用 add_session_to_memory 方法存储它，以及检索信息，允许 Agent 查询存储并使用 search_memory 方法接收相关数据。

ADK 提供了几种实现来创建这个长期知识存储。InMemoryMemoryService 提供了适合测试目的的临时存储解决方案，但数据不会在应用程序重启后保留。对于生产环境，通常使用 VertexAiRagMemoryService。此服务利用 Google Cloud 的检索增强生成（RAG）服务，实现可扩展、持久和语义搜索功能（另外，请参阅第 14 章关于 RAG）。

```python
# 示例：使用 VertexAiRagMemoryService
# 这适用于 GCP 上的可扩展生产，利用
# Vertex AI RAG（检索增强生成）实现持久的、
# 可搜索的内存。
# 需要：pip install google-adk[vertexai]，GCP
# 设置/身份验证和 Vertex AI RAG Corpus。
from google.adk.memory import VertexAiRagMemoryService

# 您的 Vertex AI RAG Corpus 的资源名称
RAG_CORPUS_RESOURCE_NAME = "projects/your-gcp-project-id/locations/us-central1/ragCorpora/your-corpus-id" # 替换为您的 Corpus 资源名称

# 检索行为的可选配置
SIMILARITY_TOP_K = 5 # 要检索的顶部结果数
VECTOR_DISTANCE_THRESHOLD = 0.7 # 向量相似度阈值

memory_service = VertexAiRagMemoryService(
   rag_corpus=RAG_CORPUS_RESOURCE_NAME,
   similarity_top_k=SIMILARITY_TOP_K,
   vector_distance_threshold=VECTOR_DISTANCE_THRESHOLD
)

# 使用此服务时，像 add_session_to_memory
# 和 search_memory 这样的方法将与指定的 Vertex AI
# RAG Corpus 交互。
```

# 实操代码：LangChain 和 LangGraph 中的内存管理

在 LangChain 和 LangGraph 中，Memory 是创建智能且自然的对话应用程序的关键组件。它允许 AI Agent 记住过去交互的信息、从反馈中学习并适应用户偏好。LangChain 的内存功能通过引用存储的历史来丰富当前提示词，然后记录最新交换以供将来使用，从而提供了这一基础。随着 Agent 处理更复杂的任务，这种能力对于效率和用户满意度变得至关重要。

**短期内存：** 这是线程范围的，意味着它跟踪单个会话或线程内的正在进行的对话。它提供即时上下文，但完整的历史记录可能会挑战 LLM 的上下文窗口，可能导致错误或性能不佳。LangGraph 将短期内存作为 Agent 状态的一部分进行管理，该状态通过检查点器持久化，允许随时恢复线程。

**长期内存：** 这存储跨会话的用户特定或应用程序级数据，并在对话线程之间共享。它保存在自定义"命名空间"中，可以在任何线程中的任何时间调用。LangGraph 提供存储来保存和调用长期记忆，使 Agent 能够无限期地保留知识。

LangChain 提供了几种工具来管理对话历史，从手动控制到链内的自动集成。

**ChatMessageHistory：手动内存管理。** 对于在正式链外直接和简单控制对话历史，ChatMessageHistory 类是理想的选择。它允许手动跟踪对话交换。

```python
from langchain.memory import ChatMessageHistory

# 初始化历史对象
history = ChatMessageHistory()

# 添加用户和 AI 消息
history.add_user_message("我下周要去纽约。")
history.add_ai_message("太好了！这是一个很棒的城市。")

# 访问消息列表
print(history.messages)
```

**ConversationBufferMemory：链的自动化内存**。要将内存直接集成到链中，ConversationBufferMemory 是一个常见的选择。它保存对话的缓冲区并使其可用于您的提示词。其行为可以通过两个关键参数自定义：

* memory_key：指定提示词中将保存聊天历史的变量名的字符串。默认为"history"。
* return_messages：决定历史格式的布尔值。
  * 如果为 False（默认），它返回单个格式化字符串，这对于标准 LLM 是理想的。
  * 如果为 True，它返回消息对象列表，这是聊天模型的推荐格式。

```python
from langchain.memory import ConversationBufferMemory

# 初始化内存
memory = ConversationBufferMemory()

# 保存对话轮次
memory.save_context({"input": "天气怎么样？"}, {"output": "今天是晴天。"})

# 将内存作为字符串加载
print(memory.load_memory_variables({}))
```

将此内存集成到 LLMChain 中允许模型访问对话的历史并提供上下文相关的响应

```python
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# 1. 定义 LLM 和提示词
llm = OpenAI(temperature=0)
template = """你是一个有帮助的旅行代理。
之前的对话：
{history}
新问题：{question}
响应："""
prompt = PromptTemplate.from_template(template)

# 2. 配置内存
# memory_key "history" 与提示词中的变量匹配
memory = ConversationBufferMemory(memory_key="history")

# 3. 构建链
conversation = LLMChain(llm=llm, prompt=prompt, memory=memory)

# 4. 运行对话
response = conversation.predict(question="我想预订航班。")
print(response)
response = conversation.predict(question="顺便说一下，我叫 Sam。")
print(response)
response = conversation.predict(question="我的名字是什么？")
print(response)
```

为了提高聊天模型的有效性，建议通过设置 `return_messages=True` 使用消息对象的结构化列表。

```python
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import (
   ChatPromptTemplate,
   MessagesPlaceholder,
   SystemMessagePromptTemplate,
   HumanMessagePromptTemplate,
)

# 1. 定义聊天模型和提示词
llm = ChatOpenAI()
prompt = ChatPromptTemplate(
   messages=[
       SystemMessagePromptTemplate.from_template("你是一个友好的助手。"),
       MessagesPlaceholder(variable_name="chat_history"),
       HumanMessagePromptTemplate.from_template("{question}")
   ]
)

# 2. 配置内存
# return_messages=True 对于聊天模型是必不可少的
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# 3. 构建链
conversation = LLMChain(llm=llm, prompt=prompt, memory=memory)

# 4. 运行对话
response = conversation.predict(question="嗨，我是 Jane。")
print(response)
response = conversation.predict(question="你记得我的名字吗？")
print(response)
```

**长期内存类型**：长期内存允许系统在不同对话中保留信息，提供更深层次的上下文和个性化。它可以分解为类似于人类记忆的三种类型：

* **语义记忆：记住事实：** 这涉及保留特定事实和概念，例如用户偏好或领域知识。它用于基础 Agent 的响应，导致更个性化和相关的交互。此信息可以作为持续更新的用户"配置文件"（JSON 文档）或作为单个事实文档的"集合"进行管理。
* **情景记忆：记住经历：** 这涉及回忆过去的事件或行动。对于 AI Agent，情景记忆通常用于记住如何完成任务。在实践中，它经常通过少样本示例提示词实现，其中 Agent 从过去成功的交互序列中学习以正确执行任务。
* **程序记忆：记住规则：** 这是关于如何执行任务的记忆——Agent 的核心指令和行为，通常包含在其系统提示词中。Agent 修改自己的提示词以适应和改进是常见的。一种有效的技术是"反思"，其中 Agent 被提示其当前指令和最近的交互，然后被要求改进自己的指令。

下面是演示 Agent 如何使用反思来更新存储在 LangGraph BaseStore 中的程序记忆的伪代码

```python
# 更新 agent 指令的节点
def update_instructions(state: State, store: BaseStore):
   namespace = ("instructions",)
   # 从存储中获取当前指令
   current_instructions = store.search(namespace)[0]
   
   # 创建提示词要求 LLM 反思对话
   # 并生成新的、改进的指令
   prompt = prompt_template.format(
       instructions=current_instructions.value["instructions"],
       conversation=state["messages"]
   )
   
   # 从 LLM 获取新指令
   output = llm.invoke(prompt)
   new_instructions = output['new_instructions']
   
   # 将更新的指令保存回存储
   store.put(("agent_instructions",), "agent_a", {"instructions": new_instructions})

# 使用指令生成响应的节点
def call_model(state: State, store: BaseStore):
   namespace = ("agent_instructions", )
   # 从存储中检索最新指令
   instructions = store.get(namespace, key="agent_a")[0]
   
   # 使用检索到的指令格式化提示词
   prompt = prompt_template.format(instructions=instructions.value["instructions"])
   # ... 应用程序逻辑继续
```

LangGraph 将长期记忆存储为存储中的 JSON 文档。每个记忆都在自定义命名空间（如文件夹）和不同的键（如文件名）下组织。这种分层结构允许轻松组织和检索信息。以下代码演示了如何使用 InMemoryStore 放置、获取和搜索记忆。

```python
from langgraph.store.memory import InMemoryStore

# 真实嵌入函数的占位符
def embed(texts: list[str]) -> list[list[float]]:
   # 在真实应用程序中，使用适当的嵌入模型
   return [[1.0, 2.0] for _ in texts]

# 初始化内存存储。对于生产，使用数据库支持的存储。
store = InMemoryStore(index={"embed": embed, "dims": 2})

# 为特定用户和应用程序上下文定义命名空间
user_id = "my-user"
application_context = "chitchat"
namespace = (user_id, application_context)

# 1. 将记忆放入存储
store.put(
   namespace,
   "a-memory",  # 此记忆的键
   {
       "rules": [
           "用户喜欢简短、直接的语言",
           "用户只说英语和 python",
       ],
       "my-key": "my-value",
   },
)

# 2. 通过其命名空间和键获取记忆
item = store.get(namespace, "a-memory")
print("检索的项目：", item)

# 3. 在命名空间内搜索记忆，按内容过滤
# 并按与查询的向量相似度排序。
items = store.search(
   namespace,
   filter={"my-key": "my-value"},
   query="语言偏好"
)
print("搜索结果：", items)
```

# Vertex Memory Bank

Memory Bank 是 Vertex AI Agent Engine 中的托管服务，为 Agent 提供持久的长期内存。该服务使用 Gemini 模型异步分析对话历史以提取关键事实和用户偏好。

此信息持久存储，按定义的范围（如用户 ID）组织，并智能更新以整合新数据并解决矛盾。在开始新会话时，Agent 通过完全数据调用或使用嵌入的相似性搜索来检索相关记忆。此过程允许 Agent 跨会话维护连续性并根据回忆的信息个性化响应。

Agent 的 runner 与 VertexAiMemoryBankService 交互，后者首先初始化。此服务处理 Agent 对话期间生成的记忆的自动存储。每个记忆都标记有唯一的 USER_ID 和 APP_NAME，确保将来准确检索。

```python
from google.adk.memory import VertexAiMemoryBankService

agent_engine_id = agent_engine.api_resource.name.split("/")[-1]
memory_service = VertexAiMemoryBankService(
   project="PROJECT_ID",
   location="LOCATION",
   agent_engine_id=agent_engine_id
)

session = await session_service.get_session(
   app_name=app_name,
   user_id="USER_ID",
   session_id=session.id
)

await memory_service.add_session_to_memory(session)
```

Memory Bank 提供与 Google ADK 的无缝集成，提供即开即用的体验。对于使用其他 Agent 框架（如 LangGraph 和 CrewAI）的用户，Memory Bank 还通过直接 API 调用提供支持。演示这些集成的在线代码示例可供感兴趣的读者使用。

# 概览

**什么**：Agent 系统需要记住过去交互的信息以执行复杂任务并提供连贯的体验。没有内存机制，Agent 是无状态的，无法维护对话上下文、从经验中学习或为用户个性化响应。这从根本上将它们限制在简单的、一次性交互中，无法处理多步骤过程或不断变化的用户需求。核心问题是如何有效管理单个对话的即时临时信息和随时间收集的大量持久知识。

**为什么：** 标准化解决方案是实现区分短期和长期存储的双组件内存系统。短期的上下文内存在 LLM 的上下文窗口内保存最近的交互数据以维护对话流程。对于必须持久的信息，长期内存解决方案使用外部数据库，通常是向量存储，以实现高效的语义检索。像 Google ADK 这样的 Agent 框架提供特定组件来管理这一点，例如用于对话线程的 Session 和用于其临时数据的 State。专用的 MemoryService 用于与长期知识库交互，允许 Agent 检索相关的过去信息并将其纳入其当前上下文。

**经验法则：** 当 Agent 需要做的不仅仅是回答单个问题时，使用此模式。对于必须在整个对话中维护上下文、跟踪多步骤任务进度或通过回忆用户偏好和历史来个性化交互的 Agent，这是必不可少的。每当 Agent 预期基于过去的成功、失败或新获得的信息进行学习或适应时，实现内存管理。

**视觉摘要**

**![][image1]**

图 1：内存管理设计模式

# 关键要点

快速回顾关于内存管理的要点：

* 内存对于 Agent 跟踪事物、学习和个性化交互非常重要。
* 对话式 AI 依赖于单个聊天中即时上下文的短期内存和跨多个会话的持久知识的长期内存。
* 短期内存（即时的东西）是临时的，通常受到 LLM 的上下文窗口或框架如何传递上下文的限制。
* 长期内存（持久的东西）使用向量数据库等外部存储跨不同聊天保存信息，并通过搜索访问。
* 像 ADK 这样的框架具有特定部分，如 Session（聊天线程）、State（临时聊天数据）和 MemoryService（可搜索的长期知识）来管理内存。
* ADK 的 SessionService 处理聊天会话的整个生命周期，包括其历史（events）和临时数据（state）。
* ADK 的 session.state 是临时聊天数据的字典。前缀（user:、app:、temp:）告诉您数据属于哪里以及是否持久。
* 在 ADK 中，您应该通过在添加事件时使用 EventActions.state_delta 或 output_key 来更新状态，而不是直接更改状态字典。
* ADK 的 MemoryService 用于将信息放入长期存储并让 Agent 搜索它，通常使用工具。
* LangChain 提供像 ConversationBufferMemory 这样的实用工具，自动将单个对话的历史注入提示词，使 Agent 能够回忆即时上下文。
* LangGraph 通过使用存储来保存和检索跨不同用户会话的语义事实、情景经验或甚至可更新的程序规则，实现高级的长期内存。
* Memory Bank 是一种托管服务，通过自动提取、存储和调用用户特定信息，为 Agent 提供持久的长期内存，以在 Google 的 ADK、LangGraph 和 CrewAI 等框架中实现个性化、持续的对话。

# 结论

本章深入探讨了 Agent 系统的内存管理的真正重要工作，展示了短暂上下文和长期持久知识之间的区别。我们讨论了这些类型的内存如何设置以及在构建更智能的 Agent 时在哪里看到它们的使用。我们详细了解了 Google ADK 如何为您提供像 Session、State 和 MemoryService 这样的特定部分来处理这一点。既然我们已经介绍了 Agent 如何记住事物（短期和长期），我们可以继续了解它们如何学习和适应。下一个模式"学习和适应"是关于 Agent 根据新经验或数据改变其思考、行动或所知的方式。

# 参考文献

1. ADK Memory, [https://google.github.io/adk-docs/sessions/memory/](https://google.github.io/adk-docs/sessions/memory/)
2. LangGraph Memory, [https://langchain-ai.github.io/langgraph/concepts/memory/](https://langchain-ai.github.io/langgraph/concepts/memory/)
3. Vertex AI Agent Engine Memory Bank, [https://cloud.google.com/blog/products/ai-machine-learning/vertex-ai-memory-bank-in-public-preview](https://cloud.google.com/blog/products/ai-machine-learning/vertex-ai-memory-bank-in-public-preview)
   

[image1]: ../images/chapter-8/image1.png