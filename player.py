from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        '''Create constructor that inherits from the turtle class'''
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    
    def move_up(self):
        '''Allow turtle to move upwards'''
        self.forward(MOVE_DISTANCE)


    def reset_position(self):
        '''Reset turtles posistion to initial posistion'''
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True


