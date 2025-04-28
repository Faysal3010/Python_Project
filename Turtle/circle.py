from turtle import Turtle,Screen

def rounding():
    while True:
        x.fillcolor("black")
        for c in ("red","blue","green","pink"):
            x.color(c)
            x.forward(100)
            x.left(100)
            x.circle(50)
            # x.left(100)
            if abs(x.pos())<1:
                return

x=Turtle()
x.shape("classic")
rounding()

my_screen=Screen()
my_screen.exitonclick()
