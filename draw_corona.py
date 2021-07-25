from turtle import *
from time import sleep

# рисуем коронавирус

color('green')
bgcolor('black')
speed(11)
# hideturtle()
b = 0

while b < 200:
    right(b)
    forward(b*3)
    b += 1
sleep(10)


