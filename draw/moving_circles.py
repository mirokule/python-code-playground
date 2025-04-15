import turtle

# 设置画布
screen = turtle.Screen()
screen.title("Moving Circles")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# 定义点击屏幕时执行的函数
def close_window(x, y):
    turtle.bye()

# 绑定点击事件
screen.onscreenclick(close_window)

# 定义三个圆的参数
circles = []
colors = ["red", "green", "blue"]
radii = [20, 30, 40]
speeds = [3, 5, 7]
angles = [30, 120, 210]

for i in range(3):
    circle = turtle.Turtle()
    circle.shape("circle")
    circle.color(colors[i])
    circle.penup()
    circle.shapesize(stretch_len=radii[i] / 10, stretch_wid=radii[i] / 10)
    circle.speed(0)
    circle.setheading(angles[i])
    circles.append(circle)

# 主循环
while True:
    for i, circle in enumerate(circles):
        # 移动圆
        circle.forward(speeds[i])

        # 获取圆的位置
        x = circle.xcor()
        y = circle.ycor()
        radius = radii[i]

        # 检查是否到达屏幕边缘
        if x > screen.window_width() / 2 + radius:
            circle.goto(-screen.window_width() / 2 - radius, y)
        elif x < -screen.window_width() / 2 - radius:
            circle.goto(screen.window_width() / 2 + radius, y)
        if y > screen.window_height() / 2 + radius:
            circle.goto(x, -screen.window_height() / 2 - radius)
        elif y < -screen.window_height() / 2 - radius:
            circle.goto(x, screen.window_height() / 2 + radius)

    # 更新屏幕
    screen.update()
    