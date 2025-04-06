import os
clear=lambda:os.system('cls')
list={int:str}
print("Welcome to the secret auction program")
max_value=0
is_end=True
while is_end:
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    list[bid]=name
    max_value=max(max_value,bid)
    bidder=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if bidder=='no':
        clear()
        is_end=False
        print(f"{list[max_value]} is winning the bid by ${max_value}")
    else:
        clear()
