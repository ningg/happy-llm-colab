#!/bin/bash

# 1. 进入 happy-llm 目录并执行 git pull
cd ../happy-llm || { echo "目录 ../happy-llm 不存在"; exit 1; }
git pull origin main

# 2. 回到原来目录，执行 md2ipynb_out.py
cd - > /dev/null
python ./python/md2ipynb_out.py

# 3. 执行 copy_images_to_outipynb.py
python ./pythoncopy_images_to_outipynb.py

# 4. 执行 copy_ext_to_outipynb.py
python ./pythoncopy_ext_to_outipynb.py
