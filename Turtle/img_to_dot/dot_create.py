from turtle import Turtle,Screen
from img_to_rgb import rgb_colors
import random
colors=rgb_colors

print(len(colors))
t=Turtle()
s=Screen()
t.speed("fastest")
s.colormode(255)
x=0
y=15
for _ in range (100):
    t.color(random.choice(colors))
    t.dot(10)
    t.up()
    t.fd(15)
    t.pd()
    x+=1
    if x==10:
        x=0
        t.up()
        t.goto(x,y)
        y+=15


s.exitonclick()

