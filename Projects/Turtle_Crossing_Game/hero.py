from turtle import Turtle
START = (0,-280)


class Hero(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(START)
        self.setheading(90)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def reset_position(self):
        self.goto(START)

