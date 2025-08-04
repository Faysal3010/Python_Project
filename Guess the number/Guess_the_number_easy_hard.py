
import random

def easy(random_value):
  for i in range(1,11):
    print(f"You have {11-i} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess<random_value:
      print("Too low.\nGuess again.")
    elif guess>random_value:
      print("Too high.\nGuess again.")
    else:
      print(f"You got it! The answer was {random_value}.")
      return
  print ("You've run out of guesses, you lose")

def hard(random_value):
  for i in range(1,6):
    print(f"You have {6-i} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess<random_value:
      print("Too low.\nGuess again.")
    elif guess>random_value:
      print("Too high.\nGuess again.")
    else:
      print(f"You got it! The answer was {random_value}.")
      return
  print ("You've run out of guesses, you lose")
  
def start():
    random_value=random.randint(1,100)
    print(f"Pssst, the correct answer is {random_value}")
    chose=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if chose=='easy':
     easy(random_value)
    elif chose=='hard':
      hard(random_value)
    else: start()

print("""Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.""")
start()
