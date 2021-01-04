from turtle import Screen
from hero import Hero
from scoreboard import Scoreboard
import  time
from cars import Cars

"""Screen setup"""
screen = Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.tracer(0)
screen.title("Turtle Crossing")

"""Main hero"""
hero = Hero()
scoreboard = Scoreboard()
cars = Cars()

screen.listen()
screen.onkey(hero.go_up,"Up")

"""Gameplay"""
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()
    for car in cars.cars_list:
        if car.distance(hero) < 20:
            game_on = False
            scoreboard.game_over()
    if hero.ycor() > 280:
        hero.reset_position()
        scoreboard.level_up()
        cars.car_level_up()

screen.exitonclick()
