import matplotlib.pyplot as plt
import numpy as np

# 定义五角星的顶点坐标
points = np.array([
    [0.0, 1.0],
    [0.5878, 0.809],
    [0.9511, 0.309],
    [0.7071, -0.7071],
    [0.1564, -0.9659],
    [-0.1564, -0.9659],
    [-0.7071, -0.7071],
    [-0.9511, 0.309],
    [-0.5878, 0.809],
    [0.0, 1.0]
])

# 提取 x 和 y 坐标
x = points[:, 0]
y = points[:, 1]

# 创建一个图形窗口
plt.figure()

# 绘制五角星
plt.plot(x, y, 'r-')

# 设置坐标轴比例为相等
plt.axis('equal')

# 隐藏坐标轴
plt.axis('off')

# 显示图形
plt.show()
    