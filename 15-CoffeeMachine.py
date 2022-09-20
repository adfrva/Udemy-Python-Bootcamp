print("Welcome to the Python Cafe")

MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
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
    "money": 0
}

def print_report():
    for i in resources:
        print(f"{i}: {resources[i]}")

def check_resources(choice):
    #First value is boolean to track if all resources are still available. If there are not enough resources, second val in list displays what resource is missing
    resource_check = [True, ""]

    milk = MENU[choice]["ingredients"]["milk"]
    water = MENU[choice]["ingredients"]["water"]
    coffee = MENU[choice]["ingredients"]["coffee"]

    if milk > resources["milk"]:
        resource_check[0] = False
        resource_check[1] = "milk"
    elif water > resources["water"]:
        resource_check[0] = False
        resource_check[1] = "water"
    elif coffee > resources["coffee"]:
        resource_check[0] = False
        resource_check[1] = "coffee"

    return resource_check

def calculate_change(quarters, dimes, nickels, pennies, drink_choice):
    change_total = 0

    change_total = (.25 * quarters) + (.10 * dimes) + (.05 * nickels) + (.01 * pennies)

    return change_total

def make_coffee(drink, change_total):
    change_difference = round(change_total - MENU[drink_choice]["cost"], 2)
    resources["money"] += change_total - change_difference

    if change_difference > 0:
        print(f"Here is your ${change_difference} dollars in change")

    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    resources["water"] -= MENU[drink]["ingredients"]["water"]

    print(f"Here is your {drink}. Enjoy!")

machine_off = False

while not machine_off:
    drink_choice = input("What would you like? (espresso, latte, cappuccino): ")

    if(drink_choice.lower() == "off"):
        machine_off = True
        print("Goodbye!")

    elif drink_choice.lower() == "report":
        print_report()

    else:
        resource_check = []
        resource_check = check_resources(drink_choice)

        if resource_check[0] == False:
            print(f"Sorry there is not enough {resource_check[1]}")

        else:
            drink_cost = MENU[drink_choice]["cost"]

            print(f"That will cost ${drink_cost}")
            print("Please insert coins.")

            quarters_put = int(input("How many quarters? "))
            dimes_put = int(input("How many dimes? "))
            nickels_put = int(input("How many nickels? "))
            pennies_put = int(input("How many pennies? "))

            change_total = calculate_change(quarters_put, dimes_put, nickels_put, pennies_put, drink_choice)

            if change_total < drink_cost:
                print("Sorry that's not enough money. Money refunded")
            else:
                make_coffee(drink_choice, change_total)
                