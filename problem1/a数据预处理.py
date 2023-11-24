import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocess_img(img_path):
    # 加载图像，应该直接是一个矩阵
    img = cv2.imread(img_path)

    # 检查图像是否正确加载
    if img is None:
        print("The image not found!!!!")
        return None

    # 高斯模糊滤波去噪声
    image_blurred = cv2.GaussianBlur(img, (5, 5), 0)

    # 调整亮度和对比度（alpha: 对比度, beta: 亮度）
    alpha = 1.5     # 对比度控制
    beta = 50    # 亮度控制
    adjusted = cv2.convertScaleAbs(image_blurred, alpha=alpha, beta=beta)

    # 转换到HSV色彩空间
    image_hsv = cv2.cvtColor(adjusted, cv2.COLOR_BGR2HSV)

    return image_hsv

# 测试函数
processed_image = preprocess_img('../apple.jpg')
if processed_image is not None:
    # 使用matplotlib显示处理后的图像
    plt.imshow(cv2.cvtColor(processed_image, cv2.COLOR_HSV2RGB))
    plt.title('Processed Image')
    plt.show()
