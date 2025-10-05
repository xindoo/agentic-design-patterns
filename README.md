![封面图](images/cover.png)

# Agentic Design Patterns（中文翻译项目）

## 👨‍💻 关于xindoo

**xindoo** - 本翻译项目的发起者和主要维护者

- **GitHub**: [xindoo](https://github.com/xindoo)
- **个人网站**: [zxs.io](https://zxs.io)
- **博客**：[xindoo](https://blog.csdn.net/xindoo)
- **个人简介**: 热衷于技术分享和开源贡献的开发者，专注于 AI 技术、系统架构、职业发展。 

## 📚 项目简介

本项目是《Agentic Design Patterns》一书的中文翻译项目。该书系统介绍了 AI Agent 系统的各种设计模式，涵盖从基础到高级的 21 个核心模式，以及多个附录章节。

## 🎯 关于本书

《Agentic Design Patterns》探讨了构建智能 AI Agent 系统的核心设计模式，包括：
- 提示链、路由、并行化等基础模式
- 反思、工具使用、规划等进阶模式
- 多智能体协作、记忆管理、知识检索等高级模式
- 安全防护、评估监控等实践模式

## 📖 目录结构

### 核心章节

1. [第1章：提示链（Prompt Chaining）](chapters/Chapter%201_%20Prompt%20Chaining.md)
2. [第2章：路由（Routing）](chapters/Chapter%202_%20Routing.md)
3. [第3章：并行化（Parallelization）](chapters/Chapter%203_%20Parallelization.md)
4. [第4章：反思（Reflection）](chapters/Chapter%204_%20Reflection.md)
5. [第5章：工具使用（Tool Use）](chapters/Chapter%205_%20Tool%20Use.md)
6. [第6章：规划（Planning）](chapters/Chapter%206_%20Planning.md)
7. [第7章：多智能体协作（Multi-Agent Collaboration）](chapters/Chapter%207_%20Multi-Agent%20Collaboration.md)
8. [第8章：记忆管理（Memory Management）](chapters/Chapter%208_%20Memory%20Management.md)
9. [第9章：学习与适应（Learning and Adaptation）](chapters/Chapter%209_%20Learning%20and%20Adaptation.md)
10. [第10章：模型上下文协议（Model Context Protocol）](chapters/Chapter%2010_%20Model%20Context%20Protocol%20(MCP).md)
11. [第11章：目标设定与监控（Goal Setting and Monitoring）](chapters/Chapter%2011_%20Goal%20Setting%20and%20Monitoring.md)
12. [第12章：异常处理与恢复（Exception Handling and Recovery）](chapters/Chapter%2012_%20Exception%20Handling%20and%20Recovery.md)
13. [第13章：人机协同（Human-in-the-Loop）](chapters/Chapter%2013_%20Human-in-the-Loop.md)
14. [第14章：知识检索（Knowledge Retrieval - RAG）](chapters/Chapter%2014_%20Knowledge%20Retrieval%20(RAG).md)
15. [第15章：智能体间通信（Inter-Agent Communication - A2A）](chapters/Chapter%2015_%20Inter-Agent%20Communication%20(A2A).md)
16. [第16章：资源感知优化（Resource-Aware Optimization）](chapters/Chapter%2016_%20Resource-Aware%20Optimization.md)
17. [第17章：推理技术（Reasoning Techniques）](chapters/Chapter%2017_%20Reasoning%20Techniques.md)
18. [第18章：安全防护模式（Guardrails/Safety Patterns）](chapters/Chapter%2018_%20Guardrails_Safety%20Patterns.md)
19. [第19章：评估与监控（Evaluation and Monitoring）](chapters/Chapter%2019_%20Evaluation%20and%20Monitoring.md)
20. [第20章：优先级排序（Prioritization）](chapters/Chapter%2020_%20Prioritization.md)
21. [第21章：探索与发现（Exploration and Discovery）](chapters/Chapter%2021_%20Exploration%20and%20Discovery.md)

### 附录章节

- [附录A：高级提示技术](chapters/Appendix%20A_%20Advanced%20Prompting%20Techniques.md)
- [附录B：AI 智能体交互：从 GUI 到真实世界环境](chapters/Appendix%20B%20-%20AI%20Agentic%20Interactions_%20From%20GUI%20to%20Real%20world%20environment.md)
- [附录C：智能体框架快速概览](chapters/Appendix%20C%20-%20Quick%20overview%20of%20Agentic%20Frameworks.md)
- [附录D：使用 AgentSpace 构建智能体（仅在线）](chapters/Appendix%20D%20-%20Building%20an%20Agent%20with%20AgentSpace%20(on-line%20only).md)
- [附录E：命令行上的 AI 智能体](chapters/Appendix%20E%20-%20AI%20Agents%20on%20the%20CLI.md)
- [附录F：深入探究：智能体推理引擎内部机制](chapters/Appendix%20F%20%20-%20Under%20the%20Hood_%20An%20Inside%20Look%20at%20the%20Agents'%20Reasoning%20Engines.md)
- [附录G：编程智能体](chapters/Appendix%20G%20-%20%20Coding%20agents.md)

### 其他内容

- [常见问题解答](chapters/Frequently%20Asked%20Questions_%20Agentic%20Design%20Patterns.md)
- [术语表](chapters/Glossary.md)
- [术语索引](chapters/Index%20of%20Terms.md)
- [总结](chapters/Conclusion.md)

## 📁 项目结构

```
agentic-design-patterns/
├── README.md                    # 项目说明文档（本文件）
├── TABLE_OF_CONTENTS.md         # 详细目录
├── CONTRIBUTING.md              # 贡献指南
├── translation-guide.md         # 翻译规范指南
├── progress.md                  # 翻译进度追踪
├── glossary.md                  # 术语对照表
├── PROJECT_STRUCTURE.md         # 项目结构说明
├── chapters/                    # 翻译后的章节目录
│   ├── Chapter 1_ Prompt Chaining.md
│   ├── Chapter 2_ Routing.md
│   └── ...                      # 其他章节
├── original/                    # 原文备份目录
│   ├── Chapter 1_ Prompt Chaining.md
│   └── ...                      # 原文章节
└── images/                      # 图片资源目录
    ├── cover.png                # 封面图片
    ├── chapter-1/               # 第1章图片
    ├── chapter-2/               # 第2章图片
    └── ...                      # 其他章节图片
```

## 🌐 在线访问

本项目已部署到 GitHub Pages，可以在线阅读：

**访问地址：** [https://xindoo.github.io/agentic-design-patterns/](https://xindoo.github.io/agentic-design-patterns/)


## � 翻译进度

查看详细翻译进度请参考 [progress.md](progress.md)

## 🤝 如何贡献

我们欢迎任何形式的贡献！参与方式：

1. **Fork 本仓库**
2. **创建特性分支** (`git checkout -b feature/translate-chapter-xx`)
3. **提交更改** (`git commit -am '完成第XX章翻译'`)
4. **推送分支** (`git push origin feature/translate-chapter-xx`)
5. **创建 Pull Request**

详细贡献指南请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)

## 📝 翻译规范

在开始翻译前，请仔细阅读 [translation-guide.md](translation-guide.md)，主要规范包括：

- **保持原文结构**：段落、标题层级保持一致
- **术语统一**：参考 [glossary.md](glossary.md) 中的术语对照表
- **代码保持原样**：代码示例、命令行等保持英文
- **图片路径**：确保图片引用路径正确指向 `images/` 目录
- **格式规范**：遵循 Markdown 格式规范
- **校对审核**：提交前进行自我校对

## 📚 相关资源

- [术语对照表](glossary.md) - 统一的技术术语翻译
- [翻译指南](translation-guide.md) - 详细的翻译规范和注意事项
- [项目结构说明](PROJECT_STRUCTURE.md) - 项目文件组织说明

## 📄 许可证

本翻译项目遵循原书的许可证条款。翻译内容仅供学习交流使用。

## 🌟 致谢

感谢所有参与翻译和审校的贡献者！

特别感谢项目创建者 **xindoo** 发起并维护这个重要的中文翻译项目，为中文技术社区带来优质的 AI Agent 设计模式知识。

---

**注意**：本项目为学习交流目的的翻译项目，如有版权问题请联系处理。