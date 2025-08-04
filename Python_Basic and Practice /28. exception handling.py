#exception = events detected during execution that interrupt the flow of a program

try:
 x=int(input())
 y=int(input())# if y =0 get error
 print(x/y)
except ZeroDivisionError:
 print("You can't divide by zero")

# except Exception:
#  print("something went wrong :(")
except ValueError as e:
 print(e)
 print("Enter only numbers plz")
# else:
# finally:  