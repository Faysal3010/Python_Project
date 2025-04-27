from turtle import Turtle,Screen

pro=Turtle()

def ghuro():
    for step in range(100):
        for c in ("red","green","blue","orange"):
            pro.color(c)
            pro.forward(step)
            pro.left(30)


pro.shape("arrow")
# pro.color("red")
ghuro()
my_screen=Screen()
my_screen.exitonclick()
