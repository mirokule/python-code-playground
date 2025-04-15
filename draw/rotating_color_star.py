import turtle
import random
import time

# 设置画布和画笔
screen = turtle.Screen()
screen.title("Rotating and Color - Changing Six - Pointed Star")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# 定义颜色列表
colors = ["red", "orange", "black", "green", "blue", "indigo", "violet"]

# 定义点击屏幕时执行的函数
def close_window(x, y):
    turtle.bye()

# 绑定点击事件
screen.onscreenclick(close_window)

# 绘制六芒星的函数
def draw_six_pointed_star(size):
    # 绘制第一个等边三角形
    for _ in range(6):
        pen.forward(size)
        pen.left(60)

# 主循环
angle = 0
while True:
    # 随机选择颜色
    color = random.choice(colors)
    pen.color(color)
    # 清空之前的绘制
    pen.clear()
    # 设置旋转角度
    pen.setheading(angle)
    # 绘制六芒星
    draw_six_pointed_star(100)
    # 增加旋转角度
    angle += 5
    # 更新屏幕
    screen.update()
    time.sleep(0.05)
