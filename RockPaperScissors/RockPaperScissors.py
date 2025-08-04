import random

def ascll(x:int):
    if x==0:
     print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''')
    elif x==1:
     print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    ''')
    else:
     print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')


print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
x=int(input())
if x>2: exit()
ascll(x)
computer=random.randint(0,2)
print("computer chose:",computer)
ascll(computer)
if x<(x+1)==computer:
    print("You lose") 
    exit()
else:
    if x==computer:
     print("Draw")
    else:
     print("You win")
    exit()
if x==0 and computer==2:
    print("You win")
    exit()
else:
    print("You lose") 
    exit()

