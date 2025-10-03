# 第 2 章：路由

## 路由模式概述

虽然通过提示词链进行顺序处理是执行确定性、线性工作流的基础技术，但其适用性在需要自适应响应的场景中受到限制。现实世界的 Agent 系统必须经常根据偶然因素在多个潜在行动之间进行仲裁，例如环境状态、用户输入或前一操作的结果。这种动态决策能力，控制流向不同的专门函数、工具或子流程，是通过一种称为路由的机制实现的。

路由将条件逻辑引入 Agent 的操作框架，使其能够从固定执行路径转变为这样一种模型：Agent 动态评估特定标准以从一组可能的后续行动中进行选择。这允许更灵活和上下文感知的系统行为。

例如，一个设计用于客户查询的 Agent，当配备路由功能时，可以首先对传入查询进行分类以确定用户的意图。基于此分类，它可以将查询定向到专门的 Agent 进行直接问答、用于帐户信息的数据库检索工具，或用于复杂问题的升级程序，而不是默认使用单一的预定响应路径。因此，使用路由的更复杂 Agent 可以：

1. 分析用户的查询。
2. 基于其**意图**路由查询：
   * 如果意图是"检查订单状态"，路由到与订单数据库交互的子 Agent 或工具链。
   * 如果意图是"产品信息"，路由到搜索产品目录的子 Agent 或链。
   * 如果意图是"技术支持"，路由到访问故障排除指南或升级到人工的不同链。
   * 如果意图不清楚，路由到澄清子 Agent 或提示词链。

路由模式的核心组件是执行评估并指导流程的机制。这种机制可以通过几种方式实现：

* **基于 LLM 的路由：** 语言模型本身可以被提示分析输入并输出指示下一步或目的地的特定标识符或指令。例如，提示词可能要求 LLM "分析以下用户查询并仅输出类别：'订单状态'、'产品信息'、'技术支持'或'其他'。" Agent 系统然后读取此输出并相应地指导工作流。
* **基于嵌入的路由：** 输入查询可以转换为向量嵌入（参见 RAG，第 14 章）。然后将此嵌入与代表不同路由或能力的嵌入进行比较。查询被路由到嵌入最相似的路由。这对于语义路由很有用，其中决策基于输入的含义而不仅仅是关键词。
* **基于规则的路由：** 这涉及使用基于关键词、模式或从输入中提取的结构化数据的预定义规则或逻辑（例如，if-else 语句、switch case）。这可以比基于 LLM 的路由更快、更确定，但在处理细微或新颖输入方面的灵活性较差。
* **基于机器学习模型的路由：** 它采用判别模型，例如分类器，该模型已经在小型标记数据语料库上专门训练以执行路由任务。虽然它与基于嵌入的方法在概念上有相似之处，但其关键特征是监督微调过程，该过程调整模型的参数以创建专门的路由功能。这种技术与基于 LLM 的路由不同，因为决策组件不是在推理时执行提示词的生成模型。相反，路由逻辑被编码在微调模型的学习权重中。虽然 LLM 可能在预处理步骤中用于生成合成数据以增强训练集，但它们不参与实时路由决策本身。

路由机制可以在 Agent 操作周期内的多个节点实现。它们可以在开始时应用以对主要任务进行分类，在处理链内的中间点应用以确定后续操作，或在子程序期间应用以从给定集合中选择最合适的工具。

诸如 LangChain、LangGraph 和 Google 的 Agent Developer Kit (ADK) 等计算框架提供了用于定义和管理这种条件逻辑的显式构造。凭借其基于状态的图架构，LangGraph 特别适合复杂的路由场景，其中决策取决于整个系统的累积状态。类似地，Google 的 ADK 提供了用于构建 Agent 能力和交互模型的基础组件，这些组件作为实现路由逻辑的基础。在这些框架提供的执行环境中，开发人员定义可能的操作路径以及决定计算图中节点之间转换的函数或基于模型的评估。

路由的实现使系统能够超越确定性顺序处理。它促进了更自适应的执行流的开发，可以动态且适当地响应更广泛的输入和状态变化。

## 实际应用与用例

路由模式是自适应 Agent 系统设计中的关键控制机制，使它们能够动态改变其执行路径以响应可变输入和内部状态。其效用通过提供必要的条件逻辑层跨越多个领域。

在人机交互中，例如虚拟助手或 AI 驱动的导师，路由用于解释用户意图。对自然语言查询的初始分析确定最合适的后续操作，无论是调用特定信息检索工具、升级到人工操作员，还是根据用户表现选择课程中的下一个模块。这使系统能够超越线性对话流并进行上下文响应。

在自动化数据和文档处理管道中，路由作为分类和分发功能。传入的数据，如电子邮件、支持票据或 API 有效载荷，根据内容、元数据或格式进行分析。然后系统将每个项目定向到相应的工作流，例如销售线索摄入流程、JSON 或 CSV 格式的特定数据转换函数，或紧急问题升级路径。

在涉及多个专门工具或 Agent 的复杂系统中，路由充当高级调度器。由用于搜索、总结和分析信息的不同 Agent 组成的研究系统将使用路由器根据当前目标将任务分配给最合适的 Agent。类似地，AI 编码助手使用路由来识别编程语言和用户意图——调试、解释或翻译——然后将代码片段传递给正确的专门工具。

最终，路由提供了创建功能多样化和上下文感知系统所必需的逻辑仲裁能力。它将 Agent 从预定义序列的静态执行器转变为可以在变化条件下就完成任务的最有效方法做出决策的动态系统。

## 实操代码示例（LangChain）

在代码中实现路由涉及定义可能的路径和决定采取哪条路径的逻辑。像 LangChain 和 LangGraph 这样的框架为此提供了特定的组件和结构。LangGraph 基于状态的图结构对于可视化和实现路由逻辑特别直观。

此代码演示了使用 LangChain 和 Google 的生成式 AI 的简单类 Agent 系统。它设置了一个"协调器"，根据请求的意图（预订、信息或不清楚）将用户请求路由到不同的模拟"子 Agent"处理程序。系统使用语言模型对请求进行分类，然后将其委托给适当的处理函数，模拟多 Agent 架构中常见的基本委托模式。

首先，确保您已安装必要的库：

```bash
pip install langchain langgraph google-cloud-aiplatform langchain-google-genai google-adk deprecated pydantic
```

您还需要使用您选择的语言模型的 API 密钥设置环境（例如，OpenAI、Google Gemini、Anthropic）。

```python
## Copyright (c) 2025 Marco Fago
## https://www.linkedin.com/in/marco-fago/
#
## 此代码根据 MIT 许可证授权。
## 请参阅仓库中的 LICENSE 文件以获取完整许可文本。
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch

## --- 配置 ---
## 确保设置了您的 API 密钥环境变量（例如，GOOGLE_API_KEY）
try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    print(f"语言模型已初始化: {llm.model}")
except Exception as e:
    print(f"初始化语言模型时出错: {e}")
    llm = None

## --- 定义模拟子 Agent 处理程序（相当于 ADK 的 sub_agents）---
def booking_handler(request: str) -> str:
    """模拟预订 Agent 处理请求。"""
    print("\n--- 委托给预订处理程序 ---")
    return f"预订处理程序处理了请求：'{request}'。结果：模拟预订操作。"

def info_handler(request: str) -> str:
    """模拟信息 Agent 处理请求。"""
    print("\n--- 委托给信息处理程序 ---")
    return f"信息处理程序处理了请求：'{request}'。结果：模拟信息检索。"

def unclear_handler(request: str) -> str:
    """处理无法委托的请求。"""
    print("\n--- 处理不清楚的请求 ---")
    return f"协调器无法委托请求：'{request}'。请澄清。"

## --- 定义协调器路由链（相当于 ADK 协调器的指令）---
## 此链决定应委托给哪个处理程序。
coordinator_router_prompt = ChatPromptTemplate.from_messages([
    ("system", """分析用户的请求并确定哪个专家处理程序应处理它。
     - 如果请求与预订航班或酒店相关，
        输出 'booker'。
     - 对于所有其他一般信息问题，输出 'info'。
     - 如果请求不清楚或不适合任一类别，
        输出 'unclear'。
     只输出一个词：'booker'、'info' 或 'unclear'。"""),
    ("user", "{request}")
])

if llm:
    coordinator_router_chain = coordinator_router_prompt | llm | StrOutputParser()

## --- 定义委托逻辑（相当于 ADK 的基于 sub_agents 的自动流）---
## 使用 RunnableBranch 根据路由链的输出进行路由。
## 为 RunnableBranch 定义分支
branches = {
    "booker": RunnablePassthrough.assign(output=lambda x: booking_handler(x['request']['request'])),
    "info": RunnablePassthrough.assign(output=lambda x: info_handler(x['request']['request'])),
    "unclear": RunnablePassthrough.assign(output=lambda x: unclear_handler(x['request']['request'])),
}

## 创建 RunnableBranch。它接受路由链的输出
## 并将原始输入（'request'）路由到相应的处理程序。
delegation_branch = RunnableBranch(
    (lambda x: x['decision'].strip() == 'booker', branches["booker"]), # 添加了 .strip()
    (lambda x: x['decision'].strip() == 'info', branches["info"]),     # 添加了 .strip()
    branches["unclear"] # 'unclear' 或任何其他输出的默认分支
)

## 将路由链和委托分支组合成单个可运行对象
## 路由链的输出（'decision'）与原始输入（'request'）一起传递
## 到 delegation_branch。
coordinator_agent = {
    "decision": coordinator_router_chain,
    "request": RunnablePassthrough()
} | delegation_branch | (lambda x: x['output']) # 提取最终输出

## --- 示例用法 ---
def main():
    if not llm:
        print("\n由于 LLM 初始化失败，跳过执行。")
        return
    
    print("--- 运行预订请求 ---")
    request_a = "给我预订去伦敦的航班。"
    result_a = coordinator_agent.invoke({"request": request_a})
    print(f"最终结果 A: {result_a}")
    
    print("\n--- 运行信息请求 ---")
    request_b = "意大利的首都是什么？"
    result_b = coordinator_agent.invoke({"request": request_b})
    print(f"最终结果 B: {result_b}")
    
    print("\n--- 运行不清楚的请求 ---")
    request_c = "告诉我关于量子物理学的事。"
    result_c = coordinator_agent.invoke({"request": request_c})
    print(f"最终结果 C: {result_c}")

if __name__ == "__main__":
    main()
```

如上所述，这段 Python 代码使用 LangChain 库和 Google 的生成式 AI 模型（特别是 gemini-2.5-flash）构建了一个简单的类 Agent 系统。详细来说，它定义了三个模拟子 Agent 处理程序：booking_handler、info_handler 和 unclear_handler，每个都设计用于处理特定类型的请求。

核心组件是 coordinator_router_chain，它利用 ChatPromptTemplate 指示语言模型将传入的用户请求分类为三个类别之一：'booker'、'info' 或 'unclear'。然后路由链的输出由 RunnableBranch 使用，将原始请求委托给相应的处理函数。RunnableBranch 检查来自语言模型的决策，并将请求数据定向到 booking_handler、info_handler 或 unclear_handler。coordinator_agent 结合了这些组件，首先路由请求以做出决策，然后将请求传递给选定的处理程序。最终输出从处理程序的响应中提取。

main 函数通过三个示例请求演示了系统的用法，展示了不同的输入如何被路由并由模拟 Agent 处理。包含了语言模型初始化的错误处理以确保健壮性。代码结构模仿了基本的多 Agent 框架，其中中央协调器根据意图将任务委托给专门的 Agent。

## 实操代码示例（Google ADK）

Agent Development Kit (ADK) 是一个用于工程化 Agent 系统的框架，为定义 Agent 的能力和行为提供了结构化环境。与基于显式计算图的架构相比，ADK 范式中的路由通常通过定义一组离散的"工具"来实现，这些工具代表 Agent 的功能。响应用户查询选择适当工具由框架的内部逻辑管理，该逻辑利用底层模型将用户意图与正确的功能处理程序匹配。

此 Python 代码演示了使用 Google ADK 库的 Agent Development Kit (ADK) 应用程序示例。它设置了一个"协调器" Agent，根据定义的指令将用户请求路由到专门的子 Agent（"Booker"用于预订，"Info"用于一般信息）。然后子 Agent 使用特定工具模拟处理请求，展示了 Agent 系统中的基本委托模式。

```python
## Copyright (c) 2025 Marco Fago
#
## 此代码根据 MIT 许可证授权。
## 请参阅仓库中的 LICENSE 文件以获取完整许可文本。
import uuid
from typing import Dict, Any, Optional
from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import FunctionTool
from google.genai import types
from google.adk.events import Event

## --- 定义工具函数 ---
## 这些函数模拟专家 Agent 的操作。
def booking_handler(request: str) -> str:
    """
    处理航班和酒店的预订请求。
    参数：
        request: 用户的预订请求。
    返回：
        确认预订已处理的消息。
    """
    print("-------------------------- 调用预订处理程序 ----------------------------")
    return f"已模拟对 '{request}' 的预订操作。"

def info_handler(request: str) -> str:
    """
    处理一般信息请求。
    参数：
        request: 用户的问题。
    返回：
        表示信息请求已处理的消息。
    """
    print("-------------------------- 调用信息处理程序 ----------------------------")
    return f"对 '{request}' 的信息请求。结果：模拟信息检索。"

def unclear_handler(request: str) -> str:
    """处理无法委托的请求。"""
    return f"协调器无法委托请求：'{request}'。请澄清。"

## --- 从函数创建工具 ---
booking_tool = FunctionTool(booking_handler)
info_tool = FunctionTool(info_handler)

## 定义配备各自工具的专门子 Agent
booking_agent = Agent(
    name="Booker",
    model="gemini-2.0-flash",
    description="一个专门的 Agent，通过调用预订工具处理所有航班和酒店预订请求。",
    tools=[booking_tool]
)

info_agent = Agent(
    name="Info",
    model="gemini-2.0-flash",
    description="一个专门的 Agent，通过调用信息工具提供一般信息并回答用户问题。",
    tools=[info_tool]
)

## 定义具有明确委托指令的父 Agent
coordinator = Agent(
    name="Coordinator",
    model="gemini-2.0-flash",
    instruction=(
        "你是主协调器。你唯一的任务是分析传入的用户请求"
        "并将它们委托给适当的专家 Agent。不要尝试直接回答用户。\n"
        "- 对于任何与预订航班或酒店相关的请求，委托给 'Booker' Agent。\n"
        "- 对于所有其他一般信息问题，委托给 'Info' Agent。"
    ),
    description="一个将用户请求路由到正确专家 Agent 的协调器。",
    # sub_agents 的存在默认启用 LLM 驱动的委托（自动流）。
    sub_agents=[booking_agent, info_agent]
)

## --- 执行逻辑 ---
async def run_coordinator(runner: InMemoryRunner, request: str):
    """使用给定请求运行协调器 Agent 并委托。"""
    print(f"\n--- 使用请求运行协调器: '{request}' ---")
    final_result = ""
    try:
        user_id = "user_123"
        session_id = str(uuid.uuid4())
        await runner.session_service.create_session(
            app_name=runner.app_name, user_id=user_id, session_id=session_id
        )
        
        for event in runner.run(
            user_id=user_id,
            session_id=session_id,
            new_message=types.Content(
                role='user',
                parts=[types.Part(text=request)]
            ),
        ):
            if event.is_final_response() and event.content:
                # 尝试直接从 event.content 获取文本
                # 以避免迭代部分
                if hasattr(event.content, 'text') and event.content.text:
                    final_result = event.content.text
                elif event.content.parts:
                    # 后备：迭代部分并提取文本（可能触发警告）
                    text_parts = [part.text for part in event.content.parts if part.text]
                    final_result = "".join(text_parts)
                # 假设循环应在最终响应后中断
                break
        
        print(f"协调器最终响应: {final_result}")
        return final_result
    except Exception as e:
        print(f"处理您的请求时出错: {e}")
        return f"处理您的请求时出错: {e}"

async def main():
    """运行 ADK 示例的主函数。"""
    print("--- Google ADK 路由示例（ADK 自动流风格）---")
    print("注意：这需要安装并认证 Google ADK。")
    
    runner = InMemoryRunner(coordinator)
    
    # 示例用法
    result_a = await run_coordinator(runner, "给我在巴黎预订一家酒店。")
    print(f"最终输出 A: {result_a}")
    
    result_b = await run_coordinator(runner, "世界上最高的山是什么？")
    print(f"最终输出 B: {result_b}")
    
    result_c = await run_coordinator(runner, "告诉我一个随机事实。") # 应该去 Info
    print(f"最终输出 C: {result_c}")
    
    result_d = await run_coordinator(runner, "查找下个月去东京的航班。") # 应该去 Booker
    print(f"最终输出 D: {result_d}")

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    await main()
```

此脚本由一个主协调器 Agent 和两个专门的子 Agent 组成：Booker 和 Info。每个专门的 Agent 都配备了一个 FunctionTool，它包装了一个模拟操作的 Python 函数。booking_handler 函数模拟处理航班和酒店预订，而 info_handler 函数模拟检索一般信息。unclear_handler 作为协调器无法委托的请求的后备包含在内，尽管当前协调器逻辑在主 run_coordinator 函数中没有明确使用它进行委托失败。

协调器 Agent 的主要角色，如其指令中定义的，是分析传入的用户消息并将它们委托给 Booker 或 Info Agent。这种委托由 ADK 的自动流机制自动处理，因为协调器定义了 sub_agents。run_coordinator 函数设置了一个 InMemoryRunner，创建一个用户和会话 ID，然后使用运行器通过协调器 Agent 处理用户的请求。runner.run 方法处理请求并产生事件，代码从 event.content 中提取最终响应文本。

main 函数通过使用不同请求运行协调器来演示系统的用法，展示了它如何将预订请求委托给 Booker，将信息请求委托给 Info Agent。

## 概览

**什么：** Agent 系统必须经常响应各种各样的输入和情况，这些无法由单一的线性流程处理。简单的顺序工作流缺乏基于上下文做出决策的能力。没有为特定任务选择正确工具或子流程的机制，系统仍然是僵化和非自适应的。这种限制使得难以构建能够管理现实世界用户请求的复杂性和可变性的复杂应用程序。

**为什么：** 路由模式通过将条件逻辑引入 Agent 的操作框架提供了标准化解决方案。它使系统能够首先分析传入查询以确定其意图或性质。基于此分析，Agent 动态地将控制流定向到最合适的专门工具、功能或子 Agent。这个决策可以由各种方法驱动，包括提示 LLM、应用预定义规则或使用基于嵌入的语义相似性。最终，路由将静态的预定执行路径转变为能够选择最佳可能操作的灵活和上下文感知工作流。

**经验法则：** 当 Agent 必须根据用户输入或当前状态在多个不同的工作流、工具或子 Agent 之间做出决策时，使用路由模式。它对于需要对传入请求进行分类或分类以处理不同类型任务的应用程序至关重要，例如客户支持机器人区分销售查询、技术支持和帐户管理问题。

#### **视觉摘要：**

![][image1]  
图 1：路由模式，使用 LLM 作为路由器

## 关键要点

* 路由使 Agent 能够根据条件动态决定工作流中的下一步。
* 它允许 Agent 处理各种输入并调整其行为，超越线性执行。
* 路由逻辑可以使用 LLM、基于规则的系统或嵌入相似性实现。
* 像 LangGraph 和 Google ADK 这样的框架提供了在 Agent 工作流中定义和管理路由的结构化方式，尽管采用不同的架构方法。

## 结论

路由模式是构建真正动态和响应式 Agent 系统的关键步骤。通过实现路由，我们超越了简单的线性执行流，使我们的 Agent 能够就如何处理信息、响应用户输入以及利用可用工具或子 Agent 做出智能决策。

我们已经看到路由如何应用于各个领域，从客户服务聊天机器人到复杂的数据处理管道。分析输入并有条件地指导工作流的能力是创建能够处理现实世界任务固有可变性的 Agent 的基础。

使用 LangChain 和 Google ADK 的代码示例展示了实现路由的两种不同但有效的方法。LangGraph 基于图的结构提供了定义状态和转换的可视化和显式方式，使其成为具有复杂路由逻辑的复杂多步工作流的理想选择。另一方面，Google ADK 通常专注于定义不同的能力（工具）并依赖框架将用户请求路由到适当工具处理程序的能力，这对于具有明确定义的离散操作集的 Agent 可能更简单。

掌握路由模式对于构建能够智能地导航不同场景并根据上下文提供定制响应或操作的 Agent 至关重要。它是创建多功能和健壮 Agent 应用程序的关键组件。

## 参考文献

1. LangGraph Documentation: [https://www.langchain.com/](https://www.langchain.com/)
2. Google Agent Developer Kit Documentation: [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)

[image1]: ../images/chapter-2/image1.png