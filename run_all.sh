#!/bin/bash

# 判断当前目录名是否为 happy-llm-colab
current_dir=$(basename "$PWD")

if [ "$current_dir" = "happy-llm-colab" ]; then
    # 获取当前分支名
    current_branch=$(git rev-parse --abbrev-ref HEAD)
    if [ "$current_branch" != "auto-ipynb" ]; then
        echo "当前分支为 $current_branch，切换到 auto-ipynb 分支..."
        git checkout auto-ipynb || { echo "切换分支失败！"; exit 1; }
    else
        echo "当前已经在 auto-ipynb 分支。"
    fi
else
    echo "需要先前往目录 happy-llm-colab ，然后重新执行命令。"
    exit 1
fi


# 1. 进入 happy-llm 目录并执行 git pull
cd ../happy-llm || { echo "目录 ../happy-llm 不存在"; exit 1; }
git pull origin main

# 2. 回到原来目录，执行 md2ipynb_out.py
cd - > /dev/null
python ./python/md2ipynb_out.py

# 3. 执行 copy_images_to_outipynb.py
python ./python/copy_images_to_outipynb.py

# 4. 执行 copy_ext_to_outipynb.py
python ./python/copy_ext_to_outipynb.py

# 5. 替换 md 链接
python python/replace_readme_md_to_ipynb.py
