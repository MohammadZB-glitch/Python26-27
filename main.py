
from joke import *
from random import*
turtle.bgcolor("cyan")
turtle.colormode(255)
turtle.tracer(0)

for times in range(150):
    bob.left(15)
    bob.forward(times)
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    c=(r,g,b)
    bob.pencolor(c)
    bob.begin_fill()
    polygon(3,20)
    bob.end_fill()
    polygon(3,20)
bob.penup()
bob.goto(0,0)
bob.pendown()
for times in range(150):
    bob.right(-15)
    bob.forward(times)
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    c=(r,g,b)
    bob.pencolor(c)
    bob.begin_fill()
    polygon(3,20)
    bob.end_fill()
    polygon(3,20)
   
    
