import turtle
import pandas

"""Screen setup"""
screen = turtle.Screen()
screen.title("US States Guess Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

"""Get coordinates"""
# def get_click_coordinates(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_click_coordinates)
# turtle.mainloop()

"""Preparing Data Frame"""
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed = []
missed = []

"""Gameplay"""
game_on = True
while game_on:
    answer = screen.textinput(title=f"{len(guessed)}/50 States Guessed", prompt="What's state's name?")
    answer = answer.title()

    if answer in states_list:
        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_answer = data[data.state == answer]
        t.goto(int(state_answer.x),int(state_answer.y))
        t.write(state_answer.state.item())

    if len(guessed) > 50:
        game_on = False

    if answer == "Exit":
        missed = [state for state in states_list if state not in guessed]
        new_data = pandas.DataFrame(missed)
        new_data.to_csv("missed_states.csv")
        break

screen.exitonclick()
