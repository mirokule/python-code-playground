import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# 创建一个图形和坐标轴
fig, ax = plt.subplots()

# 定义椭圆的参数
# 椭圆中心的坐标
center_x = 0
center_y = 0
# 椭圆的长半轴长度
width = 4
# 椭圆的短半轴长度
height = 2
# 椭圆的旋转角度（以度为单位）
angle = 0

# 创建一个椭圆对象
ellipse = Ellipse((center_x, center_y), width, height, angle=angle, edgecolor='r', facecolor='none')

# 将椭圆添加到坐标轴中
ax.add_patch(ellipse)

# 设置坐标轴的范围
ax.set_xlim(-5, 5)
ax.set_ylim(-3, 3)

# 使坐标轴比例相等，确保椭圆显示正常
ax.set_aspect('equal')

# 显示图形
plt.show()