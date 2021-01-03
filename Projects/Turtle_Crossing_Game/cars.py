from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
INCREASE_SPEED = 5
MOVE_SPEED = 10

class Cars:

    def __init__(self):
        self.cars_list = []
        self.car_speed = MOVE_SPEED

    def create_car(self):
        random_change = random.randint(1,6)
        if random_change == 6:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-250,250)
            new_car.goto(300, rand_y)
            self.cars_list.append(new_car)

    def move_car(self):
        for car in self.cars_list:
            car.backward(self.car_speed)

    def car_level_up(self):
        self.car_speed += INCREASE_SPEED
