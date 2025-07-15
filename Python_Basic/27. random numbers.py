# import random
# import time
# while True:
#  x=random.randint(1,6)
# #  y=random.random()
#  time.sleep(.3)
#  print(x,end=' ')
# #  print('{:.2f}'.format(y),end='   ')


# import random
# print("Guess random 1 to 5 and to stop press '0'")
# while True:
#  x=random.randint(1,5)
#  y=int(input("Guess random number: "))
#  if x==y:
#   print("Corret random")
#  elif y==0:
#    break
#  else:
#    print("Wrong")

import random
import time
while 1:
 myList=['Faysal','Masuk','Proyash','Ovi','Sami']
 cards=[1,2,3,4,5,'a','b','c','d','e','f','g','h']
 x=random.choice(myList)
 random.shuffle(cards)
 time.sleep(.3)
 print(x)
 print(cards)


 