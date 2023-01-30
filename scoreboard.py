from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self) -> None:
        '''Create constructor that inherits from the turtle class and initialize level attribute'''
        super().__init__()
        self.level = 0
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        '''Update level'''
        self.clear()
        self.goto(-210, 250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def level_up(self):
        '''Increase level by 1'''
        self.level += 1
        self.update_level()

    def game_over(self):
        '''Display game over when player is hit'''
        self.goto(0,0)
        self.write(f"GAVE OVER", align=ALIGNMENT, font=FONT)