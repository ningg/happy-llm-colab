import os
import nbformat
from pathlib import Path

# 当前目录
curr_root = Path('.').resolve()
# 输出目录，与当前目录同级
src_root = curr_root.parent / 'happy-llm'
out_root = curr_root.parent / 'happy-llm-colab'

def md_to_ipynb(md_path, ipynb_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    nb = nbformat.v4.new_notebook()
    nb['cells'] = [nbformat.v4.new_markdown_cell(md_content)]
    # 确保输出子目录存在
    ipynb_path.parent.mkdir(parents=True, exist_ok=True)
    with open(ipynb_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

for root, dirs, files in os.walk(src_root):
    for file in files:
        if file.endswith('.md'):
            md_file = Path(root) / file
            rel_path = md_file.relative_to(src_root)
            ipynb_file = out_root / rel_path.with_suffix('.ipynb')
            md_to_ipynb(md_file, ipynb_file)
            print(f'Converted: {md_file} -> {ipynb_file}')
