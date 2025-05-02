from turtle import Turtle, Screen
import random

t = Turtle()
t.width(5)
l=100
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

for _ in range(4):
    color=random.choice(colors)
    t.color(color)
    t.right(90)
    t.fd(l)
    

screen = Screen()
screen.exitonclick()
