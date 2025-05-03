from turtle import Turtle, Screen
import random


t = Turtle()
s = Screen()
t.width(10)
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
angles = [0, 90, 180, 270]
t.speed('fastest')

for _ in range(1000):
    t.color(random.choice(colors))
    x = random.choice(angles)
    t.setheading(x)
    t.fd(30)


s.exitonclick()
