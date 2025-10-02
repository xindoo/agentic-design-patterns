#!/usr/bin/env python3
"""
处理 Markdown 文件中的 LaTeX 特殊字符
在非代码块区域转义特殊字符，保持代码块内容不变
"""
import sys


def escape_outside_code_blocks(text):
    """
    在非代码块部分转义 LaTeX 特殊字符
    """
    # 分割文本为代码块和非代码块部分
    parts = []
    in_code_block = False
    lines = text.split('\n')
    current_block = []
    
    for line in lines:
        if line.strip().startswith('```'):
            if current_block:
                parts.append((in_code_block, '\n'.join(current_block)))
                current_block = []
            in_code_block = not in_code_block
            current_block.append(line)
        else:
            current_block.append(line)
    
    if current_block:
        parts.append((in_code_block, '\n'.join(current_block)))
    
    # 在非代码块部分转义特殊字符
    result = []
    for is_code, block in parts:
        if not is_code:
            # 转义 LaTeX 特殊字符
            block = block.replace('\\', '\\textbackslash{}')
            block = block.replace('_', '\\_')
            block = block.replace('{', '\\{')
            block = block.replace('}', '\\}')
            block = block.replace('%', '\\%')
            block = block.replace('&', '\\&')
            block = block.replace('#', '\\#')
        result.append(block)
    
    return '\n'.join(result)


def main():
    if len(sys.argv) != 2:
        print("Usage: process_latex_chars.py <markdown_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # 读取文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 处理内容
    processed = escape_outside_code_blocks(content)
    
    # 写回文件
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(processed)
    
    print(f"Successfully processed {input_file}")


if __name__ == '__main__':
    main()