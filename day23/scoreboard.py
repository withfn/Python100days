from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-130, 260)
        self.level = 0
        self.level_update()
        
    
    def level_update(self):
        self.clear()
        self.increase_level()
        self.write(f"Level: {self.level}", align="right", font=FONT)
        
    def increase_level(self):
        self.level += 1
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
