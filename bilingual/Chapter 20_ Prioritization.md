# Chapter 20: Prioritization

# 第 20 章：优先级排序

In complex, dynamic environments, Agents frequently encounter numerous potential actions, conflicting goals, and limited resources. Without a defined process for determining the subsequent action, the agents may experience reduced efficiency, operational delays, or failures to achieve key objectives. The prioritization pattern addresses this issue by enabling agents to assess and rank tasks, objectives, or actions based on their significance, urgency, dependencies, and established criteria. This ensures the agents concentrate efforts on the most critical tasks, resulting in enhanced effectiveness and goal alignment.

## Prioritization Pattern Overview

## 优先级排序模式概述

Agents employ prioritization to effectively manage tasks, goals, and sub-goals, guiding subsequent actions. This process facilitates informed decision-making when addressing multiple demands, prioritizing vital or urgent activities over less critical ones. It is particularly relevant in real-world scenarios where resources are constrained, time is limited, and objectives may conflict.

智能体使用优先级排序来有效管理任务、目标和子目标，指导后续行动。这个过程有助于在处理多个需求时做出明智决策，优先处理重要或紧急的活动，而不是次要的活动。这在资源受限、时间有限以及目标可能冲突的实际场景中尤为重要。

The fundamental aspects of agent prioritization typically involve several elements. First, criteria definition establishes the rules or metrics for task evaluation. These may include urgency (time sensitivity of the task), importance (impact on the primary objective), dependencies (whether the task is a prerequisite for others), resource availability (readiness of necessary tools or information), cost/benefit analysis (effort versus expected outcome), and user preferences for personalized agents. Second, task evaluation involves assessing each potential task against these defined criteria, utilizing methods ranging from simple rules to complex scoring or reasoning by LLMs. Third, scheduling or selection logic refers to the algorithm that, based on the evaluations, selects the optimal next action or task sequence, potentially utilizing a queue or an advanced planning component. Finally, dynamic re-prioritization allows the agent to modify priorities as circumstances change, such as the emergence of a new critical event or an approaching deadline, ensuring agent adaptability and responsiveness.

智能体优先级排序通常包含几个核心要素。首先是**标准定义**，即建立任务评估的规则或指标，这些标准可能包括：紧急性（任务的时间敏感性）、重要性（对主要目标的影响）、依赖关系（该任务是否是其他任务的前提）、资源可用性（必要工具或信息的就绪状态）、成本/收益分析（投入与预期成果的对比），以及面向个性化智能体的用户偏好。其次是**任务评估**，即根据上述标准评估每个潜在任务，评估方法可以从简单规则到大语言模型的复杂评分或推理。第三是**调度或选择逻辑**，即基于评估结果选择最佳下一步行动或任务序列的算法，可能使用队列或高级规划组件。最后是**动态重新优先级排序**，允许智能体根据情况变化（如新关键事件出现或截止日期临近）调整优先级，确保智能体的适应性和响应能力。

Prioritization can occur at various levels: selecting an overarching objective (high-level goal prioritization), ordering steps within a plan (sub-task prioritization), or choosing the next immediate action from available options (action selection). Effective prioritization enables agents to exhibit more intelligent, efficient, and robust behavior, especially in complex, multi-objective environments. This mirrors human team organization, where managers prioritize tasks by considering input from all members.

优先级排序可以在各个层面进行：选择总体目标（高层次目标优先级排序）、在计划内排序步骤（子任务优先级排序）或从可用选项中选择下一个即时行动（行动选择）。有效的优先级排序使智能体展现更智能、更高效、更稳健的行为，特别是在复杂的多目标环境中。这反映了人类团队的组织方式，其中管理者通过考虑所有成员的输入来优先处理任务。

## Practical Applications & Use Cases

## 实际应用和用例

In various real-world applications, AI agents demonstrate a sophisticated use of prioritization to make timely and effective decisions.

在各种实际应用中，AI 智能体展现了优先级排序的复杂运用，以做出及时有效的决策。

* **Automated Customer Support**: Agents prioritize urgent requests, like system outage reports, over routine matters, such as password resets. They may also give preferential treatment to high-value customers.  
* **Cloud Computing**: AI manages and schedules resources by prioritizing allocation to critical applications during peak demand, while relegating less urgent batch jobs to off-peak hours to optimize costs.  
* **Autonomous Driving Systems**: Continuously prioritize actions to ensure safety and efficiency. For example, braking to avoid a collision takes precedence over maintaining lane discipline or optimizing fuel efficiency.  
* **Financial Trading**: Bots prioritize trades by analyzing factors like market conditions, risk tolerance, profit margins, and real-time news, enabling prompt execution of high-priority transactions.  
* **Project Management**: AI agents prioritize tasks on a project board based on deadlines, dependencies, team availability, and strategic importance.  
* **Cybersecurity**: Agents monitoring network traffic prioritize alerts by assessing threat severity, potential impact, and asset criticality, ensuring immediate responses to the most dangerous threats.  
* **Personal Assistant AIs**: Utilize prioritization to manage daily lives, organizing calendar events, reminders, and notifications according to user-defined importance, upcoming deadlines, and current context.

* **自动化客户支持**：智能体优先处理紧急请求，如系统停机报告，而不是日常事务，如密码重置。他们还可能优先处理高价值客户。
* **云计算**：AI 通过优先将资源分配给高峰需求期间的关键应用程序来管理和调度资源，同时将不太紧急的批处理作业推迟到非高峰时段以优化成本。
* **自动驾驶系统**：持续优先处理行动以确保安全和效率。例如，为避免碰撞而刹车优先于保持车道纪律或优化燃油效率。
* **金融交易**：交易机器人通过分析市场条件、风险承受能力、利润率和实时新闻等因素来优先处理交易，实现高优先级交易的快速执行。
* **项目管理**：AI 智能体根据截止日期、依赖关系、团队可用性和战略重要性来优先处理项目板上的任务。
* **网络安全**：监控网络流量的智能体根据威胁严重性、潜在影响和资产关键性来优先处理警报，确保对最危险威胁的即时响应。
* **个人助理 AI**：利用优先级排序来管理日常生活，根据用户定义的重要性、即将到来的截止日期和当前上下文来组织日历事件、提醒和通知。

These examples collectively illustrate how the ability to prioritize is fundamental to the enhanced performance and decision-making capabilities of AI agents across a wide spectrum of situations.

这些示例共同说明了优先级排序能力对于增强 AI 智能体在各种情况下的性能和决策能力是多么基础。

## Hands-On Code Example

## 实践代码示例

The following demonstrates the development of a Project Manager AI agent using LangChain. This agent facilitates the creation, prioritization, and assignment of tasks to team members, illustrating the application of large language models with bespoke tools for automated project management.

以下演示了使用 LangChain 开发项目管理 AI 智能体。该智能体负责任务的创建、优先级排序和分配给团队成员，说明了大语言模型与定制工具在自动化项目管理中的应用。

```python
import os
import asyncio
from typing import List, Optional, Dict, Type
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.memory import ConversationBufferMemory

## --- 0. Configuration and Setup ---
## Loads the OPENAI_API_KEY from the .env file.
load_dotenv()

## The ChatOpenAI client automatically picks up the API key from the environment.
llm = ChatOpenAI(temperature=0.5, model="gpt-4o-mini")

## --- 1. Task Management System ---
class Task(BaseModel):
    """Represents a single task in the system."""
    id: str
    description: str
    priority: Optional[str] = None  # P0, P1, P2
    assigned_to: Optional[str] = None # Name of the worker

class SuperSimpleTaskManager:
    """An efficient and robust in-memory task manager."""
    def __init__(self):
        # Use a dictionary for O(1) lookups, updates, and deletions.
        self.tasks: Dict[str, Task] = {}
        self.next_task_id = 1

    def create_task(self, description: str) -> Task:
        """Creates and stores a new task."""
        task_id = f"TASK-{self.next_task_id:03d}"
        new_task = Task(id=task_id, description=description)
        self.tasks[task_id] = new_task
        self.next_task_id += 1
        print(f"DEBUG: Task created - {task_id}: {description}")
        return new_task

    def update_task(self, task_id: str, **kwargs) -> Optional[Task]:
        """Safely updates a task using Pydantic's model_copy."""
        task = self.tasks.get(task_id)
        if task:
            # Use model_copy for type-safe updates.
            update_data = {k: v for k, v in kwargs.items() if v is not None}
            updated_task = task.model_copy(update=update_data)
            self.tasks[task_id] = updated_task
            print(f"DEBUG: Task {task_id} updated with {update_data}")
            return updated_task
        print(f"DEBUG: Task {task_id} not found for update.")
        return None

    def list_all_tasks(self) -> str:
        """Lists all tasks currently in the system."""
        if not self.tasks:
            return "No tasks in the system."
        task_strings = []
        for task in self.tasks.values():
            task_strings.append(
                f"ID: {task.id}, Desc: '{task.description}', "
                f"Priority: {task.priority or 'N/A'}, "
                f"Assigned To: {task.assigned_to or 'N/A'}"
            )
        return "Current Tasks:\n" + "\n".join(task_strings)

task_manager = SuperSimpleTaskManager()

## --- 2. Tools for the Project Manager Agent ---
## Use Pydantic models for tool arguments for better validation and clarity.
class CreateTaskArgs(BaseModel):
    description: str = Field(description="A detailed description of the task.")

class PriorityArgs(BaseModel):
    task_id: str = Field(description="The ID of the task to update, e.g., 'TASK-001'.")
    priority: str = Field(description="The priority to set. Must be one of: 'P0', 'P1', 'P2'.")

class AssignWorkerArgs(BaseModel):
    task_id: str = Field(description="The ID of the task to update, e.g., 'TASK-001'.")
    worker_name: str = Field(description="The name of the worker to assign the task to.")

def create_new_task_tool(description: str) -> str:
    """Creates a new project task with the given description."""
    task = task_manager.create_task(description)
    return f"Created task {task.id}: '{task.description}'."

def assign_priority_to_task_tool(task_id: str, priority: str) -> str:
    """Assigns a priority (P0, P1, P2) to a given task ID."""
    if priority not in ["P0", "P1", "P2"]:
        return "Invalid priority. Must be P0, P1, or P2."
    task = task_manager.update_task(task_id, priority=priority)
    return f"Assigned priority {priority} to task {task.id}." if task else f"Task {task_id} not found."

def assign_task_to_worker_tool(task_id: str, worker_name: str) -> str:
    """Assigns a task to a specific worker."""
    task = task_manager.update_task(task_id, assigned_to=worker_name)
    return f"Assigned task {task.id} to {worker_name}." if task else f"Task {task_id} not found."

## All tools the PM agent can use
pm_tools = [
    Tool(
        name="create_new_task",
        func=create_new_task_tool,
        description="Use this first to create a new task and get its ID.",
        args_schema=CreateTaskArgs
    ),
    Tool(
        name="assign_priority_to_task",
        func=assign_priority_to_task_tool,
        description="Use this to assign a priority to a task after it has been created.",
        args_schema=PriorityArgs
    ),
    Tool(
        name="assign_task_to_worker",
        func=assign_task_to_worker_tool,
        description="Use this to assign a task to a specific worker after it has been created.",
        args_schema=AssignWorkerArgs
    ),
    Tool(
        name="list_all_tasks",
        func=task_manager.list_all_tasks,
        description="Use this to list all current tasks and their status."
    ),
]

## --- 3. Project Manager Agent Definition ---
pm_prompt_template = ChatPromptTemplate.from_messages([
    ("system", """You are a focused Project Manager LLM agent. Your goal is to manage project tasks efficiently.
       When you receive a new task request, follow these steps:
    1.  First, create the task with the given description using the `create_new_task` tool. You must do this first to get a `task_id`.
    2.  Next, analyze the user's request to see if a priority or an assignee is mentioned.
        - If a priority is mentioned (e.g., "urgent", "ASAP", "critical"), map it to P0. Use `assign_priority_to_task`.
        - If a worker is mentioned, use `assign_task_to_worker`.
    3.  If any information (priority, assignee) is missing, you must make a reasonable default assignment (e.g., assign P1 priority and assign to 'Worker A').
    4.  Once the task is fully processed, use `list_all_tasks` to show the final state.
       Available workers: 'Worker A', 'Worker B', 'Review Team'
    Priority levels: P0 (highest), P1 (medium), P2 (lowest)
    """),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

## Create the agent executor
pm_agent = create_react_agent(llm, pm_tools, pm_prompt_template)
pm_agent_executor = AgentExecutor(
    agent=pm_agent,
    tools=pm_tools,
    verbose=True,
    handle_parsing_errors=True,
    memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True)
)

## --- 4. Simple Interaction Flow ---
async def run_simulation():
    print("--- Project Manager Simulation ---")
    # Scenario 1: Handle a new, urgent feature request
    print("\n[User Request] I need a new login system implemented ASAP. It should be assigned to Worker B.")
    await pm_agent_executor.ainvoke({"input": "Create a task to implement a new login system. It's urgent and should be assigned to Worker B."})
    print("\n" + "-"*60 + "\n")

    # Scenario 2: Handle a less urgent content update with fewer details
    print("[User Request] We need to review the marketing website content.")
    await pm_agent_executor.ainvoke({"input": "Manage a new task: Review marketing website content."})
    print("\n--- Simulation Complete ---")

## Run the simulation
if __name__ == "__main__":
    asyncio.run(run_simulation())
```

This code implements a simple task management system using Python and LangChain, designed to simulate a project manager agent powered by a large language model.

此代码使用 Python 和 LangChain 实现了一个简单的任务管理系统，旨在模拟由大语言模型驱动的项目管理智能体。

The system employs a SuperSimpleTaskManager class to efficiently manage tasks within memory, utilizing a dictionary structure for rapid data retrieval. Each task is represented by a Task Pydantic model, which encompasses attributes such as a unique identifier, a descriptive text, an optional priority level (P0, P1, P2), and an optional assignee designation. Memory usage varies based on task type, the number of workers, and other contributing factors. The task manager provides methods for task creation, task modification, and retrieval of all tasks.

该系统采用 `SuperSimpleTaskManager` 类在内存中高效管理任务，利用字典结构实现快速数据检索。每个任务由 `Task` Pydantic 模型表示，包含唯一标识符、描述文本、可选优先级级别（P0、P1、P2）和可选的受让人指定等属性。内存使用量会根据任务类型、工作人员数量等因素而变化。任务管理器提供任务创建、任务修改和检索所有任务的方法。

The agent interacts with the task manager via a defined set of Tools. These tools facilitate the creation of new tasks, the assignment of priorities to tasks, the allocation of tasks to personnel, and the listing of all tasks. Each tool is encapsulated to enable interaction with an instance of the SuperSimpleTaskManager. Pydantic models are utilized to delineate the requisite arguments for the tools, thereby ensuring data validation.

智能体通过一组定义好的工具与任务管理器交互。这些工具支持创建新任务、为任务分配优先级、将任务分配给人员以及列出所有任务。每个工具都被封装为与 `SuperSimpleTaskManager` 的实例交互。Pydantic 模型用于描述工具所需的参数，从而确保数据验证。

An AgentExecutor is configured with the language model, the toolset, and a conversation memory component to maintain contextual continuity. A specific ChatPromptTemplate is defined to direct the agent's behavior in its project management role. The prompt instructs the agent to initiate by creating a task, subsequently assigning priority and personnel as specified, and concluding with a comprehensive task list. Default assignments, such as P1 priority and 'Worker A', are stipulated within the prompt for instances where information is absent.

`AgentExecutor` 配置了语言模型、工具集和对话内存组件以保持上下文连续性。定义了特定的 `ChatPromptTemplate` 来指导智能体在项目管理角色中的行为。提示词指示智能体先创建任务，然后根据指定分配优先级和人员，最后以完整的任务列表结束。当信息缺失时，提示词中规定了默认分配，例如 P1 优先级和 'Worker A'。

The code incorporates a simulation function (run\_simulation) of asynchronous nature to demonstrate the agent's operational capacity. The simulation executes two distinct scenarios: the management of an urgent task with designated personnel, and the management of a less urgent task with minimal input. The agent's actions and logical processes are outputted to the console due to the activation of verbose=True within the AgentExecutor.

代码包含一个异步模拟函数（`run_simulation`）来演示智能体的运行能力。模拟执行两个不同的场景：管理带有指定人员的紧急任务，以及管理输入信息较少的非紧急任务。由于在 `AgentExecutor` 中启用了 `verbose=True`，智能体的行动和逻辑过程会输出到控制台。

## At a Glance

## 速览

**What:** AI agents operating in complex environments face a multitude of potential actions, conflicting goals, and finite resources. Without a clear method to determine their next move, these agents risk becoming inefficient and ineffective. This can lead to significant operational delays or a complete failure to accomplish primary objectives. The core challenge is to manage this overwhelming number of choices to ensure the agent acts purposefully and logically.

**问题背景：** 在复杂环境中运行的 AI 智能体面临大量潜在行动、相互冲突的目标和有限的资源。如果没有明确的方法来确定下一步行动，这些智能体可能会变得低效且效果不佳，甚至导致严重的操作延迟或完全无法完成主要目标。核心挑战是管理这一数量庞大的选择，确保智能体有目的地、合乎逻辑地行动。

**Why:** The Prioritization pattern provides a standardized solution for this problem by enabling agents to rank tasks and goals. This is achieved by establishing clear criteria such as urgency, importance, dependencies, and resource cost. The agent then evaluates each potential action against these criteria to determine the most critical and timely course of action. This Agentic capability allows the system to dynamically adapt to changing circumstances and manage constrained resources effectively. By focusing on the highest-priority items, the agent's behavior becomes more intelligent, robust, and aligned with its strategic goals.

**解决方案：** 优先级排序模式通过使智能体对任务和目标进行排序，为这个问题提供了标准化的解决方案。这是通过建立明确的标准（如紧急性、重要性、依赖关系和资源成本）来实现的。然后智能体根据这些标准评估每个潜在行动，以确定最关键、最及时的行动方案。这种智能体能力使系统能够动态适应不断变化的环境，并有效管理受限资源。通过专注于最高优先级的项目，智能体的行为变得更加智能、稳健，并与其战略目标保持一致。

**Rule of thumb:** Use the Prioritization pattern when an Agentic system must autonomously manage multiple, often conflicting, tasks or goals under resource constraints to operate effectively in a dynamic environment.

**实践建议：** 当智能体系统必须在资源约束下自主管理多个（通常是相互冲突的）任务或目标，以在动态环境中有效运行时，使用优先级排序模式。

**Visual summary:**

**可视化摘要：**

![][image1]

图 1：优先级排序设计模式

## Key Takeaways

## 关键要点

* Prioritization enables AI agents to function effectively in complex, multi-faceted environments.  
* Agents utilize established criteria such as urgency, importance, and dependencies to evaluate and rank tasks.  
* Dynamic re-prioritization allows agents to adjust their operational focus in response to real-time changes.   
* Prioritization occurs at various levels, encompassing overarching strategic objectives and immediate tactical decisions.   
* Effective prioritization results in increased efficiency and improved operational robustness of AI agents.

* 优先级排序使 AI 智能体在复杂的多方面环境中有效运作。
* 智能体根据既定标准（如紧急性、重要性和依赖关系）来评估和排序任务。
* 动态重新优先级排序允许智能体根据实时变化调整其操作焦点。
* 优先级排序发生在各个层面，包括总体战略目标和即时战术决策。
* 有效的优先级排序可提高 AI 智能体效率和操作稳健性。

## Conclusions

## 结论

In conclusion, the prioritization pattern is a cornerstone of effective agentic AI, equipping systems to navigate the complexities of dynamic environments with purpose and intelligence. It allows an agent to autonomously evaluate a multitude of conflicting tasks and goals, making reasoned decisions about where to focus its limited resources. This agentic capability moves beyond simple task execution, enabling the system to act as a proactive, strategic decision-maker. By weighing criteria such as urgency, importance, and dependencies, the agent demonstrates a sophisticated, human-like reasoning process.

总之，优先级排序模式是有效智能体 AI 的基石，使系统能够有目的地、智能地应对动态环境的复杂性。它允许智能体评估大量相互冲突的任务和目标，对在哪里集中其有限资源做出合理的决策。这种智能体能力超越了简单的任务执行，使系统能够充当主动的战略决策者。通过权衡紧急性、重要性和依赖关系等标准，智能体展现了复杂的、类似人类的推理过程。

A key feature of this agentic behavior is dynamic re-prioritization, which grants the agent the autonomy to adapt its focus in real-time as conditions change. As demonstrated in the code example, the agent interprets ambiguous requests, autonomously selects and uses the appropriate tools, and logically sequences its actions to fulfill its objectives. This ability to self-manage its workflow is what separates a true agentic system from a simple automated script. Ultimately, mastering prioritization is fundamental for creating robust and intelligent agents that can operate effectively and reliably in any complex, real-world scenario.

这种智能体行为的一个关键特征是动态重新优先级排序，它赋予智能体在条件变化时实时调整关注点的自主权。如代码示例所示，智能体解释模糊的请求，自主选择和使用适当的工具，并逻辑地排列其行动以实现目标。这种自我管理工作流程的能力，正是真正的智能体系统与简单自动化脚本的区别所在。最终，掌握优先级排序对于创建能够在任何复杂的实际场景中有效、可靠运行的稳健且智能的智能体至关重要。

## References

## 参考文献

1. Examining the Security of Artificial Intelligence in Project Management: A Case Study of AI-driven Project Scheduling and Resource Allocation in Information Systems Projects ; [https://www.irejournals.com/paper-details/1706160](https://www.irejournals.com/paper-details/1706160)
2. AI-Driven Decision Support Systems in Agile Software Project Management: Enhancing Risk Mitigation and Resource Allocation; [https://www.mdpi.com/2079-8954/13/3/208](https://www.mdpi.com/2079-8954/13/3/208)

[image1]: ../images/chapter-20/image1.png
