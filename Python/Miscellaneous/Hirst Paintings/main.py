import colorgram
import turtle
import random

colors = colorgram.extract('painting.jpg',30)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

for i in range(5):
    del rgb_colors[0]

turtle.colormode(255)
tommy = turtle.Turtle()
tommy.penup()
tommy.speed("fastest")

tommy.hideturtle()
tommy.setheading(225)
tommy.forward(300)
tommy.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tommy.dot(20, random.choice(rgb_colors))
    tommy.forward(50)
    if dot_count % 10 == 0:
        tommy.setheading(90)
        tommy.forward(50)
        tommy.setheading(180)
        tommy.forward(500)
        tommy.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
