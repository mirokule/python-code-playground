import turtle

# 创建一个画布和画笔
pen = turtle.Turtle()

# 设置画笔速度
pen.speed(2)

# 循环绘制五角星的五条边
for i in range(5):
    # 向前移动 100 个单位
    pen.forward(100)
    # 右转 144 度
    pen.right(144)

# 完成绘制后隐藏画笔
pen.hideturtle()

# 保持窗口打开
turtle.done()
    