import random
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list=[]
print("Welcome to the PyPassword Generator!")

nr_letter=int(input("How many letters would you like in your password_list?: "))
nr_number=int(input("How many numbers would you like in your password_list?: "))
nr_symbol=int(input("How many symbols would you like in your password_list?: "))

for i in range(nr_letter):password_list.append(random.choice(letter))
for i in range(nr_number):password_list.append(random.choice(numbers))
for i in range(nr_symbol):password_list.append(random.choice(symbols))

random.shuffle(password_list)
password=""
for i in password_list:
    password+=i
print(f"password is: {password}")
