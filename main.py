from turtle import Turtle, Screen
from player import Player
from ball import Ball
from board import Board
import time
import keyboard
from tkinter import messagebox

screen = Screen()
screen.setup(610, 600)
screen.title("Breakout Game")
screen.tracer(0)

ball = Ball()
player = Player()
board = Board(levels=1)
screen.tracer(1, 0)
screen.listen()
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")
is_game_on = True


def end_game(result):
    global is_game_on
    if result:
        message = messagebox.askquestion("Congratulations! You win!", "Would you like to play again?")
    else:
        message = messagebox.askquestion("Game over!", "Would you like to play again?")

    if message == "yes":
        board.reset_board()
        ball.goto(0, 0)
        ball.move_step_x = abs(ball.move_step_x)
        ball.move_step_y = abs(ball.move_step_y)
    elif message == "no":
        is_game_on = False


while is_game_on:
    time.sleep(0.1)
    ball.move()
    if (ball.distance(player) < 40) and (ball.ycor() < -255):
        ball.move_step_y *= -1
        if keyboard.is_pressed("Left"):
            ball.color("green")
        elif keyboard.is_pressed("Right"):
            ball.color("black")
    elif ball.ycor() < -255:
        end_game(False)

    # Detect collisions with board blocks
    for block in board.blocks: # type: Turtle
        if (block.xcor() + block.shapesize()[1]*10 > ball.xcor() > block.xcor() - block.shapesize()[1]*10) and ball.distance(block) <= 20:
            ball.move_step_y *= -1
            board.blocks.remove(block)
            block.goto((block.xcor() + 1400), block.ycor())
            board.new_blocks.append(block)
        elif (block.ycor() + block.shapesize()[0] * 10 > ball.ycor() > block.ycor() - block.shapesize()[0] * 10) and ball.distance(block) <= 20:
            ball.move_step_x *= -1
            board.blocks.remove(block)
            block.goto((block.xcor() + 1400), block.ycor())
            board.new_blocks.append(block)

        if len(board.blocks) == 0:
            end_game(True)

    # Collisions with walls
    if ball.ycor() >= 275:
        ball.move_step_y *= -1
    if (ball.xcor() <= -275) or (ball.xcor() >= 275):
        ball.move_step_x *= -1
