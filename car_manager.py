import random

from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

INITIAL_MOVE_DISTANCE = 5

MOVE_INCREMENT = 5


class Carsmanager():

    def __init__(self):

        self.all_car = []

        self.carspeed = INITIAL_MOVE_DISTANCE

    def create_car(self):

        random_chance = random.randint(1, 3)

        if random_chance == 1:
            new_car = Turtle()

            new_car.shape('square')

            new_car.turtlesize(stretch_wid=1, stretch_len=2)

            new_car.penup()

            new_car.color(random.choice(COLORS))

            new_car.setheading(180)

            new_car.goto(320, random.randint(-250, 250))

            self.all_car.append(new_car)

    def move(self):

        for car in self.all_car:
            car.forward(self.carspeed)

    def level(self):

        self.carspeed += MOVE_INCREMENT
