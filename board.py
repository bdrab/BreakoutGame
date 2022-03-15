from turtle import Turtle
import random


class Board:
    def __init__(self, levels):
        super().__init__()
        self.blocks = []
        self.new_blocks = []
        self.create_board(levels)

    def create_board(self, levels):
        for level in range(0, levels):
            x_cor = -280
            while x_cor < 300:
                new_block = Turtle()
                new_block.penup()
                new_block.shape("square")
                colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
                new_colors = random.sample(colors, levels)
                new_block.color(new_colors[level])
                stretch_value = 2
                new_block.shapesize(stretch_len=2, stretch_wid=stretch_value)
                size = stretch_value * 20
                new_block.goto(x_cor, level * 40)
                x_cor += size
                self.blocks.append(new_block)

    def reset_board(self):
        for block in self.new_blocks:  # type: Turtle
            block.goto((block.xcor() - 1400), block.ycor())
            self.blocks.append(block)
        self.new_blocks.clear()
