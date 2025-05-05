from turtle import Screen, Turtle
import random

s = Screen()
s.setup(height=400, width=1000)
y_position = [-125, 125, -75, 75, -25, 25]
colours = ['red', 'orange', 'green', 'blue', 'purple', 'black']
all_t = []




user_input=s.textinput(title="Who will win the race", prompt="Choose the colors('red'/'orange'/'green'/'blue'/'purple'/'black'): ")
if user_input in colours:
    is_on=True
else: exit()

margin=Turtle()
margin.width(5)
margin.penup()
margin.goto(x=-450,y=210)
margin.pendown()
margin.goto(x=-450,y=-210)
margin.penup()
margin.goto(x=450,y=210)
margin.pendown()
margin.goto(x=450,y=-210)

def ran():
    return random.randint(0, 10)


for i in range(6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colours[i])
    t.goto(y=y_position[i], x=-450)
    all_t.append(t)
is_correct=''
while is_on:

    for turtle in all_t:
        turtle.fd(ran())
        if turtle.xcor() > 450:
            is_correct=(turtle.pencolor())
            is_on=False
            break


if user_input==is_correct:
    Turtle().write(f"You've won, The {is_correct} turtle is the winner ",font=("Arial",25,"bold"),align="center")
else: 
    Turtle().write(f"You've lost, The {is_correct} turtle is the winner",font=("Arial",25,"bold"),align="center")

s.exitonclick()
