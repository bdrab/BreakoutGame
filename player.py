from turtle import Turtle
PLAYER_STARTING_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=4)
        self.penup()
        self.goto(PLAYER_STARTING_POSITION)
        self.setheading(90)

    def go_left(self):
        if self.xcor() > -260:
            self.goto(self.xcor() - 20, -280)
        else:
            pass

    def go_right(self):
        if self.xcor() < 260:
            self.goto(self.xcor() + 20, -280)
        else:
            pass
