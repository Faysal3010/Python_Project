from turtle import Turtle,Screen
import random


t = Turtle()
s = Screen()
t.speed('fastest')
x=0
t.width(2)
# s.colormode(255)
# def random_color():
#                a=random.randint(0,255)
#                b=random.randint(0,255)
#                c=random.randint(0,255)
#                return (a,b,c)

for i in range(0,36):
    # t.color(random_color())
    # t.left(i)
    t.circle(100)
    current=t.heading()
    print(current)
    t.setheading(current+10)

s.exitonclick()
