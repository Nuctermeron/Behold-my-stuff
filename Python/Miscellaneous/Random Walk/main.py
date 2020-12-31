import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

def random_walk():
    for i in range(200):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))

def draw_spirogrpah(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

directions = [8, 98, 180, 270]
tim = t.Turtle()
t.colormode(255)
tim.pensize(5)
tim.speed("fastest")


screen = t.Screen()
screen.exitonclick()



