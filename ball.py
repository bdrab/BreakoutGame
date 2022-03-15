from turtle import Turtle
import random

BALL_STARTING_POSITION = (0, -100)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.goto(BALL_STARTING_POSITION)
        self.move_step_x = 10
        self.move_step_y = 10
        self.colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]

    def move(self):
        self.setx(self.xcor() + self.move_step_x)
        self.sety(self.ycor() + self.move_step_y)

    def change_color(self):
        self.color(random.choice(self.colors))
