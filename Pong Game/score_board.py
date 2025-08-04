from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,x):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score=0
        self.goto(x,260)
        self.update_score("initial")

    def update_score(self,side):
        self.clear()
        self.write(f"{side}:{self.score}",align="center",font=("Courier",20,"bold"))
    
    def increase_left(self):
        self.score+=1
        self.update_score("Left")

    def increase_right(self):
        self.score+=1
        self.update_score("Right")