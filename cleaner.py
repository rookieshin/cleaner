import os
import shutil

# 定义分类逻辑
ext_map = {'.jpg': 'Images', '.png': 'Images', '.pdf': 'Docs', '.zip': 'Archives'}

for file in os.listdir('.'):
    ext = os.path.splitext(file)[1].lower()
    if ext in ext_map:
        os.makedirs(ext_map[ext], exist_ok=True)
        shutil.move(file, ext_map[ext])
        print(f"移动了: {file}")
