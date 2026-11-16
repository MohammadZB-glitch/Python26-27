import turtle
bob = turtle.Turtle()
bob.speed(0)
def polygon(sides,dist):
    angle=360/sides
    for times in range(sides):
        bob.forward(dist)
        bob.left(angle)
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
