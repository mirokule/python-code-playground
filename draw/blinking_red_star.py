import turtle
import time


def draw_star(pen):
    pen.color('red')
    pen.begin_fill()
    for i in range(5):
        pen.forward(100)
        pen.right(144)
    pen.end_fill()


def blink_star():
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()

    while True:
        pen.clear()
        draw_star(pen)
        screen.update()
        time.sleep(0.5)

        pen.clear()
        screen.update()
        time.sleep(0.5)


if __name__ == "__main__":
    blink_star()
    