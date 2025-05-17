import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.refresh()

    def refresh(self):
        x = random.randint(-465, 465)
        y = random.randint(-265, 265)
        self.goto(x, y)
        print(self.position())
