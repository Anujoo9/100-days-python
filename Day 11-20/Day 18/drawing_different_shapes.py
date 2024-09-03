from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["red", "blue", "pink", "black", "orange","aqua"]

# for i in range(3,10):
#     angle = 360/i
#     for j in range(i):
#         print(i)
#         tim.forward(100)
#         tim.right(angle)
#         print(angle)


def draw_shape(num_side):
    angle = 360/num_side
    for _ in range(num_side):
        tim.color(random.choice(colors))
        tim.forward(100)
        tim.right(angle)

for shape_sides in range(3,11):
    draw_shape(shape_sides)

screen = Screen()
screen.exitonclick()