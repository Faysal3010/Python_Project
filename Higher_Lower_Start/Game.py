import random
import os
from Game_Data import data
from art import logo,vs

clear=lambda:os.system("cls")
score=0 

def operate():
    global score
    i=random.choice(data)
    j=[j for j in data if j!=i]
    # print(i)
    i=data.index(i)
    # print(i)
    print(f"Compare A: {data[i]["name"]}, a {data[i]["description"]}, from {data[i]["country"]}.")
    print(vs)
    j=random.choice(j)
    # print(j)
    j=data.index(j)
    print(f"Compare B: {data[j]["name"]}, a {data[j]["description"]}, from {data[j]["country"]}.")
    value=input("Who has more follower? Type 'A' or 'B': ")
    if data[i]['follower_count']>data[j]['follower_count'] and value=='A':
        score+=1
        return True
    elif data[i]['follower_count']<data[j]['follower_count'] and value=='B':
        score+=1
        return True
    # elif value!='A' or value!='B':
    #     print("Enter the right value! Plz")
    #     return True
    else:
        clear()
        print(logo)
        print("Sorry, that's wrong. Final score:",score)
        return False

run=True
while run:
    clear()
    print(logo)
    print("You're right! Current score:",score)
    run=operate()
    



