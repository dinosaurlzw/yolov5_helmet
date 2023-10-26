import os
import shutil

def split_files(source_directory, jpg_directory, txt_directory):
    if not os.path.exists(jpg_directory):
        os.makedirs(jpg_directory)
    if not os.path.exists(txt_directory):
        os.makedirs(txt_directory)

    files = os.listdir(source_directory)
    for file in files:
        source_file = os.path.join(source_directory, file)
        if file.endswith('.jpg') or file.endswith('.jpeg'):
            destination_file = os.path.join(jpg_directory, file)
            shutil.move(source_file, destination_file)
        elif file.endswith('.txt'):
            destination_file = os.path.join(txt_directory, file)
            shutil.move(source_file, destination_file)

# 指定源文件夹、目标 JPG 文件夹和目标 TXT 文件夹的路径
source_directory = 'data/hat_1 裁剪'  # 替换为源文件夹的路径
jpg_directory = 'data/hat_1 裁剪/images'  # 替换为目标 JPG 文件夹的路径
txt_directory = 'data/hat_1 裁剪/labels'  # 替换为目标 TXT 文件夹的路径

# 调用函数进行文件分割
split_files(source_directory, jpg_directory, txt_directory)