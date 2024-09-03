from importlib.resources import Resource


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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

machine_status = True

def report():
    print(f"Water:{resources['water']}ml")
    print(f"Milk:{resources['milk']}ml")
    print(f"Coffee:{resources['coffee']}g")
    print(f"Money:{profit}$")

def transaction_status(drink_cost,payment):
    """Return True when payment is accepted and False when not"""
    if drink_cost < payment:
        change = payment - drink_cost
        print(f"Here is the change {change}$")
        global profit
        profit+= drink_cost
        return True
    
    else:
        print("Sorry that's not enough money. Money returned")
        return False

def process_coins():
    """Return the total calculted from inserted coins"""
    total = int(input("How many quaters ? : "))*0.25
    total += int(input("How many dimes ? : "))*0.1
    total += int(input("How many nickles ? : "))*0.05
    total += int(input("How many pennies ? : "))*0.01

    return total

def make_coffe(drink_name , order_ingredients):
    """Deducts the required ingredeints from the resources"""
    for item in order_ingredients:
        resources[item]= resources[item] - order_ingredients[item]

    print(f"Here is your {choice} , Enjoy :)")

def resource_sufficient(order_ingredient):
    """Return True when order can be made , False if ingredients are insuffiecint"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough{item}.")
            return False
    return True

while machine_status:

    choice = input ("What would you like? (espresso/latte/cappuccino):").lower()

    if choice == 'off':
        machine_status = False
    elif choice == 'report':
        report()
    else :
        drink = MENU[choice]
        if resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_status(drink['cost'] ,payment) :
                make_coffe(choice, drink["ingredients"])

        


