import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    #Detect if turtle collides with a car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    car_manager.create_car()
    car_manager.move()
    
    #Detect if player arrived at the edge
    if player.is_at_finish_line():
        time.sleep(1)
        car_manager.increase_speed()
        player.reset_position()
        scoreboard.level_update()
        
        
    
screen.exitonclick()
