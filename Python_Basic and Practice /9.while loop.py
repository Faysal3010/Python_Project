#while loop: a statement that will execute it's block of code, as long as it's condition remains true

# while (1):
#     print("Help, I'm stuck in a loop!")

# name=""
# while len(name)==0:
#     name=input("Enter Your Name: ")
# print("Hello,",name) 
   
name=None
while not name:
    name=input("Enter Your Name: ")
print("Hello,",name)    


import time
n=int(input())
while n:
    time.sleep(1)
    n-=1
    print(n)
print("Done!")    