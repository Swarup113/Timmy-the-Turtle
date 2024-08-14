from turtle import Turtle
import turtle
FONT = ('Courier', 13, 'normal')

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()

        self.level = 1

        self.hideturtle()

        self.penup()

        self.goto(-270, 265)

        self.write(f"Difficulty: {self.level}",align='left',font=FONT)

    def increase_level(self):

        self.level += 1

        self.clear()

        self.color('red')

        self.write(f"Difficulty: {self.level}", align='left', font=('Courier', 13, 'normal'))

        if self.level == 2:
            turtle.bgcolor("cyan")
        elif self.level == 3:
            turtle.bgcolor("#46C9C4")


    def crash(self):
        self.color('red')
        self.write("Game Over!",align='center',font=('Courier', 48, "bold"))