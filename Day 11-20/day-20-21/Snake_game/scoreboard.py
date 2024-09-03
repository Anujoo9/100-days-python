from turtle import Turtle
ALIGNTMENT = "center"
FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
    

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align = ALIGNTMENT, font=FONT)
        
    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNTMENT, font=FONT )
