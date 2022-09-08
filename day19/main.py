from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win the race? Enter a color: ")
colors =  ["red", "orange", "yellow", "green", "blue", "Purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

message = Turtle()
message.hideturtle()

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -230, y= y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            screen.clear()
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                message.write(arg= f"You've won! The {winning_color} turtle is the winner!", align= "center", font=('Arial', 18, 'normal'))
            else:
                message.write(arg= f"You've lost! The {winning_color} turtle is the winner!", align= "center", font=('Arial', 18, 'normal'))

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()