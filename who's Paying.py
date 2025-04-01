import random
persons=input("Enter the members: ")
person=persons.split(", ")
print(f"{random.choice(person)} is going to buy the meal today!")
