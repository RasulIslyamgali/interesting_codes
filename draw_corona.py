from turtle import *
from time import sleep
'''Код не мой. Взято из простора интернета. Попробуйте запускать у себя).'''
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


