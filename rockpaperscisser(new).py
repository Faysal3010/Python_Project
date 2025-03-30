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

while 1:
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    x=int(input())
    ascll(x)
    computer=random.randint(0,2)
    print("computer chose:",computer)
    ascll(computer)

    if x>2 or x<0:
        print("You typed an invalid number, you lose!")
    if x==computer:
       print("Draw") 
    elif x==0 and computer==2:
        print("You win!")
    elif computer==0 and x==2:
        print("You lose")
    elif x<computer:
        print("You lose")
    else:
        print("You win!")


