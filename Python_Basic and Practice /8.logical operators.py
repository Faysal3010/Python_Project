#logical operators (and,or,not) = used to check if two or more conditional statements is true

temp=int(input("What is the temperature outside?: "))

# if temp>=0 and temp<=30:
#     print("The temperature outside is good today")
#     print("Go outside")
# elif temp<0 or temp>30:
#     print("The temperature outside is bad")
#     if temp<0:
#      print("The temperature outside is too low ❄️")    
#     elif temp>30:
#      print("The temperature outside is hot 🔥")


if not(temp>=0 and temp<=30):
    print("The temperature outside is bad")
    if temp<0:
     print("The temperature outside is too low ❄️")    
    elif temp>30:
     print("The temperature outside is hot 🔥")
    
    

elif not(temp<0 or temp>30):
 print("The temperature outside is good today")
 print("Go outside")
       