import os
import shutil
from pathlib import Path

curr_root = Path('.').resolve()
# 输出目录，与当前目录同级
src_root = curr_root.parent / 'happy-llm'
out_root = curr_root.parent / 'happy-llm-colab'


for root, dirs, files in os.walk(src_root):
    if 'images' in dirs:
        images_dir = Path(root) / 'images'
        rel_path = images_dir.relative_to(src_root)
        out_images_dir = out_root / rel_path
        out_images_dir.mkdir(parents=True, exist_ok=True)
        for img_file in images_dir.iterdir():
            if img_file.is_file():
                shutil.copy2(img_file, out_images_dir / img_file.name)
                print(f'Copied: {img_file} -> {out_images_dir / img_file.name}')
