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

# TODO: 4) Check resources sufficient?
def check_resources(order):
    if order in MENU:
        order_ingredients = MENU[order]["ingredients"]
        for key in order_ingredients:
            if resources[key] < order_ingredients[key]:
                print(f"Sorry there is not enough {key}.")
                return False
    else:
        print("Pleas Select from the menu!!")
        return False
    return True


# TODO: 5) Process coins
def process_coins():
    print("Please insert coins.")
    quarters = input("How Many Quarters? ")
    if quarters == "off":
        return "off"
    dimes = input("How Many Dimes? ")
    if dimes == "off":
        return "off"
    nickles = input("How Many Nickles? ")
    if nickles == "off":
        return "off"
    pennies = input("How Many Pennies? ")
    if pennies == "off":
        return "off"
    quarters = int(quarters)
    dimes = int(dimes)
    nickles = int(nickles)
    pennies = int(pennies)
    total_paid_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total_paid_money


# TODO: 1) Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO: 2) Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: 3) Print report.
# TODO: 6) Check transaction successful?
program_state = "on"
while program_state == "on":
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        program_state = "off"
    elif order == "report":
        for key in resources:
            unit = 'ml'
            if key == "coffee":
                unit = 'g'
            print(f"{key}: {resources[key]}{unit}")
        print(f"Money: ${profit}")
    else:
        if not check_resources(order):
            continue
        else:
            total_paid_money = process_coins()
            if total_paid_money == "off":
                program_state = "off"
            elif total_paid_money < MENU[order]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                profit += MENU[order]["cost"]
                charge = round((total_paid_money - MENU[order]["cost"]),2)
                order_ingredients = MENU[order]["ingredients"]
                if charge > 0:
                    print(f"Here is ${charge} dollars in change")
# TODO: 7) Make Coffee.
                for key in order_ingredients:
                    resources[key] -= order_ingredients[key]
                print(f"Here is your {order}☕. Enjoy!")
