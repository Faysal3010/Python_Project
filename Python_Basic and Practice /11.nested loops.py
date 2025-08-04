# nested loops = The "ïnner" will  finish all of it's itertions before finishing one iteration of the "outer loop"

# row=int(input("How many rows: "))
# column=int(input("How many columns: "))
# symbol=input("Symbol: ")

# for i in range(row):
#     for j in range(column):
#         print(symbol,end="")
#     print("")   


'''row=int(input("How many rows: "))
column=int(input("How many columns: "))
symbol=input("Symbol: ")

for i in range(row):
    for j in range(column):
        print(symbol,end="")
    print("")    
'''

row=int(input("Enter row: "))
colum=int(input("Enter colum: "))

for i in range(row):
    for j in range(colum):
     if(i==j or i==0 or j==0 or i==colum-1 or j==row-1 or row-1==i+j):
        print("@",end='')
     else:
        print(' ',end='')   
    print()  