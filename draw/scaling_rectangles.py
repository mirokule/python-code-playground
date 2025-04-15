import turtle

# 设置画布和画笔
screen = turtle.Screen()
screen.title("Scaling Overlapping Rectangles")
pen1 = turtle.Turtle()
pen2 = turtle.Turtle()
pen1.speed(0)
pen2.speed(0)
pen1.pensize(5)
pen2.pensize(3)
pen1.color("blue")
pen2.color("green")


# 定义点击屏幕时执行的函数
def close_window(x, y):
    turtle.bye()

# 绑定点击事件
screen.onscreenclick(close_window)

# 初始大小
width1 = 100
height1 = 50
width2 = 70
height2 = 120

# 缩放速率
scale_rate1 = 3
scale_rate2 = 5

# 绘制长方形的函数
def draw_rectangle(pen, width, height):
    pen.penup()
    pen.goto(-width / 2, -height / 2)
    pen.pendown()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)

# 主循环
while True:
    # 清空之前的绘制
    pen1.clear()
    pen2.clear()

    # 绘制长方形
    draw_rectangle(pen1, width1, height1)
    draw_rectangle(pen2, width2, height2)

    # 更新大小
    width1 += scale_rate1
    height1 += scale_rate1
    width2 += scale_rate2
    height2 += scale_rate2

    # 当长方形大小超出范围时反转缩放方向
    if width1 > 200 or width1 < 50:
        scale_rate1 = -scale_rate1
    if width2 > 200 or width2 < 50:
        scale_rate2 = -scale_rate2

    # 更新屏幕
    screen.update()
    