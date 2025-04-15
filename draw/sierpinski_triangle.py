import turtle


def sierpinski(t, order, size):
    if order == 0:
        for _ in range(3):
            t.forward(size)
            t.left(120)
    else:
        sierpinski(t, order - 1, size / 2)
        t.forward(size / 2)
        sierpinski(t, order - 1, size / 2)
        t.backward(size / 2)
        t.left(60)
        t.forward(size / 2)
        t.right(60)
        sierpinski(t, order - 1, size / 2)
        t.left(60)
        t.backward(size / 2)
        t.right(60)


# 创建画布和画笔
screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)

# 绘制谢尔宾斯基三角形
sierpinski(pen, 3, 300)

# 完成绘制
turtle.done()
    