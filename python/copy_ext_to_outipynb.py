import os
import shutil
from pathlib import Path

# 设置需要复制的文件后缀，可以修改或增加后缀
EXTS = ['.py', '.txt', '.sh', '.json']  # 你可以修改为任意后缀列表，如 ['.py', '.csv']

# 当前目录
curr_root = Path('.').resolve()
# 输出目录，与当前目录同级
src_root = curr_root.parent / 'happy-llm'
out_root = curr_root.parent / 'happy-llm-colab'

for root, dirs, files in os.walk(src_root):
    for file in files:
        if any(file.endswith(ext) for ext in EXTS):
            src_file = Path(root) / file
            rel_path = src_file.relative_to(src_root)
            dst_file = out_root / rel_path
            dst_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_file, dst_file)
            print(f'Copied: {src_file} -> {dst_file}')
