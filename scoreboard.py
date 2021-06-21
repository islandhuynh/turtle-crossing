from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=-290, y=260)
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.score}", font=FONT)

    def increase_Score(self):
        self.score_count += 1
        self.clear()
        self.update_score()


