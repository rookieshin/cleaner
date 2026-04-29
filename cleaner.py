import os
import shutil

# 1. 扩展更全的分类
ext_map = {
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
    '.pdf': 'Docs', '.docx': 'Docs', '.txt': 'Docs', '.xlsx': 'Docs',
    '.zip': 'Archives', '.rar': 'Archives', '.7z': 'Archives',
    '.mp4': 'Video', '.mov': 'Video'
}

# 获取当前脚本的文件名，避免把自己也移动了
current_script = os.path.basename(__file__)

for file in os.listdir('.'):
    # 跳过文件夹本身和当前运行的脚本
    if os.path.isdir(file) or file == current_script:
        continue
        
    ext = os.path.splitext(file)[1].lower()
    if ext in ext_map:
        target_dir = ext_map[ext]
        os.makedirs(target_dir, exist_ok=True)
        
        # 处理同名文件冲突：如果目标文件夹已有同名文件，先不移动或重命名
        if not os.path.exists(os.path.join(target_dir, file)):
            shutil.move(file, target_dir)
            print(f"✅ 整理完成: {file} -> {target_dir}")
        else:
            print(f"⚠️ 跳过重名文件: {file}")
