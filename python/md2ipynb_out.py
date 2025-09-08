import os
import nbformat
from pathlib import Path
import re
import json

# 当前目录
curr_root = Path('.').resolve()
# 输出目录，与当前目录同级
src_root = curr_root.parent / 'happy-llm'
out_root = curr_root.parent / 'happy-llm-colab'


def get_existing_cell_ids(ipynb_path):
    """从现有的ipynb文件中获取cell ID，如果文件不存在则返回None"""
    if ipynb_path.exists():
        try:
            with open(ipynb_path, 'r', encoding='utf-8') as f:
                nb = json.load(f)
                if 'cells' in nb:
                    return [cell.get('id', None) for cell in nb['cells']]
        except:
            pass
    return None


def create_cell_with_id(cell_type, source, cell_id=None, **kwargs):
    """创建带有指定ID的cell"""
    if cell_type == 'markdown':
        cell = nbformat.v4.new_markdown_cell(source, **kwargs)
    elif cell_type == 'code':
        cell = nbformat.v4.new_code_cell(source, **kwargs)
    else:
        cell = nbformat.v4.new_raw_cell(source, **kwargs)
    
    # 如果提供了ID，则使用它；否则使用默认的随机ID
    if cell_id is not None:
        cell['id'] = cell_id
    
    return cell


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
    header_pattern = re.compile(r'^#+\s+')

    # 获取现有的cell ID
    existing_ids = get_existing_cell_ids(ipynb_path)
    current_id_index = 0

    for line in lines:
        code_block_start = code_block_pattern.match(line)
        code_block_end = code_block_end_pattern.match(line)
        is_header = header_pattern.match(line)

        if not in_code_block and code_block_start:
            # 进入代码块
            in_code_block = True
            code_block_lang = code_block_start.group(1)
            # 若有之前的 md 段落，先存为 md 单元
            if md_lines:
                cell_id = existing_ids[current_id_index] if existing_ids and current_id_index < len(existing_ids) else None
                cells.append(create_cell_with_id('markdown', ''.join(md_lines).rstrip(), cell_id))
                current_id_index += 1
                md_lines = []
            code_lines = []
        elif in_code_block and code_block_end:
            # 结束代码块
            in_code_block = False
            metadata = {"language": code_block_lang} if code_block_lang else {}
            cell_id = existing_ids[current_id_index] if existing_ids and current_id_index < len(existing_ids) else None
            cells.append(create_cell_with_id('code', ''.join(code_lines).rstrip(), cell_id, metadata=metadata))
            current_id_index += 1
            code_lines = []
            code_block_lang = ''
        elif in_code_block:
            code_lines.append(line)
        elif is_header:
            # 遇到标题，先保存之前的md内容（如果有）
            if md_lines:
                cell_id = existing_ids[current_id_index] if existing_ids and current_id_index < len(existing_ids) else None
                cells.append(create_cell_with_id('markdown', ''.join(md_lines).rstrip(), cell_id))
                current_id_index += 1
                md_lines = []
            # 标题独占一个cell
            line = re.sub(r'!\[\]\(/img', '![](../img', line)
            cell_id = existing_ids[current_id_index] if existing_ids and current_id_index < len(existing_ids) else None
            cells.append(create_cell_with_id('markdown', line.rstrip(), cell_id))
            current_id_index += 1
        else:
            md_lines.append(line)

    # 文件结尾剩余 md 作为 markdown 单元
    if md_lines:
        cell_id = existing_ids[current_id_index] if existing_ids and current_id_index < len(existing_ids) else None
        cells.append(create_cell_with_id('markdown', ''.join(md_lines).rstrip(), cell_id))

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
