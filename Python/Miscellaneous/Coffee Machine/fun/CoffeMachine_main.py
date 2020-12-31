# Coffee Machine project

import Coffee_menu
profit: int = 0

def choice():
    """Function to pick a coffee"""
    choice: str = input("What cofee would you like? espresso, latte, cappucino?\n")
    return choice

def resource_check(order_ing):
    for item in order_ing:
        if order_ing[item] > Coffee_menu.RESOURCES[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True

def get_payment():
    print('Please insert coins')
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_payment_successful(money_received, cost):
    if money_received >= cost:
        change = round(money_received - cost,2)
        print(f"Your change: {change}")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, that's not enough. Money refunded.")
        return False

def make_cofee_drink(drink_name, ingredients):
    for item in ingredients:
        Coffee_menu.RESOURCES[item] -= ingredients[item]
    print(f"Here's your {drink_name}. Enjoy your drink!")

def coffee_making_process() -> object:
    """Whole process of cofee making"""
    make_coffee_process = True
    while make_coffee_process:
        coffee = choice()
        if coffee == 'off':
            make_coffee_process = False
        elif coffee == 'report':
            print(f"Water: {Coffee_menu.RESOURCES['water']}\nMilk: {Coffee_menu.RESOURCES['milk']}\nCofee: {Coffee_menu.RESOURCES['coffee']}\nMoney: $ {profit}")
        else:
            drink = Coffee_menu.MENU[coffee]
            if resource_check(drink["ingredients"]):
                payment = get_payment()
                if is_payment_successful(payment, drink["cost"]):
                    make_cofee_drink(coffee,drink['ingredients'])

coffee_making_process()
