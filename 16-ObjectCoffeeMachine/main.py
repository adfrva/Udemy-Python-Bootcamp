from platform import machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome to the Python Cafe")

##Initialize coffe maker, money machine, and menu objects

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

machine_off = False

while not machine_off:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}) ")

    if user_input.lower() == "off":
        machine_off = True
        print("Goodbye")
    elif user_input.lower() == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        
        drink_choice = menu.find_drink(user_input.lower())
        resource_sufficient = coffee_maker.is_resource_sufficient(drink_choice)

        if resource_sufficient:
            
            if money_machine.make_payment(drink_choice.cost):
                coffee_maker.make_coffee(drink_choice)
