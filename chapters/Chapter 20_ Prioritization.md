# 第 20 章：优先级排序

在复杂、动态的环境中，Agent 经常会遇到大量潜在的行动、相互冲突的目标以及有限的资源。如果没有明确的流程来确定后续行动，Agent 可能会遭遇效率降低、操作延迟或无法实现关键目标的情况。优先级排序模式通过使 Agent 能够根据重要性、紧迫性、依赖关系和既定标准来评估和排序任务、目标或行动，从而解决这一问题。这确保了 Agent 将精力集中在最关键的任务上，从而提高有效性和目标一致性。

# 优先级排序模式概述

Agent 使用优先级排序来有效管理任务、目标和子目标，指导后续行动。这个过程有助于在处理多个需求时做出明智的决策，优先处理重要或紧急的活动，而不是不太关键的活动。这在资源受限、时间有限以及目标可能冲突的实际场景中尤为相关。

Agent 优先级排序的基本方面通常涉及几个要素。首先，**标准定义**建立用于任务评估的规则或指标。这些可能包括紧急性（任务的时间敏感性）、重要性（对主要目标的影响）、依赖关系（该任务是否是其他任务的前提条件）、资源可用性（必要工具或信息的就绪状态）、成本/收益分析（努力与预期结果的对比），以及个性化 Agent 的用户偏好。其次，**任务评估**涉及根据这些定义的标准评估每个潜在任务，利用从简单规则到 LLM 复杂评分或推理的各种方法。第三，**调度或选择逻辑**是指基于评估结果选择最优下一步行动或任务序列的算法，可能利用队列或高级规划组件。最后，**动态重新优先级排序**允许 Agent 随着情况变化修改优先级，例如新关键事件的出现或截止日期的临近，确保 Agent 的适应性和响应能力。

优先级排序可以在各个层面发生：选择总体目标（高层次目标优先级排序）、在计划内排序步骤（子任务优先级排序）或从可用选项中选择下一个即时行动（行动选择）。有效的优先级排序使 Agent 能够展现更智能、更高效、更稳健的行为，特别是在复杂的多目标环境中。这反映了人类团队组织，其中管理者通过考虑所有成员的输入来优先处理任务。

# 实际应用和用例

在各种实际应用中，AI Agent 展示了对优先级排序的复杂运用，以做出及时有效的决策。

* **自动化客户支持**：Agent 优先处理紧急请求，如系统停机报告，而不是日常事务，如密码重置。他们还可能优先处理高价值客户。
* **云计算**：AI 通过优先将资源分配给高峰需求期间的关键应用程序来管理和调度资源，同时将不太紧急的批处理作业推迟到非高峰时段以优化成本。
* **自动驾驶系统**：持续优先处理行动以确保安全和效率。例如，为避免碰撞而刹车优先于保持车道纪律或优化燃油效率。
* **金融交易**：交易机器人通过分析市场条件、风险承受能力、利润率和实时新闻等因素来优先处理交易，实现高优先级交易的快速执行。
* **项目管理**：AI Agent 根据截止日期、依赖关系、团队可用性和战略重要性来优先处理项目板上的任务。
* **网络安全**：监控网络流量的 Agent 通过评估威胁严重性、潜在影响和资产关键性来优先处理警报，确保对最危险威胁的即时响应。
* **个人助理 AI**：利用优先级排序来管理日常生活，根据用户定义的重要性、即将到来的截止日期和当前上下文来组织日历事件、提醒和通知。

这些示例共同说明了优先级排序能力对于增强 AI Agent 在各种情况下的性能和决策能力是多么基础。

# 实践代码示例

以下演示了使用 LangChain 开发项目管理 AI Agent。该 Agent 促进任务的创建、优先级排序和分配给团队成员，说明了大型语言模型与定制工具在自动化项目管理中的应用。

| ``import os import asyncio from typing import List, Optional, Dict, Type from dotenv import load_dotenv from pydantic import BaseModel, Field from langchain_core.prompts import ChatPromptTemplate from langchain_core.tools import Tool from langchain_openai import ChatOpenAI from langchain.agents import AgentExecutor, create_react_agent from langchain.memory import ConversationBufferMemory # --- 0. 配置和设置 --- # 从 .env 文件加载 OPENAI_API_KEY。 load_dotenv() # ChatOpenAI 客户端自动从环境中获取 API 密钥。 llm = ChatOpenAI(temperature=0.5, model="gpt-4o-mini") # --- 1. 任务管理系统 --- class Task(BaseModel):    """表示系统中的单个任务。"""    id: str    description: str    priority: Optional[str] = None  # P0, P1, P2    assigned_to: Optional[str] = None # 工作人员的名字 class SuperSimpleTaskManager:    """一个高效且稳健的内存任务管理器。"""    def __init__(self):        # 使用字典实现 O(1) 查找、更新和删除。        self.tasks: Dict[str, Task] = {}        self.next_task_id = 1    def create_task(self, description: str) -> Task:        """创建并存储一个新任务。"""        task_id = f"TASK-{self.next_task_id:03d}"        new_task = Task(id=task_id, description=description)        self.tasks[task_id] = new_task        self.next_task_id += 1        print(f"DEBUG: 任务已创建 - {task_id}: {description}")        return new_task    def update_task(self, task_id: str, **kwargs) -> Optional[Task]:        """使用 Pydantic 的 model_copy 安全地更新任务。"""        task = self.tasks.get(task_id)        if task:            # 使用 model_copy 进行类型安全的更新。            update_data = {k: v for k, v in kwargs.items() if v is not None}            updated_task = task.model_copy(update=update_data)            self.tasks[task_id] = updated_task            print(f"DEBUG: 任务 {task_id} 已更新为 {update_data}")            return updated_task                   print(f"DEBUG: 未找到任务 {task_id} 进行更新。")        return None    def list_all_tasks(self) -> str:        """列出系统中当前的所有任务。"""        if not self.tasks:            return "系统中没有任务。"               task_strings = []        for task in self.tasks.values():            task_strings.append(                f"ID: {task.id}, 描述: '{task.description}', "                f"优先级: {task.priority or 'N/A'}, "                f"分配给: {task.assigned_to or 'N/A'}"            )        return "当前任务:\n" + "\n".join(task_strings) task_manager = SuperSimpleTaskManager() # --- 2. 项目管理 Agent 的工具 --- # 使用 Pydantic 模型作为工具参数以获得更好的验证和清晰度。 class CreateTaskArgs(BaseModel):    description: str = Field(description="任务的详细描述。") class PriorityArgs(BaseModel):    task_id: str = Field(description="要更新的任务 ID，例如 'TASK-001'。")    priority: str = Field(description="要设置的优先级。必须是以下之一：'P0'、'P1'、'P2'。") class AssignWorkerArgs(BaseModel):    task_id: str = Field(description="要更新的任务 ID，例如 'TASK-001'。")    worker_name: str = Field(description="要分配任务的工作人员的名字。") def create_new_task_tool(description: str) -> str:    """使用给定的描述创建一个新的项目任务。"""    task = task_manager.create_task(description)    return f"已创建任务 {task.id}: '{task.description}'。" def assign_priority_to_task_tool(task_id: str, priority: str) -> str:    """为给定的任务 ID 分配优先级（P0、P1、P2）。"""    if priority not in ["P0", "P1", "P2"]:        return "优先级无效。必须是 P0、P1 或 P2。"    task = task_manager.update_task(task_id, priority=priority)    return f"已为任务 {task.id} 分配优先级 {priority}。" if task else f"未找到任务 {task_id}。" def assign_task_to_worker_tool(task_id: str, worker_name: str) -> str:    """将任务分配给特定的工作人员。"""    task = task_manager.update_task(task_id, assigned_to=worker_name)    return f"已将任务 {task.id} 分配给 {worker_name}。" if task else f"未找到任务 {task_id}。" # PM Agent 可以使用的所有工具 pm_tools = [    Tool(        name="create_new_task",        func=create_new_task_tool,        description="首先使用此工具创建一个新任务并获取其 ID。",        args_schema=CreateTaskArgs    ),    Tool(        name="assign_priority_to_task",        func=assign_priority_to_task_tool,        description="使用此工具在创建任务后为其分配优先级。",        args_schema=PriorityArgs    ),    Tool(        name="assign_task_to_worker",        func=assign_task_to_worker_tool,        description="使用此工具在创建任务后将其分配给特定的工作人员。",        args_schema=AssignWorkerArgs    ),    Tool(        name="list_all_tasks",        func=task_manager.list_all_tasks,        description="使用此工具列出所有当前任务及其状态。"    ), ] # --- 3. 项目管理 Agent 定义 --- pm_prompt_template = ChatPromptTemplate.from_messages([    ("system", """你是一个专注的项目管理 LLM Agent。你的目标是高效地管理项目任务。       当你收到新的任务请求时，遵循以下步骤：    1.  首先，使用 `create_new_task` 工具创建具有给定描述的任务。你必须首先执行此操作以获取 `task_id`。    2.  接下来，分析用户的请求以查看是否提到了优先级或受让人。        - 如果提到优先级（例如，"紧急"、"ASAP"、"关键"），将其映射到 P0。使用 `assign_priority_to_task`。        - 如果提到工作人员，使用 `assign_task_to_worker`。    3.  如果缺少任何信息（优先级、受让人），你必须做出合理的默认分配（例如，分配 P1 优先级并分配给 'Worker A'）。    4.  一旦任务完全处理完毕，使用 `list_all_tasks` 显示最终状态。       可用的工作人员：'Worker A'、'Worker B'、'Review Team'    优先级级别：P0（最高）、P1（中等）、P2（最低）    """),    ("placeholder", "{chat_history}"),    ("human", "{input}"),    ("placeholder", "{agent_scratchpad}") ]) # 创建 Agent 执行器 pm_agent = create_react_agent(llm, pm_tools, pm_prompt_template) pm_agent_executor = AgentExecutor(    agent=pm_agent,    tools=pm_tools,    verbose=True,    handle_parsing_errors=True,    memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True) ) # --- 4. 简单交互流程 --- async def run_simulation():    print("--- 项目管理模拟 ---")    # 场景 1：处理新的紧急功能请求    print("\n[用户请求] 我需要尽快实现一个新的登录系统。它应该分配给 Worker B。")    await pm_agent_executor.ainvoke({"input": "创建一个实现新登录系统的任务。这很紧急，应该分配给 Worker B。"})    print("\n" + "-"*60 + "\n")    # 场景 2：处理细节较少的不太紧急的内容更新    print("[用户请求] 我们需要审查营销网站内容。")    await pm_agent_executor.ainvoke({"input": "管理一个新任务：审查营销网站内容。"})    print("\n--- 模拟完成 ---") # 运行模拟 if __name__ == "__main__":    asyncio.run(run_simulation())`` |
| :---- |

此代码使用 Python 和 LangChain 实现了一个简单的任务管理系统，旨在模拟由大型语言模型驱动的项目管理 Agent。

该系统采用 [`SuperSimpleTaskManager`](chapters/Chapter 20_ Prioritization.md:46) 类在内存中高效管理任务，利用字典结构实现快速数据检索。每个任务由 [`Task`](chapters/Chapter 20_ Prioritization.md:43) Pydantic 模型表示，该模型包含唯一标识符、描述性文本、可选的优先级级别（P0、P1、P2）和可选的受让人指定等属性。内存使用量根据任务类型、工作人员数量和其他因素而变化。任务管理器提供用于任务创建、任务修改和检索所有任务的方法。

Agent 通过一组定义的工具与任务管理器交互。这些工具促进新任务的创建、向任务分配优先级、将任务分配给人员以及列出所有任务。每个工具都被封装以与 [`SuperSimpleTaskManager`](chapters/Chapter 20_ Prioritization.md:46) 的实例交互。Pydantic 模型用于描述工具所需的参数，从而确保数据验证。

[`AgentExecutor`](chapters/Chapter 20_ Prioritization.md:104) 配置了语言模型、工具集和对话内存组件以保持上下文连续性。定义了特定的 [`ChatPromptTemplate`](chapters/Chapter 20_ Prioritization.md:92) 来指导 Agent 在项目管理角色中的行为。提示词指示 Agent 首先创建任务，随后根据指定分配优先级和人员，并以全面的任务列表结束。在缺少信息的情况下，提示词中规定了默认分配，例如 P1 优先级和 'Worker A'。

代码包含一个异步性质的模拟函数（[`run_simulation`](chapters/Chapter 20_ Prioritization.md:112)）来演示 Agent 的操作能力。模拟执行两个不同的场景：管理具有指定人员的紧急任务，以及管理具有最少输入的不太紧急的任务。由于在 [`AgentExecutor`](chapters/Chapter 20_ Prioritization.md:104) 中激活了 `verbose=True`，Agent 的行动和逻辑过程会输出到控制台。

# 一览

**定义（What）：** 在复杂环境中运行的 AI Agent 面临大量潜在行动、相互冲突的目标和有限的资源。如果没有明确的方法来确定下一步行动，这些 Agent 将面临效率低下和效果不佳的风险。这可能导致严重的操作延迟或完全无法完成主要目标。核心挑战是管理这一压倒性数量的选择，以确保 Agent 有目的性和逻辑性地行动。

**原因（Why）：** 优先级排序模式通过使 Agent 能够对任务和目标进行排序，为这个问题提供了标准化的解决方案。这是通过建立明确的标准（如紧急性、重要性、依赖关系和资源成本）来实现的。然后 Agent 根据这些标准评估每个潜在行动，以确定最关键和最及时的行动方案。这种 Agentic 能力允许系统动态适应不断变化的环境并有效管理受限资源。通过专注于最高优先级的项目，Agent 的行为变得更加智能、稳健，并与其战略目标保持一致。

**经验法则（Rule of thumb）：** 当 Agentic 系统必须在资源约束下自主管理多个（通常是相互冲突的）任务或目标，以在动态环境中有效运行时，使用优先级排序模式。

**视觉总结：**

**![][image1]**

图 1：优先级排序设计模式

# 关键要点

* 优先级排序使 AI Agent 能够在复杂的多方面环境中有效运作。
* Agent 利用既定标准（如紧急性、重要性和依赖关系）来评估和排序任务。
* 动态重新优先级排序允许 Agent 根据实时变化调整其操作焦点。
* 优先级排序发生在各个层面，包括总体战略目标和即时战术决策。
* 有效的优先级排序可提高 AI Agent 的效率和操作稳健性。

# 结论

总之，优先级排序模式是有效 Agentic AI 的基石，使系统能够有目的性和智能地应对动态环境的复杂性。它允许 Agent 自主评估大量相互冲突的任务和目标，对在哪里集中其有限资源做出合理的决策。这种 Agentic 能力超越了简单的任务执行，使系统能够充当主动的战略决策者。通过权衡紧急性、重要性和依赖关系等标准，Agent 展示了复杂的、类似人类的推理过程。

这种 Agentic 行为的关键特征是动态重新优先级排序，它赋予 Agent 在条件变化时实时调整其焦点的自主权。如代码示例所示，Agent 解释模糊的请求，自主选择和使用适当的工具，并逻辑地排列其行动以实现其目标。这种自我管理工作流程的能力是真正的 Agentic 系统与简单的自动化脚本的区别所在。最终，掌握优先级排序对于创建能够在任何复杂的实际场景中有效可靠地运行的稳健和智能 Agent 至关重要。

# 参考文献

1. Examining the Security of Artificial Intelligence in Project Management: A Case Study of AI-driven Project Scheduling and Resource Allocation in Information Systems Projects ; [https://www.irejournals.com/paper-details/1706160](https://www.irejournals.com/paper-details/1706160)   
2. AI-Driven Decision Support Systems in Agile Software Project Management: Enhancing Risk Mitigation and Resource Allocation; [https://www.mdpi.com/2079-8954/13/3/208](https://www.mdpi.com/2079-8954/13/3/208)  

[image1]: ../images/chapter-20/image1.png