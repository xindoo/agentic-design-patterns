# 第 16 章：资源感知优化

资源感知优化使智能 Agent 能够在运行期间动态监控和管理计算、时间和财务资源。这与简单的规划不同，后者主要关注动作排序。资源感知优化要求 Agent 就动作执行做出决策，以在指定的资源预算内实现目标或优化效率。这涉及在更准确但昂贵的模型与更快速、成本更低的模型之间做出选择，或者决定是否分配额外的计算资源以获得更精细的响应，还是返回更快但细节较少的答案。

例如，考虑一个被指派为金融分析师分析大型数据集的 Agent。如果分析师立即需要初步报告，Agent 可能会使用更快、更实惠的模型来快速总结关键趋势。然而，如果分析师需要高度准确的预测用于关键投资决策，并且有更大的预算和更多时间，Agent 将分配更多资源来利用强大、较慢但更精确的预测模型。此类别中的一个关键策略是回退机制，它在首选模型由于过载或受限而不可用时充当保障。为了确保优雅降级，系统会自动切换到默认或更实惠的模型，保持服务连续性而不是完全失败。

# 实际应用和用例

实际用例包括：

* **成本优化的 LLM 使用**：Agent 根据预算约束，决定是对复杂任务使用大型、昂贵的 LLM，还是对简单查询使用更小、更实惠的 LLM。
* **延迟敏感操作**：在实时系统中，Agent 选择更快但可能不够全面的推理路径以确保及时响应。
* **能源效率**：对于部署在边缘设备或电力有限的 Agent，优化其处理以节省电池寿命。
* **服务可靠性回退**：当主要选择不可用时，Agent 自动切换到备份模型，确保服务连续性和优雅降级。
* **数据使用管理**：Agent 选择摘要数据检索而不是完整数据集下载，以节省带宽或存储。
* **自适应任务分配**：在多 Agent 系统中，Agent 根据其当前计算负载或可用时间自行分配任务。

# 实践代码示例

一个用于回答用户问题的智能系统可以评估每个问题的难度。对于简单查询，它使用成本效益高的语言模型，如 Gemini Flash。对于复杂查询，会考虑更强大但更昂贵的语言模型（如 Gemini Pro）。使用更强大模型的决定还取决于资源可用性，特别是预算和时间约束。这个系统动态选择适当的模型。

例如，考虑一个使用分层 Agent 构建的旅行规划器。高级规划（涉及理解用户的复杂请求，将其分解为多步骤行程，并做出逻辑决策）将由像 Gemini Pro 这样的复杂且更强大的 LLM 管理。这是需要深入理解上下文和推理能力的"规划器"Agent。

然而，一旦计划建立，该计划中的各个任务，如查询航班价格、检查酒店可用性或查找餐厅评论，本质上是简单的、重复的网络查询。这些"工具函数调用"可以由更快、更实惠的模型（如 Gemini Flash）执行。更容易理解为什么实惠模型可以用于这些直接的网络搜索，而复杂的规划阶段需要更高级模型的更强智能来确保连贯和合逻辑的旅行计划。

Google 的 ADK 通过其多 Agent 架构支持这种方法，允许模块化和可扩展的应用程序。不同的 Agent 可以处理专门的任务。模型灵活性使得可以直接使用各种 Gemini 模型，包括 Gemini Pro 和 Gemini Flash，或通过 LiteLLM 集成其他模型。ADK 的编排能力支持动态、LLM 驱动的路由以实现自适应行为。内置的评估功能允许系统评估 Agent 性能，可用于系统改进（参见评估和监控章节）。

接下来，将定义两个具有相同设置但使用不同模型和成本的 Agent。

```python
# 概念性的类 Python 结构，非可运行代码
from google.adk.agents import Agent
# from google.adk.models.lite_llm import LiteLlm # 如果使用 ADK 默认 Agent 不直接支持的模型

# 使用更昂贵的 Gemini Pro 2.5 的 Agent
gemini_pro_agent = Agent(
    name="GeminiProAgent",
    model="gemini-2.5-pro", # 如果实际模型名称不同，这是占位符
    description="A highly capable agent for complex queries.",
    instruction="You are an expert assistant for complex problem-solving."
)

# 使用更便宜的 Gemini Flash 2.5 的 Agent
gemini_flash_agent = Agent(
    name="GeminiFlashAgent",
    model="gemini-2.5-flash", # 如果实际模型名称不同，这是占位符
    description="A fast and efficient agent for simple queries.",
    instruction="You are a quick assistant for straightforward questions."
)
```

路由器 Agent 可以基于简单的指标（如查询长度）引导查询，其中较短的查询转到较便宜的模型，较长的查询转到更强大的模型。然而，更复杂的路由器 Agent 可以利用 LLM 或 ML 模型来分析查询的细微差别和复杂性。这个 LLM 路由器可以确定哪个下游语言模型最合适。例如，请求事实回忆的查询被路由到 flash 模型，而需要深入分析的复杂查询被路由到 pro 模型。

优化技术可以进一步增强 LLM 路由器的有效性。提示词调优涉及精心设计提示词以指导路由器 LLM 做出更好的路由决策。在查询及其最优模型选择的数据集上微调 LLM 路由器可提高其准确性和效率。这种动态路由能力在响应质量和成本效益之间取得平衡。

```python
# 概念性的类 Python 结构，非可运行代码
from google.adk.agents import Agent, BaseAgent
from google.adk.events import Event
from google.adk.agents.invocation_context import InvocationContext
import asyncio

class QueryRouterAgent(BaseAgent):
    name: str = "QueryRouter"
    description: str = "Routes user queries to the appropriate LLM agent based on complexity."

    async def _run_async_impl(self, context: InvocationContext) -> AsyncGenerator[Event, None]:
        user_query = context.current_message.text # 假设文本输入
        query_length = len(user_query.split()) # 简单指标：单词数

        if query_length < 20: # 示例阈值，用于简单性与复杂性的区分
            print(f"Routing to Gemini Flash Agent for short query (length: {query_length})")
            # 在真实的 ADK 设置中，您会使用 'transfer_to_agent' 或直接调用
            # 为了演示，我们将模拟一个调用并产生其响应
            response = await gemini_flash_agent.run_async(context.current_message)
            yield Event(author=self.name, content=f"Flash Agent processed: {response}")
        else:
            print(f"Routing to Gemini Pro Agent for long query (length: {query_length})")
            response = await gemini_pro_agent.run_async(context.current_message)
            yield Event(author=self.name, content=f"Pro Agent processed: {response}")
```

批评 Agent 评估语言模型的响应，提供具有多种功能的反馈。对于自我纠正，它识别错误或不一致，促使回答 Agent 改进其输出以提高质量。它还系统地评估响应以进行性能监控，跟踪准确性和相关性等指标，用于优化。

此外，其反馈可以为强化学习或微调提供信号；例如，持续识别 Flash 模型响应不足可以改进路由器 Agent 的逻辑。虽然不直接管理预算，批评 Agent 通过识别次优路由选择（例如将简单查询定向到 Pro 模型或将复杂查询定向到 Flash 模型，导致结果不佳）来间接管理预算。这为改进资源分配和节约成本的调整提供了信息。

批评 Agent 可以配置为仅审查回答 Agent 生成的文本，或同时审查原始查询和生成的文本，从而能够全面评估响应与初始问题的一致性。

```text
CRITIC_SYSTEM_PROMPT = """
You are the **Critic Agent**, serving as the quality assurance arm of our collaborative research assistant system. Your primary function is to **meticulously review and challenge** information from the Researcher Agent, guaranteeing **accuracy, completeness, and unbiased presentation**. Your duties encompass:
* **Assessing research findings** for factual correctness, thoroughness, and potential leanings.
* **Identifying any missing data** or inconsistencies in reasoning.
* **Raising critical questions** that could refine or expand the current understanding.
* **Offering constructive suggestions** for enhancement or exploring different angles.
* **Validating that the final output is comprehensive** and balanced.
All criticism must be constructive. Your goal is to fortify the research, not invalidate it. Structure your feedback clearly, drawing attention to specific points for revision. Your overarching aim is to ensure the final research product meets the highest possible quality standards.
"""
```

批评 Agent 基于预定义的系统提示词运行，该提示词概述其角色、职责和反馈方法。为此 Agent 设计良好的提示词必须清楚地确立其作为评估者的功能。它应指定批评重点领域，并强调提供建设性反馈而不仅仅是拒绝。提示词还应鼓励识别优势和弱点，并且必须指导 Agent 如何构建和呈现其反馈。

# 使用 OpenAI 的实践代码

该系统使用资源感知优化策略来有效处理用户查询。它首先将每个查询分类为三个类别之一，以确定最合适和最具成本效益的处理路径。这种方法避免在简单请求上浪费计算资源，同时确保复杂查询获得必要的关注。三个类别是：

* simple：用于可以直接回答而无需复杂推理或外部数据的简单问题。
* reasoning：用于需要逻辑推理或多步骤思考过程的查询，这些查询被路由到更强大的模型。
* internet_search：用于需要当前信息的问题，会自动触发 Google 搜索以提供最新答案。

代码在 MIT 许可证下，可在 Github 上获取：([https://github.com/mahtabsyed/21-Agentic-Patterns/blob/main/16\_Resource\_Aware\_Opt\_LLM\_Reflection\_v2.ipynb](https://github.com/mahtabsyed/21-Agentic-Patterns/blob/main/16_Resource_Aware_Opt_LLM_Reflection_v2.ipynb))

```python
# MIT License
# Copyright (c) 2025 Mahtab Syed
# https://www.linkedin.com/in/mahtabsyed/

import os
import requests
import json
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_CUSTOM_SEARCH_API_KEY = os.getenv("GOOGLE_CUSTOM_SEARCH_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

if not OPENAI_API_KEY or not GOOGLE_CUSTOM_SEARCH_API_KEY or not GOOGLE_CSE_ID:
    raise ValueError(
        "Please set OPENAI_API_KEY, GOOGLE_CUSTOM_SEARCH_API_KEY, and GOOGLE_CSE_ID in your .env file."
    )

client = OpenAI(api_key=OPENAI_API_KEY)

# --- 步骤 1：分类提示词 ---
def classify_prompt(prompt: str) -> dict:
    system_message = {
        "role": "system",
        "content": (
            "You are a classifier that analyzes user prompts and returns one of three categories ONLY:\n\n"
            "- simple\n"
            "- reasoning\n"
            "- internet_search\n\n"
            "Rules:\n"
            "- Use 'simple' for direct factual questions that need no reasoning or current events.\n"
            "- Use 'reasoning' for logic, math, or multi-step inference questions.\n"
            "- Use 'internet_search' if the prompt refers to current events, recent data, or things not in your training data.\n\n"
            "Respond ONLY with JSON like:\n"
            '{ "classification": "simple" }'
        ),
    }
    user_message = {"role": "user", "content": prompt}
    response = client.chat.completions.create(
        model="gpt-4o", messages=[system_message, user_message], temperature=1
    )
    reply = response.choices[0].message.content
    return json.loads(reply)

# --- 步骤 2：Google 搜索 ---
def google_search(query: str, num_results=1) -> list:
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_CUSTOM_SEARCH_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": query,
        "num": num_results,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        results = response.json()
        if "items" in results and results["items"]:
            return [
                {
                    "title": item.get("title"),
                    "snippet": item.get("snippet"),
                    "link": item.get("link"),
                }
                for item in results["items"]
            ]
        else:
            return []
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# --- 步骤 3：生成响应 ---
def generate_response(prompt: str, classification: str, search_results=None) -> str:
    if classification == "simple":
        model = "gpt-4o-mini"
        full_prompt = prompt
    elif classification == "reasoning":
        model = "o4-mini"
        full_prompt = prompt
    elif classification == "internet_search":
        model = "gpt-4o"
        # 将每个搜索结果字典转换为可读字符串
        if search_results:
            search_context = "\n".join(
                [
                    f"Title: {item.get('title')}\nSnippet: {item.get('snippet')}\nLink: {item.get('link')}"
                    for item in search_results
                ]
            )
        else:
            search_context = "No search results found."
        full_prompt = f"""Use the following web results to answer the user query: {search_context} Query: {prompt}"""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": full_prompt}],
        temperature=1,
    )
    return response.choices[0].message.content, model

# --- 步骤 4：组合路由器 ---
def handle_prompt(prompt: str) -> dict:
    classification_result = classify_prompt(prompt)
    # 删除或注释掉下一行以避免重复打印
    # print("\n🔍 Classification Result:", classification_result)
    classification = classification_result["classification"]
    search_results = None
    if classification == "internet_search":
        search_results = google_search(prompt)
        # print("\n🔍 Search Results:", search_results)
    answer, model = generate_response(prompt, classification, search_results)
    return {"classification": classification, "response": answer, "model": model}

test_prompt = "What is the capital of Australia?"
# test_prompt = "Explain the impact of quantum computing on cryptography."
# test_prompt = "When does the Australian Open 2026 start, give me full date?"
result = handle_prompt(test_prompt)
print("🔍 Classification:", result["classification"])
print("🧠 Model Used:", result["model"])
print("🧠 Response:\n", result["response"])
```

这段 Python 代码实现了一个提示词路由系统来回答用户问题。它首先从 .env 文件加载 OpenAI 和 Google 自定义搜索的必要 API 密钥。核心功能在于将用户的提示词分类为三个类别：simple、reasoning 或 internet search。专用函数利用 OpenAI 模型进行此分类步骤。如果提示词需要当前信息，则使用 Google 自定义搜索 API 执行 Google 搜索。另一个函数然后生成最终响应，根据分类选择适当的 OpenAI 模型。对于互联网搜索查询，搜索结果作为上下文提供给模型。主 handle_prompt 函数编排此工作流，在生成响应之前调用分类和搜索（如果需要）函数。它返回分类、使用的模型和生成的答案。该系统有效地将不同类型的查询引导到优化的方法以获得更好的响应。

# 实践代码示例（OpenRouter）

OpenRouter 通过单个 API 端点提供对数百个 AI 模型的统一接口。它提供自动故障转移和成本优化，可通过您首选的 SDK 或框架轻松集成。

```python
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "HTTP-Referer": "<YOUR_SITE_URL>", # 可选。用于 openrouter.ai 上排名的网站 URL。
    "X-Title": "<YOUR_SITE_NAME>", # 可选。用于 openrouter.ai 上排名的网站标题。
  },
  data=json.dumps({
    "model": "openai/gpt-4o", # 可选
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  })
)
```

这段代码片段使用 requests 库与 OpenRouter API 交互。它向聊天完成端点发送带有用户消息的 POST 请求。请求包括带有 API 密钥和可选网站信息的授权头。目标是从指定的语言模型（在本例中为"openai/gpt-4o"）获得响应。

Openrouter 提供两种不同的方法来路由和确定用于处理给定请求的计算模型。

* **自动模型选择**：此功能将请求路由到从一组精选可用模型中选择的优化模型。选择基于用户提示词的特定内容。最终处理请求的模型的标识符在响应的元数据中返回。

```json
{
  "model": "openrouter/auto",
  ... // 其他参数
}
```

* **顺序模型回退**：此机制通过允许用户指定分层模型列表来提供运营冗余。系统将首先尝试使用序列中指定的主要模型处理请求。如果此主要模型由于任何错误条件（如服务不可用、速率限制或内容过滤）而无法响应，系统将自动将请求重新路由到序列中的下一个指定模型。此过程继续，直到列表中的模型成功执行请求或列表耗尽。操作的最终成本和响应中返回的模型标识符将对应于成功完成计算的模型。

```json
{
  "models": ["anthropic/claude-3.5-sonnet", "gryphe/mythomax-l2-13b"],
  ... // 其他参数
}
```

OpenRouter 提供详细的排行榜（[https://openrouter.ai/rankings](https://openrouter.ai/rankings)），根据可用 AI 模型的累积 token 生成对其进行排名。它还提供来自不同提供商（ChatGPT、Gemini、Claude）的最新模型（见图 1）

![][image1]  
图 1：OpenRouter 网站（[https://openrouter.ai/](https://openrouter.ai/)）

# 超越动态模型切换：Agent 资源优化的范围

资源感知优化对于开发在现实世界约束内高效有效运行的智能 Agent 系统至关重要。让我们看看一些额外的技术：

**动态模型切换**是一项关键技术，涉及根据手头任务的复杂性和可用计算资源战略性地选择大语言模型。当面对简单查询时，可以部署轻量级、成本效益高的 LLM，而复杂的、多方面的问题则需要利用更复杂和资源密集型的模型。

**自适应工具使用和选择**确保 Agent 可以智能地从一套工具中进行选择，为每个特定子任务选择最合适和高效的工具，并仔细考虑 API 使用成本、延迟和执行时间等因素。这种动态工具选择通过优化外部 API 和服务的使用来提高整体系统效率。

**上下文修剪和摘要**在管理 Agent 处理的信息量方面发挥着至关重要的作用，通过智能摘要和选择性保留交互历史中最相关的信息，战略性地最小化提示词 token 计数并降低推理成本，防止不必要的计算开销。

**主动资源预测**涉及通过预测未来工作负载和系统需求来预测资源需求，这允许主动分配和管理资源，确保系统响应性并防止瓶颈。

**成本敏感探索**在多 Agent 系统中将优化考虑扩展到包括通信成本以及传统计算成本，影响 Agent 用于协作和共享信息的策略，旨在最小化整体资源支出。

**节能部署**专门针对资源严格约束的环境，旨在最小化智能 Agent 系统的能源足迹，延长运营时间并降低整体运行成本。

**并行化和分布式计算感知**利用分布式资源来增强 Agent 的处理能力和吞吐量，将计算工作负载分布到多台机器或处理器上，以实现更高的效率和更快的任务完成。

**学习型资源分配策略**引入学习机制，使 Agent 能够根据反馈和性能指标随时间调整和优化其资源分配策略，通过持续改进来提高效率。

**优雅降级和回退机制**确保智能 Agent 系统即使在资源约束严重时也能继续运行，尽管可能以降低的能力运行，优雅地降低性能并回退到替代策略以维持运营并提供基本功能。

# 概览

**什么**：资源感知优化解决了在智能系统中管理计算、时间和财务资源消耗的挑战。基于 LLM 的应用程序可能既昂贵又缓慢，为每项任务选择最佳模型或工具通常效率低下。这在系统输出的质量与产生它所需的资源之间创建了基本权衡。如果没有动态管理策略，系统无法适应不同的任务复杂性或在预算和性能约束内运行。

**为什么**：标准化解决方案是构建一个智能监控和分配资源的 agentic 系统。此模式通常使用"路由器 Agent"首先对传入请求的复杂性进行分类。然后将请求转发到最合适的 LLM 或工具——对于简单查询使用快速、廉价的模型，对于复杂推理使用更强大的模型。"批评 Agent"可以通过评估响应质量来进一步改进流程，提供反馈以随时间改进路由逻辑。这种动态、多 Agent 方法确保系统高效运行，在响应质量和成本效益之间取得平衡。

**经验法则**：在以下情况下使用此模式：在 API 调用或计算能力的严格财务预算下运行，构建对延迟敏感的应用程序（其中快速响应时间至关重要），在资源受限的硬件（如电池寿命有限的边缘设备）上部署 Agent，以编程方式平衡响应质量和运营成本之间的权衡，以及管理复杂的、多步骤的工作流（其中不同任务具有不同的资源需求）。

**视觉摘要**

**![][image2]**

图 2：资源感知优化设计模式

# 关键要点

* 资源感知优化至关重要：智能 Agent 可以动态管理计算、时间和财务资源。根据实时约束和目标做出关于模型使用和执行路径的决策。
* 可扩展性的多 Agent 架构：Google 的 ADK 提供多 Agent 框架，实现模块化设计。不同的 Agent（回答、路由、批评）处理特定任务。
* 动态、LLM 驱动的路由：路由器 Agent 根据查询复杂性和预算将查询引导到语言模型（简单查询使用 Gemini Flash，复杂查询使用 Gemini Pro）。这优化了成本和性能。
* 批评 Agent 功能：专用批评 Agent 提供自我纠正、性能监控和改进路由逻辑的反馈，增强系统有效性。
* 通过反馈和灵活性进行优化：批评和模型集成灵活性的评估能力有助于自适应和自我改进的系统行为。
* 其他资源感知优化：其他方法包括自适应工具使用和选择、上下文修剪和摘要、主动资源预测、多 Agent 系统中的成本敏感探索、节能部署、并行化和分布式计算感知、学习型资源分配策略、优雅降级和回退机制，以及关键任务的优先级排序。

# 结论

资源感知优化对于智能 Agent 的开发至关重要，能够在现实世界约束内高效运行。通过管理计算、时间和财务资源，Agent 可以实现最佳性能和成本效益。动态模型切换、自适应工具使用和上下文修剪等技术对于实现这些效率至关重要。高级策略，包括学习型资源分配策略和优雅降级，增强了 Agent 在不同条件下的适应性和弹性。将这些优化原则集成到 Agent 设计中对于构建可扩展、强大和可持续的 AI 系统至关重要。

# 参考文献

1. Google's Agent Development Kit (ADK): [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)
2. Gemini Flash 2.5 & Gemini 2.5 Pro:  [https://aistudio.google.com/](https://aistudio.google.com/)
3. OpenRouter: [https://openrouter.ai/docs/quickstart](https://openrouter.ai/docs/quickstart)

[image1]: ../images/chapter-16/image1.png

[image2]: ../images/chapter-16/image2.png