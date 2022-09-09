from turtle import Turtle

ALIGMENT = "center"
FONT = "Arial"
FONT_SIZE = 16

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(x=0, y=250)

        self.scoreboard_update()
        
    def scoreboard_update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=(FONT, FONT_SIZE))
        
    def increase_score(self):
        self.score += 1
        self.scoreboard_update()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.scoreboard_update()