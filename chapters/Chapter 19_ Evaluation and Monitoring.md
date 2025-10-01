# 第 19 章：评估和监控

本章探讨了使智能 Agent 能够系统地评估其性能、监控目标进展以及检测操作异常的方法论。虽然第 11 章概述了目标设定和监控，第 17 章讨论了推理机制，但本章侧重于持续的、通常是外部的、对 Agent 有效性、效率和合规性要求的测量。这包括定义指标、建立反馈循环以及实施报告系统，以确保 Agent 性能在操作环境中与期望保持一致（见图 1）。

![][image1]

图 1：评估和监控的最佳实践

# 实际应用与用例

最常见的应用和用例：

* **实时系统中的性能跟踪：** 持续监控部署在生产环境中的 Agent 的准确性、延迟和资源消耗（例如，客户服务聊天机器人的解决率、响应时间）。
* **Agent 改进的 A/B 测试：** 系统地并行比较不同 Agent 版本或策略的性能，以确定最优方法（例如，为物流 Agent 尝试两种不同的规划算法）。
* **合规性和安全审计：** 生成自动化审计报告，跟踪 Agent 随时间遵守道德准则、监管要求和安全协议的情况。这些报告可以由人机协同或另一个 Agent 验证，并可以生成 KPI 或在发现问题时触发警报。
* **企业系统：** 为了治理企业系统中的 Agentic AI，需要一种新的控制工具，即 AI"合约"。这种动态协议为 AI 委派的任务编纂目标、规则和控制。
* **漂移检测：** 随时间监控 Agent 输出的相关性或准确性，检测其性能何时因输入数据分布变化（概念漂移）或环境变化而退化。
* **Agent 行为中的异常检测：** 识别 Agent 采取的异常或意外操作，这些操作可能表明错误、恶意攻击或涌现的不良行为。
* **学习进度评估：** 对于设计为学习的 Agent，跟踪它们的学习曲线、特定技能的改进或在不同任务或数据集上的泛化能力。

# 实践代码示例

为 AI Agent 开发一个全面的评估框架是一项具有挑战性的工作，其复杂性堪比学术学科或大量出版物。这种困难源于需要考虑的众多因素，如模型性能、用户交互、道德影响和更广泛的社会影响。然而，对于实际实施，可以将重点缩小到对 AI Agent 高效有效运行至关重要的关键用例。

**Agent 响应评估：** 这个核心过程对于评估 Agent 输出的质量和准确性至关重要。它涉及确定 Agent 是否针对给定输入提供相关、正确、合乎逻辑、无偏见和准确的信息。评估指标可能包括事实正确性、流畅性、语法精确性和对用户预期目的的遵守。

```python
def evaluate_response_accuracy(agent_output: str, expected_output: str) -> float:
    """计算 Agent 响应的简单准确度分数。"""
    # 这是一个非常基本的精确匹配；现实世界会使用更复杂的指标
    return 1.0 if agent_output.strip().lower() == expected_output.strip().lower() else 0.0

# 示例使用
agent_response = "The capital of France is Paris."
ground_truth = "Paris is the capital of France."
score = evaluate_response_accuracy(agent_response, ground_truth)
print(f"Response accuracy: {score}")
```

Python 函数 `evaluate_response_accuracy` 通过对 Agent 输出和期望输出进行精确的、不区分大小写的比较（在去除前导和尾随空格后），计算 AI Agent 响应的基本准确度分数。对于精确匹配，它返回 1.0 分，否则返回 0.0，表示二元的正确或不正确评估。这种方法虽然适合简单检查，但不考虑诸如释义或语义等价性等变化。

问题在于其比较方法。该函数执行两个字符串的严格的、逐字符比较。在提供的示例中：

* agent_response："The capital of France is Paris."
* ground_truth："Paris is the capital of France."

即使在去除空格并转换为小写后，这两个字符串也不完全相同。因此，该函数将错误地返回准确度分数 `0.0`，即使两个句子传达相同的含义。

简单的比较在评估语义相似性方面不足，只有当 Agent 的响应与期望输出完全匹配时才能成功。更有效的评估需要高级自然语言处理（NLP）技术来辨别句子之间的含义。对于真实世界场景中的全面 AI Agent 评估，更复杂的指标通常是必不可少的。这些指标可以包括字符串相似性度量（如 Levenshtein 距离和 Jaccard 相似性）、关键词分析（特定关键词的存在或缺失）、使用嵌入模型的语义相似性（余弦相似性）、LLM-as-a-Judge 评估（稍后讨论，用于评估细微的正确性和有用性）以及 RAG 特定指标（如忠实性和相关性）。

**延迟监控：** 对 Agent 操作的延迟监控在 AI Agent 响应或操作速度是关键因素的应用中至关重要。此过程测量 Agent 处理请求和生成输出所需的持续时间。较高的延迟会对用户体验和 Agent 的整体有效性产生不利影响，特别是在实时或交互式环境中。在实际应用中，仅将延迟数据打印到控制台是不够的。建议将此信息记录到持久存储系统。选项包括结构化日志文件（例如 JSON）、时间序列数据库（例如 InfluxDB、Prometheus）、数据仓库（例如 Snowflake、BigQuery、PostgreSQL）或可观测性平台（例如 Datadog、Splunk、Grafana Cloud）。

**跟踪 LLM 交互的 Token 使用量：** 对于 LLM 驱动的 Agent，跟踪 token 使用量对于管理成本和优化资源分配至关重要。LLM 交互的计费通常取决于处理的 token 数量（输入和输出）。因此，高效的 token 使用直接降低运营费用。此外，监控 token 计数有助于识别提示词工程或响应生成过程中的潜在改进领域。

```python
# 这是概念性的，因为实际的 token 计数取决于 LLM API
class LLMInteractionMonitor:
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0

    def record_interaction(self, prompt: str, response: str):
        # 在真实场景中，使用 LLM API 的 token 计数器或 tokenizer
        input_tokens = len(prompt.split()) # 占位符
        output_tokens = len(response.split()) # 占位符
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        print(f"已记录交互：输入 tokens={input_tokens}，输出 tokens={output_tokens}")

    def get_total_tokens(self):
        return self.total_input_tokens, self.total_output_tokens

# 示例使用
monitor = LLMInteractionMonitor()
monitor.record_interaction("What is the capital of France?", "The capital of France is Paris.")
monitor.record_interaction("Tell me a joke.", "Why don't scientists trust atoms? Because they make up everything!")
input_t, output_t = monitor.get_total_tokens()
print(f"总输入 tokens：{input_t}，总输出 tokens：{output_t}")
```

本节介绍了一个概念性的 Python 类 `LLMInteractionMonitor`，旨在跟踪大型语言模型交互中的 token 使用量。该类包含输入和输出 token 的计数器。其 `record_interaction` 方法通过分割提示词和响应字符串来模拟 token 计数。在实际实现中，将使用特定的 LLM API tokenizer 进行精确的 token 计数。随着交互的发生，监视器累积总的输入和输出 token 计数。`get_total_tokens` 方法提供对这些累积总数的访问，这对于成本管理和 LLM 使用优化至关重要。

**使用 LLM-as-a-Judge 的"有用性"自定义指标：** 评估 AI Agent 的"有用性"等主观品质带来了超越标准客观指标的挑战。一个潜在的框架涉及使用 LLM 作为评估者。这种 LLM-as-a-Judge 方法根据预定义的"有用性"标准评估另一个 AI Agent 的输出。利用 LLM 的高级语言能力，此方法提供细微的、类人的主观品质评估，超越了简单的关键词匹配或基于规则的评估。虽然仍在发展中，但这项技术显示出自动化和扩展定性评估的前景。

```python
import google.generativeai as genai
import os
import json
import logging
from typing import Optional

# --- 配置 ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 将您的 API 密钥设置为环境变量以运行此脚本
# 例如，在您的终端中：export GOOGLE_API_KEY='your_key_here'
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except KeyError:
    logging.error("错误：GOOGLE_API_KEY 环境变量未设置。")
    exit(1)

# --- 法律调查质量的 LLM-as-a-Judge 评分标准 ---
LEGAL_SURVEY_RUBRIC = """
您是一位专家法律调查方法学家和严格的法律审查员。您的任务是评估给定法律调查问题的质量。为整体质量提供 1 到 5 的分数，以及详细的理由和具体反馈。重点关注以下标准：
1.  **清晰性和精确性（分数 1-5）：**
    * 1：极度模糊、高度歧义或令人困惑。
    * 3：中等清晰，但可以更精确。
    * 5：完全清晰、无歧义，在法律术语（如适用）和意图上精确。
2.  **中立性和偏见（分数 1-5）：**
    * 1：高度引导性或有偏见，明确影响受访者偏向特定答案。
    * 3：略微暗示性或可能被解释为引导性。
    * 5：完全中立、客观，没有任何引导性语言或带有倾向性的术语。
3.  **相关性和焦点（分数 1-5）：**
    * 1：与声明的调查主题无关或超出范围。
    * 3：松散相关，但可以更集中。
    * 5：与调查目标直接相关，并且集中于单一概念。
4.  **完整性（分数 1-5）：**
    * 1：遗漏了准确回答所需的关键信息或提供的上下文不足。
    * 3：基本完整，但缺少次要细节。
    * 5：提供受访者彻底回答所需的所有必要上下文和信息。
5.  **受众适当性（分数 1-5）：**
    * 1：使用目标受众无法理解的术语或对专家来说过于简单。
    * 3：通常适当，但某些术语可能具有挑战性或过于简化。
    * 5：完全适合目标调查受众的假定法律知识和背景。

**输出格式：** 您的响应必须是具有以下键的 JSON 对象：
* `overall_score`：一个从 1 到 5 的整数（标准分数的平均值或您的整体判断）。
* `rationale`：给出此分数原因的简明摘要，突出主要优势和劣势。
* `detailed_feedback`：详细说明每个标准（清晰性、中立性、相关性、完整性、受众适当性）反馈的要点列表。建议具体改进。
* `concerns`：任何具体的法律、道德或方法学问题的列表。
* `recommended_action`：简短的建议（例如"修改以保持中立"，"按原样批准"，"明确范围"）。
"""

class LLMJudgeForLegalSurvey:
    """使用生成式 AI 模型评估法律调查问题的类。"""
    def __init__(self, model_name: str = 'gemini-1.5-flash-latest', temperature: float = 0.2):
        """
        初始化 LLM Judge。

        Args:
            model_name (str)：要使用的 Gemini 模型名称。
                               推荐使用 'gemini-1.5-flash-latest' 以获得速度和成本效益。
                               'gemini-1.5-pro-latest' 提供最高质量。
            temperature (float)：生成温度。较低的温度更适合确定性评估。
        """
        self.model = genai.GenerativeModel(model_name)
        self.temperature = temperature

    def _generate_prompt(self, survey_question: str) -> str:
        """为 LLM judge 构建完整提示词。"""
        return f"{LEGAL_SURVEY_RUBRIC}\n\n---\n**要评估的法律调查问题：**\n{survey_question}\n---"

    def judge_survey_question(self, survey_question: str) -> Optional[dict]:
        """
        使用 LLM 判断单个法律调查问题的质量。

        Args:
            survey_question (str)：要评估的法律调查问题。
        Returns:
            Optional[dict]：包含 LLM 判断的字典，如果发生错误则返回 None。
        """
        full_prompt = self._generate_prompt(survey_question)

        try:
            logging.info(f"向 '{self.model.model_name}' 发送判断请求...")
            response = self.model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=self.temperature,
                    response_mime_type="application/json"
                )
            )
            # 检查内容审核或其他导致响应为空的原因。
            if not response.parts:
                safety_ratings = response.prompt_feedback.safety_ratings
                logging.error(f"LLM 响应为空或被阻止。安全评级：{safety_ratings}")
                return None

            return json.loads(response.text)
        except json.JSONDecodeError:
            logging.error(f"无法将 LLM 响应解码为 JSON。原始响应：{response.text}")
            return None
        except Exception as e:
            logging.error(f"LLM 判断期间发生意外错误：{e}")
            return None

# --- 示例使用 ---
if __name__ == "__main__":
    judge = LLMJudgeForLegalSurvey()

    # --- 好的示例 ---
    good_legal_survey_question = """
    在多大程度上您同意或不同意瑞士当前的知识产权法充分保护新兴的 AI 生成内容，假设该内容满足联邦最高法院确立的原创性标准？
    （选择一项：强烈不同意、不同意、中立、同意、强烈同意）
    """
    print("\n--- 评估好的法律调查问题 ---")
    judgment_good = judge.judge_survey_question(good_legal_survey_question)
    if judgment_good:
        print(json.dumps(judgment_good, indent=2))

    # --- 有偏见/差的示例 ---
    biased_legal_survey_question = """
    难道您不同意像 FADP 这样过度限制性的数据隐私法正在阻碍瑞士的基本技术创新和经济增长吗？
    （选择一项：是、否）
    """
    print("\n--- 评估有偏见的法律调查问题 ---")
    judgment_biased = judge.judge_survey_question(biased_legal_survey_question)
    if judgment_biased:
        print(json.dumps(judgment_biased, indent=2))

    # --- 模糊/含糊的示例 ---
    vague_legal_survey_question = """
    您对法律科技有什么想法？
    """
    print("\n--- 评估含糊的法律调查问题 ---")
    judgment_vague = judge.judge_survey_question(vague_legal_survey_question)
    if judgment_vague:
        print(json.dumps(judgment_vague, indent=2))
```

Python 代码定义了一个名为 LLMJudgeForLegalSurvey 的类，旨在使用生成式 AI 模型评估法律调查问题的质量。它利用 google.generativeai 库与 Gemini 模型交互。

核心功能涉及将调查问题与详细的评估标准一起发送给模型。评分标准指定了判断调查问题的五个标准：清晰性和精确性、中立性和偏见、相关性和焦点、完整性以及受众适当性。对于每个标准，分配 1 到 5 的分数，并要求在输出中提供详细的理由和反馈。代码构建一个提示词，其中包括标准和要评估的调查问题。

judge_survey_question 方法将此提示词发送到配置的 Gemini 模型，请求根据定义的结构格式化的 JSON 响应。期望的输出 JSON 包括整体分数、摘要理由、每个标准的详细反馈、问题列表和推荐的操作。该类处理 AI 模型交互期间的潜在错误，例如 JSON 解码问题或空响应。脚本通过评估法律调查问题的示例来演示其操作，说明 AI 如何根据预定义的标准评估质量。

在结束之前，让我们检查各种评估方法，考虑它们的优势和劣势。

| 评估方法 | 优势 | 劣势 |
| :---- | :---- | :---- |
| 人工评估 | 捕获细微行为 | 难以扩展、昂贵且耗时，因为它考虑主观的人为因素。 |
| LLM-as-a-Judge | 一致、高效且可扩展。 | 可能忽略中间步骤。受 LLM 能力限制。 |
| 自动化指标 | 可扩展、高效且客观 | 在捕获完整能力方面可能存在限制。 |

# Agent 轨迹

评估 Agent 的轨迹至关重要，因为传统的软件测试是不够的。标准代码产生可预测的通过/失败结果，而 Agent 以概率方式运行，需要对最终输出和 Agent 的轨迹——达到解决方案所采取的步骤序列——进行定性评估。评估多 Agent 系统具有挑战性，因为它们不断变化。这需要开发超越个体性能的复杂指标来衡量沟通和团队合作的有效性。此外，环境本身不是静态的，要求评估方法（包括测试用例）随时间适应。

这涉及检查决策的质量、推理过程和整体结果。实施自动化评估很有价值，特别是对于超越原型阶段的开发。分析轨迹和工具使用包括评估 Agent 用于实现目标的步骤，例如工具选择、策略和任务效率。例如，处理客户产品查询的 Agent 可能理想地遵循涉及意图确定、数据库搜索工具使用、结果审查和报告生成的轨迹。将 Agent 的实际操作与这个预期的或真实的轨迹进行比较，以识别错误和低效率。比较方法包括精确匹配（要求与理想序列完美匹配）、按序匹配（正确的操作按顺序，允许额外步骤）、任意顺序匹配（正确的操作以任何顺序，允许额外步骤）、精确度（测量预测操作的相关性）、召回率（测量捕获了多少基本操作）和单工具使用（检查特定操作）。指标选择取决于特定的 Agent 要求，高风险场景可能要求精确匹配，而更灵活的情况可能使用按序或任意顺序匹配。

AI Agent 的评估涉及两种主要方法：使用测试文件和使用评估集文件。测试文件以 JSON 格式表示单个、简单的 Agent-模型交互或会话，非常适合在活跃开发期间进行单元测试，侧重于快速执行和简单的会话复杂性。每个测试文件包含一个带有多个回合的单个会话，其中回合是一个用户-Agent 交互，包括用户的查询、预期的工具使用轨迹、中间 Agent 响应和最终响应。例如，测试文件可能详细说明用户请求"关闭卧室中的 device_2"，指定 Agent 使用带有参数（如 location: Bedroom、device_id: device_2 和 status: OFF）的 set_device_info 工具，以及预期的最终响应"我已将 device_2 状态设置为关闭"。测试文件可以组织到文件夹中，并可能包含 test_config.json 文件来定义评估标准。评估集文件利用称为"evalset"的数据集来评估交互，包含多个可能很长的会话，适合模拟复杂的多回合对话和集成测试。评估集文件包含多个"评估"，每个评估代表一个具有一个或多个"回合"的不同会话，其中包括用户查询、预期的工具使用、中间响应和参考最终响应。示例评估集可能包括一个会话，其中用户首先询问"你能做什么？"然后说"掷两次 10 面骰子，然后检查 9 是否是质数"，定义预期的 roll_die 工具调用和 check_prime 工具调用，以及总结骰子结果和质数检查的最终响应。

**多 Agent：** 评估具有多个 Agent 的复杂 AI 系统非常像评估团队项目。因为有许多步骤和交接，其复杂性是一个优势，允许您检查每个阶段的工作质量。您可以检查每个单独的"Agent"如何执行其特定工作，但您还必须评估整个系统作为一个整体的表现如何。

为此，您需要提出关于团队动态的关键问题，并以具体示例作为支持：

* Agent 是否有效合作？例如，在"航班预订 Agent"确保航班后，它是否成功地将正确的日期和目的地传递给"酒店预订 Agent"？合作失败可能导致酒店预订在错误的周。
* 他们是否制定了好的计划并坚持执行？想象计划是首先预订航班，然后预订酒店。如果"酒店 Agent"在航班确认之前尝试预订房间，它已经偏离了计划。您还要检查 Agent 是否卡住，例如，无休止地搜索"完美"租车，从不进入下一步。
* 是否为正确的任务选择了正确的 Agent？如果用户询问他们旅行的天气，系统应该使用提供实时数据的专门"天气 Agent"。如果它使用提供通用答案（如"夏天通常很温暖"）的"通用知识 Agent"，它为这项工作选择了错误的工具。
* 最后，添加更多 Agent 是否提高了性能？如果您向团队添加一个新的"餐厅预订 Agent"，它是否使整体旅行规划更好、更高效？还是它会造成冲突并减慢系统速度，表明可扩展性存在问题？

# 从 Agent 到高级承包商

最近，有人提出（Agent Companion，gulli 等人）从简单的 AI Agent 演变为高级"承包商"，从概率性的、通常不可靠的系统转向为复杂的、高风险环境设计的更确定性和可问责的系统（见图 2）。

当今常见的 AI Agent 基于简短的、规格不明确的指令运行，这使得它们适合简单的演示，但在生产中很脆弱，因为歧义会导致失败。"承包商"模型通过建立用户和 AI 之间严格的、正式化的关系来解决这个问题，该关系建立在明确定义和相互同意的条款基础上，就像人类世界中的法律服务协议一样。这种转变得到四个关键支柱的支持，这些支柱共同确保了以前超出自主系统范围的任务的清晰性、可靠性和稳健执行。

首先是正式化合约的支柱，这是一个详细的规范，作为任务的唯一真实来源。它远远超出了简单的提示词。例如，财务分析任务的合约不会只说"分析上个季度的销售"；它会要求"一份 20 页的 PDF 报告，分析 2025 年第一季度的欧洲市场销售，包括五个特定的数据可视化、与 2024 年第一季度的比较分析以及基于提供的供应链中断数据集的风险评估"。此合约明确定义了所需的可交付成果、其精确规格、可接受的数据源、工作范围，甚至预期的计算成本和完成时间，使结果客观可验证。

第二是动态的协商和反馈生命周期支柱。合约不是静态命令，而是对话的开始。承包商 Agent 可以分析初始条款并进行协商。例如，如果合约要求使用 Agent 无法访问的特定专有数据源，它可以返回反馈，说明"指定的 XYZ 数据库不可访问。请提供凭据或批准使用替代公共数据库，这可能会略微改变数据的粒度。"这个协商阶段也允许 Agent 标记歧义或潜在风险，在执行开始之前解决误解，防止代价高昂的失败，并确保最终输出与用户的实际意图完全一致。

![][image2]

图 2：Agent 之间的合约执行示例

第三个支柱是以质量为中心的迭代执行。与为低延迟响应设计的 Agent 不同，承包商优先考虑正确性和质量。它基于自我验证和纠正的原则运作。例如，对于代码生成合约，Agent 不会只是编写代码；它会生成多个算法方法，根据合约中定义的一套单元测试编译和运行它们，对性能、安全性和可读性等指标对每个解决方案进行评分，并且只提交通过所有验证标准的版本。这种生成、审查和改进自己的工作的内部循环，直到满足合约的规格，对于建立对其输出的信任至关重要。

最后，第四个支柱是通过子合约的层次化分解。对于复杂度很高的任务，主承包商 Agent 可以充当项目经理，将主要目标分解为更小的、更易管理的子任务。它通过生成新的、正式的"子合约"来实现这一点。例如，"构建电子商务移动应用程序"的主合约可以由主 Agent 分解为"设计 UI/UX"、"开发用户身份验证模块"、"创建产品数据库架构"和"集成支付网关"的子合约。这些子合约中的每一个都是一个完整的、独立的合约，具有自己的可交付成果和规格，可以分配给其他专门的 Agent。这种结构化的分解使系统能够以高度组织和可扩展的方式处理巨大的、多方面的项目，标志着 AI 从简单工具向真正自主和可靠的问题解决引擎的转变。

最终，这个承包商框架通过将正式规范、协商和可验证执行的原则直接嵌入到 Agent 的核心逻辑中，重新构想了 AI 交互。这种方法化的方法将人工智能从一个有前途但经常不可预测的助手提升为能够以可审计的精度自主管理复杂项目的可靠系统。通过解决歧义和可靠性的关键挑战，该模型为在信任和问责至关重要的关键任务领域部署 AI 铺平了道路。

# Google 的 ADK

在结束之前，让我们看一个支持评估的框架的具体示例。使用 Google 的 ADK 进行 Agent 评估（见图 3）可以通过三种方法进行：基于 Web 的 UI（adk web）用于交互式评估和数据集生成、使用 pytest 的编程集成用于整合到测试管道中，以及直接命令行界面（adk eval）用于适合定期构建生成和验证过程的自动化评估。

![][image3]

图 3：Google ADK 的评估支持

基于 Web 的 UI 支持交互式会话创建并保存到现有或新的评估集中，显示评估状态。Pytest 集成允许通过调用 AgentEvaluator.evaluate 并指定 Agent 模块和测试文件路径，将测试文件作为集成测试的一部分运行。

命令行界面通过提供 Agent 模块路径和评估集文件来促进自动化评估，并具有指定配置文件或打印详细结果的选项。可以通过在评估集文件名后列出（用逗号分隔）来选择较大评估集中的特定评估以供执行。

# 一览

**内容：** Agentic 系统和 LLM 在复杂的动态环境中运行，它们的性能可能会随时间退化。它们的概率性和非确定性本质意味着传统的软件测试不足以确保可靠性。评估动态多 Agent 系统是一项重大挑战，因为它们不断变化的性质以及其环境的性质要求开发适应性测试方法和能够测量超越个体性能的协作成功的复杂指标。部署后可能出现数据漂移、意外交互、工具调用和偏离预期目标等问题。因此，持续评估对于测量 Agent 的有效性、效率以及对操作和安全要求的遵守是必要的。

**原因：** 标准化的评估和监控框架提供了一种系统的方式来评估和确保智能 Agent 的持续性能。这涉及为准确性、延迟和资源消耗（如 LLM 的 token 使用量）定义明确的指标。它还包括高级技术，例如分析 Agent 轨迹以理解推理过程，以及采用 LLM-as-a-Judge 进行细微的、定性的评估。通过建立反馈循环和报告系统，该框架允许持续改进、A/B 测试以及检测异常或性能漂移，确保 Agent 与其目标保持一致。

**经验法则：** 在部署 Agent 到实时性能和可靠性至关重要的生产环境时使用此模式。此外，当需要系统地比较 Agent 或其底层模型的不同版本以推动改进时，以及在需要合规性、安全性和道德审计的受监管或高风险领域运营时使用它。当 Agent 的性能可能由于数据或环境变化（漂移）而随时间退化时，或者在评估复杂的 Agent 行为时（包括操作序列（轨迹）和主观输出（如有用性）的质量），此模式也适用。

**视觉摘要**

![][image4]
图 4：评估和监控设计模式

# 关键要点

* 评估智能 Agent 超越了传统测试，在真实世界环境中持续测量其有效性、效率以及对要求的遵守。
* Agent 评估的实际应用包括实时系统中的性能跟踪、改进的 A/B 测试、合规审计以及检测行为中的漂移或异常。
* 基本 Agent 评估涉及评估响应准确性，而真实世界场景需要更复杂的指标，如延迟监控和 LLM 驱动 Agent 的 token 使用跟踪。
* Agent 轨迹（Agent 采取的步骤序列）对于评估至关重要，将实际操作与理想的、真实的路径进行比较，以识别错误和低效率。
* ADK 通过用于单元测试的单个测试文件和用于集成测试的综合评估集文件提供结构化的评估方法，两者都定义了预期的 Agent 行为。
* Agent 评估可以通过基于 Web 的 UI 进行交互式测试、使用 pytest 进行 CI/CD 集成的编程方式，或通过命令行界面进行自动化工作流执行。
* 为了使 AI 在复杂的、高风险的任务中可靠，我们必须从简单的提示词转向精确定义可验证可交付成果和范围的正式"合约"。这种结构化协议允许 Agent 协商、澄清歧义并迭代验证其自己的工作，将其从不可预测的工具转变为可问责和值得信赖的系统。

# 结论

总之，有效评估 AI Agent 需要超越简单的准确性检查，对其在动态环境中的性能进行持续的、多方面的评估。这涉及实际监控延迟和资源消耗等指标，以及通过其轨迹对 Agent 决策过程进行复杂分析。对于有用性等细微品质，诸如 LLM-as-a-Judge 之类的创新方法变得必不可少，而像 Google 的 ADK 这样的框架为单元和集成测试提供了结构化的工具。对于多 Agent 系统，挑战加剧，重点转向评估协作成功和有效合作。

为了确保关键应用中的可靠性，范式正在从简单的、提示词驱动的 Agent 转向受正式协议约束的高级"承包商"。这些承包商 Agent 在明确的、可验证的条款上运作，允许它们协商、分解任务并自我验证其工作以满足严格的质量标准。这种结构化方法将 Agent 从不可预测的工具转变为能够处理复杂的、高风险任务的可问责系统。最终，这种演变对于建立在关键任务领域部署复杂的 Agentic AI 所需的信任至关重要。

# 参考文献

相关研究包括：

1. ADK Web：[https://github.com/google/adk-web](https://github.com/google/adk-web)
2. ADK Evaluate：[https://google.github.io/adk-docs/evaluate/](https://google.github.io/adk-docs/evaluate/)
3. Survey on Evaluation of LLM-based Agents：[https://arxiv.org/abs/2503.16416](https://arxiv.org/abs/2503.16416)
4. Agent-as-a-Judge: Evaluate Agents with Agents：[https://arxiv.org/abs/2410.10934](https://arxiv.org/abs/2410.10934)
5. Agent Companion, gulli et al：[https://www.kaggle.com/whitepaper-agent-companion](https://www.kaggle.com/whitepaper-agent-companion)

[image1]: ../images/chapter-19/image1.png

[image2]: ../images/chapter-19/image2.png

[image3]: ../images/chapter-19/image3.png

[image4]: ../images/chapter-19/image4.png