from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-270, 250)
        self.write(f"Level: {self.score}", align="left", font=("Arial", 20, "normal"))

    def level_up(self):
        self.score += 1
        self.update_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 20, "normal"))


