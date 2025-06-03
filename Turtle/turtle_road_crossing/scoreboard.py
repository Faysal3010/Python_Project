from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.goto(-200, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def increase(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        t = Turtle()
        t.hideturtle()
        t.write(f"Game Over", align="center", font=("Courier", 30, "bold"))
        
