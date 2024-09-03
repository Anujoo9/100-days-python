import turtle as t
import random

tim = t.Turtle()

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

direction = [0,90,180,270]


for i in range(500):
    tim.pensize(15)
    tim.speed(15)
    tim.color(random_color())
    tim.setheading(random.choice(direction))
    tim.forward(30)
    
