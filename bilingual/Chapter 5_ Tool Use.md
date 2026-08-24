# Chapter 5: Tool Use (Function Calling)

# 第 5 章：工具使用

## Tool Use Pattern Overview

## 工具使用模式概述

So far, we've discussed agentic patterns that primarily involve orchestrating interactions between language models and managing the flow of information within the agent's internal workflow (Chaining, Routing, Parallelization, Reflection). However, for agents to be truly useful and interact with the real world or external systems, they need the ability to use Tools.

截至目前，我们探讨的智能体模式主要聚焦于编排语言模型间的交互以及管理智能体内部工作流的信息流（提示词链、路由、并行化、反思）。然而，要让智能体真正发挥作用并与现实世界或外部系统交互，它们需要具备使用工具的能力。

The Tool Use pattern, often implemented through a mechanism called Function Calling, enables an agent to interact with external APIs, databases, services, or even execute code. It allows the LLM at the core of the agent to decide when and how to use a specific external function based on the user's request or the current state of the task.

工具使用模式通常通过**函数调用（Function Calling）**机制实现，使智能体能够与外部 API、数据库、服务交互，甚至执行代码。该机制让位于智能体核心的大语言模型（LLM）能根据用户请求或任务当前状态，决定何时以及如何调用特定的外部函数。

The process typically involves:

该过程通常包括：

1. **Tool Definition:** External functions or capabilities are defined and described to the LLM. This description includes the function's purpose, its name, and the parameters it accepts, along with their types and descriptions.  
2. **LLM Decision:** The LLM receives the user's request and the available tool definitions. Based on its understanding of the request and the tools, the LLM decides if calling one or more tools is necessary to fulfill the request.  
3. **Function Call Generation:** If the LLM decides to use a tool, it generates a structured output (often a JSON object) that specifies the name of the tool to call and the arguments (parameters) to pass to it, extracted from the user's request.  
4. **Tool Execution:** The agentic framework or orchestration layer intercepts this structured output. It identifies the requested tool and executes the actual external function with the provided arguments.  
5. **Observation/Result:** The output or result from the tool execution is returned to the agent.  
6. **LLM Processing (Optional but common):** The LLM receives the tool's output as context and uses it to formulate a final response to the user or decide on the next step in the workflow (which might involve calling another tool, reflecting, or providing a final answer).

1. **工具定义：** 向 LLM 定义并描述外部函数或能力。描述内容包括函数的用途、名称，以及它接受的参数及其类型和描述。
2. **LLM 决策：** LLM 接收用户的请求和可用的工具定义。基于其对请求和工具的理解，LLM 决定是否需要调用一个或多个工具来满足请求。
3. **函数调用生成：** 如果 LLM 决定使用工具，它会生成结构化输出（通常是 JSON 对象），指定要调用的工具名称和要传递给它的参数，这些参数从用户请求中提取。
4. **工具执行：** 智能体框架或编排层拦截此结构化输出。它识别请求的工具并使用提供的参数执行实际的外部函数。
5. **观察/结果：** 工具执行的输出或结果返回给智能体。
6. **LLM 处理（可选但常见）：** LLM 接收工具的输出作为上下文，并使用它向用户制定最终响应或决定工作流中的下一步（可能涉及调用另一个工具、反思或提供最终答案）。

This pattern is fundamental because it breaks the limitations of the LLM's training data and allows it to access up-to-date information, perform calculations it can't do internally, interact with user-specific data, or trigger real-world actions. Function calling is the technical mechanism that bridges the gap between the LLM's reasoning capabilities and the vast array of external functionalities available.

该模式是基础性的，因为它打破了 LLM 训练数据的限制，允许它访问最新信息、执行内部无法完成的计算、与用户特定数据交互或触发现实世界的行动。工具调用是连接 LLM 推理能力与大量可用外部功能之间差距的技术机制。

While "function calling" aptly describes invoking specific, predefined code functions, it's useful to consider the more expansive concept of "tool calling." This broader term acknowledges that an agent's capabilities can extend far beyond simple function execution. A "tool" can be a traditional function, but it can also be a complex API endpoint, a request to a database, or even an instruction directed at another specialized agent. This perspective allows us to envision more sophisticated systems where, for instance, a primary agent might delegate a complex data analysis task to a dedicated "analyst agent" or query an external knowledge base through its API. Thinking in terms of "tool calling" better captures the full potential of agents to act as orchestrators across a diverse ecosystem of digital resources and other intelligent entities.

虽然"函数调用"准确描述了调用预定义代码函数的过程，但采用更广泛的"工具调用"概念更具实践价值。这一更宽泛的术语承认智能体的能力可以远超简单函数执行范畴——"工具"既可以是传统函数，也可以是复杂的 API 端点、数据库查询请求，甚至是向其他专业智能体发出的指令。这种视角帮助我们构建更复杂的系统，例如主智能体可以将复杂数据分析任务委托给专用的"分析师智能体"，或通过 API 查询外部知识库。从"工具调用"的角度思考，能更好地把握智能体作为跨多样化数字资源和其他智能实体生态系统编排者的全部潜力。

Frameworks like LangChain, LangGraph, and Google Agent Developer Kit (ADK) provide robust support for defining tools and integrating them into agent workflows, often leveraging the native function calling capabilities of modern LLMs like those in the Gemini or OpenAI series. On the "canvas" of these frameworks, you define the tools and then configure agents (typically LLM Agents) to be aware of and capable of using these tools.

像 LangChain、LangGraph 和 Google 智能体开发工具包（ADK）这样的框架为定义工具并将它们集成到智能体工作流提供了强大支持，通常利用现代 LLM（如 Gemini 或 OpenAI 系列中的模型）的原生函数调用能力。在这些框架的"画布"上，您定义工具，然后配置智能体（通常是 LLM 智能体）以了解并能够使用这些工具。

Tool Use is a cornerstone pattern for building powerful, interactive, and externally aware agents.

工具使用是构建强大、交互式且具外部环境感知能力的智能体的基石模式。

## Practical Applications & Use Cases

## 实际应用与用例

The Tool Use pattern is applicable in virtually any scenario where an agent needs to go beyond generating text to perform an action or retrieve specific, dynamic information:

工具使用模式几乎适用于智能体超越生成文本来执行操作或检索特定动态信息的任何场景：

1. Information Retrieval from External Sources:
Accessing real-time data or information that is not present in the LLM's training data.

1. **从外部源检索信息：**
访问 LLM 训练数据中不存在的实时数据或信息。

* **Use Case:** A weather agent.  
  * **Tool:** A weather API that takes a location and returns the current weather conditions.  
  * **Agent Flow:** User asks, "What's the weather in London?", LLM identifies the need for the weather tool, calls the tool with "London", tool returns data, LLM formats the data into a user-friendly response.

* **用例：** 天气智能体。
  * **工具：** 接受位置并返回当前天气状况的天气 API。
  * **智能体流程：** 用户问"伦敦的天气如何？"，LLM 识别需要天气工具，用"伦敦"调用工具，工具返回数据，LLM 将数据格式化为用户友好的响应。

2. Interacting with Databases and APIs:
Performing queries, updates, or other operations on structured data.

2. **与数据库和 API 交互：**
对结构化数据执行查询、更新或其他操作。

* **Use Case:** An e-commerce agent.  
  * **Tools:** API calls to check product inventory, get order status, or process payments.  
  * **Agent Flow:** User asks "Is product X in stock?", LLM calls the inventory API, tool returns stock count, LLM tells the user the stock status.

* **用例：** 电子商务智能体。
  * **工具：** API 调用以检查产品库存、获取订单状态或处理付款。
  * **智能体流程：** 用户问"产品 X 有库存吗？"，LLM 调用库存 API，工具返回库存数量，LLM 告诉用户库存状态。

3. Performing Calculations and Data Analysis:
Using external calculators, data analysis libraries, or statistical tools.

3. **执行计算和数据分析：**
使用外部计算器、数据分析库或统计工具。

* **Use Case:** A financial agent.  
  * **Tools:** A calculator function, a stock market data API, a spreadsheet tool.  
  * **Agent Flow:** User asks "What's the current price of AAPL and calculate the potential profit if I bought 100 shares at $150?", LLM calls stock API, gets current price, then calls calculator tool, gets result, formats response.

* **用例：** 金融智能体。
  * **工具：** 计算器函数、股票市场数据 API、电子表格工具。
  * **智能体流程：** 用户问"AAPL 的当前价格是多少，如果我以 150 美元购买 100 股，计算潜在利润？"，LLM 调用股票 API，获取当前价格，然后调用计算器工具，获取结果，格式化响应。

4. Sending Communications:
Sending emails, messages, or making API calls to external communication services.

4. **发送通信：**
发送电子邮件、消息或对外部通信服务进行 API 调用。

* **Use Case:** A personal assistant agent.  
  * **Tool:** An email sending API.  
  * **Agent Flow:** User says, "Send an email to John about the meeting tomorrow.", LLM calls an email tool with the recipient, subject, and body extracted from the request.

* **用例：** 个人助理智能体。
  * **工具：** 电子邮件发送 API。
  * **智能体流程：** 用户说"给 John 发一封关于明天会议的电子邮件。"，LLM 使用从请求中提取的收件人、主题和正文调用电子邮件工具。

5. Executing Code:
Running code snippets in a safe environment to perform specific tasks.

5. **执行代码：**
在安全环境中运行代码片段以执行特定任务。

* **Use Case:** A coding assistant agent.  
  * **Tool:** A code interpreter.  
  * **Agent Flow:** User provides a Python snippet and asks, "What does this code do?", LLM uses the interpreter tool to run the code and analyze its output.

* **用例：** 编码助手智能体。
  * **工具：** 代码解释器。
  * **智能体流程：** 用户提供 Python 代码片段并问"这段代码做什么？"，LLM 使用解释器工具运行代码并分析其输出。

6. Controlling Other Systems or Devices:
Interacting with smart home devices, IoT platforms, or other connected systems.

6. **控制其他系统或设备：**
与智能家居设备、物联网平台或其他连接系统交互。

* **Use Case:** A smart home agent.  
  * **Tool:** An API to control smart lights.  
  * **Agent Flow:** User says, "Turn off the living room lights." LLM calls the smart home tool with the command and target device.

* **用例：** 智能家居智能体。
  * **工具：** 控制智能灯的 API。
  * **智能体流程：** 用户说"关闭客厅的灯。"LLM 使用命令和目标设备调用智能家居工具。

Tool Use is what transforms a language model from a text generator into an agent capable of sensing, reasoning, and acting in the digital or physical world (see Fig. 1)

工具使用正是将语言模型从文本生成器转变为能够在数字或物理世界中感知、推理和行动的智能体的关键（见图 1）。

![][image1]

Fig.1: Some examples of an Agent using Tools

图 1：智能体使用工具的一些示例

## Hands-On Code Example (LangChain)

## 实操代码示例（LangChain）

The implementation of tool use within the LangChain framework is a two-stage process. Initially, one or more tools are defined, typically by encapsulating existing Python functions or other runnable components. Subsequently, these tools are bound to a language model, thereby granting the model the capability to generate a structured tool-use request when it determines that an external function call is required to fulfill a user's query.

在 LangChain 框架中实现工具使用分为两个阶段。首先，定义一个或多个工具，通常通过封装现有的 Python 函数或其他可运行组件。随后，将这些工具与语言模型绑定，从而使模型能够在确定需要调用外部函数来满足用户查询时，生成结构化的工具使用请求。

The following implementation will demonstrate this principle by first defining a simple function to simulate an information retrieval tool. Following this, an agent will be constructed and configured to leverage this tool in response to user input. The execution of this example requires the installation of the core LangChain libraries and a model-specific provider package. Furthermore, proper authentication with the selected language model service, typically via an API key configured in the local environment, is a necessary prerequisite.

以下实现将通过首先定义一个简单函数来模拟信息检索工具，以此演示此原理。随后，将构建并配置一个智能体，利用此工具响应用户输入。执行此示例需要安装核心 LangChain 库和特定于模型的提供程序包。此外，使用所选语言模型服务进行适当的身份验证（通常通过在本地环境中配置的 API 密钥）是必要的先决条件。

```python
import os, getpass
import asyncio
import nest_asyncio
from typing import List
from dotenv import load_dotenv
import logging
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool as langchain_tool
from langchain.agents import create_tool_calling_agent, AgentExecutor

## UNCOMMENT
## Prompt the user securely and set API keys as an environment variables
os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")
os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

try:
  # A model with function/tool calling capabilities is required.
  llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
  print(f"✅ Language model initialized: {llm.model}")
except Exception as e:
  print(f"🛑 Error initializing language model: {e}")
  llm = None

## --- Define a Tool ---
@langchain_tool
def search_information(query: str) -> str:
  """
  Provides factual information on a given topic. Use this tool to find answers to phrases
  like 'capital of France' or 'weather in London?'.
  """
  print(f"\n--- 🛠️ Tool Called: search_information with query: '{query}' ---")
  # Simulate a search tool with a dictionary of predefined results.
  simulated_results = {
      "weather in london": "The weather in London is currently cloudy with a temperature of 15°C.",
      "capital of france": "The capital of France is Paris.",
      "population of earth": "The estimated population of Earth is around 8 billion people.",
      "tallest mountain": "Mount Everest is the tallest mountain above sea level.",
      "default": f"Simulated search result for '{query}': No specific information found, but the topic seems interesting."
  }
  result = simulated_results.get(query.lower(), simulated_results["default"])
  print(f"--- TOOL RESULT: {result} ---")
  return result

tools = [search_information]

## --- Create a Tool-Calling Agent ---
if llm:
  # This prompt template requires an `agent_scratchpad` placeholder for the agent's internal steps.
  agent_prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful assistant."),
      ("human", "{input}"),
      ("placeholder", "{agent_scratchpad}"),
  ])
  # Create the agent, binding the LLM, tools, and prompt together.
  agent = create_tool_calling_agent(llm, tools, agent_prompt)
  # AgentExecutor is the runtime that invokes the agent and executes the chosen tools.
  # The 'tools' argument is not needed here as they are already bound to the agent.
  agent_executor = AgentExecutor(agent=agent, verbose=True, tools=tools)

async def run_agent_with_tool(query: str):
  """Invokes the agent executor with a query and prints the final response."""
  print(f"\n--- 🏃 Running Agent with Query: '{query}' ---")
  try:
      response = await agent_executor.ainvoke({"input": query})
      print("\n--- ✅ Final Agent Response ---")
      print(response["output"])
  except Exception as e:
      print(f"\n🛑 An error occurred during agent execution: {e}")

async def main():
  """Runs all agent queries concurrently."""
  tasks = [
      run_agent_with_tool("What is the capital of France?"),
      run_agent_with_tool("What's the weather like in London?"),
      run_agent_with_tool("Tell me something about dogs.") # Should trigger the default tool response
  ]
  await asyncio.gather(*tasks)

nest_asyncio.apply()
asyncio.run(main())
```

The code sets up a tool-calling agent using the LangChain library and the Google Gemini model. It defines a search\_information tool that simulates providing factual answers to specific queries. The tool has predefined responses for "weather in london," "capital of france," and "population of earth," and a default response for other queries. A ChatGoogleGenerativeAI model is initialized, ensuring it has tool-calling capabilities. A ChatPromptTemplate is created to guide the agent's interaction. The create\_tool\_calling\_agent function is used to combine the language model, tools, and prompt into an agent. An AgentExecutor is then set up to manage the agent's execution and tool invocation. The run\_agent\_with\_tool asynchronous function is defined to invoke the agent with a given query and print the result. The main asynchronous function prepares multiple queries to be run concurrently. These queries are designed to test both the specific and default responses of the search\_information tool. Finally, the asyncio.run(main()) call executes all the agent tasks. The code includes checks for successful LLM initialization before proceeding with agent setup and execution.

代码使用 LangChain 库和 Google Gemini 模型设置了一个工具调用智能体。它定义了一个 `search_information` 工具，模拟为特定查询提供事实答案。该工具对"weather in london"、"capital of france"和"population of earth"有预定义响应，以及其他查询的默认响应。初始化了一个 `ChatGoogleGenerativeAI` 模型，确保其具有工具调用能力。创建了一个 `ChatPromptTemplate` 来指导智能体的交互。使用 `create_tool_calling_agent` 函数将语言模型、工具和提示词组合成一个智能体。然后设置一个 `AgentExecutor` 来管理智能体的执行和工具调用。定义了 `run_agent_with_tool` 异步函数以使用给定查询调用智能体并打印结果。`main` 异步函数准备多个要并发运行的查询。这些查询旨在测试 `search_information` 工具的特定响应和默认响应。最后，`asyncio.run(main())` 调用执行所有智能体任务。代码在继续进行智能体设置和执行之前，包含了对 LLM 初始化成功的检查。

## Hands-On Code Example (CrewAI)

## 实操代码示例（CrewAI）

This code provides a practical example of how to implement function calling (Tools) within the CrewAI framework. It sets up a simple scenario where an agent is equipped with a tool to look up information. The example specifically demonstrates fetching a simulated stock price using this agent and tool.

此代码演示了在 CrewAI 框架中实现工具调用（工具）的具体案例。通过设置简单场景：让配备信息查询工具的智能体模拟股价，展示核心实现逻辑。

```python
## pip install crewai langchain-openai
import os
from crewai import Agent, Task, Crew
from crewai.tools import tool
import logging

## --- Best Practice: Configure Logging ---
## A basic logging setup helps in debugging and tracking the crew's execution.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

## --- Set up your API Key ---
## For production, it's recommended to use a more secure method for key management
## like environment variables loaded at runtime or a secret manager.
#
## Set the environment variable for your chosen LLM provider (e.g., OPENAI_API_KEY)
## os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
## os.environ["OPENAI_MODEL_NAME"] = "gpt-4o"

## --- 1. Refactored Tool: Returns Clean Data ---
## The tool now returns raw data (a float) or raises a standard Python error.
## This makes it more reusable and forces the agent to handle outcomes properly.
@tool("Stock Price Lookup Tool")
def get_stock_price(ticker: str) -> float:
   """
   Fetches the latest simulated stock price for a given stock ticker symbol.
   Returns the price as a float. Raises a ValueError if the ticker is not found.
   """
   logging.info(f"Tool Call: get_stock_price for ticker '{ticker}'")
   simulated_prices = {
       "AAPL": 178.15,
       "GOOGL": 1750.30,
       "MSFT": 425.50,
   }
   price = simulated_prices.get(ticker.upper())
   if price is not None:
       return price
   else:
       # Raising a specific error is better than returning a string.
       # The agent is equipped to handle exceptions and can decide on the next action.
       raise ValueError(f"Simulated price for ticker '{ticker.upper()}' not found.")

## --- 2. Define the Agent ---
## The agent definition remains the same, but it will now leverage the improved tool.
financial_analyst_agent = Agent(
 role='Senior Financial Analyst',
 goal='Analyze stock data using provided tools and report key prices.',
 backstory="You are an experienced financial analyst adept at using data sources to find stock information. You provide clear, direct answers.",
 verbose=True,
 tools=[get_stock_price],
 # Allowing delegation can be useful, but is not necessary for this simple task.
 allow_delegation=False,
)

## --- 3. Refined Task: Clearer Instructions and Error Handling ---
## The task description is more specific and guides the agent on how to react
## to both successful data retrieval and potential errors.
analyze_aapl_task = Task(
 description=(
     "What is the current simulated stock price for Apple (ticker: AAPL)? "
     "Use the 'Stock Price Lookup Tool' to find it. "
     "If the ticker is not found, you must report that you were unable to retrieve the price."
 ),
 expected_output=(
     "A single, clear sentence stating the simulated stock price for AAPL. "
     "For example: 'The simulated stock price for AAPL is $178.15.' "
     "If the price cannot be found, state that clearly."
 ),
 agent=financial_analyst_agent,
)

## --- 4. Formulate the Crew ---
## The crew orchestrates how the agent and task work together.
financial_crew = Crew(
 agents=[financial_analyst_agent],
 tasks=[analyze_aapl_task],
 verbose=True # Set to False for less detailed logs in production
)

## --- 5. Run the Crew within a Main Execution Block ---
## Using a __name__ == "__main__": block is a standard Python best practice.
def main():
   """Main function to run the crew."""
   # Check for API key before starting to avoid runtime errors.
   if not os.environ.get("OPENAI_API_KEY"):
       print("ERROR: The OPENAI_API_KEY environment variable is not set.")
       print("Please set it before running the script.")
       return
   print("\n## Starting the Financial Crew...")
   print("---------------------------------")
   
   # The kickoff method starts the execution.
   result = financial_crew.kickoff()
   print("\n---------------------------------")
   print("## Crew execution finished.")
   print("\nFinal Result:\n", result)

if __name__ == "__main__":
   main()
```

This code demonstrates a simple application using the Crew.ai library to simulate a financial analysis task. It defines a custom tool, get\_stock\_price, that simulates looking up stock prices for predefined tickers. The tool is designed to return a floating-point number for valid tickers or raise a ValueError for invalid ones. A Crew.ai Agent named financial\_analyst\_agent is created with the role of a Senior Financial Analyst. This agent is given the get\_stock\_price tool to interact with. A Task is defined, analyze\_aapl\_task, specifically instructing the agent to find the simulated stock price for AAPL using the tool. The task description includes clear instructions on how to handle both success and failure cases when using the tool. A Crew is assembled, comprising the financial\_analyst\_agent and the analyze\_aapl\_task. The verbose setting is enabled for both the agent and the crew to provide detailed logging during execution. The main part of the script runs the crew's task using the kickoff() method within a standard if \_\_name\_\_ \== "\_\_main\_\_": block. Before starting the crew, it checks if the OPENAI\_API\_KEY environment variable is set, which is required for the agent to function. The result of the crew's execution, which is the output of the task, is then printed to the console. The code also includes basic logging configuration for better tracking of the crew's actions and tool calls. It uses environment variables for API key management, though it notes that more secure methods are recommended for production environments. In short, the core logic showcases how to define tools, agents, and tasks to create a collaborative workflow in Crew.ai.

此代码演示了使用 CrewAI 库模拟财务分析任务的简单应用程序。它定义了一个自定义工具 get_stock_price，模拟查找预定义股票代码的价格。该工具设计为对有效代码返回浮点数，或对无效代码引发 ValueError。创建了一个名为 financial_analyst_agent 的 CrewAI Agent，角色为高级财务分析师。该智能体被赋予 get_stock_price 工具进行交互。定义了一个任务 analyze_aapl_task，专门指示智能体查找 AAPL 的模拟股票价格。任务描述包括关于使用工具时如何处理成功和失败情况的明确说明。组建了一个团队，包含 financial_analyst_agent 和 analyze_aapl_task。为智能体和团队设置详细日志，以在执行期间提供详细日志。脚本的主要部分在标准 if __name__ == "__main__": 块中使用 kickoff() 方法运行团队的任务。在启动团队之前，它会检查是否设置了 OPENAI_API_KEY 环境变量，这是智能体运行所必需的。最后将团队执行的结果（即任务的输出）打印到控制台。代码还包括基本日志配置，以更好地跟踪团队的行动和工具调用。它使用环境变量进行 API 密钥管理，尽管它指出对于生产环境建议使用更安全的方法。简而言之，核心逻辑展示了如何定义工具、Agent 和任务，以在 CrewAI 中创建协作工作流。

## Hands-on code (Google ADK)

## 实操代码（Google ADK）

The Google Agent Developer Kit (ADK) includes a library of natively integrated tools that can be directly incorporated into an agent's capabilities. 

Google 智能体开发工具包 (ADK) 提供原生集成工具库，可直接扩展智能体的能力。

**Google search:** A primary example of such a component is the Google Search tool. This tool serves as a direct interface to the Google Search engine, equipping the agent with the functionality to perform web searches and retrieve external information.

**Google 搜索：** 此类组件的主要示例是 Google 搜索工具。此工具作为 Google 搜索引擎的直接接口，为智能体提供执行网络搜索和检索外部信息的功能。

```python
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types
import nest_asyncio
import asyncio

## Define variables required for Session setup and Agent execution
APP_NAME="Google Search_agent"
USER_ID="user1234"
SESSION_ID="1234"

## Define Agent with access to search tool
root_agent = Agent(
  name="basic_search_agent",
  model="gemini-2.0-flash-exp",
  description="Agent to answer questions using Google Search.",
  instruction="I can answer your questions by searching the internet. Just ask me anything!",
  tools=[google_search] # Google Search is a pre-built tool to perform Google searches.
)

## Agent Interaction
async def call_agent(query):
  """
  Helper function to call the agent with a query.
  """
  # Session and Runner
  session_service = InMemorySessionService()
  session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
  runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)
  content = types.Content(role='user', parts=[types.Part(text=query)])
  events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)
  for event in events:
      if event.is_final_response():
          final_response = event.content.parts[0].text
          print("Agent Response: ", final_response)

nest_asyncio.apply()
asyncio.run(call_agent("what's the latest ai news?"))
```

This code demonstrates how to create and use a basic agent powered by the Google ADK for Python. The agent is designed to answer questions by utilizing Google Search as a tool. First, necessary libraries from IPython, google.adk, and google.genai are imported. Constants for the application name, user ID, and session ID are defined. An Agent instance named "basic\_search\_agent" is created with a description and instructions indicating its purpose. It's configured to use the Google Search tool, which is a pre-built tool provided by the ADK. An InMemorySessionService (see Chapter 8\) is initialized to manage sessions for the agent. A new session is created for the specified application, user, and session IDs. A Runner is instantiated, linking the created agent with the session service. This runner is responsible for executing the agent's interactions within a session. A helper function call\_agent is defined to simplify the process of sending a query to the agent and processing the response. Inside call\_agent, the user's query is formatted as a types.Content object with the role 'user'. The runner.run method is called with the user ID, session ID, and the new message content. The runner.run method returns a list of events representing the agent's actions and responses. The code iterates through these events to find the final response. If an event is identified as the final response, the text content of that response is extracted. The extracted agent response is then printed to the console. Finally, the call\_agent function is called with the query "what's the latest ai news?" to demonstrate the agent in action.

此代码演示了如何使用 Python 的 Google ADK 创建和使用由其驱动的基本智能体。该智能体旨在通过利用 Google 搜索作为工具来回答问题。首先，从 IPython、google.adk 和 google.genai 导入必要的库。定义了应用程序名称、用户 ID 和会话 ID 的常量。创建了一个名为"basic_search_agent"的智能体，具有描述和说明指示其目的。它被配置为使用 Google 搜索工具，这是 ADK 提供的预构建工具。初始化 InMemorySessionService（见第 8 章）以管理智能体的会话。为指定的应用程序、用户和会话 ID 创建新会话。实例化 Runner，将创建的智能体与会话服务链接。此运行器负责在会话中执行智能体的交互。定义了一个名为 call_agent 的函数，以简化向智能体发送查询和处理响应的过程。在 call_agent 内部，用户的查询被格式化为具有角色"user"的 types.Content 对象。使用用户 ID、会话 ID 和新消息内容调用 runner.run 方法。runner.run 方法返回表示智能体操作和响应的事件列表。遍历这些事件以查找最终响应。如果事件被识别为最终响应，则提取该响应的文本内容。提取的智能体响应然后打印到控制台。最后，使用查询"what's the latest ai news?"调用 call_agent 函数以演示智能体的运行情况。

**Code execution:** The Google ADK features integrated components for specialized tasks, including an environment for dynamic code execution. The built\_in\_code\_execution tool provides an agent with a sandboxed Python interpreter. This allows the model to write and run code to perform computational tasks, manipulate data structures, and execute procedural scripts. Such functionality is critical for addressing problems that require deterministic logic and precise calculations, which are outside the scope of probabilistic language generation alone.

**代码执行：** Google ADK 包含专为动态代码执行设计的组件。built_in_code_execution 工具提供沙盒化 Python 解释器，让模型能编写运行代码执行计算、操作数据结构及运行脚本。此功能对需要确定性逻辑和精确计算的任务至关重要，弥补了概率性语言生成的不足。

```python
import os, getpass
import asyncio
import nest_asyncio
from typing import List
from dotenv import load_dotenv
import logging
from google.adk.agents import Agent as ADKAgent, LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.adk.code_executors import BuiltInCodeExecutor
from google.genai import types

## Define variables required for Session setup and Agent execution
APP_NAME="calculator"
USER_ID="user1234"
SESSION_ID="session_code_exec_async"

## Agent Definition
code_agent = LlmAgent(
  name="calculator_agent",
  model="gemini-2.0-flash",
  code_executor=BuiltInCodeExecutor(),
  instruction="""You are a calculator agent.
  When given a mathematical expression, write and execute Python code to calculate the result.
  Return only the final numerical result as plain text, without markdown or code blocks.
  """,
  description="Executes Python code to perform calculations.",
)

## Agent Interaction (Async)
async def call_agent_async(query):
  # Session and Runner
  session_service = InMemorySessionService()
  session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
  runner = Runner(agent=code_agent, app_name=APP_NAME, session_service=session_service)
  content = types.Content(role='user', parts=[types.Part(text=query)])
  print(f"\n--- Running Query: {query} ---")
  final_response_text = "No final text response captured."
  try:
      # Use run_async
      async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
          print(f"Event ID: {event.id}, Author: {event.author}")
          # --- Check for specific parts FIRST ---
          # has_specific_part = False
          if event.content and event.content.parts and event.is_final_response():
              for part in event.content.parts: # Iterate through all parts
                  if part.executable_code:
                      # Access the actual code string via .code
                      print(f"  Debug: Agent generated code:\n```python\n{part.executable_code.code}\n```")
                      has_specific_part = True
                  elif part.code_execution_result:
                      # Access outcome and output correctly
                      print(f"  Debug: Code Execution Result: {part.code_execution_result.outcome} - Output:\n{part.code_execution_result.output}")
                      has_specific_part = True
                  # Also print any text parts found in any event for debugging
                  elif part.text and not part.text.isspace():
                      print(f"  Text: '{part.text.strip()}'")
                      # Do not set has_specific_part=True here, as we want the final response logic below
              # --- Check for final response AFTER specific parts ---
              text_parts = [part.text for part in event.content.parts if part.text]
              final_result = "".join(text_parts)
              print(f"==> Final Agent Response: {final_result}")
  except Exception as e:
      print(f"ERROR during agent run: {e}")
  print("-" * 30)

## Main async function to run the examples
async def main():
  await call_agent_async("Calculate the value of (5 + 7) * 3")
  await call_agent_async("What is 10 factorial?")

## Execute the main async function
try:
  nest_asyncio.apply()
  asyncio.run(main())
except RuntimeError as e:
  # Handle specific error when running asyncio.run in an already running loop (like Jupyter/Colab)
  if "cannot be called from a running event loop" in str(e):
      print("\nRunning in an existing event loop (like Colab/Jupyter).")
      print("Please run `await main()` in a notebook cell instead.")
      # If in an interactive environment (like a notebook), you might need to run:
      # await main()
  else:
      raise e # Re-raise other runtime errors
```

This script uses Google's Agent Development Kit (ADK) to create an agent that solves mathematical problems by writing and executing Python code. It defines an LlmAgent specifically instructed to act as a calculator, equipping it with the built\_in\_code\_execution tool. The primary logic resides in the call\_agent\_async function, which sends a user's query to the agent's runner and processes the resulting events. Inside this function, an asynchronous loop iterates through events, printing the generated Python code and its execution result for debugging. The code carefully distinguishes between these intermediate steps and the final event containing the numerical answer. Finally, a main function runs the agent with two different mathematical expressions to demonstrate its ability to perform calculations.

此脚本使用 Google 的智能体开发工具包（ADK）创建一个通过编写和执行 Python 代码解决数学问题的智能体。它定义了一个 `LlmAgent`，专门指示其充当计算器，为其配备 `built_in_code_execution` 工具。主要逻辑位于 `call_agent_async` 函数中，该函数向智能体发送用户查询并处理结果事件。在此函数内部，异步循环遍历事件，打印生成的 Python 代码及其执行结果以进行调试。代码仔细区分这些中间步骤和包含数值答案的最终事件。最后，`main` 函数使用两个不同的数学表达式运行智能体，以演示其执行计算的能力。

**Enterprise search:** This code defines a Google ADK application using the google.adk library in Python. It specifically uses a VSearchAgent, which is designed to answer questions by searching a specified Vertex AI Search datastore. The code initializes a VSearchAgent named "q2\_strategy\_vsearch\_agent", providing a description, the model to use ("gemini-2.0-flash-exp"), and the ID of the Vertex AI Search datastore. The DATASTORE\_ID is expected to be set as an environment variable. It then sets up a Runner for the agent, using an InMemorySessionService to manage conversation history. An asynchronous function call\_vsearch\_agent\_async is defined to interact with the agent. This function takes a query, constructs a message content object, and calls the runner's run\_async method to send the query to the agent. The function then streams the agent's response back to the console as it arrives. It also prints information about the final response, including any source attributions from the datastore. Error handling is included to catch exceptions during the agent's execution, providing informative messages about potential issues like an incorrect datastore ID or missing permissions. Another asynchronous function run\_vsearch\_example is provided to demonstrate how to call the agent with example queries. The main execution block checks if the DATASTORE\_ID is set and then runs the example using asyncio.run. It includes a check to handle cases where the code is run in an environment that already has a running event loop, like a Jupyter notebook. 

**企业搜索：** 此代码使用 Python 中的 google.adk 库定义了一个 Google ADK 应用程序。它专门使用 `VSearchAgent`，该智能体通过搜索指定的 Vertex AI 搜索数据存储来回答问题。代码初始化一个名为"q2_strategy_vsearch_agent"的 `VSearchAgent`，提供描述、要使用的模型（"gemini-2.0-flash-exp"）和 Vertex AI 搜索数据存储的 ID。`DATASTORE_ID` 预期设置为环境变量。然后为智能体设置 Runner，使用 `InMemorySessionService` 管理对话历史。定义了异步函数 `call_vsearch_agent_async` 以与智能体交互。它接受查询，构造消息内容对象，并调用运行器的 `run_async` 方法将查询发送到智能体。然后该函数将智能体的响应流式传输到控制台。它还打印有关最终响应的信息，包括来自数据存储的任何来源归因。包含错误处理以捕获智能体执行期间的异常，并提供有关潜在问题（如数据存储 ID 不正确或缺少权限）的信息性消息。提供了另一个异步函数 `run_vsearch_example` 以演示如何使用示例查询调用智能体。主执行块检查 `DATASTORE_ID` 是否已设置，然后使用 `asyncio.run` 运行示例。它包括检查以处理在已有运行事件循环的环境（如 Jupyter 笔记本）中运行代码的情况。

```python
import asyncio
from google.genai import types
from google.adk import agents
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
import os

## --- Configuration ---
## Ensure you have set your GOOGLE_API_KEY and DATASTORE_ID environment variables
## For example:
## os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"
## os.environ["DATASTORE_ID"] = "YOUR_DATASTORE_ID"
DATASTORE_ID = os.environ.get("DATASTORE_ID")

## --- Application Constants ---
APP_NAME = "vsearch_app"
USER_ID = "user_123"  # Example User ID
SESSION_ID = "session_456" # Example Session ID

## --- Agent Definition (Updated with the newer model from the guide) ---
vsearch_agent = agents.VSearchAgent(
   name="q2_strategy_vsearch_agent",
   description="Answers questions about Q2 strategy documents using Vertex AI Search.",
   model="gemini-2.0-flash-exp", # Updated model based on the guide's examples
   datastore_id=DATASTORE_ID,
   model_parameters={"temperature": 0.0}
)

## --- Runner and Session Initialization ---
runner = Runner(
   agent=vsearch_agent,
   app_name=APP_NAME,
   session_service=InMemorySessionService(),
)

## --- Agent Invocation Logic ---
async def call_vsearch_agent_async(query: str):
   """Initializes a session and streams the agent's response."""
   print(f"User: {query}")
   print("Agent: ", end="", flush=True)
   try:
       # Construct the message content correctly
       content = types.Content(role='user', parts=[types.Part(text=query)])
       # Process events as they arrive from the asynchronous runner
       async for event in runner.run_async(
           user_id=USER_ID,
           session_id=SESSION_ID,
           new_message=content
       ):
           # For token-by-token streaming of the response text
           if hasattr(event, 'content_part_delta') and event.content_part_delta:
               print(event.content_part_delta.text, end="", flush=True)
           # Process the final response and its associated metadata
           if event.is_final_response():
               print() # Newline after the streaming response
               if event.grounding_metadata:
                   print(f"  (Source Attributions: {len(event.grounding_metadata.grounding_attributions)} sources found)")
               else:
                   print("  (No grounding metadata found)")
               print("-" * 30)
   except Exception as e:
       print(f"\nAn error occurred: {e}")
       print("Please ensure your datastore ID is correct and that the service account has the necessary permissions.")
       print("-" * 30)

## --- Run Example ---
async def run_vsearch_example():
   # Replace with a question relevant to YOUR datastore content
   await call_vsearch_agent_async("Summarize the main points about the Q2 strategy document.")
   await call_vsearch_agent_async("What safety procedures are mentioned for lab X?")

## --- Execution ---
if __name__ == "__main__":
   if not DATASTORE_ID:
       print("Error: DATASTORE_ID environment variable is not set.")
   else:
       try:
           asyncio.run(run_vsearch_example())
       except RuntimeError as e:
           # This handles cases where asyncio.run is called in an environment
           # that already has a running event loop (like a Jupyter notebook).
           if "cannot be called from a running event loop" in str(e):
               print("Skipping execution in a running event loop. Please run this script directly.")
           else:
               raise e
```

Overall, this code provides a basic framework for building a conversational AI application that leverages Vertex AI Search to answer questions based on information stored in a datastore. It demonstrates how to define an agent, set up a runner, and interact with the agent asynchronously while streaming the response. The focus is on retrieving and synthesizing information from a specific datastore to answer user queries.

总的来说，此代码为构建利用 Vertex AI Search 根据存储在数据存储中的信息回答问题的对话式 AI 应用程序提供了基本框架。它演示了如何定义智能体、设置运行器以及在流式传输响应的同时异步与智能体交互。重点是从特定数据存储检索和综合信息以回答用户查询。

**Vertex Extensions:** A Vertex AI extension is a structured API wrapper that enables a model to connect with external APIs for real-time data processing and action execution. Extensions offer enterprise-grade security, data privacy, and performance guarantees. They can be used for tasks like generating and running code, querying websites, and analyzing information from private datastores. Google provides prebuilt extensions for common use cases like Code Interpreter and Vertex AI Search, with the option to create custom ones. The primary benefit of extensions includes strong enterprise controls and seamless integration with other Google products. The key difference between extensions and function calling lies in their execution: Vertex AI automatically executes extensions, whereas function calls require manual execution by the user or client.

**Vertex Extensions：** Vertex AI 扩展是一个结构化的 API 包装器，使模型能够连接到外部 API 以进行实时数据处理和操作执行。扩展提供企业级安全性、数据隐私和性能保证。它们可用于生成和运行代码、查询网站以及分析来自私有数据存储的信息等任务。Google 为常见用例提供预构建扩展，如代码解释器和 Vertex AI Search，并可选择创建自定义扩展。扩展的主要好处包括强大的企业控制和与其他 Google 产品的无缝集成。扩展和函数调用之间的关键区别在于它们的执行：Vertex AI 自动执行扩展，而函数调用需要用户或客户端手动执行。

## At a Glance

## 速览

**What:** LLMs are powerful text generators, but they are fundamentally disconnected from the outside world. Their knowledge is static, limited to the data they were trained on, and they lack the ability to perform actions or retrieve real-time information. This inherent limitation prevents them from completing tasks that require interaction with external APIs, databases, or services. Without a bridge to these external systems, their utility for solving real-world problems is severely constrained.

**问题背景：** 大型语言模型（LLM）是强大的文本生成器，但它们基本上与外部世界断开连接。它们的知识是静态的，仅限于训练数据，并且缺乏执行操作或检索实时信息的能力。这种固有的限制阻止它们完成需要与外部 API、数据库或服务交互的任务。没有通往这些外部系统的桥梁，它们解决现实世界问题的效用受到严重限制。

**Why:** The Tool Use pattern, often implemented via function calling, provides a standardized solution to this problem. It works by describing available external functions, or "tools," to the LLM in a way it can understand. Based on a user's request, the agentic LLM can then decide if a tool is needed and generate a structured data object (like a JSON) specifying which function to call and with what arguments. An orchestration layer executes this function call, retrieves the result, and feeds it back to the LLM. This allows the LLM to incorporate up-to-date, external information or the result of an action into its final response, effectively giving it the ability to act.

**解决方案：** 工具使用模式（通常通过工具调用实现）为此问题提供了标准化解决方案。它的工作原理是以 LLM 可以理解的方式向其描述可用的外部函数或"工具"。基于用户的请求，智能体 LLM 可以决定是否需要工具，并生成指定要调用哪个函数以及使用什么参数的结构化数据对象（如 JSON）。编排层执行此工具调用，检索结果，并将其反馈给 LLM。这允许 LLM 将最新的外部信息或操作结果合并到其最终响应中，有效地赋予其行动能力。

**Rule of thumb:** Use the Tool Use pattern whenever an agent needs to break out of the LLM's internal knowledge and interact with the outside world. This is essential for tasks requiring real-time data (e.g., checking weather, stock prices), accessing private or proprietary information (e.g., querying a company's database), performing precise calculations, executing code, or triggering actions in other systems (e.g., sending an email, controlling smart devices).

**实践建议：** 当智能体需要突破 LLM 的内部知识并与外部世界交互时，使用工具使用模式。这对于需要实时数据（例如，检查天气、股票价格）、访问私有或专有信息（例如，查询公司数据库）、执行精确计算、执行代码或触发其他系统中的操作（例如，发送电子邮件、控制智能设备）的任务至关重要。

**Visual summary:**

**可视化摘要：**

![][image2]

Fig.2: Tool use design pattern

图 2：工具使用设计模式

## Key Takeaways

## 关键要点

* Tool Use (Function Calling) allows agents to interact with external systems and access dynamic information.  
* It involves defining tools with clear descriptions and parameters that the LLM can understand.  
* The LLM decides when to use a tool and generates structured function calls.  
* Agentic frameworks execute the actual tool calls and return the results to the LLM.  
* Tool Use is essential for building agents that can perform real-world actions and provide up-to-date information.  
* LangChain simplifies tool definition using the @tool decorator and provides create\_tool\_calling\_agent and AgentExecutor for building tool-using agents.  
* Google ADK has a number of very useful pre-built tools such as Google Search, Code Execution and Vertex AI Search Tool.

* 工具使用（函数调用）允许智能体与外部系统交互并访问动态信息。
* 它涉及定义具有 LLM 可以理解的清晰描述和参数的工具。
* LLM 决定何时使用工具并生成结构化工具调用。
* 智能体框架执行实际的工具调用并将结果返回给 LLM。
* 工具使用对于构建可以执行现实世界操作并提供最新信息的智能体至关重要。
* LangChain 使用 @tool 装饰器简化工具定义，并提供 create_tool_calling_agent 和 AgentExecutor 用于构建工具使用智能体。
* Google ADK 有许多非常有用的预构建工具，如 Google 搜索、代码执行和 Vertex AI 搜索工具。

## Conclusion

## 结论

The Tool Use pattern is a critical architectural principle for extending the functional scope of large language models beyond their intrinsic text generation capabilities. By equipping a model with the ability to interface with external software and data sources, this paradigm allows an agent to perform actions, execute computations, and retrieve information from other systems. This process involves the model generating a structured request to call an external tool when it determines that doing so is necessary to fulfill a user's query. Frameworks such as LangChain, Google ADK, and Crew AI offer structured abstractions and components that facilitate the integration of these external tools. These frameworks manage the process of exposing tool specifications to the model and parsing its subsequent tool-use requests. This simplifies the development of sophisticated agentic systems that can interact with and take action within external digital environments.

工具使用模式是将大型语言模型的功能范围扩展到其固有文本生成能力之外的关键架构原则。通过为模型配备与外部软件和数据源交互的能力，此范式允许智能体执行操作、进行计算并从其他系统检索信息。此过程涉及模型在确定满足用户查询需要时生成调用外部工具的结构化请求。LangChain、Google ADK 和 CrewAI 等框架提供结构化抽象和组件，促进这些外部工具的集成。这些框架管理向模型公开工具规范并解析其后续工具使用请求的过程。这简化了可以与外部数字环境交互并在其中采取行动的复杂智能体系统的开发。

## References

## 参考文献

1. LangChain Documentation (Tools): [https://python.langchain.com/docs/integrations/tools/](https://python.langchain.com/docs/integrations/tools/)   
2. Google Agent Developer Kit (ADK) Documentation (Tools): [https://google.github.io/adk-docs/tools/](https://google.github.io/adk-docs/tools/)   
3. OpenAI Function Calling Documentation: [https://platform.openai.com/docs/guides/function-calling](https://platform.openai.com/docs/guides/function-calling)   
4. CrewAI Documentation (Tools): [https://docs.crewai.com/concepts/tools](https://docs.crewai.com/concepts/tools) 

[image1]: ../images/chapter-5/image1.png

[image2]: ../images/chapter-5/image2.png
