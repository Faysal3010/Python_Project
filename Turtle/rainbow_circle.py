from turtle import Turtle, Screen
import random

t = Turtle()
t.width(3)
l=3
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

while True:
    color=random.choice(colors)
    t.color(color)
    # turtle_drawer.right(90)
    t.fd(l)
    t.left(1)
    if abs(t.pos())<1:
        break
    

screen = Screen()
screen.exitonclick()


