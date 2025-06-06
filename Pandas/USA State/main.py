from turtle import Turtle,Screen
import pandas as pd

s=Screen()
t=Turtle()

s.title("U.S.A STATES")
img="Pandas/blank_states_img.gif"

s.addshape(img)
t.shape(img)

data=pd.read_csv("Pandas/50_states.csv")
all_state_list=data.state.to_list()
total_state=len(all_state_list)
guess_state=[]

while len(guess_state)<total_state:
    value=s.textinput(f"{len(guess_state)}/{total_state} Guess the state","Input: ").title()
    if value=='Exit':
        break
    elif value in all_state_list:
        guess_state.append(value)
        x_y=Turtle()
        x_y.hideturtle()
        x_y.penup()
        data_state=data[data.state==value]
        x_y.goto(int(data_state.x),int(data_state.y))
        x_y.write(value)




# def mouse_coor(x,y):
#     print(x,y)
# s.onscreenclick(mouse_coor)
# s.mainloop()