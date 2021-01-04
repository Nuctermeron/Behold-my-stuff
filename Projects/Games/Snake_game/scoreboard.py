from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def score_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highscore.txt", mode="w") as highscore_text:
                highscore_text.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

    def get_highscore(self):
        with open("highscore.txt") as highscore_text:
            return int(highscore_text.read())

