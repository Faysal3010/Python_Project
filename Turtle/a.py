from turtle import Turtle,Screen

pro=Turtle()

def ghuro():
    while True:
        pro.forward(200)
        pro.left(170)
        if abs(pro.pos())<1:
            break

pro.shape("arrow")
pro.color("red")
ghuro()
my_screen=Screen()
my_screen.exitonclick()
