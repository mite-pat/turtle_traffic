from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self) -> None:
        '''Constructor to create car manager objet with array and speed'''
        # array to hold all car objects
        self.all_cars = []
        # car speed
        self.move_speed = STARTING_MOVE_DISTANCE
        
    def move(self):
        '''Move all cars in array forward'''
        for car in self.all_cars:
            car.forward(self.move_speed)

    def speed_up(self):
        '''Increase speed of car by increment'''
        self.move_speed += MOVE_INCREMENT

    def car_generator(self):
        '''Generate cars for game'''
        # To slow down generation
        random_int = random.randint(1,6)
        if random_int == 6:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.setheading(180)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)