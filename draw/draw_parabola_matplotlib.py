import numpy as np
import matplotlib.pyplot as plt

# 定义抛物线的参数
a = 1
b = 0
c = 0

# 生成 x 值
x = np.linspace(-10, 10, 400)

# 计算对应的 y 值
y = a * x**2 + b * x + c

# 创建绘图
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'$y = {a}x^{2}+{b}x + {c}$')

# 设置图形标题和坐标轴标签
plt.title('Parabola')
plt.xlabel('x')
plt.ylabel('y')

# 添加图例
plt.legend()

# 显示网格线
plt.grid(True)

# 显示图形
plt.show()