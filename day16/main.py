from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from essential import sleep, clear

menu = Menu()
coffe_machine = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == "off":
        is_on = False
    elif order == "report":
        coffe_machine.report()
        money_machine.report()
    else:
        if menu.find_drink(order):
            drink = menu.find_drink(order)
            if coffe_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffe_machine.make_coffee(drink)
    sleep(2)
    clear()