import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Traffic!")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate cars and move them
    car_manager.car_generator()
    car_manager.move()

    # If player reaches top increase level and speed of cars
    if player.reset_position():
        scoreboard.level_up()
        car_manager.speed_up()
    
    # Check collision between player and cars
    for x in range(len(car_manager.all_cars)):
        if player.distance(car_manager.all_cars[x]) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()