from turtle import Turtle,Screen

t=Turtle()
s=Screen()

a=t.penup()
b=t.pendown()

def up():
    t.fd(10)
def down():
    t.bk(10)
def left():
    t.left(90)
def right():
    t.right(90)

    
s.onkey(key='Up',fun=up)
s.onkey(key='Down',fun=down)
s.onkey(key='Left',fun=left)
s.onkey(key='Right',fun=right)
s.listen()

s.exitonclick()
