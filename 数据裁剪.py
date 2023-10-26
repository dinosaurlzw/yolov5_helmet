import os
import random
import shutil

def random_delete_dataset(dataset_dir, delete_ratio):
    # 获取数据集目录下所有图像文件和对应的标注文件列表
    image_files = [f for f in os.listdir(dataset_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    annotation_files = [f.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt')
                        for f in image_files]

    # 计算需要删除的样本数量
    num_samples = len(image_files)
    num_samples_to_delete = int(num_samples * delete_ratio)

    # 随机选择要删除的样本
    samples_to_delete = random.sample(range(num_samples), num_samples_to_delete)

    # 删除选定的样本
    for sample_idx in sorted(samples_to_delete, reverse=True):
        image_file = os.path.join(dataset_dir, image_files[sample_idx])
        annotation_file = os.path.join(dataset_dir, annotation_files[sample_idx])

        os.remove(image_file)
        os.remove(annotation_file)

    print(f"Deleted {num_samples_to_delete} out of {num_samples} samples.")

# 指定数据集目录和要删除的比例
dataset_directory = 'data/hat_1 裁剪'  # 替换为你的数据集目录
delete_ratio = 0.1  # 要删除的比例，此处为 20%

# 调用函数进行随机删除
random_delete_dataset(dataset_directory, delete_ratio)