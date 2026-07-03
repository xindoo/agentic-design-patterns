# 第 14 章：知识检索（RAG）

LLM 在生成类人文本方面展现出了强大的能力。然而，它们的知识库通常局限于训练时使用的数据，这限制了它们对实时信息、特定公司数据或高度专业化细节的访问。知识检索（RAG，即检索增强生成）技术正是为了解决这一局限性而设计的。RAG 使 LLM 能够访问和整合外部信息、实时数据和特定上下文内容，从而显著提高其输出的准确性、相关性和事实基础。

对于 AI 智能体来说，这一能力尤为关键——它让智能体能够基于实时、可验证的数据来采取行动和作出回应，而不仅仅依赖于静态的训练数据。这种能力使得智能体能够准确地执行复杂任务，例如查询最新的公司政策来回答特定问题，或在下订单前检查当前库存状况。通过整合外部知识，RAG 将智能体从简单的对话者转变为能够执行有意义工作的有效、数据驱动的工具。

## 知识检索（RAG）模式概述

知识检索（RAG）模式通过在生成响应之前赋予 LLM 访问外部知识库的权限，显著增强了它们的能力。与仅依赖内部预训练知识不同，RAG 允许 LLM "查找"信息，就像人类查阅书籍或搜索互联网一样。这一过程使 LLM 能够提供更准确、更新及时且可验证的答案。

当用户向使用 RAG 的 AI 系统提出问题或发出指令时，查询不会直接发送给 LLM。相反，系统首先在一个庞大的外部知识库（高度组织化的文档、数据库或网页集合）中搜索相关信息。这种搜索不是简单的关键字匹配，而是一种能够理解用户意图和词语背后含义的"语义搜索"。初始搜索会提取出最相关的信息片段或"块"。然后，这些提取的片段被"增强"到原始提示中，形成一个更丰富、信息量更大的查询。最后，这个增强的提示被发送给 LLM。借助这些额外的上下文信息，LLM 能够生成不仅流畅自然，而且在事实上基于检索数据的响应。

RAG 框架提供了几个重要优势。它允许 LLM 访问最新信息，从而克服了静态训练数据的局限性。这种方法还通过将响应建立在可验证的数据上，减少了"幻觉"（生成虚假信息）的风险。此外，LLM 可以利用内部公司文档或维基中的专业知识。这一过程的另一个重要优势是能够提供"引用"，即明确指出信息的来源，从而增强 AI 响应的可信度和可验证性。

要充分理解 RAG 的工作原理，需要掌握几个核心概念（见图 1）：

**嵌入（Embeddings）**：在 LLM 的语境中，嵌入是文本的数值表示形式，可以是单词、短语或整个文档。这些表示以向量的形式存在，即一系列数字。其核心思想是在数学空间中捕捉不同文本片段的语义含义和关系。具有相似含义的单词或短语在向量空间中会彼此靠近。例如，想象一个简单的二维坐标系，"cat"这个词可能位于坐标 (2, 3)，而"kitten"则非常接近，位于 (2.1, 3.1)。相比之下，"car"这个词的位置则较远，比如 (8, 1)，反映出其不同的含义。实际上，这些嵌入存在于具有数百甚至数千个维度的高维空间中，从而能够对语言进行非常细致的理解。

**文本相似度**：文本相似度指的是衡量两段文本相似程度的指标。这可以是表面层次的，主要关注词汇的重叠（词汇相似度），也可以是更深层次的，基于文本的含义。在 RAG 的语境中，文本相似度对于在知识库中查找与用户查询最相关的信息至关重要。例如，考虑这两个句子："What is the capital of France?"和"Which city is the capital of France?"。虽然措辞不同，但它们询问的是同一个问题。一个好的文本相似度模型能够识别这一点，并为这两个句子分配较高的相似度分数，即使它们只共享少数几个单词。这通常通过计算文本的嵌入来实现。

**语义相似度和距离**：语义相似度是文本相似度的一种更高级形式，它纯粹关注文本的含义和上下文，而不仅仅是使用的单词。其目标是理解两段文本是否传达相同的概念或想法。语义距离则是语义相似度的反义词；高语义相似度意味着低语义距离，反之亦然。在 RAG 中，语义搜索依赖于查找与用户查询语义距离最小的文档。例如，短语"a furry feline companion"和"a domestic cat"除了冠词"a"外没有共同的单词。然而，能够理解语义相似度的模型会识别出它们指的是同一事物，并认为它们高度相似。这是因为它们的嵌入在向量空间中非常接近，表明语义距离很小。这就是 RAG 能够找到相关信息的"智能搜索"机制——即使用户的措辞与知识库中的文本不完全匹配。

![][image1]

图 1：RAG 核心概念：分块、嵌入和向量数据库

**文档分块**：分块是将大型文档分解为更小、更易于管理的片段或"块"的过程。为了使 RAG 系统高效工作，它不能将整个大型文档直接输入 LLM，而是处理这些更小的块。文档分块的方式对于保持信息的上下文和含义至关重要。例如，与其将 50 页的用户手册视为单个文本块，分块策略可能会将其分解为章节、段落甚至句子。这样，"故障排除"部分就可以与"安装指南"分开作为独立的块。当用户询问特定问题时，RAG 系统可以检索最相关的故障排除块，而不是整个手册。这使得检索过程更快，提供给 LLM 的信息更加集中，更符合用户的直接需求。

文档分块完成后，RAG 系统必须使用检索技术来找到给定查询的最相关片段。主要方法是向量搜索，它利用嵌入和语义距离来查找概念上与用户问题相似的块。另一种较旧但仍然有价值的技术是 BM25，这是一种基于关键字的算法，根据词频对块进行排名，但不理解语义含义。为了获得两全其美的效果，通常使用混合搜索方法，将 BM25 的关键字精度与语义搜索的上下文理解相结合。这种融合实现了更强大和准确的检索，能够捕获字面匹配和概念相关性。

**向量数据库**：向量数据库是一种专门设计用于高效存储和查询嵌入的专用数据库类型。在文档被分块并转换为嵌入后，这些高维向量被存储在向量数据库中。传统的检索技术（如基于关键字的搜索）非常擅长查找包含查询中确切单词的文档，但缺乏对语言的深入理解。它们无法识别"furry feline companion"意味着"cat"。这就是向量数据库的优势所在——它们专门为语义搜索而构建。通过将文本存储为数值向量，它们可以基于概念含义而不仅仅是关键字重叠来查找结果。

当用户的查询也被转换为向量时，数据库使用高度优化的算法（如 HNSW——分层可导航小世界）快速搜索数百万个向量，并找到在含义上"最接近"的向量。这种方法对于 RAG 来说要优越得多，因为即使用户的措辞与源文档完全不同，它也能发现相关上下文。本质上，虽然其他技术搜索单词，向量数据库搜索含义。

这项技术以各种形式实现，从托管数据库如 Pinecone 和 Weaviate，到开源解决方案如 Chroma DB、Milvus 和 Qdrant。甚至现有数据库也可以增强向量搜索功能，如 Redis、Elasticsearch 和 Postgres（使用 pgvector 扩展）。核心检索机制通常由 Meta AI 的 FAISS 或 Google Research 的 ScaNN 等库提供支持，这些库对这些系统的效率至关重要。

**RAG 的挑战**：尽管功能强大，RAG 模式并非没有挑战。一个主要问题出现在回答查询所需的信息不局限于单个块，而是分散在文档的多个部分甚至多个文档中时。在这种情况下，检索器可能无法收集所有必要的上下文，导致答案不完整或不准确。系统的有效性还高度依赖于分块和检索过程的质量；如果检索到不相关的块，可能会引入噪声并混淆 LLM。此外，有效综合来自潜在矛盾来源的信息仍然是这些系统的一个重大障碍。

除此之外，另一个挑战是 RAG 需要将整个知识库预处理并存储在专门的数据库中（如向量或图数据库），这是一项相当大的工作。因此，这些知识需要定期更新以保持最新，这在处理不断演变的来源（如公司维基）时是一项关键任务。整个过程可能对性能产生明显影响，增加延迟、运营成本和最终提示中使用的 token 数量。

总之，检索增强生成（RAG）模式代表了使 AI 更加知识渊博和可靠的重大飞跃。通过将外部知识检索步骤无缝集成到生成过程中，RAG 解决了独立 LLM 的一些核心局限。嵌入和语义相似度的基础概念，结合关键字和混合搜索等检索技术，允许系统智能地找到相关信息，通过战略性分块使其可管理。这整个检索过程由专门的向量数据库提供支持，这些数据库旨在大规模存储和高效查询数百万个嵌入。虽然检索碎片化或矛盾信息的挑战仍然存在，RAG 使 LLM 能够产生不仅在上下文上适当而且建立在可验证事实基础上的答案，从而在 AI 中培养更大的信任和实用性。

**图 RAG（Graph RAG）**：GraphRAG 是检索增强生成的一种高级形式，它利用知识图谱而不是简单的向量数据库进行信息检索。它通过在这个结构化知识库中导航数据实体（节点）之间的明确关系（边）来回答复杂查询。一个关键优势是它能够综合来自多个文档的碎片化信息来生成答案，这是传统 RAG 的常见失败之处。通过理解这些连接，GraphRAG 提供了更多上下文准确和细致的响应。

用例包括复杂的金融分析（将公司与市场事件联系起来）以及用于发现基因和疾病之间关系的科学研究。然而，主要缺点是构建和维护高质量知识图谱所需的显著复杂性、成本和专业知识。与更简单的向量搜索系统相比，这种设置也不太灵活，并且可能引入更高的延迟。系统的有效性完全取决于底层图结构的质量和完整性。因此，GraphRAG 为复杂问题提供了卓越的上下文推理，但实施和维护成本要高得多。总之，在深度、互联的洞察比标准 RAG 的速度和简单性更重要的情况下，它表现出色。

**Agentic RAG**：这种模式的演进被称为 **Agentic RAG**（见图 2），它引入了一个推理和决策层，以显著增强信息提取的可靠性。Agentic RAG 不仅仅是检索和增强，一个"智能体"——一个专门的 AI 组件——充当知识的关键守门人和精炼者。这个智能体不是被动地接受最初检索的数据，而是主动质疑其质量、相关性和完整性，如以下场景所示。

首先，智能体擅长反思和源验证。如果用户问："我们公司的远程工作政策是什么？"标准 RAG 可能会提取 2020 年的博客文章和官方的 2025 年政策文档。然而，智能体会分析文档的元数据，识别 2025 年政策为最新和最权威的来源，并在将正确的上下文发送到 LLM 以获得精确答案之前丢弃过时的博客文章。

![][image2]

图 2：Agentic RAG 引入了一个推理智能体，它主动评估、协调和精炼检索的信息，以确保更准确和可信的最终响应。

其次，智能体擅长协调知识冲突。想象一位金融分析师问："Alpha 项目的第一季度预算是多少？"系统检索到两个文档：一个初始提案说明预算为 50,000 欧元，一个最终的财务报告列出为 65,000 欧元。Agentic RAG 会识别这种矛盾，将财务报告优先作为更可靠的来源，并向 LLM 提供经过验证的数字，确保最终答案基于最准确的数据。

第三，智能体可以执行多步推理来综合复杂答案。如果用户问："我们产品的功能和定价与竞争对手 X 相比如何？"智能体会将此分解为单独的子查询。它会为自己产品的功能、定价、竞争对手 X 的功能和竞争对手 X 的定价启动不同的搜索。在收集这些单独的信息片段后，智能体会将它们综合成结构化的比较上下文，然后再将其提供给 LLM，从而实现简单检索无法产生的全面响应。

第四，智能体可以识别知识差距并使用外部工具。假设用户问："市场对我们昨天推出的新产品的即时反应如何？"智能体搜索每周更新的内部知识库，没有找到相关信息。识别到这个差距，它可以激活一个工具——例如实时网络搜索 API——来查找最近的新闻文章和社交媒体情绪。然后智能体使用这些新收集的外部信息来提供最新的答案，克服其静态内部数据库的限制。

**Agentic RAG 的挑战**：虽然功能强大，但智能体层引入了其自身的一系列挑战。主要缺点是复杂性和成本的显著增加。设计、实施和维护智能体的决策逻辑和工具集成需要大量的工程工作，并增加了计算费用。这种复杂性也可能导致延迟增加，因为智能体的反思、工具使用和多步推理循环比标准的直接检索过程需要更多时间。此外，智能体本身可能成为新的错误来源；有缺陷的推理过程可能导致它陷入无用的循环，误解任务，或不当丢弃相关信息，最终降低最终响应的质量。

**总结：** Agentic RAG 代表了标准检索模式的复杂演进，将其从被动的数据管道转变为主动的、解决问题的框架。通过嵌入一个可以评估来源、协调冲突、分解复杂问题和使用外部工具的推理层，智能体显著提高了生成答案的可靠性和深度。这一进步使 AI 更加可信和有能力，尽管它带来了必须仔细管理的系统复杂性、延迟和成本方面的重要权衡。

## 实际应用和用例

知识检索（RAG）正在改变 LLM 在各个行业中的使用方式，显著增强了它们提供更准确和上下文相关响应的能力。

主要应用包括：

* **企业搜索和问答**：组织可以开发内部聊天机器人，利用内部文档（如 HR 政策、技术手册和产品规格）来响应员工查询。RAG 系统从这些文档中提取相关部分，为 LLM 的响应提供信息支持。
* **客户支持和帮助台**：基于 RAG 的系统可以通过访问产品手册、常见问题解答（FAQ）和支持工单中的信息，为客户查询提供精确和一致的响应。这可以减少对常规问题的直接人工干预需求，提高服务效率。
* **个性化内容推荐**：与基本的关键字匹配不同，RAG 能够识别和检索与用户偏好或先前交互在语义上相关的内容（如文章、产品），从而提供更加精准和个性化的推荐。
* **新闻和时事摘要**：LLM 可以与实时新闻源集成。当被询问关于时事的问题时，RAG 系统会检索最近的文章，使 LLM 能够生成基于最新信息的摘要。

通过整合外部知识，RAG 将 LLM 的能力从简单的通信工具扩展到作为知识处理系统发挥作用，大大提升了其实用价值。

## 实践代码示例（ADK）

为了说明知识检索（RAG）模式，让我们看三个示例。

首先，是如何使用 Google Search 进行 RAG 并将 LLM 建立在搜索结果上。由于 RAG 涉及访问外部信息，Google Search 工具是内置检索机制的直接示例，可以增强 LLM 的知识。

```python
from google.adk.tools import google_search
from google.adk.agents import Agent

search_agent = Agent(
    name="research_assistant",
    model="gemini-2.0-flash-exp",
    instruction="你帮助用户研究主题。当被问及时，请使用 Google Search 工具",
    tools=[google_search]
)
```

其次，本节介绍如何在 Google ADK 中利用 Vertex AI RAG 功能。提供的代码演示了如何从 ADK 初始化 VertexAiRagMemoryService，从而建立与 Google Cloud Vertex AI RAG Corpus 的连接。该服务通过指定 corpus 资源名称和可选参数（如 SIMILARITY_TOP_K 和 VECTOR_DISTANCE_THRESHOLD）进行配置，这些参数会影响检索过程。SIMILARITY_TOP_K 定义要检索的最相似结果数量，VECTOR_DISTANCE_THRESHOLD 设置检索结果的语义距离限制。这种设置使智能体能够从指定的 RAG Corpus 执行可扩展和持久的语义知识检索，有效地将 Google Cloud 的 RAG 功能集成到 ADK 智能体中，从而支持开发基于事实数据的响应。

```python
## 从 google.adk.memory 模块导入必要的 VertexAiRagMemoryService 类。
from google.adk.memory import VertexAiRagMemoryService

RAG_CORPUS_RESOURCE_NAME = "projects/your-gcp-project-id/locations/us-central1/ragCorpora/your-corpus-id"

## 为要检索的最相似结果的数量定义一个可选参数。
## 这控制 RAG 服务将返回多少相关文档块。
SIMILARITY_TOP_K = 5

## 为向量距离阈值定义一个可选参数。
## 此阈值确定检索结果允许的最大语义距离；
## 距离大于此值的结果可能会被过滤掉。
VECTOR_DISTANCE_THRESHOLD = 0.7

## 初始化 VertexAiRagMemoryService 的实例。
## 这设置了与您的 Vertex AI RAG Corpus 的连接。
## - rag_corpus: 指定您的 RAG Corpus 的唯一标识符。
## - similarity_top_k: 设置要获取的相似结果的最大数量。
## - vector_distance_threshold: 定义用于过滤结果的相似度阈值。
memory_service = VertexAiRagMemoryService(
    rag_corpus=RAG_CORPUS_RESOURCE_NAME,
    similarity_top_k=SIMILARITY_TOP_K,
    vector_distance_threshold=VECTOR_DISTANCE_THRESHOLD
)
```

## 实践代码示例（LangChain）

第三，让我们使用 LangChain 走一遍完整的示例。

```python
import os
import requests
from typing import List, Dict, Any, TypedDict
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Weaviate
from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langgraph.graph import StateGraph, END
import weaviate
from weaviate.embedded import EmbeddedOptions
import dotenv

## 加载环境变量（例如，OPENAI_API_KEY）
dotenv.load_dotenv()

## 设置您的 OpenAI API 密钥（确保从 .env 加载或在此处设置）
## os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

## --- 1. 数据准备（预处理） ---
## 加载数据
url = "https://github.com/langchain-ai/langchain/blob/master/docs/docs/how_to/state_of_the_union.txt"
res = requests.get(url)
with open("state_of_the_union.txt", "w") as f:
    f.write(res.text)
loader = TextLoader('./state_of_the_union.txt')
documents = loader.load()

## 分块文档
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

## 嵌入并将块存储在 Weaviate 中
client = weaviate.Client(
    embedded_options = EmbeddedOptions()
)
vectorstore = Weaviate.from_documents(
    client = client,
    documents = chunks,
    embedding = OpenAIEmbeddings(),
    by_text = False
)

## 定义检索器
retriever = vectorstore.as_retriever()

## 初始化 LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

## --- 2. 为 LangGraph 定义状态 ---
class RAGGraphState(TypedDict):
    question: str
    documents: List[Document]
    generation: str

## --- 3. 定义节点（函数） ---
def retrieve_documents_node(state: RAGGraphState) -> RAGGraphState:
    """基于用户的问题检索文档。"""
    question = state["question"]
    documents = retriever.invoke(question)
    return {"documents": documents, "question": question, "generation": ""}

def generate_response_node(state: RAGGraphState) -> RAGGraphState:
    """基于检索的文档使用 LLM 生成响应。"""
    question = state["question"]
    documents = state["documents"]
    # PDF 中的提示模板
    template = """你是一个用于问答任务的助手。使用以下检索到的上下文来回答问题。如果你不知道答案，就直接说不知道。最多使用三句话，并保持回答简洁。
问题：{question}
上下文：{context}
回答："""
    prompt = ChatPromptTemplate.from_template(template)

    # 从文档格式化上下文
    context = "\n\n".join([doc.page_content for doc in documents])

    # 创建 RAG 链
    rag_chain = prompt | llm | StrOutputParser()

    # 调用链
    generation = rag_chain.invoke({"context": context, "question": question})
    return {"question": question, "documents": documents, "generation": generation}

## --- 4. 构建 LangGraph 图 ---
workflow = StateGraph(RAGGraphState)

## 添加节点
workflow.add_node("retrieve", retrieve_documents_node)
workflow.add_node("generate", generate_response_node)

## 设置入口点
workflow.set_entry_point("retrieve")

## 添加边（转换）
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

## 编译图
app = workflow.compile()

## --- 5. 运行 RAG 应用程序 ---
if __name__ == "__main__":
    print("\n--- 运行 RAG 查询 ---")
    query = "总统对布雷耶大法官说了什么"
    inputs = {"question": query}
    for s in app.stream(inputs):
        print(s)

    print("\n--- 运行另一个 RAG 查询 ---")
    query_2 = "总统对经济说了什么？"
    inputs_2 = {"question": query_2}
    for s in app.stream(inputs_2):
        print(s)
```

这段 Python 代码说明了使用 LangChain 和 LangGraph 实现的检索增强生成（RAG）管道。该过程首先从文本文档创建知识库——文档被分割成块并转换为嵌入，然后将这些嵌入存储在 Weaviate 向量存储中，便于高效的信息检索。LangGraph 中的 StateGraph 用于管理两个关键函数之间的工作流：`retrieve_documents_node` 和 `generate_response_node`。`retrieve_documents_node` 函数查询向量存储，基于用户输入识别相关文档块。随后，`generate_response_node` 函数利用检索的信息和预定义的提示模板，使用 OpenAI LLM 生成响应。`app.stream` 方法允许通过 RAG 管道执行查询，展示了系统生成上下文相关输出的能力。

## 速览

**问题背景**：LLM 在文本生成方面具有令人印象深刻的能力，但其知识从根本上受到训练数据的限制。这些知识是静态的，意味着它不包括实时信息或私有的、特定领域的数据。因此，LLM 的响应可能过时、不准确或缺乏专业任务所需的特定上下文。这一局限性限制了它们在需要当前和事实答案的应用中的可靠性。

**解决方案**：检索增强生成（RAG）模式通过将 LLM 连接到外部知识源提供了标准化的解决方案。当收到查询时，系统首先从指定的知识库中检索相关信息片段，然后将这些片段附加到原始提示中，用及时和特定的上下文丰富它。最后，这个增强的提示被发送到 LLM，使其能够生成准确、可验证且基于外部数据的响应。这个过程有效地将 LLM 从闭卷推理者转变为开卷推理者，显著增强其实用性和可信度。

**实践建议**：当您需要 LLM 基于特定的、最新的或专有信息（不属于其原始训练数据）回答问题或生成内容时，使用此模式。它非常适合在内部文档上构建问答系统、客户支持机器人，以及需要可验证的、基于事实的响应和引用的应用程序。

**可视化摘要**

**![][image3]**

知识检索模式：AI 智能体从结构化数据库查询和检索信息

**![][image4]**

图 3：知识检索模式：AI 智能体响应用户查询，从公共互联网查找和综合信息。

## 关键要点

* 知识检索（RAG）通过允许 LLM 访问外部的、最新的和特定的信息来增强它们。
* 该过程涉及检索（在知识库中搜索相关片段）和增强（将这些片段添加到 LLM 的提示中）。
* RAG 帮助 LLM 克服过时训练数据等局限，减少"幻觉"，并实现特定领域知识集成。
* RAG 允许可归因的答案，因为 LLM 的响应基于检索的来源。
* GraphRAG 利用知识图谱来理解不同信息片段之间的关系，允许它回答需要从多个来源综合数据的复杂问题。
* Agentic RAG 超越了简单的信息检索，使用智能体主动推理、验证和精炼外部知识，确保更准确和可靠的答案。
* 实际应用涵盖企业搜索、客户支持、法律研究和个性化推荐。

## 结论

总之，检索增强生成（RAG）通过将 LLM 连接到外部、实时的数据源，有效解决了其静态知识的核心限制。该工作流程首先检索相关信息片段，然后增强用户的提示，使 LLM 能够生成更准确和上下文感知的响应。这一过程依赖于嵌入、语义搜索和向量数据库等基础技术，这些技术基于语义含义而不仅仅是关键字来查找信息。通过将输出建立在可验证的数据上，RAG 显著减少了事实错误，并允许使用专有信息，通过引用来源增强了可信度。

RAG 的高级演进形式——Agentic RAG，引入了一个推理层，主动验证、协调和综合检索的知识，以获得更大的可靠性。类似地，像 GraphRAG 这样的专门方法利用知识图谱来导航明确的数据关系，使系统能够综合回答高度复杂、相互关联的查询。这种智能体可以解决冲突信息，执行多步查询，并使用外部工具查找缺失的数据。虽然这些高级方法增加了复杂性和延迟，但它们显著提高了最终响应的深度和可信度。这些模式的实际应用正在改变各个行业，从企业搜索和客户支持到个性化内容交付。尽管存在挑战，RAG 是使 AI 更加知识渊博、可靠和有用的关键模式。最终，它将 LLM 从闭卷对话工具转变为强大的开卷推理系统。

## 参考文献

1. Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. [https://arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)
2. Google AI for Developers Documentation.  *Retrieval Augmented Generation - [https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview)*
3. Retrieval-Augmented Generation with Graphs (GraphRAG), [https://arxiv.org/abs/2501.00309](https://arxiv.org/abs/2501.00309)
4. LangChain and LangGraph: Leonie Monigatti, "Retrieval-Augmented Generation (RAG): From Theory to LangChain Implementation,"  [*https://medium.com/data-science/retrieval-augmented-generation-rag-from-theory-to-langchain-implementation-4e9bd5f6a4f2*](https://medium.com/data-science/retrieval-augmented-generation-rag-from-theory-to-langchain-implementation-4e9bd5f6a4f2)
5.  Google Cloud Vertex AI RAG Corpus [*https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/manage-your-rag-corpus\#corpus-management*](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/manage-your-rag-corpus#corpus-management)

[image1]: ../images/chapter-14/image1.png

[image2]: ../images/chapter-14/image2.png

[image3]: ../images/chapter-14/image3.png

[image4]: ../images/chapter-14/image4.png