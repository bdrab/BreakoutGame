from turtle import Turtle, Screen
from player import Player
from ball import Ball
from board import Board

screen = Screen()
screen.setup(610, 600)
screen.title("Breakout Game")
screen.tracer(0)

ball = Ball()


screen.exitonclick()

