from turtle import Turtle,Screen
sc=Screen()
t=Turtle()
l=50
t.width(5)
ang=50
while True:
    t.fd(l)
    t.pu()
    t.fd(l)
    t.pd()
    t.left(ang)
    if abs(t.pos())<1:
        break



print(t.pos())
sc.exitonclick()
