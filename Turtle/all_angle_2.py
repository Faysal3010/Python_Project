from turtle import Turtle,Screen

t=Turtle()
s=Screen()

def shape_(side):
    angle=360/side
    for _ in range (side):
        t.fd(100)
        t.left(angle)

for side in range(3,26):
    shape_(side)

s.exitonclick()
