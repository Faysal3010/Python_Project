
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name=(name1+name2).lower()
t=name.count('t')
r=name.count('r')
u=name.count('u')
e=name.count('e')
l=name.count('l')
o=name.count('o')
v=name.count('v')
e=name.count('e')
true=t+r+u+e
love=l+o+v+e
print(f"{true}{love}%")  
