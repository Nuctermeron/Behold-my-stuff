from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

"""Screen setup"""
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

"""Middle lines"""
new_y = 260
for line in range(14):
    new_line = Paddle((0,0))
    new_line.shapesize(1,0.5)
    new_line.goto(0,new_y)
    new_y += -40


"""Paddle objects and control"""
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

"""Gameplay"""
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball.move_speed *= 0.9
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball.move_speed = 0.1
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        ball.move_speed = 0.1

screen.exitonclick()
