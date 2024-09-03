from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")

tim.color('green')

# for _ in range(2):
#     tim.forward(_)
#     tim.right(40)

# import heroes

# print(heroes.gen())


for _ in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.right(_)

screen = Screen()
screen.exitonclick()