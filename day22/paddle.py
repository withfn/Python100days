from turtle import Turtle, width

WIDTH = 1
HEIGHT = 5
MOVE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("White")
        self.penup()
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.goto(self.position)
        
    
    def up(self):
        if self.ycor() < 280:
            new_y = self.ycor() + MOVE
            self.goto(self.xcor(), new_y)
    
    def down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - MOVE
            self.goto(self.xcor(), new_y)