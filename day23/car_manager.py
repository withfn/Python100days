from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.distance = STARTING_MOVE_DISTANCE
        self.create_car()
        
    
    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            random_x = randint(250, 300)
            random_y = randint(-250, 250)
            new_car = Turtle(shape="square")
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.goto(random_x, random_y)
            self.cars.append(new_car)
        
    
    def move(self):
        for car in self.cars:
            car.forward(self.distance)
            
    def increase_speed(self):
        if self.distance < 50:
            self.distance += MOVE_INCREMENT
