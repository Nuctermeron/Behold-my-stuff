from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def go_forward():
    tom.forward(10)


def go_backwards():
    tom.backward(10)


def turn_left():
    heading = tom.heading() + 10
    tom.setheading(heading)


def turn_right():
    heading = tom.heading() - 10
    tom.setheading(heading)


def clear_screen():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()
screen.onkey(go_forward, "w")
screen.onkey(go_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()
