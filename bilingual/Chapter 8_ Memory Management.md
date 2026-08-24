# Chapter 8: Memory Management

# 第 8 章：记忆管理

Effective memory management is crucial for intelligent agents to retain information. Agents require different types of memory, much like humans, to operate efficiently. This chapter delves into memory management, specifically addressing the immediate (short-term) and persistent (long-term) memory requirements of agents.

有效的记忆管理对于智能体保留信息至关重要。与人类类似，智能体需要不同类型的记忆才能高效运行。本章深入探讨记忆管理，重点关注智能体的短期记忆和持久（长期）记忆需求。

In agent systems, memory refers to an agent's ability to retain and utilize information from past interactions, observations, and learning experiences. This capability allows agents to make informed decisions, maintain conversational context, and improve over time. Agent memory is generally categorized into two main types:

在智能体系统中，记忆指智能体保留和利用过去交互、观察和学习经验中信息的能力。这种能力帮助智能体做出明智决策、维护对话上下文并持续改进。智能体记忆通常分为两大主要类型：

* **Short-Term Memory (Contextual Memory):** Similar to working memory, this holds information currently being processed or recently accessed. For agents using large language models (LLMs), short-term memory primarily exists within the context window. This window contains recent messages, agent replies, tool usage results, and agent reflections from the current interaction, all of which inform the LLM's subsequent responses and actions. The context window has a limited capacity, restricting the amount of recent information an agent can directly access. Efficient short-term memory management involves keeping the most relevant information within this limited space, possibly through techniques like summarizing older conversation segments or emphasizing key details. The advent of models with 'long context' windows simply expands the size of this short-term memory, allowing more information to be held within a single interaction. However, this context is still ephemeral and is lost once the session concludes, and it can be costly and inefficient to process every time. Consequently, agents require separate memory types to achieve true persistence, recall information from past interactions, and build a lasting knowledge base.

* **短期记忆（上下文记忆）：** 类似于工作记忆，保存当前正在处理或最近访问的信息。对于使用大语言模型（LLM）的智能体，短期记忆主要存在于上下文窗口中。该窗口包含最近消息、智能体回复、工具使用结果以及当前交互中的其他相关信息，所有这些都为 LLM 的后续响应和操作提供信息支撑。上下文窗口容量有限，制约了智能体可访问的近期信息量。高效的短期记忆管理需要在有限空间内保留最相关信息，可能通过总结旧对话片段或突出关键细节等技术实现。具有"长上下文"窗口的模型只是扩展了短期记忆容量，允许单次交互保存更多信息。然而，这种上下文仍是临时的，会话结束即丢失，且每次处理可能成本高昂。因此，智能体需要独立的记忆类型来实现真正的持久性、调用过往信息并建立持久知识库。

* **Long-Term Memory (Persistent Memory):** This acts as a repository for information agents need to retain across various interactions, tasks, or extended periods, akin to long-term knowledge bases. Data is typically stored outside the agent's immediate processing environment, often in databases, knowledge graphs, or vector databases. In vector databases, information is converted into numerical vectors and stored, enabling agents to retrieve data based on semantic similarity rather than exact keyword matches, a process known as semantic search. When an agent needs information from long-term memory, it queries the external storage, retrieves relevant data, and integrates it into the short-term context for immediate use, thus combining prior knowledge with the current interaction.

* **长期记忆（持久记忆）：** 作为智能体在交互、任务或更长时间内所需信息的存储库，类似于长期知识库。数据通常存储在智能体环境之外，常见于数据库、知识图谱或向量数据库中。在向量数据库中，信息被转换为数字向量存储，使智能体能通过相似性（而非精确关键字匹配）检索数据，这个过程称为语义搜索。当智能体需要长期记忆时，会查询外部存储、检索相关数据并集成到短期上下文中供即时使用，从而将先前知识与当前交互结合起来。

## Practical Applications & Use Cases

## 实际应用与用例

Memory management is vital for agents to track information and perform intelligently over time. This is essential for agents to surpass basic question-answering capabilities. Applications include:

记忆管理对于智能体跟踪信息并随时间智能执行至关重要。这是智能体超越基本问答能力的必要条件。主要应用包括：

* **Chatbots and Conversational AI:** Maintaining conversation flow relies on short-term memory. Chatbots require remembering prior user inputs to provide coherent responses. Long-term memory enables chatbots to recall user preferences, past issues, or prior discussions, offering personalized and continuous interactions.

* **聊天机器人与对话式 AI：** 维护对话流程依赖短期记忆。聊天机器人需要记住先前用户输入以提供连贯响应。长期记忆使聊天机器人能回忆用户偏好、过往问题或先前讨论，提供个性化和持续的交互体验。

* **Task-Oriented Agents:** Agents managing multi-step tasks need short-term memory to track previous steps, current progress, and overall goals. This information might reside in the task's context or temporary storage. Long-term memory is crucial for accessing specific user-related data not in the immediate context.

* **面向任务的智能体：** 管理多步骤任务的智能体使用短期记忆跟踪先前步骤、当前进度和总体目标。此类信息可能驻留在任务上下文或临时存储中。长期记忆对于访问不在即时上下文中的特定用户相关数据至关重要。

* **Personalized Experiences:** Agents offering tailored interactions utilize long-term memory to store and retrieve user preferences, past behaviors, and personal information. This allows agents to adapt their responses and suggestions.

* **个性化体验：** 提供定制交互的智能体使用长期记忆存储和检索用户偏好、过往行为和个人信息。这使智能体能够提供个性化响应和建议。

* **Learning and Improvement:** Agents can refine their performance by learning from past interactions. Successful strategies, mistakes, and new information are stored in long-term memory, facilitating future adaptations. Reinforcement learning agents store learned strategies or knowledge in this way.

* **学习与改进：** 智能体通过从过去交互中学习来提升性能。成功策略、错误和新信息存储于长期记忆中，促进未来适应。强化学习智能体可以存储学习策略或知识。

* **Information Retrieval (RAG):** Agents designed for answering questions access a knowledge base, their long-term memory, often implemented within Retrieval Augmented Generation (RAG). The agent retrieves relevant documents or data to inform its responses.

* **信息检索（RAG）：** 设计用于回答问题的智能体访问知识库（即其长期记忆），通常在检索增强生成（RAG）中实现。智能体检索相关文档或数据以指导其响应。

* **Autonomous Systems:** Robots or self-driving cars require memory for maps, routes, object locations, and learned behaviors. This involves short-term memory for immediate surroundings and long-term memory for general environmental knowledge.

* **自主系统：** 机器人或自动驾驶汽车需要记忆来存储地图、路线、对象位置和学习行为。这涉及用于即时环境的短期记忆和用于通用环境知识的长期记忆。

Memory enables agents to maintain history, learn, personalize interactions, and manage complex, time-dependent problems.

记忆使智能体维护历史、持续学习、个性化交互并管理复杂的时间依赖问题。

## Hands-On Code: Memory Management in Google Agent Developer Kit (ADK)

## 实操代码：Google ADK 中的记忆管理

The Google Agent Developer Kit (ADK) offers a structured method for managing context and memory, including components for practical application. A solid grasp of ADK's Session, State, and Memory is vital for building agents that need to retain information.

Google 智能体开发工具包（ADK）提供了结构化的上下文和记忆管理方法，包含实际应用组件。深入理解 ADK 的 Session、State 和 Memory 对构建需保留信息的智能体至关重要。

Just as in human interactions, agents require the ability to recall previous exchanges to conduct coherent and natural conversations. ADK simplifies context management through three core concepts and their associated services.

与人类交互类似，智能体需要能够回忆先前交流以进行连贯对话。ADK 通过三个核心概念简化了上下文管理：

Every interaction with an agent can be considered a unique conversation thread. Agents might need to access data from earlier interactions. ADK structures this as follows:

每次与智能体的交互可视为独特的对话线程，智能体可能需要访问早期数据。ADK 将其结构化如下：

* **Session:** An individual chat thread that logs messages and actions (Events) for that specific interaction, also storing temporary data (State) relevant to that conversation.

* **Session（会话）：** 独立的聊天线程，记录该特定交互的消息和操作（Events），同时存储与该对话相关的临时数据（State）。

* **State (session.state):** Data stored within a Session, containing information relevant only to the current, active chat thread.

* **State（状态）（session.state）：** 存储在 Session 中的数据，包含仅与当前活动聊天线程相关的信息。

* **Memory:** A searchable repository of information sourced from various past chats or external sources, serving as a resource for data retrieval beyond the immediate conversation.

* **Memory（记忆）：** 来自各种过往聊天或外部来源信息的可搜索存储库，作为超出即时对话范围的数据检索资源。

ADK provides dedicated services for managing critical components essential for building complex, stateful, and context-aware agents. The SessionService manages chat threads (Session objects) by handling their initiation, recording, and termination, while the MemoryService oversees the storage and retrieval of long-term knowledge (Memory).

ADK 为构建复杂、有状态和上下文感知的智能体提供专用服务：SessionService 管理聊天线程（启动、记录和终止 Session 对象），MemoryService 监督长期知识（Memory）的存储和检索。

Both the SessionService and MemoryService offer various configuration options, allowing users to choose storage methods based on application needs. In-memory options are available for testing purposes, though data will not persist across restarts. For persistent storage and scalability, ADK also supports database and cloud-based services.

SessionService 和 MemoryService 均提供多种配置选项，允许根据应用需求选择存储方法。内存选项适用于测试目的（数据不持久），持久存储和可扩展需求则支持数据库和云服务。

## Session: Keeping Track of Each Chat

## Session：跟踪每次聊天

A Session object in ADK is designed to track and manage individual chat threads. Upon initiation of a conversation with an agent, the SessionService generates a Session object, represented as `google.adk.sessions.Session`. This object encapsulates all data relevant to a specific conversation thread, including unique identifiers (id, app_name, user_id), a chronological record of events as Event objects, a storage area for session-specific temporary data known as state, and a timestamp indicating the last update (last_update_time). Developers typically interact with Session objects indirectly through the SessionService. The SessionService is responsible for managing the lifecycle of conversation sessions, which includes initiating new sessions, resuming previous sessions, recording session activity (including state updates), identifying active sessions, and managing the removal of session data. The ADK provides several SessionService implementations with varying storage mechanisms for session history and temporary data, such as the InMemorySessionService, which is suitable for testing but does not provide data persistence across application restarts.

ADK 中的 Session 对象旨在跟踪和管理单个聊天线程。在与智能体对话时，SessionService 会生成一个 Session 对象，表示为 `google.adk.sessions.Session`。此对象封装了与特定对话线程相关的所有数据，包括唯一标识符（id、app_name、user_id）、作为 Event 对象的事件的时间顺序记录、用于会话特定临时数据的存储区域（称为 state）以及指示最后更新的时间戳（last_update_time）。开发人员通常通过 SessionService 间接与 Session 对象交互。SessionService 负责管理对话会话的生命周期，包括启动新会话、恢复先前的会话、记录会话活动（包括状态更新）、识别活动会话以及管理会话数据的删除。ADK 提供几种具有不同存储机制的 SessionService 实现，用于会话历史和临时数据，例如 InMemorySessionService，适合测试但不提供跨应用程序重启的数据持久性。

```python
## Example: Using InMemorySessionService
## This is suitable for local development and testing where data
## persistence across application restarts is not required.
from google.adk.sessions import InMemorySessionService

session_service = InMemorySessionService()
```

Then there's DatabaseSessionService if you want reliable saving to a database you manage.

然后是 DatabaseSessionService，如果您想可靠地保存到您管理的数据库。

```python
## Example: Using DatabaseSessionService
## This is suitable for production or development requiring persistent storage.
## You need to configure a database URL (e.g., for SQLite, PostgreSQL, etc.).
## Requires: pip install google-adk[sqlalchemy] and a database driver (e.g., psycopg2 for PostgreSQL)
from google.adk.sessions import DatabaseSessionService

## Example using a local SQLite file:
db_url = "sqlite:///./my_agent_data.db"
session_service = DatabaseSessionService(db_url=db_url)
```

Besides, there's VertexAiSessionService which uses Vertex AI infrastructure for scalable production on Google Cloud.

此外，还有 VertexAiSessionService，它使用 Vertex AI 基础设施在 Google Cloud 上进行可扩展的生产。

```python
## Example: Using VertexAiSessionService
## This is suitable for scalable production on Google Cloud Platform, leveraging
## Vertex AI infrastructure for session management.
## Requires: pip install google-adk[vertexai] and GCP setup/authentication
from google.adk.sessions import VertexAiSessionService

PROJECT_ID = "your-gcp-project-id" # Replace with your GCP project ID
LOCATION = "us-central1" # Replace with your desired GCP location

## The app_name used with this service should correspond to the Reasoning Engine ID or name
REASONING_ENGINE_APP_NAME = "projects/your-gcp-project-id/locations/us-central1/reasoningEngines/your-engine-id" # Replace with your Reasoning Engine resource name

session_service = VertexAiSessionService(project=PROJECT_ID, location=LOCATION)

## When using this service, pass REASONING_ENGINE_APP_NAME to service methods:
## session_service.create_session(app_name=REASONING_ENGINE_APP_NAME, ...)
## session_service.get_session(app_name=REASONING_ENGINE_APP_NAME, ...)
## session_service.append_event(session, event, app_name=REASONING_ENGINE_APP_NAME)
## session_service.delete_session(app_name=REASONING_ENGINE_APP_NAME, ...)
```

Choosing an appropriate SessionService is crucial as it determines how the agent's interaction history and temporary data are stored and their persistence.

选择适当的 SessionService 至关重要，因为它决定了智能体交互历史和临时数据的存储方式及其持久性。

Each message exchange involves a cyclical process: A message is received, the Runner retrieves or establishes a Session using the SessionService, the agent processes the message using the Session's context (state and historical interactions), the agent generates a response and may update the state, the Runner encapsulates this as an Event, and the session_service.append_event method records the new event and updates the state in storage. The Session then awaits the next message. Ideally, the delete_session method is employed to terminate the session when the interaction concludes. This process illustrates how the SessionService maintains continuity by managing the Session-specific history and temporary data.

每次消息交换都涉及一个循环过程：接收消息，Runner 使用 SessionService 检索或建立 Session，Agent 使用 Session 的上下文（状态和历史交互）处理消息，Agent 生成响应并可能更新状态，Runner 将其封装为 Event，session_service.append_event 方法记录新事件并更新存储中的状态。然后 Session 等待下一条消息。理想情况下，当交互结束时使用 delete_session 方法终止会话。此过程说明了 SessionService 如何通过管理特定于 Session 的历史和临时数据来维护连续性。

## State: The Session's Scratchpad

## State：Session 的草稿本

In the ADK, each Session, representing a chat thread, includes a state component akin to an agent's temporary working memory for the duration of that specific conversation. While session.events logs the entire chat history, session.state stores and updates dynamic data points relevant to the active chat.

在 ADK 中，每个代表聊天线程的 Session 都包含 state 组件，类似于智能体在特定对话期间的临时工作记忆。虽然 session.events 记录整个聊天历史，但 session.state 存储和更新与活动聊天相关的动态数据点。

Fundamentally, session.state operates as a dictionary, storing data as key-value pairs. Its core function is to enable the agent to retain and manage details essential for coherent dialogue, such as user preferences, task progress, incremental data collection, or conditional flags influencing subsequent agent actions.

从根本上讲，session.state 作为字典运行，以键值对形式存储数据。其核心功能是使智能体保留和管理对连贯对话至关重要的详细信息，如用户偏好、任务进度、增量数据收集或影响后续智能体行为的事件标志。

The state's structure comprises string keys paired with values of serializable Python types, including strings, numbers, booleans, lists, and dictionaries containing these basic types. State is dynamic, evolving throughout the conversation. The permanence of these changes depends on the configured SessionService.

状态结构包含字符串键与可序列化 Python 类型值的配对，包括字符串、数字、布尔值、列表及包含这些基本类型的字典。State 是动态的，在整个对话过程中不断演变。这些更改的持久性取决于配置的 SessionService。

State organization can be achieved using key prefixes to define data scope and persistence. Keys without prefixes are session-specific.

可使用键前缀定义数据范围和持久性来组织状态：

* The user: prefix associates data with a user ID across all sessions.

* user: 前缀将数据与跨所有会话的用户 ID 关联。

* The app: prefix designates data shared among all users of the application.

* app: 前缀指定应用程序所有用户间共享的数据。

* The temp: prefix indicates data valid only for the current processing turn and is not persistently stored.

* temp: 前缀指示仅对当前处理轮次有效且不持久存储的数据。

The agent accesses all state data through a single session.state dictionary. The SessionService handles data retrieval, merging, and persistence. State should be updated upon adding an Event to the session history via session_service.append_event(). This ensures accurate tracking, proper saving in persistent services, and safe handling of state changes.

Agent 通过单个 session.state 字典访问所有状态数据。SessionService 处理数据检索、合并和持久性。应在通过 session_service.append_event() 向会话历史添加 Event 时更新状态。这确保了准确跟踪、在持久服务中的正确保存以及状态更改的安全处理。

1. **The Simple Way: Using output_key (for Agent Text Replies):** This is the easiest method if you just want to save your agent's final text response directly into the state. When you set up your LlmAgent, just tell it the output_key you want to use. The Runner sees this and automatically creates the necessary actions to save the response to the state when it appends the event. Let's look at a code example demonstrating state update via output_key.

1. **简单方法：使用 output_key（用于智能体回复）：** 如果您只想将智能体的文本响应直接保存到状态中，这是最简单的方法。设置 LlmAgent 时，只需告诉它要使用的 output_key。Runner 看到这一点并在追加事件时自动创建必要的操作以将响应保存到状态。让我们看一个通过 output_key 演示状态更新的代码示例。

```python
## Import necessary classes from the Google Agent Developer Kit (ADK)
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService, Session
from google.adk.runners import Runner
from google.genai.types import Content, Part

## Define an LlmAgent with an output_key.
greeting_agent = LlmAgent(
   name="Greeter",
   model="gemini-2.0-flash",
   instruction="Generate a short, friendly greeting.",
   output_key="last_greeting"
)

## --- Setup Runner and Session ---
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
print(f"Initial state: {session.state}")

## --- Run the Agent ---
user_message = Content(parts=[Part(text="Hello")])
print("\n--- Running the agent ---")
for event in runner.run(
   user_id=user_id,
   session_id=session_id,
   new_message=user_message
):
   if event.is_final_response():
     print("Agent responded.")

## --- Check Updated State ---
## Correctly check the state *after* the runner has finished processing all events.
updated_session = session_service.get_session(app_name, user_id, session_id)
print(f"\nState after agent run: {updated_session.state}")
```

Behind the scenes, the Runner sees your output_key and automatically creates the necessary actions with a state_delta when it calls append_event.

在幕后，Runner 看到您的 output_key，并在调用 append_event 时自动创建具有 state_delta 的必要操作。

2. **The Standard Way: Using EventActions.state_delta (for More Complicated Updates):** For times when you need to do more complex things – like updating several keys at once, saving things that aren't just text, targeting specific scopes like user: or app:, or making updates that aren't tied to the agent's final text reply – you'll manually build a dictionary of your state changes (the state_delta) and include it within the EventActions of the Event you're appending. Let's look at one example:

2. **标准方法：使用 EventActions.state_delta（用于更复杂的更新）：** 对于需要执行更复杂操作的时候——例如一次更新多个键、保存不只是文本的内容、针对特定范围（如 user: 或 app:）或进行与智能体文本回复无关的更新——您将手动构建状态更改的字典（state_delta）并将其包含在要追加的 Event 的 EventActions 中。让我们看一个例子：

```python
import time
from google.adk.tools.tool_context import ToolContext
from google.adk.sessions import InMemorySessionService

## --- Define the Recommended Tool-Based Approach ---
def log_user_login(tool_context: ToolContext) -> dict:
   """
   Updates the session state upon a user login event.
   This tool encapsulates all state changes related to a user login.
   Args:
       tool_context: Automatically provided by ADK, gives access to session state.
   Returns:
       A dictionary confirming the action was successful.
   """
   # Access the state directly through the provided context.
   state = tool_context.state
   
   # Get current values or defaults, then update the state.
   # This is much cleaner and co-locates the logic.
   login_count = state.get("user:login_count", 0) + 1
   state["user:login_count"] = login_count
   state["task_status"] = "active"
   state["user:last_login_ts"] = time.time()
   state["temp:validation_needed"] = True
   
   print("State updated from within the `log_user_login` tool.")
   
   return {
       "status": "success",
       "message": f"User login tracked. Total logins: {login_count}."
   }

## --- Demonstration of Usage ---
## In a real application, an LLM Agent would decide to call this tool.
## Here, we simulate a direct call for demonstration purposes.

## 1. Setup
session_service = InMemorySessionService()
app_name, user_id, session_id = "state_app_tool", "user3", "session3"
session = session_service.create_session(
   app_name=app_name,
   user_id=user_id,
   session_id=session_id,
   state={"user:login_count": 0, "task_status": "idle"}
)
print(f"Initial state: {session.state}")

## 2. Simulate a tool call (in a real app, the ADK Runner does this)
## We create a ToolContext manually just for this standalone example.
from google.adk.tools.tool_context import InvocationContext
mock_context = ToolContext(
   invocation_context=InvocationContext(
       app_name=app_name, user_id=user_id, session_id=session_id,
       session=session, session_service=session_service
   )
)

## 3. Execute the tool
log_user_login(mock_context)

## 4. Check the updated state
updated_session = session_service.get_session(app_name, user_id, session_id)
print(f"State after tool execution: {updated_session.state}")

## Expected output will show the same state change as the
## "Before" case,
## but the code organization is significantly cleaner
## and more robust.
```

This code demonstrates a tool-based approach for managing user session state in an application. It defines a function *log_user_login*, which acts as a tool. This tool is responsible for updating the session state when a user logs in.

此代码演示了一种基于工具的方法来管理应用程序中的用户会话状态。它定义了一个函数 *log_user_login*，充当工具。此工具负责在用户登录时更新会话状态。

The function takes a ToolContext object, provided by the ADK, to access and modify the session's state dictionary. Inside the tool, it increments a *user:login_count*, sets the *task_status* to "active", records the *user:last_login_ts (timestamp)*, and adds a temporary flag temp:validation_needed.

该函数接受由 ADK 提供的 ToolContext 对象，以访问和修改会话的状态字典。在工具内部，它递增 *user:login_count*，将 *task_status* 设置为"active"，记录 *user:last_login_ts（时间戳）*，并添加临时标志 temp:validation_needed。

The demonstration part of the code simulates how this tool would be used. It sets up an in-memory session service and creates an initial session with some predefined state. A ToolContext is then manually created to mimic the environment in which the ADK Runner would execute the tool. The log_user_login function is called with this mock context. Finally, the code retrieves the session again to show that the state has been updated by the tool's execution. The goal is to show how encapsulating state changes within tools makes the code cleaner and more organized compared to directly manipulating state outside of tools.

代码的演示部分模拟了如何使用此工具。它设置了内存会话服务并创建了具有一些预定义状态的初始会话。然后手动创建 ToolContext 以模拟 ADK Runner 执行工具的环境。使用此模拟上下文调用 log_user_login 函数。最后，代码再次检索会话以显示状态已通过工具的执行更新。目标是展示将状态更改封装在工具中如何使代码比直接在工具外部操作状态更清晰、更有组织。

Note that direct modification of the `session.state` dictionary after retrieving a session is strongly discouraged as it bypasses the standard event processing mechanism. Such direct changes will not be recorded in the session's event history, may not be persisted by the selected `SessionService`, could lead to concurrency issues, and will not update essential metadata such as timestamps. The recommended methods for updating the session state are using the `output_key` parameter on an `LlmAgent` (specifically for the agent's final text responses) or including state changes within `EventActions.state_delta` when appending an event via `session_service.append_event()`. The `session.state` should primarily be used for reading existing data.

请注意，强烈不建议在检索会话后直接修改 `session.state` 字典，因为它会绕过标准事件处理机制。这种直接更改不会记录在会话的事件历史中，可能不会被选定的 `SessionService` 持久化，可能导致并发问题，并且不会更新时间戳等基本元数据。更新会话状态的推荐方法是在 `LlmAgent` 上使用 `output_key` 参数（专门用于智能体最终文本响应）或在通过 `session_service.append_event()` 追加事件时在 `EventActions.state_delta` 中包含状态更改。`session.state` 应主要用于读取现有数据。

To recap, when designing your state, keep it simple, use basic data types, give your keys clear names and use prefixes correctly, avoid deep nesting, and always update state using the append_event process.

总而言之，在设计状态时，保持简单，使用基本数据类型，为键提供清晰的名称并正确使用前缀，避免深度嵌套，并始终使用 append_event 过程更新状态。

## Memory: Long-Term Knowledge with MemoryService

## Memory：使用 MemoryService 的长期知识

In agent systems, the Session component maintains a record of the current chat history (events) and temporary data (state) specific to a single conversation. However, for agents to retain information across multiple interactions or access external data, long-term knowledge management is necessary. This is facilitated by the MemoryService.

在智能体中，Session 组件维护当前聊天历史（events）和特定于单个对话的临时数据（state）的记录。然而，为使智能体在交互中保留信息或访问外部数据，需要长期知识管理。这由 MemoryService 促进实现。

```python
## Example: Using InMemoryMemoryService
## This is suitable for local development and testing where data
## persistence across application restarts is not required.
## Memory content is lost when the app stops.
from google.adk.memory import InMemoryMemoryService

memory_service = InMemoryMemoryService()
```

Session and State can be conceptualized as short-term memory for a single chat session, whereas the Long-Term Knowledge managed by the MemoryService functions as a persistent and searchable repository. This repository may contain information from multiple past interactions or external sources. The MemoryService, as defined by the BaseMemoryService interface, establishes a standard for managing this searchable, long-term knowledge. Its primary functions include adding information, which involves extracting content from a session and storing it using the add_session_to_memory method, and retrieving information, which allows an agent to query the store and receive relevant data using the search_memory method.

Session 和 State 可概念化为单个聊天会话的短期记忆，而由 MemoryService 管理的长期知识则充当持久且可搜索的存储库。此存储库可能包含来自多个过往交互或外部来源的信息。由 BaseMemoryService 接口定义的 MemoryService 为管理这种可搜索的长期知识建立了标准。其主要功能包括添加信息（涉及从会话中提取内容并使用 add_session_to_memory 方法存储）以及检索信息（允许智能体查询该存储库并使用 search_memory 方法接收相关数据）。

The ADK offers several implementations for creating this long-term knowledge store. The InMemoryMemoryService provides a temporary storage solution suitable for testing purposes, but data is not preserved across application restarts. For production environments, the VertexAiRagMemoryService is typically utilized. This service leverages Google Cloud's Retrieval Augmented Generation (RAG) service, enabling scalable, persistent, and semantic search capabilities (Also, refer to the chapter 14 on RAG).

ADK 提供了几种实现来创建这种长期知识存储。InMemoryMemoryService 提供适合测试目的的临时存储解决方案，但数据不会在应用重启后保留。对于生产环境，通常使用 VertexAiRagMemoryService。此服务利用 Google Cloud 的检索增强生成（RAG）服务，实现可扩展、持久和语义搜索功能（另请参阅第 14 章关于 RAG）。

```python
## Example: Using VertexAiRagMemoryService
## This is suitable for scalable production on GCP, leveraging
## Vertex AI RAG (Retrieval Augmented Generation) for persistent,
## searchable memory.
## Requires: pip install google-adk[vertexai], GCP
## setup/authentication, and a Vertex AI RAG Corpus.
from google.adk.memory import VertexAiRagMemoryService

## The resource name of your Vertex AI RAG Corpus
RAG_CORPUS_RESOURCE_NAME = "projects/your-gcp-project-id/locations/us-central1/ragCorpora/your-corpus-id" # Replace with your Corpus resource name

## Optional configuration for retrieval behavior
SIMILARITY_TOP_K = 5 # Number of top results to retrieve
VECTOR_DISTANCE_THRESHOLD = 0.7 # Threshold for vector similarity

memory_service = VertexAiRagMemoryService(
   rag_corpus=RAG_CORPUS_RESOURCE_NAME,
   similarity_top_k=SIMILARITY_TOP_K,
   vector_distance_threshold=VECTOR_DISTANCE_THRESHOLD
)

## When using this service, methods like add_session_to_memory
## and search_memory will interact with the specified Vertex AI
## RAG Corpus.
```

## Hands-on code: Memory Management in LangChain and LangGraph

## 实操代码：LangChain 和 LangGraph 中的记忆管理

In LangChain and LangGraph, Memory is a critical component for creating intelligent and natural-feeling conversational applications. It allows an AI agent to remember information from past interactions, learn from feedback, and adapt to user preferences. LangChain's memory feature provides the foundation for this by referencing a stored history to enrich current prompts and then recording the latest exchange for future use. As agents handle more complex tasks, this capability becomes essential for both efficiency and user satisfaction.

在 LangChain 和 LangGraph 中，Memory 是创建智能自然对话应用的关键组件。它使 AI 智能体能够记住过去交互信息、从反馈中学习并适应用户偏好。LangChain 的记忆功能通过引用存储历史来丰富当前提示词，然后记录最新交换供将来使用，从而提供此基础。随着智能体执行复杂任务，这种能力对效率和用户满意度变得至关重要。

**Short-Term Memory:** This is thread-scoped, meaning it tracks the ongoing conversation within a single session or thread. It provides immediate context, but a full history can challenge an LLM's context window, potentially leading to errors or poor performance. LangGraph manages short-term memory as part of the agent's state, which is persisted via a checkpointer, allowing a thread to be resumed at any time.

**短期记忆：** 这是线程范围的，意味着它跟踪单个会话或线程内正在进行的对话。它提供即时上下文，但完整历史可能挑战 LLM 的上下文窗口，导致错误或性能下降。LangGraph 将短期记忆作为智能体的一部分管理，该状态通过检查点器持久化，允许随时恢复线程。

**Long-Term Memory:** This stores user-specific or application-level data across sessions and is shared between conversational threads. It is saved in custom "namespaces" and can be recalled at any time in any thread. LangGraph provides stores to save and recall long-term memories, enabling agents to retain knowledge indefinitely.

**长期记忆：** 存储跨会话的用户特定或应用级数据，在对话线程间共享。它保存在自定义"命名空间"中，可在任何线程的任何时间调用。LangGraph 提供存储来保存和调用长期记忆，使智能体能够无限期保留知识。

LangChain provides several tools for managing conversation history, ranging from manual control to automated integration within chains.

LangChain 提供了多种工具管理对话历史，从手动控制到链内自动集成。

**ChatMessageHistory: Manual Memory Management.** For direct and simple control over a conversation's history outside of a formal chain, the ChatMessageHistory class is ideal. It allows for the manual tracking of dialogue exchanges.

**ChatMessageHistory：手动记忆管理。** 对于在正式链外直接简单控制对话历史，ChatMessageHistory 类是理想选择。它允许手动跟踪对话交换。

```python
from langchain.memory import ChatMessageHistory

## Initialize the history object
history = ChatMessageHistory()

## Add user and AI messages
history.add_user_message("I'm heading to New York next week.")
history.add_ai_message("Great! It's a fantastic city.")

## Access the list of messages
print(history.messages)
```

**ConversationBufferMemory: Automated Memory for Chains**. For integrating memory directly into chains, ConversationBufferMemory is a common choice. It holds a buffer of the conversation and makes it available to your prompt. Its behavior can be customized with two key parameters:

**ConversationBufferMemory：链的自动化记忆。** 要将记忆直接集成到链中，ConversationBufferMemory 是一个常见的选择。它保存对话的缓冲区并使其可用于您的提示词。其行为可以通过两个关键参数自定义：

* memory_key: A string that specifies the variable name in your prompt that will hold the chat history. It defaults to "history".

* memory_key：指定提示词中将保存聊天历史的变量名的字符串。默认为"history"。

* return_messages: A boolean that dictates the format of the history.
  * If False (the default), it returns a single formatted string, which is ideal for standard LLMs.
  * If True, it returns a list of message objects, which is the recommended format for Chat Models.

* return_messages：决定历史格式的布尔值。
  * 如果为 False（默认），它返回单个格式化字符串，这对于标准 LLM 是理想的。
  * 如果为 True，它返回消息对象列表，这是聊天模型的推荐格式。

```python
from langchain.memory import ConversationBufferMemory

## Initialize memory
memory = ConversationBufferMemory()

## Save a conversation turn
memory.save_context({"input": "What's the weather like?"}, {"output": "It's sunny today."})

## Load the memory as a string
print(memory.load_memory_variables({}))
```

Integrating this memory into an LLMChain allows the model to access the conversation's history and provide contextually relevant responses

将此记忆集成到 LLMChain 中允许模型访问对话的历史并提供上下文相关的响应。

```python
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

## 1. Define LLM and Prompt
llm = OpenAI(temperature=0)
template = """You are a helpful travel agent.
Previous conversation: {history}
New question: {question}
Response:"""
prompt = PromptTemplate.from_template(template)

## 2. Configure Memory
## The memory_key "history" matches the variable in the prompt
memory = ConversationBufferMemory(memory_key="history")

## 3. Build the Chain
conversation = LLMChain(llm=llm, prompt=prompt, memory=memory)

## 4. Run the Conversation
response = conversation.predict(question="I want to book a flight.")
print(response)
response = conversation.predict(question="My name is Sam, by the way.")
print(response)
response = conversation.predict(question="What was my name again?")
print(response)
```

For improved effectiveness with chat models, it is recommended to use a structured list of message objects by setting `return_messages=True`.

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

## 1. Define Chat Model and Prompt
llm = ChatOpenAI()
prompt = ChatPromptTemplate(
   messages=[
       SystemMessagePromptTemplate.from_template("You are a friendly assistant."),
       MessagesPlaceholder(variable_name="chat_history"),
       HumanMessagePromptTemplate.from_template("{question}")
   ]
)

## 2. Configure Memory
## return_messages=True is essential for chat models
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

## 3. Build the Chain
conversation = LLMChain(llm=llm, prompt=prompt, memory=memory)

## 4. Run the Conversation
response = conversation.predict(question="Hi, I'm Jane.")
print(response)
response = conversation.predict(question="Do you remember my name?")
print(response)
```

**Types of Long-Term Memory**: Long-term memory allows systems to retain information across different conversations, providing a deeper level of context and personalization. It can be broken down into three types analogous to human memory:

**长期记忆类型**：长期记忆允许系统在不同对话中保留信息，提供更深层次上下文和个性化。可分解为类似人类记忆的三种类型：

* **Semantic Memory: Remembering Facts:** This involves retaining specific facts and concepts, such as user preferences or domain knowledge. It is used to ground an agent's responses, leading to more personalized and relevant interactions. This information can be managed as a continuously updated user "profile" (a JSON document) or as a "collection" of individual factual documents.

* **语义记忆：记住事实** 涉及保留特定事实和概念，如用户偏好或领域知识。用于为智能体提供基础，带来更个性化和相关的交互。此信息可作为持续更新的用户"配置文件"（JSON 文档）或作为单个事实文档的"集合"管理。

* **Episodic Memory: Remembering Experiences:** This involves recalling past events or actions. For AI agents, episodic memory is often used to remember how to accomplish a task. In practice, it's frequently implemented through few-shot example prompting, where an agent learns from past successful interaction sequences to perform tasks correctly.

* **情景记忆：记住经历** 涉及回忆过去事件或行动。对于 AI Agent，情景记忆通常用于记住如何完成任务。实践中常通过少样本示例提示实现，Agent 从过去成功交互序列中学习以正确执行任务。

* **Procedural Memory: Remembering Rules:**  This is the memory of how to perform tasks—the agent's core instructions and behaviors, often contained in its system prompt. It's common for agents to modify their own prompts to adapt and improve. An effective technique is "Reflection," where an agent is prompted with its current instructions and recent interactions, then asked to refine its own instructions.

* **程序记忆：记住规则** 关于如何执行任务的记忆——Agent 的核心指令和行为，通常包含在其系统提示中。Agent 修改自身提示以适应和改进很常见。有效技术是"反思"，其中智能体审查其当前指令和最近交互，然后被要求改进自身指令。

Below is pseudo-code demonstrating how an agent might use reflection to update its procedural memory stored in a LangGraph BaseStore

下面是演示智能体使用反思来更新存储在 LangGraph BaseStore 中的程序记忆的伪代码。

```python
## Node that updates the agent's instructions
def update_instructions(state: State, store: BaseStore):
   namespace = ("instructions",)
   # Get the current instructions from the store
   current_instructions = store.search(namespace)[0]
   
   # Create a prompt to ask the LLM to reflect on the conversation
   # and generate new, improved instructions
   prompt = prompt_template.format(
       instructions=current_instructions.value["instructions"],
       conversation=state["messages"]
   )
   
   # Get the new instructions from the LLM
   output = llm.invoke(prompt)
   new_instructions = output['new_instructions']
   
   # Save the updated instructions back to the store
   store.put(("agent_instructions",), "agent_a", {"instructions": new_instructions})

## Node that uses the instructions to generate a response
def call_model(state: State, store: BaseStore):
   namespace = ("agent_instructions", )
   # Retrieve the latest instructions from the store
   instructions = store.get(namespace, key="agent_a")[0]
   
   # Use the retrieved instructions to format the prompt
   prompt = prompt_template.format(instructions=instructions.value["instructions"])
   # ... application logic continues
```

LangGraph stores long-term memories as JSON documents in a store. Each memory is organized under a custom namespace (like a folder) and a distinct key (like a filename). This hierarchical structure allows for easy organization and retrieval of information. The following code demonstrates how to use InMemoryStore to put, get, and search for memories.

LangGraph 将长期记忆存储为存储中的 JSON 文档。每个记忆都在自定义命名空间（如文件夹）和不同的键（如文件名）下组织。这种分层结构便于组织和检索信息。以下代码演示了如何使用 InMemoryStore 放置、获取和搜索记忆。

```python
from langgraph.store.memory import InMemoryStore

## A placeholder for a real embedding function
def embed(texts: list[str]) -> list[list[float]]:
   # In a real application, use a proper embedding model
   return [[1.0, 2.0] for _ in texts]

## Initialize an in-memory store. For production, use a database-backed store.
store = InMemoryStore(index={"embed": embed, "dims": 2})

## Define a namespace for a specific user and application context
user_id = "my-user"
application_context = "chitchat"
namespace = (user_id, application_context)

## 1. Put a memory into the store
store.put(
   namespace,
   "a-memory",  # The key for this memory
   {
       "rules": [
           "User likes short, direct language",
           "User only speaks English & python",
       ],
       "my-key": "my-value",
   },
)

## 2. Get the memory by its namespace and key
item = store.get(namespace, "a-memory")
print("Retrieved Item:", item)

## 3. Search for memories within the namespace, filtering by content
## and sorting by vector similarity to the query.
items = store.search(
   namespace,
   filter={"my-key": "my-value"},
   query="language preferences"
)
print("Search Results:", items)
```

## Vertex Memory Bank

## Vertex Memory Bank（记忆库）

Memory Bank, a managed service in the Vertex AI Agent Engine, provides agents with persistent, long-term memory. The service uses Gemini models to asynchronously analyze conversation histories to extract key facts and user preferences.

Memory Bank 是 Vertex AI Agent Engine 的托管服务，为智能体提供长期记忆。该服务使用 Gemini 模型异步分析对话历史，提取关键事实和用户偏好。

This information is stored persistently, organized by a defined scope like user ID, and intelligently updated to consolidate new data and resolve contradictions. Upon starting a new session, the agent retrieves relevant memories through either a full data recall or a similarity search using embeddings. This process allows an agent to maintain continuity across sessions and personalize responses based on recalled information.

此信息持久存储，按定义范围（如用户 ID）组织，并智能更新（整合新数据、解决矛盾）。开始新会话时，Agent 通过完整数据调用或嵌入相似度搜索检索相关记忆，实现跨会话连续性及基于回忆信息的个性化响应。

The agent's runner interacts with the VertexAiMemoryBankService, which is initialized first. This service handles the automatic storage of memories generated during the agent's conversations. Each memory is tagged with a unique USER_ID and APP_NAME, ensuring accurate retrieval in the future.

Agent 的 runner 与 VertexAiMemoryBankService 交互，后者需要先初始化。此服务处理智能体运行期间生成记忆的自动存储。每个记忆标记有唯一的 USER_ID 和 APP_NAME，确保将来能准确检索。

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

Memory Bank offers seamless integration with the Google ADK, providing an immediate out-of-the-box experience. For users of other agent frameworks, such as LangGraph and CrewAI, Memory Bank also offers support through direct API calls. Online code examples demonstrating these integrations are readily available for interested readers.

Memory Bank 提供与 Google ADK 的无缝集成，提供即开即用的体验。对于使用其他智能体框架（如 LangGraph 和 CrewAI）的用户，Memory Bank 还通过直接 API 调用提供支持。演示这些集成的在线代码示例可供感兴趣的读者使用。

## At a Glance

## 速览

**What**: Agentic systems need to remember information from past interactions to perform complex tasks and provide coherent experiences. Without a memory mechanism, agents are stateless, unable to maintain conversational context, learn from experience, or personalize responses for users. This fundamentally limits them to simple, one-shot interactions, failing to handle multi-step processes or evolving user needs. The core problem is how to effectively manage both the immediate, temporary information of a single conversation and the vast, persistent knowledge gathered over time.

**问题背景：**智能体需要记住过去交互信息以执行复杂任务并提供连贯体验。缺乏记忆机制时，Agent 无法维护对话上下文、从经验中学习或提供个性化响应，被限制在简单的一次性交互中，无法处理多步骤过程或变化需求。核心问题是如何有效管理单个对话的即时临时信息和随时间积累的持久知识。

**Why:** The standardized solution is to implement a dual-component memory system that distinguishes between short-term and long-term storage. Short-term, contextual memory holds recent interaction data within the LLM's context window to maintain conversational flow. For information that must persist, long-term memory solutions use external databases, often vector stores, for efficient, semantic retrieval. Agentic frameworks like the Google ADK provide specific components to manage this, such as Session for the conversation thread and State for its temporary data. A dedicated MemoryService is used to interface with the long-term knowledge base, allowing the agent to retrieve and incorporate relevant past information into its current context.

**解决方案：** 标准化解决方案是实现区分短期和长期存储的双组件记忆系统：短期上下文记忆在 LLM 窗口内保存最近交互以维护对话流；长期记忆使用外部数据库（如向量存储）实现高效的语义检索。Google ADK 等框架提供特定组件来管理此过程（如 Session 管理对话线程，State 处理临时数据）。专用的 MemoryService 与长期知识库交互，允许智能体将相关的过去信息纳入当前上下文。

**Rule of thumb:** Use this pattern when an agent needs to do more than answer a single question. It is essential for agents that must maintain context throughout a conversation, track progress in multi-step tasks, or personalize interactions by recalling user preferences and history. Implement memory management whenever the agent is expected to learn or adapt based on past successes, failures, or newly acquired information.

**实践建议：** 当智能体做更多事情（不仅是回答单个问题）时使用此模式。对于需维护对话上下文、跟踪多步骤任务进度或通过回忆用户偏好历史来提供个性化交互的 Agent，此模式必不可少。当智能体从过去的成功/失败或新信息中学习并适应时，应实现记忆管理。

**Visual summary**

**可视化摘要**

**![][image1]**

Fig.1: Memory management design pattern

图 1：记忆管理设计模式

## Key Takeaways

## 关键要点

To quickly recap the main points about memory management:

快速回顾记忆管理的核心要点：

* Memory is super important for agents to keep track of things, learn, and personalize interactions.

* 记忆对于智能体处理事务、学习和个性化交互至关重要。

* Conversational AI relies on both short-term memory for immediate context within a single chat and long-term memory for persistent knowledge across multiple sessions.

* 对话式 AI 依赖单个聊天中即时上下文的短期记忆和跨多个会话持久知识的长期记忆。

* Short-term memory (the immediate stuff) is temporary, often limited by the LLM's context window or how the framework passes context.

* 短期记忆（即时信息）是临时的，通常受 LLM 上下文窗口或框架传递上下文方式的限制。

* Long-term memory (the stuff that sticks around) saves info across different chats using outside storage like vector databases and is accessed by searching.

* 长期记忆（持久信息）使用向量数据库等外部存储跨不同聊天保存信息，并通过搜索访问。

* Frameworks like ADK have specific parts like Session (the chat thread), State (temporary chat data), and MemoryService (the searchable long-term knowledge) to manage memory.

* 像 ADK 这样的框架具有特定部分，如 Session（聊天线程）、State（临时聊天数据）和 MemoryService（可搜索的长期知识）来管理记忆。

* ADK's SessionService handles the whole life of a chat session, including its history (events) and temporary data (state).

* ADK 的 SessionService 处理聊天会话的整个生命周期，包括其历史（events）和临时数据（state）。

* ADK's session.state is a dictionary for temporary chat data. Prefixes (user:, app:, temp:) tell you where the data belongs and if it sticks around.

* ADK 的 session.state 是临时聊天数据的字典。前缀（user:、app:、temp:）指示数据归属位置及是否持久。

* In ADK, you should update state by using EventActions.state_delta or output_key when adding events, not by changing the state dictionary directly.

* 在 ADK 中，应通过在添加事件时使用 EventActions.state_delta 或 output_key 更新状态，而非直接更改状态字典。

* ADK's MemoryService is for putting info into long-term storage and letting agents search it, often using tools.

* ADK 的 MemoryService 用于将信息放入长期存储并让智能体检索，通常使用工具。

* LangChain offers practical tools like ConversationBufferMemory to automatically inject the history of a single conversation into a prompt, enabling an agent to recall immediate context.

* LangChain 提供如 ConversationBufferMemory 的实用工具，自动将单个对话历史注入提示，使智能体回忆即时上下文。

* LangGraph enables advanced, long-term memory by using a store to save and retrieve semantic facts, episodic experiences, or even updatable procedural rules across different user sessions.

* LangGraph 通过使用存储来保存和检索跨不同用户会话的语义事实、情景经验甚至可更新的程序规则，实现高级长期记忆。

* Memory Bank is a managed service that provides agents with persistent, long-term memory by automatically extracting, storing, and recalling user-specific information to enable personalized, continuous conversations across frameworks like Google's ADK, LangGraph, and CrewAI.

* Memory Bank 是托管服务，通过自动提取、存储和调用用户特定信息为智能体提供持久长期记忆，在 Google 的 ADK、LangGraph 和 CrewAI 等框架中实现个性化的持续对话。

## Conclusion

## 结论

This chapter dove into the really important job of memory management for agent systems, showing the difference between the short-lived context and the knowledge that sticks around for a long time. We talked about how these types of memory are set up and where you see them used in building smarter agents that can remember things. We took a detailed look at how Google ADK gives you specific pieces like Session, State, and MemoryService to handle this. Now that we've covered how agents can remember things, both short-term and long-term, we can move on to how they can learn and adapt. The next pattern ​​"Learning and Adaptation" is about an agent changing how it thinks, acts, or what it knows, all based on new experiences or data.

本章深入探讨智能体记忆管理，展示了短暂上下文与长期持久知识之间的区别。我们讨论了这些记忆类型的设置方式以及在构建更智能智能体中的应用。详细了解了 Google ADK 如何通过 Session、State 和 MemoryService 等组件处理此过程。既然已介绍智能体如何管理记忆（短期和长期），我们将继续探讨其如何学习和适应。下一模式"学习和适应"关注智能体如何根据新经验或数据改变其思维方式、行动或知识。

## References

## 参考文献

1. ADK Memory, [https://google.github.io/adk-docs/sessions/memory/](https://google.github.io/adk-docs/sessions/memory/)
2. LangGraph Memory, [https://langchain-ai.github.io/langgraph/concepts/memory/](https://langchain-ai.github.io/langgraph/concepts/memory/)
3. Vertex AI Agent Engine Memory Bank, [https://cloud.google.com/blog/products/ai-machine-learning/vertex-ai-memory-bank-in-public-preview](https://cloud.google.com/blog/products/ai-machine-learning/vertex-ai-memory-bank-in-public-preview)

[image1]: ../images/chapter-8/image1.png
