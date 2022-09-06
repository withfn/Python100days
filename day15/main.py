from essential import clear, sleep

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_drink():
    while True:
        user_drink = input("What would you like? (espresso/latte/cappuccino): ")
        if user_drink == "off": return "off"
        if user_drink == "report": return user_drink
        if user_drink in MENU: return user_drink
        print("Sorry, We don't have this drink. Try again.")
        sleep(2)

def check_resources(drink):
    for item in drink:
        if drink[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction_successful(payment, drink_cost):
    global MONEY
    if payment > drink_cost:
        change = user_money - drink_cost
        print("Here is {:.2f} in change." .format(change))
    elif payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    MONEY += drink_cost
    return True
    
def make_coffee(drink, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink} ☕️. Enjoy!")
    sleep(2)
    clear()

def report():
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: ${MONEY}"

MONEY = 0
is_on = True
while is_on:
    user_drink = check_drink()
    if user_drink == 'off':
        print("Machine is off")
        is_on = False    
    elif user_drink == 'report':
        print(report()) 
    else:
        drink = MENU[user_drink]
        if check_resources(drink['ingredients']):
            user_money = (process_coins())
            if transaction_successful(user_money, drink["cost"]):
                make_coffee(user_drink, drink['ingredients'])
