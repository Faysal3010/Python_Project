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
        '''update the food to random position'''
        x = random.randint(-460, 460)
        y = random.randint(-260, 260)
        self.goto(x, y)
        print(self.position())
