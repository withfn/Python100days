from essential import clear, sleep

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

clear()

#checks if the drink is on the menu or if it is an administrative command (report/off).
def check_drink():
    x = True
    while x:
        user_drink = input("What would you like? (espresso/latte/cappuccino): ")
        if user_drink == "off":
            print("In maintenance...")
            return "off"
        
        if user_drink == "report":
            return user_drink
        
        if user_drink in MENU:
            return user_drink
        
        print("Sorry, We don't have this drink. Try again.")
        sleep(2)

#checks if the machine has enough resources to make the drink.
def check_resources(drink):
    for item in drink:
        if drink[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return 'not enough'
    return 'enough'

#Receive customer coins and returns the total.
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total_coins = quarters + dimes + nickles + pennies
    return total_coins

#reduces resources according to the drink.
def make_coffee(drink):
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['milk'] -= MENU[drink]['ingredients']['milk']
    resources["coffee"] -= MENU[drink]['ingredients']['coffee']

#return informations of the resources.
def report():
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: ${MONEY}"

        
MONEY = 0
is_on = True

#coffee machine working
while is_on:
    #receives the drink chosen by the customer.
    user_drink = check_drink()
    if user_drink == 'off':
        is_on = False
        continue
    
    #print report of resources.
    elif user_drink == 'report':
        print(report())
    
    #Check if resources are enough.
    
    resources_suffient = check_resources(MENU[user_drink]['ingredients'])
    if resources_suffient == 'not enough':
        print('refuel the machine.')
        continue
    
    #Receive the client's money
    user_money = (process_coins())
    drink_cost = MENU[user_drink]['cost']
    if user_money > drink_cost:
        MONEY += drink_cost
        change = user_money - drink_cost
        print("Here is {:.2f} in change." .format(change))
    elif user_money < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        continue
    else:
        MONEY += drink_cost
    
    make_coffee(user_drink)
    print(f"Here is your {user_drink}. Enjoy!")
    
