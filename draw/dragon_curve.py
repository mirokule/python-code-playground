import turtle


def dragon_curve(t, order, length, turn='r'):
    if order == 0:
        t.forward(length)
    else:
        if turn == 'r':
            dragon_curve(t, order - 1, length, 'r')
            t.right(90)
            dragon_curve(t, order - 1, length, 'l')
        else:
            dragon_curve(t, order - 1, length, 'r')
            t.left(90)
            dragon_curve(t, order - 1, length, 'l')


# 创建画布和画笔
screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)

# 绘制龙形曲线
dragon_curve(pen, 10, 10)

# 完成绘制
turtle.done()
    