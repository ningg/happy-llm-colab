import os
import nbformat
from pathlib import Path
import re

# 当前目录
curr_root = Path('.').resolve()
# 输出目录，与当前目录同级
src_root = curr_root.parent / 'happy-llm'
out_root = curr_root.parent / 'happy-llm-colab'


# 核心转换逻辑
def md_to_ipynb(md_path, ipynb_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cells = []
    in_code_block = False
    code_block_lang = ''
    code_lines = []
    md_lines = []

    code_block_pattern = re.compile(r'^```(\w*)')
    code_block_end_pattern = re.compile(r'^```$')

    for line in lines:
        code_block_start = code_block_pattern.match(line)
        code_block_end = code_block_end_pattern.match(line)

        if not in_code_block and code_block_start:
            # 进入代码块
            in_code_block = True
            code_block_lang = code_block_start.group(1)
            # 若有之前的 md 段落，先存为 md 单元
            if md_lines:
                cells.append(nbformat.v4.new_markdown_cell(''.join(md_lines).rstrip()))
                md_lines = []
            code_lines = []
        elif in_code_block and code_block_end:
            # 结束代码块
            in_code_block = False
            cells.append(
                nbformat.v4.new_code_cell(''.join(code_lines).rstrip(),
                                         metadata={"language": code_block_lang} if code_block_lang else {}))
            code_lines = []
            code_block_lang = ''
        elif in_code_block:
            code_lines.append(line)
        else:
            md_lines.append(line)

    # 文件结尾剩余 md 作为 markdown 单元
    if md_lines:
        cells.append(nbformat.v4.new_markdown_cell(''.join(md_lines).rstrip()))

    nb = nbformat.v4.new_notebook()
    nb['cells'] = cells

    ipynb_path.parent.mkdir(parents=True, exist_ok=True)
    with open(ipynb_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)


# 逐个文件处理.
for root, dirs, files in os.walk(src_root):
    for file in files:
        if file.endswith('.md'):
            md_file = Path(root) / file
            rel_path = md_file.relative_to(src_root)
            ipynb_file = out_root / rel_path.with_suffix('.ipynb')
            md_to_ipynb(md_file, ipynb_file)
            print(f'Converted: {md_file} -> {ipynb_file}')
