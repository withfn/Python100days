from turtle import Turtle

ALIGMENT = "center"
FONT = "Arial"
FONT_SIZE = 16

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(x=0, y=250)
        self.score = 0
        self.scoreboard_update()
        
    def scoreboard_update(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font=(FONT, FONT_SIZE))
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.scoreboard_update()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGMENT, font=(FONT, FONT_SIZE))
        