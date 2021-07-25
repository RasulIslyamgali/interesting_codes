from turtle import *
from time import sleep
# мой код. просто запустите программа.
# i love


def word_a():
    down()
    # рисуем левую часть А
    right(120)
    forward(100)
    # возвращаемя в начальную точку
    backward(100)
    # рисуем часть правой буквы А
    left(60)
    forward(50)
    # draw center A
    right(120)
    forward(50)
    # back turtle
    backward(50)
    # end draw A
    left(120)
    forward(50)
    # turtle go to dot for draw next word
    up()
    left(60)
    forward(100)
    left(90)
    forward(86)


def word_i(i):
    down()
    speed(speed=10)
    for j in range(i):
        # рисуем палочку
        if j == 0:
            right(90)
        else:
            left(90)
        forward(150 + j)
        # рисуем нижнюю часть i
        right(90)
        forward(20 + j**2)
        backward(40 + j**2)
        forward(20 + 1)
        # возвращаемся на начальную точку и рисуем верх i
        right(90)
        forward(150 + 1)
        # draw top i
        left(90)
        forward(20 + 1)
        backward(40 + 1)
        forward(20 + 1)
    # turtle go to dot for draw next word
    up()
    right(180)
    forward(200)
    right(90)
    forward(150)


def turtle_hurt():
    down()
    speed(speed=0)
    # turtle.bgcolor("black")
    pensize(3)

    def curve():
        for i in range(200):
            right(1)
            forward(1)

    color("black", "red")
    begin_fill()

    right(130)
    forward(111.65)
    curve()

    left(120)
    curve()

    forward(111.65)
    end_fill()
    hideturtle()


word_i(11)
turtle_hurt()
sleep(5)
