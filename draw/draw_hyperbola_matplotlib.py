import numpy as np
import matplotlib.pyplot as plt

# 定义双曲线的参数
a = 1
b = 1

# 生成 y 值
y = np.linspace(-10, 10, 400)

# 计算 x 值
x_positive = b * np.sqrt((y**2 / a**2) - 1)
x_negative = -b * np.sqrt((y**2 / a**2) - 1)

# 创建绘图
plt.figure(figsize=(8, 6))

# 绘制双曲线的右半部分
plt.plot(x_positive[np.abs(y) >= a], y[np.abs(y) >= a], label=r'$\frac{y^{2}}{a^{2}}-\frac{x^{2}}{b^{2}} = 1$ (right part)', color='red')
# 绘制双曲线的左半部分
plt.plot(x_negative[np.abs(y) >= a], y[np.abs(y) >= a], color='red')

# 设置图形标题和坐标轴标签
plt.title('Hyperbola with Foci on the y-axis')
plt.xlabel('x')
plt.ylabel('y')

# 添加图例
plt.legend()

# 显示网格线
plt.grid(True)

# 显示图形
plt.show()
