import turtle

STARTING_POSITION = (0, -270)

MOVE_DISTANCE = 10

FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):

    def __init__(self):

        super().__init__()

        self.shape('turtle')

        self.color('black')

        self.penup()

        self.setheading(90)

        self.reset_position()

        # Create the starting line
        starting_line = turtle.Turtle()
        starting_line.penup()
        starting_line.goto(-100, -270)
        starting_line.pendown()
        starting_line.pensize(5)
        starting_line.color("black")
        starting_line.goto(100, -270)
        starting_line.hideturtle()

        # Create the finishing line
        finish_line = turtle.Turtle()
        finish_line.penup()
        finish_line.goto(-300, 290)
        finish_line.pendown()
        finish_line.pensize(5)
        finish_line.color("#196F3D")
        finish_line.goto(300, 290)
        finish_line.hideturtle()

    def reset_position(self):

        self.goto(STARTING_POSITION)

    def move_forward(self):

        self.setheading(90)  # Set direction to upward
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_backward(self):

        self.setheading(270)  # Set direction to downward
        y = self.ycor()
        y -= 20
        self.sety(y)

    def move_left(self):

        x = self.xcor()
        x -= 20
        if x < -280:
            x = -280
        self.setx(x)

    def move_right(self):

        x = self.xcor()
        x += 20
        if x > 280:
            x = 280
        self.setx(x)

    def finished(self):

        if self.ycor() > FINISH_LINE_Y:

            return True

        else:

            return False
