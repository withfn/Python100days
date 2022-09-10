from turtle import Turtle
from bank_states import BankStates

ALIGMENT = "center"
FONT = "Arial"
FONT_SIZE = 12

class Writer(BankStates):
    def __init__(self):
        super().__init__()
        self.tw = Turtle()
        self.tw.hideturtle()
        self.tw.penup()

        self.tn = Turtle()
        self.tn.hideturtle()
        self.tn.penup()
        self.update_score()
        
    #put the state name on the map
    def update_states(self):
        self.update_score()
        self.tw.goto(self.position)
        self.tw.write(f"{self.answer_state}", align=ALIGMENT, font=(FONT, FONT_SIZE))
    
    #update score user
    def update_score(self):
        self.tn.goto(-320, 220)
        self.tn.clear()
        self.tn.write(f"{self.score}/{self.all_states}", align=ALIGMENT, font=(FONT, FONT_SIZE))
