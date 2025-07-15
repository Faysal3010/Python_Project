# nested loops = The "ïnner" will  finish all of it's itertions before finishing one iteration of the "outer loop"

# row=int(input("How many rows: "))
# column=int(input("How many columns: "))
# symbol=input("Symbol: ")

# for i in range(row):
#     for j in range(column):
#         print(symbol,end="")
#     print("")   


row=int(input("How many rows: "))
column=int(input("How many columns: "))
symbol=input("Symbol: ")

for i in range(row):
    for j in range(column):
        print(symbol,end="")
    print("")    
