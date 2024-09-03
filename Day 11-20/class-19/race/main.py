from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
axis = -100

all_turtle = []

for turtle_index in colors:
    new_turutle = Turtle(shape = "turtle")
    new_turutle.color(turtle_index)
    new_turutle.penup()
    new_turutle.goto(x=-230,y=axis)
    axis = axis + 30
    all_turtle.append(new_turutle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                 print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()