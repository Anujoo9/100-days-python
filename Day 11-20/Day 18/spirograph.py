import turtle as t
import random

tim = t.Turtle()

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
def draw_spiropgraph(size_of_the_gap):
    for _ in range(int(360 / size_of_the_gap)):
        tim.color(random_color())
        # tim.speed(150)
        tim.speed("fastest")
        tim.circle(100)
        # current_heading = tim.heading()
        # tim.setheading(current_heading + 10)
        tim.setheading(tim.heading() + size_of_the_gap)
draw_spiropgraph(5)

# for _ in range(0,1000):
#     tim.color(random_color())
#     # tim.speed(150)
#     tim.speed("fastest")
#     tim.circle(100)
#     tim.right(5)



screen = t.Screen()
screen.exitonclick()