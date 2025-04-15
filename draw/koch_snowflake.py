import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)


def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


# 创建画布和画笔
screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)

# 绘制科赫雪花
koch_snowflake(pen, 3, 300)

# 完成绘制
turtle.done()
    