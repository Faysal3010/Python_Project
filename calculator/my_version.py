import os
clear=lambda:os.system('cls')
clear()
def res(num,num1,op)->int:
  if op=='/':
   return num/num1
  elif op=='+':
   return num+num1
  elif op=='-':
   return num-num1
  elif op=='*':
   return num*num1
  
def yes(remain):
    op=input("Pick an operation: ")
    num1=int(input("What's the next number?: "))
    value=res(remain,num1,op)
    print(f"{remain} {op} {num1} = {value}")
    return value

def new():
    num=int(input("What's the first number?: "))
    op=input("Pick an operation: ")
    num1=int(input("What's the next number?: "))
    remain=res(num,num1,op)
    print(f"{num} {op} {num1} = {remain}")
    return remain

num=int(input("What's the first number?: "))
print("'+' , '-' , '*' , '/'")
op=input("Pick an operation: ")
num1=int(input("What's the next number?: "))
remain=res(num,num1,op)
print(f"{num} {op} {num1} = {remain}")

run=True
while run:
  continue_calculation=input(f"Type 'y' to continue calculationing with {remain}, or type 'n' to start a new calculation: ")
  if continue_calculation=='y':
    remain=yes(remain)
  elif continue_calculation=='n':
    remain=new()  
