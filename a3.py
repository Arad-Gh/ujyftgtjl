import turtle
import random
c = ["black" , "white" , "yellow" ]
def square() :
    r = random.choice(c)
    turtle.fillcolor(r)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()
a = 0
b = 0
x = int(input(": "))
for i in range(x) :
    turtle.penup()
    a = random.randint(-250,250)
    b = random.randint(-250,250)
    turtle.goto(a,b)
    turtle.pendown()
    square()

turtle.done()