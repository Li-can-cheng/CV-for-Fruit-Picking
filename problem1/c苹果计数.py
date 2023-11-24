import cv2
import numpy as np
import matplotlib.pyplot as plt
from b苹果识别 import detect_apples
from a数据预处理 import preprocess_img

def count_apples(apple_segments):
    # 转换到灰度图像
    gray = cv2.cvtColor(apple_segments, cv2.COLOR_BGR2GRAY)

    # 二值化
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

    # 查找轮廓
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 过滤和计数苹果
    apple_count = 0
    for contour in contours:
        # 可以根据需要设置面积阈值来过滤轮廓
        if cv2.contourArea(contour) > 100:  # 假设的面积阈值
            apple_count += 1
            cv2.drawContours(apple_segments, [contour], -1, (0, 255, 0), 3)

    return apple_count, apple_segments


# 使用前面的函数
processed_image = preprocess_img('../apple.jpg')
if processed_image is not None:
    apple_segments = detect_apples(processed_image)
    apple_count, apple_contours = count_apples(apple_segments)

    print("苹果的数量: ", apple_count)

    # 显示带有轮廓的图像
    plt.imshow(cv2.cvtColor(apple_contours, cv2.COLOR_HSV2RGB))
    plt.title('Apple Count')
    plt.show()
