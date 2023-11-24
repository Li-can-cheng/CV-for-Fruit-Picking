import cv2
import numpy as np
import matplotlib.pyplot as plt
from problem1.a数据预处理 import preprocess_img
def detect_apples(image_hsv):
    # 定义苹果的颜色范围（HSV色彩空间）
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # 创建掩码，只保留红色区域
    mask = cv2.inRange(image_hsv, lower_red, upper_red)

    # 使用掩码获取原图中的红色区域
    apple_segments = cv2.bitwise_and(image_hsv, image_hsv, mask=mask)

    # 返回识别出的苹果区域
    return apple_segments

# 使用前面的预处理函数
processed_image = preprocess_img('../apple.jpg')
if processed_image is not None:
    apple_segments = detect_apples(processed_image)

    # 使用matplotlib显示识别出的苹果区域
    plt.imshow(cv2.cvtColor(apple_segments, cv2.COLOR_HSV2RGB))
    plt.title('Detected Apples')
    plt.show()
