from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def l_score_increase(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_score_increase(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 220)
        self.write(arg=self.l_score, align="center", font=("Courier", 50, "bold"))
        self.goto(100, 220)
        self.write(arg=self.r_score, align="center", font=("Courier", 50, "bold"))
