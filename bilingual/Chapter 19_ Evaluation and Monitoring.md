# Chapter 19: Evaluation and Monitoring

# 第 19 章：评估和监控

This chapter examines methodologies that allow intelligent agents to systematically assess their performance, monitor progress toward goals, and detect operational anomalies. While Chapter 11 outlines goal setting and monitoring, and Chapter 17 addresses Reasoning mechanisms, this chapter focuses on the continuous, often external, measurement of an agent's effectiveness, efficiency, and compliance with requirements. This includes defining metrics, establishing feedback loops, and implementing reporting systems to ensure agent performance aligns with expectations in operational environments (see Fig.1)

本章探讨使智能体能够系统地评估其性能、监控目标进展以及检测操作异常的方法论。虽然第 11 章概述了目标设定和监控，第 17 章讨论了推理机制，但本章侧重于对智能体效率、效能和合规性要求进行持续的（通常是外部的）测量。这包括定义指标、建立反馈循环以及实施报告系统，以确保智能体的性能在操作环境中与期望保持一致（见图 1）。

![][image1]

Fig:1. Best practices for evaluation and monitoring

图 1：评估和监控的最佳实践

## Practical Applications & Use Cases

## 实际应用与用例

Most Common Applications and Use Cases:

最常见的应用和用例：

* **Performance Tracking in Live Systems:** Continuously monitoring the accuracy, latency, and resource consumption of an agent deployed in a production environment (e.g., a customer service chatbot's resolution rate, response time).  

* **实时系统中的性能跟踪：** 持续监控部署在生产环境中的智能体的准确性、延迟和资源消耗（例如，客户服务聊天机器人的问题解决率、响应时间）。

* **A/B Testing for Agent Improvements:** Systematically comparing the performance of different agent versions or strategies in parallel to identify optimal approaches (e.g., trying two different planning algorithms for a logistics agent).  

* **智能体改进的 A/B 测试：** 系统地并行比较不同智能体版本或策略的性能，以确定最优方法（例如，为物流智能体尝试两种不同的规划算法）。

* **Compliance and Safety Audits:** Generate automated audit reports that track an agent's compliance with ethical guidelines, regulatory requirements, and safety protocols over time. These reports can be verified by a human-in-the-loop or another agent, and can generate KPIs or trigger alerts upon identifying issues.  

* **合规性和安全审计：** 生成自动化审计报告，跟踪智能体随时间遵守道德准则、监管要求和安全协议的情况。这些报告可以由人机协同或另一个智能体验证，可以生成关键绩效指标（KPI）或在发现问题时触发警报。

* **Enterprise systems:** To govern Agentic AI in corporate systems, a new control instrument, the AI "Contract," is needed. This dynamic agreement codifies the objectives, rules, and controls for AI-delegated tasks.  

* **企业系统：** 为了治理企业系统中的 Agentic AI，需要一种新的控制工具，即 AI"合约"。这种动态协议为 AI 委派的任务编纂目标、规则和控制机制。

* **Drift Detection:** Monitoring the relevance or accuracy of an agent's outputs over time, detecting when its performance degrades due to changes in input data distribution (concept drift) or environmental shifts.  

* **漂移检测：** 随时间监控智能体输出的相关性或准确性，检测其性能何时因输入数据分布变化（概念漂移）或环境变化而退化。

* **Anomaly Detection in Agent Behavior:** Identifying unusual or unexpected actions taken by an agent that might indicate an error, a malicious attack, or an emergent un-desired behavior.  

* **智能体行为中的异常检测：** 识别智能体的异常或意外操作，这些操作可能表明错误、恶意攻击或涌现的不良行为。

* **Learning Progress Assessment:** For agents designed to learn, tracking their learning curve, improvement in specific skills, or generalization capabilities over different tasks or data sets.

* **学习进度评估：** 对于设计为学习的智能体，跟踪它们的学习曲线、特定技能的改进或在不同任务或数据集上的泛化能力。

## Hands-On Code Example

## 实践代码示例

Developing a comprehensive evaluation framework for AI agents is a challenging endeavor, comparable to an academic discipline or a substantial publication in its complexity. This difficulty stems from the multitude of factors to consider, such as model performance, user interaction, ethical implications, and broader societal impact. Nevertheless, for practical implementation, the focus can be narrowed to critical use cases essential for the efficient and effective functioning of AI agents.

为 AI 智能体开发一个全面的评估框架是一项具有挑战性的工作，其复杂性堪比一门学术学科或一部重要著作。这种困难源于需要考虑的众多因素，如模型性能、用户交互、道德影响和更广泛的社会影响。然而，对于实际实施，可以将重点缩小到对 AI 智能体高效运行至关重要的关键用例。

**Agent Response Assessment:** This core process is essential for evaluating the quality and accuracy of an agent's outputs. It involves determining if the agent delivers pertinent, correct,  logical, unbiased, and accurate information in response to given inputs. Assessment metrics may include factual correctness, fluency, grammatical precision, and adherence to the user's intended purpose.

**智能体响应评估：** 这个核心过程对于评估智能体输出的质量和准确性至关重要。它涉及确定智能体是否针对给定输入提供了相关、正确、合乎逻辑、无偏见和准确的信息。评估指标可能包括事实正确性、流畅性、语法精确性和对用户预期目的的遵守。

```python
def evaluate_response_accuracy(agent_output: str, expected_output: str) -> float:
    """Calculates a simple accuracy score for agent responses."""
    # This is a very basic exact match; real-world would use more sophisticated metrics
    return 1.0 if agent_output.strip().lower() == expected_output.strip().lower() else 0.0

## Example usage
agent_response = "The capital of France is Paris."
ground_truth = "Paris is the capital of France."
score = evaluate_response_accuracy(agent_response, ground_truth)
print(f"Response accuracy: {score}")
```

The Python function `evaluate_response_accuracy` calculates a basic accuracy score for an AI agent's response by performing an exact, case-insensitive comparison between the agent's output and the expected output, after removing leading or trailing whitespace. It returns a score of 1.0 for an exact match and 0.0 otherwise, representing a binary correct or incorrect evaluation. This method, while straightforward for simple checks, does not account for variations like paraphrasing or semantic equivalence.

Python 函数 `evaluate_response_accuracy` 通过对智能体输出和期望输出进行精确的、不区分大小写的比较（在去除前导和尾随空格后），计算 AI 智能体响应的基本准确度分数。对于精确匹配，它返回 1.0 分，否则返回 0.0，表示二元的正确或不正确评估。这种方法虽然适合简单检查，但不考虑释义或语义等价性等变化。

The problem lies in its method of comparison. The function performs a strict, character-for-character comparison of the two strings. In the example provided:

问题在于其比较方法。该函数执行两个字符串的严格逐字符比较。在提供的示例中：

* agent_response: "The capital of France is Paris."  
* ground_truth: "Paris is the capital of France."

* agent_response："The capital of France is Paris."
* ground_truth："Paris is the capital of France."

Even after removing whitespace and converting to lowercase, these two strings are not identical. As a result, the function will incorrectly return an accuracy score of `0.0`, even though both sentences convey the same meaning.

即使在去除空格并转换为小写后，这两个字符串也不完全相同。因此，该函数将错误地返回准确度分数 `0.0`，尽管两个句子传达了相同的含义。

A straightforward comparison falls short in assessing semantic similarity, only succeeding if an agent's response exactly matches the expected output. A more effective evaluation necessitates advanced Natural Language Processing (NLP) techniques to discern the meaning between sentences. For thorough AI agent evaluation in real-world scenarios, more sophisticated metrics are often indispensable. These metrics can encompass String Similarity Measures like Levenshtein distance and Jaccard similarity, Keyword Analysis for the presence or absence of specific keywords, Semantic Similarity using cosine similarity with embedding models, LLM-as-a-Judge Evaluations (discussed later for assessing nuanced correctness and helpfulness), and RAG-specific Metrics such as faithfulness and relevance.

简单的比较在评估语义相似性方面存在不足，只有当智能体响应与期望输出完全匹配时才能成功。更有效的评估需要高级自然语言处理（NLP）技术来辨别句子之间的含义差异。对于真实世界场景中的全面 AI 智能体评估，更复杂的指标通常是必不可少的。这些指标可以包括字符串相似性度量（如 Levenshtein 距离和 Jaccard 相似性）、关键词分析（特定关键词的存在或缺失）、使用嵌入模型的语义相似性（余弦相似性）、LLM-as-a-Judge 评估（稍后讨论，用于评估细微的正确性和有用性）以及 RAG 特定指标（如忠实性和相关性）。

**Latency Monitoring:** Latency Monitoring for Agent Actions is crucial in applications where the speed of an AI agent's response or action is a critical factor. This process measures the duration required for an agent to process requests and generate outputs. Elevated latency can adversely affect user experience and the agent's overall effectiveness, particularly in real-time or interactive environments. In practical applications, simply printing latency data to the console is insufficient. Logging this information to a persistent storage system is recommended. Options include structured log files (e.g., JSON), time-series databases (e.g., InfluxDB, Prometheus), data warehouses (e.g., Snowflake, BigQuery, PostgreSQL), or observability platforms (e.g., Datadog, Splunk, Grafana Cloud).

**延迟监控：** 对智能体操作的延迟监控在 AI 智能体响应或操作速度是关键因素的应用中至关重要。此过程测量智能体处理请求并生成输出所需的时间。较高的延迟会对用户体验和智能体的整体效能产生不利影响，特别是在实时或交互式环境中。在实际应用中，仅将延迟数据打印到控制台是不够的。建议将此信息记录到持久存储系统，可选方案包括结构化日志文件（例如 JSON）、时间序列数据库（例如 InfluxDB、Prometheus）、数据仓库（例如 Snowflake、BigQuery、PostgreSQL）或可观测性平台（例如 Datadog、Splunk、Grafana Cloud）。

**Tracking Token Usage for LLM Interactions:** For LLM-powered agents, tracking token usage is crucial for managing costs and optimizing resource allocation. Billing for LLM interactions often depends on the number of tokens processed (input and output). Therefore, efficient token usage directly reduces operational expenses. Additionally, monitoring token counts helps identify potential areas for improvement in prompt engineering or response generation processes.

**跟踪 LLM 交互的 Token 使用量：** 对于 LLM 驱动的智能体，跟踪 token 使用量对于管理成本和优化资源分配至关重要。LLM 交互的计费通常取决于处理的 token 数量（输入和输出）。因此，高效的 token 使用直接降低运营费用。此外，监控 token 计数有助于识别提示词工程或响应生成过程中的潜在改进领域。

```python
## This is conceptual as actual token counting depends on the LLM API
class LLMInteractionMonitor:
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0

    def record_interaction(self, prompt: str, response: str):
        # In a real scenario, use LLM API's token counter or a tokenizer
        input_tokens = len(prompt.split())  # Placeholder
        output_tokens = len(response.split())  # Placeholder
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        print(f"Recorded interaction: Input tokens={input_tokens}, Output tokens={output_tokens}")

    def get_total_tokens(self):
        return self.total_input_tokens, self.total_output_tokens

## Example usage
monitor = LLMInteractionMonitor()
monitor.record_interaction("What is the capital of France?", "The capital of France is Paris.")
monitor.record_interaction("Tell me a joke.", "Why don't scientists trust atoms? Because they make up everything!")
input_t, output_t = monitor.get_total_tokens()
print(f"Total input tokens: {input_t}, Total output tokens: {output_t}")
```

This section introduces a conceptual Python class, `LLMInteractionMonitor`, developed to track token usage in large language model interactions. The class incorporates counters for both input and output tokens. Its `record_interaction` method simulates token counting by splitting the prompt and response strings. In a practical implementation, specific LLM API tokenizers would be employed for precise token counts. As interactions occur, the monitor accumulates the total input and output token counts. The `get_total_tokens` method provides access to these cumulative totals, essential for cost management and optimization of LLM usage.

本节介绍了一个概念性的 Python 类 `LLMInteractionMonitor`，旨在跟踪大语言模型交互中的 token 使用量。该类包含输入和输出 token 的计数器。其 `record_interaction` 方法通过分割提示词和响应字符串来模拟 token 计数。在实际实现中，将使用特定的 LLM API tokenizer 进行精确的 token 计数。随着交互的发生，监视器累积总的输入和输出 token 计数。`get_total_tokens` 方法提供对这些累积总数的访问，这对于成本管理和 LLM 使用优化至关重要。

**Custom Metric for "Helpfulness" using LLM-as-a-Judge:** Evaluating subjective qualities like an AI agent's "helpfulness" presents challenges beyond standard objective metrics. A potential framework involves using an LLM as an evaluator. This LLM-as-a-Judge approach assesses another AI agent's output based on predefined criteria for "helpfulness." Leveraging the advanced linguistic capabilities of LLMs, this method offers nuanced, human-like evaluations of subjective qualities, surpassing simple keyword matching or rule-based assessments. Though in development, this technique shows promise for automating and scaling qualitative evaluations.

**使用 LLM-as-a-Judge 的"有用性"自定义指标：** 评估 AI 智能体"有用性"等主观品质带来了超越标准客观指标的挑战。一个潜在的框架涉及使用 LLM 作为评估者。这种 LLM-as-a-Judge 方法根据预定义的"有用性"标准评估另一个 AI 智能体的输出。利用 LLM 的高级语言能力，此方法提供细微的、类人的主观品质评估，超越了简单的关键词匹配或基于规则的评估。虽然仍在发展中，但这项技术显示出自动化和扩展定性评估的前景。

```python
import google.generativeai as genai
import os
import json
import logging
from typing import Optional

## --- Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

## Set your API key as an environment variable to run this script
## For example, in your terminal: export GOOGLE_API_KEY='your_key_here'
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except KeyError:
    logging.error("Error: GOOGLE_API_KEY environment variable not set.")
    exit(1)

## --- LLM-as-a-Judge Rubric for Legal Survey Quality ---
LEGAL_SURVEY_RUBRIC = """
You are an expert legal survey methodologist and a critical legal reviewer.
Your task is to evaluate the quality of a given legal survey question.
Provide a score from 1 to 5 for overall quality, along with a detailed rationale and specific feedback.
Focus on the following criteria:

1.  **Clarity & Precision (Score 1-5):**
    * 1: Extremely vague, highly ambiguous, or confusing.
    * 3: Moderately clear, but could be more precise.
    * 5: Perfectly clear, unambiguous, and precise in its legal terminology (if applicable) and intent.
2.  **Neutrality & Bias (Score 1-5):**
    * 1: Highly leading or biased, clearly influencing the respondent towards a specific answer.
    * 3: Slightly suggestive or could be interpreted as leading.
    * 5: Completely neutral, objective, and free from any leading language or loaded terms.
3.  **Relevance & Focus (Score 1-5):**
    * 1: Irrelevant to the stated survey topic or out of scope.
    * 3: Loosely related but could be more focused.
    * 5: Directly relevant to the survey's objectives and well-focused on a single concept.
4.  **Completeness (Score 1-5):**
    * 1: Omits critical information needed to answer accurately or provides insufficient context.
    * 3: Mostly complete, but minor details are missing.
    * 5: Provides all necessary context and information for the respondent to answer thoroughly.
5.  **Appropriateness for Audience (Score 1-5):**
    * 1: Uses jargon inaccessible to the target audience or is overly simplistic for experts.
    * 3: Generally appropriate, but some terms might be challenging or oversimplified.
    * 5: Perfectly tailored to the assumed legal knowledge and background of the target survey audience.

**Output Format:**
Your response MUST be a JSON object with the following keys:
* `overall_score`: An integer from 1 to 5 (average of criterion scores, or your holistic judgment).
* `rationale`: A concise summary of why this score was given, highlighting major strengths and weaknesses.
* `detailed_feedback`: A bullet-point list detailing feedback for each criterion (Clarity, Neutrality, Relevance, Completeness, Audience Appropriateness). Suggest specific improvements.
* `concerns`: A list of any specific legal, ethical, or methodological concerns.
* `recommended_action`: A brief recommendation (e.g., "Revise for neutrality", "Approve as is", "Clarify scope").
"""

class LLMJudgeForLegalSurvey:
    """A class to evaluate legal survey questions using a generative AI model."""
    def __init__(self, model_name: str = 'gemini-1.5-flash-latest', temperature: float = 0.2):
        """
        Initializes the LLM Judge.

        Args:
            model_name (str): The name of the Gemini model to use.
                              'gemini-1.5-flash-latest' is recommended for speed and cost.
                              'gemini-1.5-pro-latest' offers the highest quality.
            temperature (float): The generation temperature. Lower is better for deterministic evaluation.
        """
        self.model = genai.GenerativeModel(model_name)
        self.temperature = temperature

    def _generate_prompt(self, survey_question: str) -> str:
        """Constructs the full prompt for the LLM judge."""
        return f"{LEGAL_SURVEY_RUBRIC}\n\n---\n**LEGAL SURVEY QUESTION TO EVALUATE:**\n{survey_question}\n---"

    def judge_survey_question(self, survey_question: str) -> Optional[dict]:
        """
        Judges the quality of a single legal survey question using the LLM.
        Args:
            survey_question (str): The legal survey question to be evaluated.
        Returns:
            Optional[dict]: A dictionary containing the LLM's judgment, or None if an error occurs.
        """
        full_prompt = self._generate_prompt(survey_question)

        try:
            logging.info(f"Sending request to '{self.model.model_name}' for judgment...")
            response = self.model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=self.temperature,
                    response_mime_type="application/json"
                )
            )
            # Check for content moderation or other reasons for an empty response.
            if not response.parts:
                safety_ratings = response.prompt_feedback.safety_ratings
                logging.error(f"LLM response was empty or blocked. Safety Ratings: {safety_ratings}")
                return None

            return json.loads(response.text)
        except json.JSONDecodeError:
            logging.error(f"Failed to decode LLM response as JSON. Raw response: {response.text}")
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred during LLM judgment: {e}")
            return None

## --- Example Usage ---
if __name__ == "__main__":
    judge = LLMJudgeForLegalSurvey()

    # --- Good Example ---
    good_legal_survey_question = """
    To what extent do you agree or disagree that current intellectual property laws in Switzerland adequately protect emerging AI-generated content, assuming the content meets the originality criteria established by the Federal Supreme Court?
    (Select one: Strongly Disagree, Disagree, Neutral, Agree, Strongly Agree)
    """
    print("\n--- Evaluating Good Legal Survey Question ---")
    judgment_good = judge.judge_survey_question(good_legal_survey_question)
    if judgment_good:
        print(json.dumps(judgment_good, indent=2))

    # --- Biased/Poor Example ---
    biased_legal_survey_question = """
    Don't you agree that overly restrictive data privacy laws like the FADP are hindering essential technological innovation and economic growth in Switzerland?
    (Select one: Yes, No)
    """
    print("\n--- Evaluating Biased Legal Survey Question ---")
    judgment_biased = judge.judge_survey_question(biased_legal_survey_question)
    if judgment_biased:
        print(json.dumps(judgment_biased, indent=2))

    # --- Ambiguous/Vague Example ---
    vague_legal_survey_question = """
    What are your thoughts on legal tech?
    """
    print("\n--- Evaluating Vague Legal Survey Question ---")
    judgment_vague = judge.judge_survey_question(vague_legal_survey_question)
    if judgment_vague:
        print(json.dumps(judgment_vague, indent=2))
```

The Python code defines a class LLMJudgeForLegalSurvey designed to evaluate the quality of legal survey questions using a generative AI model. It utilizes the google.generativeai library to interact with Gemini models. 

Python 代码定义了一个名为 LLMJudgeForLegalSurvey 的类，旨在使用生成式 AI 模型评估法律调查问题的质量。它利用 google.generativeai 库与 Gemini 模型交互。

The core functionality involves sending a survey question to the model along with a detailed rubric for evaluation. The rubric specifies five criteria for judging survey questions: Clarity & Precision, Neutrality & Bias, Relevance & Focus, Completeness, and Appropriateness for Audience. For each criterion, a score from 1 to 5 is assigned, and a detailed rationale and feedback are required in the output. The code constructs a prompt that includes the rubric and the survey question to be evaluated. 

核心功能涉及将调查问题与详细的评估标准一起发送给模型。评分标准指定了判断调查问题的五个标准：清晰性和精确性、中立性和偏见、相关性和焦点、完整性以及受众适当性。对于每个标准，分配 1 到 5 的分数，并要求在输出中提供详细的理由和反馈。代码构建一个提示词，其中包括标准和要评估的调查问题。

The judge_survey_question method sends this prompt to the configured Gemini model, requesting a JSON response formatted according to the defined structure. The expected output JSON includes an overall score, a summary rationale, detailed feedback for each criterion, a list of concerns, and a recommended action. The class handles potential errors during the AI model interaction, such as JSON decoding issues or empty responses. The script demonstrates its operation by evaluating examples of legal survey questions, illustrating how the AI assesses quality based on the predefined criteria.

judge_survey_question 方法将此提示词发送到配置的 Gemini 模型，请求根据定义的结构格式化的 JSON 响应。期望的输出 JSON 包括整体分数、摘要理由、每个标准的详细反馈、关注点列表和推荐的操作。该类处理 AI 模型交互期间的潜在错误，例如 JSON 解码问题或空响应。脚本通过评估法律调查问题的示例来演示其操作，说明 AI 如何根据预定义的标准评估质量。

Before we conclude, let's examine various evaluation methods, considering their strengths and weaknesses.

在结束之前，让我们检查各种评估方法，考虑它们的优势和劣势。

| Evaluation Method | Strengths | Weaknesses |
| :---- | :---- | :---- |
| Human Evaluation  | Captures subtle behavior | Difficult to scale, expensive, and time-consuming, as it considers subjective human factors. |
| LLM-as-a-Judge | Consistent, efficient, and scalable.  | Intermediate steps may be overlooked. Limited by LLM capabilities. |
| Automated Metrics  | Scalable, efficient, and objective | Potential limitation in capturing complete capabilities. |

| 评估方法 | 优势 | 劣势 |
| :---- | :---- | :---- |
| 人工评估 | 捕获细微行为 | 难以扩展、昂贵且耗时，因为它考虑主观的人为因素。 |
| LLM-as-a-Judge | 一致、高效且可扩展。 | 可能忽略中间步骤。受 LLM 能力限制。 |
| 自动化指标 | 可扩展、高效且客观 | 在捕获完整能力方面可能存在限制。 |

## Agent Trajectories

## 智能体轨迹

Evaluating agents' trajectories is essential, as traditional software tests are insufficient. Standard code yields predictable pass/fail results, whereas agents operate probabilistically, necessitating qualitative assessment of both the final output and the agent's trajectory—the sequence of steps taken to reach a solution. Evaluating multi-agent systems is challenging because they are constantly in flux. This requires developing sophisticated metrics that go beyond individual performance to measure the effectiveness of communication and teamwork. Moreover, the environments themselves are not static, demanding that evaluation methods, including test cases, adapt over time.

评估智能体的轨迹至关重要，因为传统的软件测试是不够的。标准代码产生可预测的通过/失败结果，而智能体以概率方式运行，需要对最终输出和智能体的轨迹——即达到解决方案所采取的步骤序列——进行定性评估。评估多智能体系统具有挑战性，因为它们不断变化。这需要开发超越个体性能的复杂指标来衡量沟通和团队合作的有效性。此外，环境本身不是静态的，要求评估方法（包括测试用例）随时间适应。

This involves examining the quality of decisions, the reasoning process, and the overall outcome. Implementing automated evaluations is valuable, particularly for development beyond the prototype stage. Analyzing trajectory and tool use includes evaluating the steps an agent employs to achieve a goal, such as tool selection, strategies, and task efficiency. For example, an agent addressing a customer's product query might ideally follow a trajectory involving intent determination, database search tool use, result review, and report generation. The agent's actual actions are compared to this expected, or ground truth, trajectory to identify errors and inefficiencies. Comparison methods include exact match (requiring a perfect match to the ideal sequence), in-order match (correct actions in order, allowing extra steps), any-order match (correct actions in any order, allowing extra steps), precision (measuring the relevance of predicted actions), recall (measuring how many essential actions are captured), and single-tool use (checking for a specific action). Metric selection depends on specific agent requirements, with high-stakes scenarios potentially demanding an exact match, while more flexible situations might use an in-order or any-order match.

这涉及检查决策的质量、推理过程和整体结果。实施自动化评估很有价值，特别是对于超越原型阶段的开发。分析轨迹和工具使用包括评估智能体实现目标的步骤，例如工具选择、策略和任务效率。例如，处理客户产品查询的智能体可能理想地遵循涉及意图确定、数据库搜索工具使用、结果审查和报告生成的轨迹。将智能体的实际操作与这个预期的或真实的轨迹进行比较，以识别错误和低效率。比较方法包括精确匹配（要求与理想序列完美匹配）、按序匹配（正确的操作按顺序，允许额外步骤）、任意顺序匹配（正确的操作以任何顺序，允许额外步骤）、精确度（测量预测操作的相关性）、召回率（测量捕获了多少基本操作）和单工具使用（检查特定操作）。指标选择取决于特定的智能体要求，高风险场景可能要求精确匹配，而更灵活的情况可能使用按序或任意顺序匹配。

Evaluation of AI agents involves two primary approaches: using test files and using evalset files. Test files, in JSON format, represent single, simple agent-model interactions or sessions and are ideal for unit testing during active development, focusing on rapid execution and simple session complexity. Each test file contains a single session with multiple turns, where a turn is a user-agent interaction including the user's query, expected tool use trajectory, intermediate agent responses, and final response. For example, a test file might detail a user request to "Turn off device_2 in the Bedroom," specifying the agent's use of a set_device_info tool with parameters like location: Bedroom, device_id: device_2, and status: OFF, and an expected final response of "I have set the device_2 status to off." Test files can be organized into folders and may include a test_config.json file to define evaluation criteria. Evalset files utilize a dataset called an "evalset" to evaluate interactions, containing multiple potentially lengthy sessions suited for simulating complex, multi-turn conversations and integration tests. An evalset file comprises multiple "evals," each representing a distinct session with one or more "turns" that include user queries, expected tool use, intermediate responses, and a reference final response. An example evalset might include a session where the user first asks "What can you do?" and then says "Roll a 10 sided dice twice and then check if 9 is a prime or not," defining expected roll_die tool calls and a check_prime tool call, along with the final response summarizing the dice rolls and the prime check. 

AI 智能体评估涉及两种主要方法：使用测试文件和使用评估集文件。测试文件以 JSON 格式表示单个、简单的智能体-模型交互或会话，非常适合在活跃开发期间进行单元测试，侧重于快速执行和简单的会话复杂性。每个测试文件包含一个带有多个回合的单个会话，其中回合是一个用户-智能体交互，包括用户的查询、预期的工具使用轨迹、中间智能体响应和最终响应。例如，测试文件可能详细说明用户请求"关闭卧室中的 device_2"，指定智能体使用带有 location: Bedroom、device_id: device_2 和 status: OFF 等参数的 set_device_info 工具，以及预期的最终响应"我已将 device_2 状态设置为关闭"。测试文件可以组织到文件夹中，并可能包含 test_config.json 文件来定义评估标准。评估集文件利用称为"evalset"的数据集来评估交互，包含多个可能很长的会话，适合模拟复杂的多回合对话和集成测试。评估集文件包含多个"评估"，每个评估代表一个具有一个或多个"回合"的不同会话，其中包括用户查询、预期的工具使用、中间响应和参考最终响应。示例评估集可能包括一个会话，其中用户首先询问"你能做什么？"然后说"掷两次 10 面骰子，然后检查 9 是否是质数"，定义预期的 roll_die 工具调用和 check_prime 工具调用，以及总结骰子结果和质数检查的最终响应。

**Multi-agents**: Evaluating a complex AI system with multiple agents is much like assessing a team project. Because there are many steps and handoffs, its complexity is an advantage, allowing you to check the quality of work at each stage. You can examine how well each individual "agent" performs its specific job, but you must also evaluate how the entire system is performing as a whole.

**多智能体：** 评估具有多个智能体的复杂 AI 系统非常像评估团队项目。因为有许多步骤和交接，其复杂性是一个优势，允许您检查每个阶段的工作质量。您可以检查每个单独的"智能体"如何执行其特定工作，但您还必须评估整个系统作为一个整体的表现如何。

To do this, you ask key questions about the team's dynamics, supported by concrete examples:

为此，您需要提出关于团队动态的关键问题，并以具体示例作为支持：

* Are the agents cooperating effectively? For instance, after a 'Flight-Booking Agent' secures a flight, does it successfully pass the correct dates and destination to the 'Hotel-Booking Agent'? A failure in cooperation could lead to a hotel being booked for the wrong week.  

* 智能体是否有效合作？例如，在"航班预订智能体"成功预订航班后，它是否成功地将正确的日期和目的地传递给"酒店预订智能体"？合作失败可能导致酒店预订在错误的周。

* Did they create a good plan and stick to it? Imagine the plan is to first book a flight, then a hotel. If the 'Hotel Agent' tries to book a room before the flight is confirmed, it has deviated from the plan. You also check if an agent gets stuck, for example, endlessly searching for a "perfect" rental car and never moving on to the next step.  

* 他们是否制定了好的计划并坚持执行？想象计划是首先预订航班，然后预订酒店。如果"酒店智能体"在航班确认之前尝试预订房间，它已经偏离了计划。您还要检查智能体是否卡住，例如，无休止地搜索"完美"租车，从不进入下一步。

* Is the right agent being chosen for the right task? If a user asks about the weather for their trip, the system should use a specialized 'Weather Agent' that provides live data. If it instead uses a 'General Knowledge Agent' that gives a generic answer like "it's usually warm in summer," it has chosen the wrong tool for the job.  

* 是否为正确的任务选择了正确的智能体？如果用户询问他们旅行的天气，系统应该使用提供实时数据的专门"天气智能体"。如果它使用提供通用答案（如"夏天通常很温暖"）的"通用知识智能体"，它为这项工作选择了错误的工具。

* Finally, does adding more agents improve performance? If you add a new 'Restaurant-Reservation Agent' to the team, does it make the overall trip-planning better and more efficient? Or does it create conflicts and slow the system down, indicating a problem with scalability?.

* 最后，添加更多智能体是否提高了性能？如果您向团队添加一个新的"餐厅预订智能体"，它是否使整体旅行规划更好、更高效？还是它会造成冲突并减慢系统速度，表明可扩展性存在问题？

## From Agents to Advanced Contractors

## 从智能体到高级承包商

Recently, it has been proposed (Agent Companion, gulli et al.) an evolution from simple AI agents to advanced "contractors", moving from probabilistic, often unreliable systems to more deterministic and accountable ones designed for complex, high-stakes environments (see Fig.2). 

最近，有人提出（Agent Companion，gulli 等人）从简单的 AI 智能体演进为高级"承包商"，从概率性的、通常不可靠的系统转向为复杂的、高风险环境设计的更确定性和可问责的系统（见图 2）。

Today's common AI agents operate on brief, underspecified instructions, which makes them suitable for simple demonstrations but brittle in production, where ambiguity leads to failure. The "contractor" model addresses this by establishing a rigorous, formalized relationship between the user and the AI, built upon a foundation of clearly defined and mutually agreed-upon terms, much like a legal service agreement in the human world. This transformation is supported by four key pillars that collectively ensure clarity, reliability, and robust execution of tasks that were previously beyond the scope of autonomous systems.

当今常见的 AI 智能体以简短的、规格不明确的指令运行，这使得它们适合简单的演示，但在生产中很脆弱，因为歧义会导致失败。"承包商"模型通过建立用户和 AI 之间严格的、正式化的关系来解决这个问题，该关系建立在明确定义和相互同意的条款基础上，就像人类世界中的法律服务协议一样。这种转变得到四个关键支柱的支持，这些支柱共同确保了以前超出自主系统范围的任务的清晰性、可靠性和稳健执行。

First is the pillar of the Formalized Contract, a detailed specification that serves as the single source of truth for a task. It goes far beyond a simple prompt. For example, a contract for a financial analysis task wouldn't just say "analyze last quarter's sales"; it would demand "a 20-page PDF report analyzing European market sales from Q1 2025, including five specific data visualizations, a comparative analysis against Q1 2024, and a risk assessment based on the included dataset of supply chain disruptions." This contract explicitly defines the required deliverables, their precise specifications, the acceptable data sources, the scope of work, and even the expected computational cost and completion time, making the outcome objectively verifiable.

首先是正式化合约的支柱，这是一个详细的规范，作为任务的唯一真实来源。它远远超出了简单的提示词。例如，财务分析任务的合约不会只说"分析上个季度的销售"；它会要求"一份 20 页的 PDF 报告，分析 2025 年第一季度的欧洲市场销售，包括五个特定的数据可视化、与 2024 年第一季度的比较分析以及基于提供的供应链中断数据集的风险评估"。此合约明确定义了所需的可交付成果、其精确规格、可接受的数据源、工作范围，甚至预期的计算成本和完成时间，使结果客观可验证。

Second is the pillar of a Dynamic Lifecycle of Negotiation and Feedback. The contract is not a static command but the start of a dialogue. The contractor agent can analyze the initial terms and negotiate. For instance, if a contract demands the use of a specific proprietary data source the agent cannot access, it can return feedback stating, "The specified XYZ database is inaccessible. Please provide credentials or approve the use of an alternative public database, which may slightly alter the data's granularity." This negotiation phase, which also allows the agent to flag ambiguities or potential risks, resolves misunderstandings before execution begins, preventing costly failures and ensuring the final output aligns perfectly with the user's actual intent.

第二是动态的协商和反馈生命周期支柱。合约不是静态命令，而是对话的开始。承包商智能体可以分析初始条款并进行协商。例如，如果合约要求使用智能体无法访问的特定专有数据源，它可以返回反馈，说明"指定的 XYZ 数据库不可访问。请提供凭据或批准使用替代公共数据库，这可能会略微改变数据的粒度。"这个协商阶段也允许智能体标记歧义或潜在风险，在执行开始之前解决误解，防止代价高昂的失败，并确保最终输出与用户的实际意图完全一致。

![][image2]

Fig. 2: Contract execution example among agents

图 2：智能体之间的合约执行示例

The third pillar is Quality-Focused Iterative Execution. Unlike agents designed for low-latency responses, a contractor prioritizes correctness and quality. It operates on a principle of self-validation and correction. For a code generation contract, for example, the agent would not just write the code; it would generate multiple algorithmic approaches, compile and run them against a suite of unit tests defined within the contract, score each solution on metrics like performance, security, and readability, and only submit the version that passes all validation criteria. This internal loop of generating, reviewing, and improving its own work until the contract's specifications are met is crucial for building trust in its outputs.

第三个支柱是以质量为中心的迭代执行。与为低延迟响应设计的智能体不同，承包商优先考虑正确性和质量。它基于自我验证和纠正的原则运作。例如，对于代码生成合约，智能体不会只是编写代码；它会生成多个算法方法，根据合约中定义的一套单元测试编译和运行它们，对性能、安全性和可读性等指标对每个解决方案进行评分，并且只提交通过所有验证标准的版本。这种生成、审查和改进自己的工作的内部循环，直到满足合约的规格，对于建立对其输出的信任至关重要。

Finally, the fourth pillar is Hierarchical Decomposition via Subcontracts. For tasks of significant complexity, a primary contractor agent can act as a project manager, breaking the main goal into smaller, more manageable sub-tasks. It achieves this by generating new, formal "subcontracts." For example, a master contract to "build an e-commerce mobile application" could be decomposed by the primary agent into subcontracts for "designing the UI/UX," "developing the user authentication module," "creating the product database schema," and "integrating a payment gateway." Each of these subcontracts is a complete, independent contract with its own deliverables and specifications, which could be assigned to other specialized agents. This structured decomposition allows the system to tackle immense, multifaceted projects in a highly organized and scalable manner, marking the transition of AI from a simple tool to a truly autonomous and reliable problem-solving engine.

最后，第四个支柱是通过子合约的层次化分解。对于复杂度很高的任务，主承包商智能体可以充当项目经理，将主要目标分解为更小的、更易管理的子任务。它通过生成新的、正式的"子合约"来实现这一点。例如，"构建电子商务移动应用程序"的主合约可以由主智能体分解为"设计 UI/UX"、"开发用户身份验证模块"、"创建产品数据库架构"和"集成支付网关"的子合约。这些子合约中的每一个都是一个完整的、独立的合约，具有自己的可交付成果和规格，可以分配给其他专门的智能体。这种结构化的分解使系统能够以高度组织和可扩展的方式处理巨大的、多方面的项目，标志着 AI 从简单工具向真正自主和可靠的问题解决引擎的转变。

Ultimately, this contractor framework reimagines AI interaction by embedding principles of formal specification, negotiation, and verifiable execution directly into the agent's core logic. This methodical approach elevates artificial intelligence from a promising but often unpredictable assistant into a dependable system capable of autonomously managing complex projects with auditable precision. By solving the critical challenges of ambiguity and reliability, this model paves the way for deploying AI in mission-critical domains where trust and accountability are paramount.

最终，这个承包商框架通过将正式规范、协商和可验证执行的原则直接嵌入到智能体的核心逻辑中，重新构想了 AI 交互。这种系统化的方法将人工智能从一个有前途但经常不可预测的助手提升为能够以可审计的精度自主管理复杂项目的可靠系统。通过解决歧义和可靠性的关键挑战，该模型为在信任和问责至关重要的关键任务领域部署 AI 铺平了道路。

## Google's ADK 

## Google 的 ADK

Before concluding, let's look at a concrete example of a framework that supports evaluation. Agent evaluation with Google's ADK (see Fig.3) can be conducted via three methods: web-based UI (adk web) for interactive evaluation and dataset generation, programmatic integration using pytest for incorporation into testing pipelines, and direct command-line interface (adk eval) for automated evaluations suitable for regular build generation and verification processes. 

在结束之前，让我们看一个支持评估的框架的具体示例。使用 Google 的 ADK 进行智能体评估（见图 3）可以通过三种方法进行：基于 Web 的 UI（adk web）用于交互式评估和数据集生成、使用 pytest 的编程集成用于整合到测试管道中，以及直接命令行界面（adk eval）用于适合定期构建生成和验证过程的自动化评估。

![][image3]

Fig.3: Evaluation Support for Google ADK

图 3：Google ADK 的评估支持

The web-based UI enables interactive session creation and saving into existing or new eval sets, displaying evaluation status. Pytest integration allows running test files as part of integration tests by calling AgentEvaluator.evaluate, specifying the agent module and test file path. 

基于 Web 的 UI 支持交互式会话创建并保存到现有或新的评估集中，显示评估状态。Pytest 集成允许通过调用 AgentEvaluator.evaluate 并指定智能体模块和测试文件路径，将测试文件作为集成测试的一部分运行。

The command-line interface facilitates automated evaluation by providing the agent module path and eval set file, with options to specify a configuration file or print detailed results. Specific evals within a larger eval set can be selected for execution by listing them after the eval set filename, separated by commas.

命令行界面通过提供智能体模块路径和评估集文件来促进自动化评估，并具有指定配置文件或打印详细结果的选项。可以通过在评估集文件名后列出（用逗号分隔）来选择较大评估集中的特定评估以供执行。

## At a Glance

## 速览

**What:** Agentic systems and LLMs operate in complex, dynamic environments where their performance can degrade over time. Their probabilistic and non-deterministic nature means that traditional software testing is insufficient for ensuring reliability. Evaluating dynamic multi-agent systems is a significant challenge because their constantly changing nature and that of their environments demand the development of adaptive testing methods and sophisticated metrics that can measure collaborative success beyond individual performance. Problems like data drift, unexpected interactions, tool calling, and deviations from intended goals can arise after deployment. Continuous assessment is therefore necessary to measure an agent's effectiveness, efficiency, and adherence to operational and safety requirements.

**内容：** Agentic 系统和 LLM 在复杂的动态环境中运行，它们的性能可能会随时间退化。它们的概率性和非确定性本质意味着传统的软件测试不足以确保可靠性。评估动态多智能体系统是一项重大挑战，因为它们不断变化的性质以及其环境的性质要求开发适应性测试方法和能够测量超越个体性能的协作成功的复杂指标。部署后可能出现数据漂移、意外交互、工具调用和偏离预期目标等问题。因此，持续评估对于测量智能体的效能、效率以及对操作和安全要求的遵守是必要的。

**Why:** A standardized evaluation and monitoring framework provides a systematic way to assess and ensure the ongoing performance of intelligent agents. This involves defining clear metrics for accuracy, latency, and resource consumption, like token usage for LLMs. It also includes advanced techniques such as analyzing agentic trajectories to understand the reasoning process and employing an LLM-as-a-Judge for nuanced, qualitative assessments. By establishing feedback loops and reporting systems, this framework allows for continuous improvement, A/B testing, and the detection of anomalies or performance drift, ensuring the agent remains aligned with its objectives.

**原因：** 标准化的评估和监控框架提供了一种系统的方式来评估和确保智能体的持续性能。这涉及为准确性、延迟和资源消耗（如 LLM 的 token 使用量）定义明确的指标。它还包括高级技术，例如分析智能体轨迹以理解推理过程，以及采用 LLM-as-a-Judge 进行细微的、定性的评估。通过建立反馈循环和报告系统，该框架允许持续改进、A/B 测试以及检测异常或性能漂移，确保智能体与目标保持一致。

**Rule of thumb:** Use this pattern when deploying agents in live, production environments where real-time performance and reliability are critical. Additionally, use it when needing to systematically compare different versions of an agent or its underlying models to drive improvements, and when operating in regulated or high-stakes domains requiring compliance, safety, and ethical audits. This pattern is also suitable when an agent's performance may degrade over time due to changes in data or the environment (drift), or when evaluating complex agentic behavior, including the sequence of actions (trajectory) and the quality of subjective outputs like helpfulness.

**实践建议：** 在部署智能体到实时性能和可靠性至关重要的生产环境时使用此模式。此外，当需要系统地比较智能体或其底层模型的不同版本以推动改进时，以及在需要合规性、安全性和道德审计的受监管或高风险领域运营时使用它。当智能体的性能可能由于数据或环境变化（漂移）而随时间退化时，或者在评估复杂的智能体行为时（包括操作序列（轨迹）和主观输出（如有用性）的质量），此模式也适用。

**Visual summary** 

**可视化摘要**

![][image4]  

Fig.4: Evaluation and Monitoring design pattern

图 4：评估和监控设计模式

## Key Takeaways

## 关键要点

* Evaluating intelligent agents goes beyond traditional tests to continuously measure their effectiveness, efficiency, and adherence to requirements in real-world environments.  

* 评估智能体超越了传统测试，在真实世界环境中持续测量其有效性、效率以及对要求的遵守。

* Practical applications of agent evaluation include performance tracking in live systems, A/B testing for improvements, compliance audits, and detecting drift or anomalies in behavior.  

* 智能体评估的实际应用包括实时系统中的性能跟踪、用于改进的 A/B 测试、合规审计以及检测行为中的漂移或异常。

* Basic agent evaluation involves assessing response accuracy, while real-world scenarios demand more sophisticated metrics like latency monitoring and token usage tracking for LLM-powered agents.  

* 基本智能体评估涉及评估响应准确性，而真实世界场景需要更复杂的指标，如延迟监控和 LLM 驱动智能体的 token 使用跟踪。

* Agent trajectories, the sequence of steps an agent takes, are crucial for evaluation, comparing actual actions against an ideal, ground-truth path to identify errors and inefficiencies.  

* 智能体轨迹（智能体采取的步骤序列）对于评估至关重要，将实际操作与理想的、真实的路径进行比较，以识别错误和低效率。

* The ADK provides structured evaluation methods through individual test files for unit testing and comprehensive evalset files for integration testing, both defining expected agent behavior.  

* ADK 通过用于单元测试的单个测试文件和用于集成测试的综合评估集文件提供结构化的评估方法，两者都定义了预期的智能体行为。

* Agent evaluations can be executed via a web-based UI for interactive testing, programmatically with pytest for CI/CD integration, or through a command-line interface for automated workflows.  

* 智能体评估可以通过基于 Web 的 UI 进行交互式测试、使用 pytest 进行 CI/CD 集成的编程方式，或通过命令行界面进行自动化工作流执行。

* In order to make AI reliable for complex, high-stakes tasks, we must move from simple prompts to formal "contracts" that precisely define verifiable deliverables and scope. This structured agreement allows the Agents to negotiate, clarify ambiguities, and iteratively validate its own work, transforming it from an unpredictable tool into an accountable and trustworthy system.

* 为了使 AI 在复杂的、高风险的任务中可靠，我们必须从简单的提示词转向精确定义可验证可交付成果和范围的正式"合约"。这种结构化协议允许智能体协商、澄清歧义并迭代验证其自己的工作，将其从不可预测的工具转变为可问责和值得信赖的系统。

## Conclusions

## 结论

In conclusion, effectively evaluating AI agents requires moving beyond simple accuracy checks to a continuous, multi-faceted assessment of their performance in dynamic environments. This involves practical monitoring of metrics like latency and resource consumption, as well as sophisticated analysis of an agent's decision-making process through its trajectory. For nuanced qualities like helpfulness, innovative methods such as the LLM-as-a-Judge are becoming essential, while frameworks like Google's ADK provide structured tools for both unit and integration testing. The challenge intensifies with multi-agent systems, where the focus shifts to evaluating collaborative success and effective cooperation.

总之，有效评估 AI 智能体需要超越简单的准确性检查，对其在动态环境中的性能进行持续的、多方面的评估。这涉及实际监控延迟和资源消耗等指标，以及通过其轨迹对智能体决策过程进行复杂分析。对于有用性等细微品质，诸如 LLM-as-a-Judge 之类的创新方法变得必不可少，而像 Google 的 ADK 这样的框架为单元和集成测试提供了结构化的工具。对于多智能体系统，挑战加剧，重点转向评估协作成功和有效合作。

To ensure reliability in critical applications, the paradigm is shifting from simple, prompt-driven agents to advanced "contractors" bound by formal agreements. These contractor agents operate on explicit, verifiable terms, allowing them to negotiate, decompose tasks, and self-validate their work to meet rigorous quality standards. This structured approach transforms agents from unpredictable tools into accountable systems capable of handling complex, high-stakes tasks. Ultimately, this evolution is crucial for building the trust required to deploy sophisticated agentic AI in mission-critical domains.

为了确保关键应用中的可靠性，范式正在从简单的、提示词驱动的智能体转向受正式协议约束的高级"承包商"。这些承包商智能体在明确的、可验证的条款上运作，允许它们协商、分解任务并自我验证其工作以满足严格的质量标准。这种结构化方法将智能体从不可预测的工具转变为能够处理复杂的、高风险任务的可问责系统。最终，这种演变对于建立在关键任务领域部署复杂的 Agentic AI 所需的信任至关重要。

## References

## 参考文献

Relevant research includes:

相关研究包括：

1. ADK Web: [https://github.com/google/adk-web](https://github.com/google/adk-web)   
2. ADK Evaluate: [https://google.github.io/adk-docs/evaluate/](https://google.github.io/adk-docs/evaluate/)  
3. Survey on Evaluation of LLM-based Agents, [https://arxiv.org/abs/2503.16416](https://arxiv.org/abs/2503.16416)   
4. Agent-as-a-Judge: Evaluate Agents with Agents, [https://arxiv.org/abs/2410.10934](https://arxiv.org/abs/2410.10934)   
5. Agent Companion, gulli et al: [https://www.kaggle.com/whitepaper-agent-companion](https://www.kaggle.com/whitepaper-agent-companion) 

[image1]: ../images/chapter-19/image1.png

[image2]: ../images/chapter-19/image2.png

[image3]: ../images/chapter-19/image3.png

[image4]: ../images/chapter-19/image4.png
