#author:lanxiaoning

import math
import turtle as t
import random

_speed=10
gridlen=30
niddlelen=gridlen/2
niddlenum=500
spliterList=[]

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
    spliterList.append(gridlen*10)
    for i in range(20-1):
        t.penup()
        t.goto(-(gridlen*20),gridlen*(10-1-i))
        t.pendown()
        t.forward(gridlen*40)
        spliterList.append(gridlen*(10-1-i))
    spliterList.append(gridlen * -10)
    #print(spliterList)


def throwniddles():
    t.pencolor('red')
    realrk=0
    matchcount=0
    for i in range(niddlenum):
        rk=random.randint(0,360)
        realrk=(realrk+rk)%360
        rx=random.randint(gridlen*(-20),gridlen*20)
        ry=random.randint(gridlen*(-10),gridlen*10)
        t.penup()
        t.goto(rx,ry)
        t.pendown()
        t.right(rk)
        t.forward(niddlelen)
        dy=ry-niddlelen*math.sin(realrk*(math.pi/180))
        if(checkmatch(ry,dy)):
            matchcount=matchcount+1

    print('total '+str(niddlenum)+' niddles, matched '+str(matchcount)+', PI is '+str(1/(matchcount/niddlenum)))


def checkmatch(ry,dy):
    if(ry>=dy):
        maxone=ry
        minone=dy
    else:
        maxone=dy
        minone=ry
    for i in spliterList:
        if(minone<=i<=maxone):
            return True

    return False



if(__name__=='__main__'):
    init()
    drawbackground()
    drawspliter()
    throwniddles()
    t.done()
