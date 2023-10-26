from PIL import Image
import os

# 原始图片路径和目标路径
input_dir = 'datasets/50张安全帽图片'
output_dir = 'datasets/50张672安全帽图片'

# 调整后的图像尺寸
new_size = (672, 672)

# 遍历原始图片目录中的所有图片文件
for filename in os.listdir(input_dir):
    # 如果文件不是图片文件，跳过
    if not (filename.endswith('.jpg') or filename.endswith('.png')):
        continue

    # 打开原始图片
    image = Image.open(os.path.join(input_dir, filename))

    # 调整图像尺寸
    resized_image = image.resize(new_size)

    # 保存调整后的图像
    resized_image.save(os.path.join(output_dir, filename))