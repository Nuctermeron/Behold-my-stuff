from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# Game difficulty
def difficulty_level(diff_lev):
    if diff_lev.lower() == "Easy".lower():
        return 0.5
    elif diff_lev.lower() == "Medium".lower():
        return 0.25
    else:
        return 0.1


"""Screen configuration"""
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

"""Creating snake class instance"""
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

"""Gameplay"""
difficulty = screen.textinput("Difficulty", "What level would you like to get? Easy, Medium or Hard?\n")
screen.listen()
game_on = True

while game_on:
    screen.update()
    time.sleep(difficulty_level(difficulty))
    snake.move_snake()
    if snake.head.distance(food) < 15:  # Collision with food
        food.change_location()
        snake.grow_larger()
        scoreboard.score_point()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:  # Collision with wall
        game_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:  # Collision with tail
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
