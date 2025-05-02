from turtle import Turtle,Screen
import random

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
sc=Screen()
t=Turtle()
l=100
t.width(3)
for i in range(3,11):
    t.color(random.choice(colors))
    while True:
        t.fd(l)
        t.left(360/i)
        if abs(t.pos())<1:
            break
for i in range(3,11):
    t.color(random.choice(colors))
    while True:
        t.fd(l)
        t.right(360/i)
        if abs(t.pos())<1:
            break

print(t.pos())
sc.exitonclick()
