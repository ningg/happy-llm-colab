import os
from pathlib import Path


# 当前目录
curr_root = Path('.').resolve()
# 输出目录，与当前目录同级
src_root = curr_root.parent / 'happy-llm'
out_root = curr_root.parent / 'happy-llm-colab'

for root, dirs, files in os.walk(out_root):
    for file in files:
        if file.startswith('README'):
            file_path = Path(root) / file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = content.replace('.md)', '.ipynb)')
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Processed: {file_path}")
