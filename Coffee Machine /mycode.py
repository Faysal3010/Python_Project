from random import choice

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources={
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
def make_coffe(ingredients):
     for item in ingredients:
         resources[item]-=ingredients[item]

def exchange(value):
    print(f"Here is ${value} in change.")

def  check_transaction(total,item):
    x= MENU[item]["cost"]
    if total>=x:
        resources["money"]+=x
        exchange_value=round(total-x,2)
        exchange(exchange_value)
        return True
    print(f"Sorry, {total} is not enough money. Money refunded.")
    return False


def is_resource_sufficient(ingredients):
    """ If all ingredients """
    for item in ingredients:
        # print(item,ingredients[item])
        if ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def  process_coins(item):
    """ return all inserted coins value in 'total' """
    print("Print insert coins.")
    total=int(input("How many quarters?: "))* 0.25
    total+=int(input("How many dimes?: "))* 0.10
    total+=int(input("How many nickles?: "))*0.05
    total += int(input("How many nickles?: ")) * 0.01
    return check_transaction(round(total,2),item)

is_on=True
while is_on:
    Choice=input("What would you like? (espresso/latte/cappuccino): ")
    if Choice=="off":
        is_on=False
    elif Choice=="report":
        for item in resources:
         print(f"{item} : {resources[item]}")
    else :
        drink=MENU[Choice]
        if is_resource_sufficient(drink["ingredients"]) and process_coins(Choice):
            make_coffe(drink["ingredients"])
            print("Here is your",Choice,"🍵. Enjoy !!")
