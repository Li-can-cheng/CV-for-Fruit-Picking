import matplotlib.pyplot as plt

# 假设apple_counts是一个包含苹果数量的列表
# 例如，每个元素代表一个图像中的苹果数量
apple_counts = [10, 12, 15, 7, 8, 9, 14, 11, 13, 10]  # 示例数据

# 绘制直方图
plt.hist(apple_counts, bins=5, color='green', alpha=0.7)
plt.title('Apple Count Distribution')
plt.xlabel('Number of Apples')
plt.ylabel('Frequency')
plt.show()
