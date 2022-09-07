from turtle import Turtle, Screen, colormode
from random import choice

colors = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), 
        (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85)]
    
x_position = -250
y_position = -250
colormode(255)
turtle = Turtle(shape="triangle")
turtle.speed(8)
turtle.penup()
turtle.setposition(x_position, y_position)
turtle.pensize(25)

for _ in range(10):
    for step in range(10):
        turtle.pencolor(choice(colors))
        turtle.pendown()
        turtle.forward(1)
        turtle.penup()
        turtle.forward(50)

    y_position += 50
    turtle.setposition(x_position, y_position)
            
screen = Screen()
screen.setup(width= 600, height= 600, startx= 0, starty= 0)
screen.exitonclick()