from turtle import Screen
import time

screen = Screen()

screen.bgcolor("white")
screen.setup (width=600, height=600)
screen.title("road-cross")
screen.tracer(0)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()