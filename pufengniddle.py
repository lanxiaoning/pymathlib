#author:lanxiaoning

import math
import turtle as t
import random

_speed=10
gridlen=30
niddlelen=gridlen/2
niddlenum=2000

def init():
    t.setup(width=0.95,height=0.95)
    t.pencolor('blue')
    t.hideturtle()
    t.speed(_speed)

def drawbackground():
    t.penup()
    t.goto(-(gridlen*20),gridlen*10)
    t.pendown()
    t.forward(gridlen*40)
    t.right(90)
    t.forward(gridlen*20)
    t.right(90)
    t.forward(gridlen*40)
    t.right(90)
    t.forward(gridlen*20)
    t.right(90)

def drawspliter():
    for i in range(20-1):
        t.penup()
        t.goto(-(gridlen*20),gridlen*(10-1-i))
        t.pendown()
        t.forward(gridlen*40)

if(__name__=='__main__'):
    init()
    drawbackground()
    drawspliter()
    #main()
    t.done()