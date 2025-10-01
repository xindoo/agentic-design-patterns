# 项目结构说明

```
agentic-design-patterns/
│
├── README.md                 # 项目主说明文档
├── CONTRIBUTING.md          # 贡献指南
├── translation-guide.md     # 翻译指南
├── progress.md              # 翻译进度追踪
├── glossary.md              # 术语对照表
├── TABLE_OF_CONTENTS.md     # 全书目录
├── PROJECT_STRUCTURE.md     # 本文件 - 项目结构说明
├── .gitignore               # Git 忽略文件配置
│
├── chapters/                # 翻译后的章节目录
│   ├── README.md            # 章节目录说明
│   ├── chapter-01.md        # 第1章（待添加原文后翻译）
│   ├── chapter-02.md        # 第2章
│   ├── ...                  # 第3-24章
│   └── chapter-25.md        # 第25章
│
├── original/                # 原文备份目录
│   ├── README.md            # 原文目录说明
│   ├── chapter-01.md        # 原文第1章（待添加）
│   ├── ...                  # 其他原文章节
│   └── chapter-25.md        # 原文第25章
│
├── images/                  # 图片资源目录
│   ├── README.md            # 图片目录说明
│   ├── common/              # 公共图片资源
│   ├── chapter-1/           # 第1章图片
│   ├── chapter-2/           # 第2章图片
│   ├── ...                  # 第3-24章图片目录
│   └── chapter-25/          # 第25章图片
│
└── assets/                  # 其他资源文件目录
    └── README.md            # 资源目录说明

```

## 目录说明

### 根目录文件

- **README.md**: 项目总体介绍，包括项目简介、结构、贡献方式等
- **CONTRIBUTING.md**: 详细的贡献指南，包括翻译规范、工作流程、审核标准
- **translation-guide.md**: 翻译指南，包括翻译原则、格式规范、术语对照
- **progress.md**: 翻译进度追踪表，记录每章的翻译状态和负责人
- **glossary.md**: 术语对照表，统一专业术语的翻译
- **TABLE_OF_CONTENTS.md**: 全书目录，包含所有章节链接
- **.gitignore**: Git 版本控制忽略文件配置

### 核心目录

1. **chapters/**: 存放翻译后的中文章节
   - 每个文件对应一章内容
   - 命名格式：`chapter-XX.md`（XX 为 01-25）
   
2. **original/**: 存放英文原文
   - 便于翻译时对照参考
   - 保持与 chapters 相同的命名结构

3. **images/**: 存放所有图片资源
   - `common/`: 公共图片（logo、通用图标等）
   - `chapter-XX/`: 各章节专用图片
   
4. **assets/**: 其他资源文件
   - 可存放字体、样式、脚本等辅助文件

## 使用流程

1. **准备阶段**
   - 将原书的英文章节文件放入 `original/` 目录
   - 将原书的图片按章节分类放入对应的 `images/chapter-XX/` 目录

2. **翻译阶段**
   - 在 Issues 中认领要翻译的章节
   - 参考 `original/` 中的原文进行翻译
   - 将翻译结果保存到 `chapters/` 目录
   - 更新图片引用路径

3. **审核阶段**
   - 提交 Pull Request
   - 其他贡献者审核翻译质量
   - 根据反馈修改完善

4. **完成阶段**
   - PR 合并后更新 `progress.md`
   - 继续下一章节的翻译

## 注意事项

- 所有 Markdown 文件使用 UTF-8 编码
- 图片引用使用相对路径
- 保持目录结构清晰有序
- 及时更新进度文件