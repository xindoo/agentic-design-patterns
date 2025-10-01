# 图片资源目录

本目录用于存放书籍中使用的所有图片资源。

## 目录结构

- `common/` - 公共图片资源（如 logo、图标等）
- `chapter-XX/` - 各章节的图片资源（01-25）

## 文件命名规范

- 使用英文命名，小写字母，单词间用连字符分隔
- 格式：`descriptive-name.png` 或 `.jpg` 等
- 示例：`architecture-diagram.png`、`code-example-01.png`

## 图片格式

- 优先使用 PNG 格式（透明背景、高质量）
- 照片类图片可使用 JPG 格式
- 图表建议使用 SVG 格式（可缩放）

## 引用方式

在 Markdown 文件中引用图片：

```markdown
![图片描述](../images/chapter-01/example-image.png)
```

## 注意事项

- 图片文件大小尽量控制在合理范围内
- 确保图片清晰度适合阅读
- 如图片包含文字需要翻译，请创建中文版本