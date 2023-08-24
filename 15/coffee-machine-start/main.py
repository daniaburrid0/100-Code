# Global Constants
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

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

# Global Variables
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def main():
    """Coffee Machine"""
    # start machine
    start = "on"
    start_machine(start)


def start_machine(start):
    """Start the coffee machine"""
    # will loop until machine is turned off with the off command
    while start == "on":
        # ask user for input
        order = ask_the_user()
        # check if the user wants to turn off the machine
        if order == "off":
            start = "off"
            print("Turning off the machine.")
            continue
        # check if the user wants to see the report
        elif order == "report":
            print_report()
            continue
        # Check the resources for the order
        if check_resources(order):
            # Ask the user for money
            money_input = ask_for_money()
            # Check if the user has enough money
            if money_input <= MENU[order]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                # Make the coffee
                make_coffee(order)
                update_resources(order)
                give_change(order, money_input)
                continue
        else:
            print("Sorry there is not enough resources.")
            continue


def ask_the_user():
    """Ask the user for input"""
    while True:
        order = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        if check_order(order):
            return order
        else:
            print("Please enter a valid order.")
            continue


def check_order(order):
    """Check if the order is valid"""
    return order in {"espresso", "latte", "cappuccino", "off", "report"}


def check_resources(order):
    """Check the resources for the order"""
    for ingredient, amount in MENU[order]["ingredients"].items():
        if resources[ingredient] < amount:
            return False
    return True


def ask_for_money():
    total = 0
    for coin, value in COINS.items():
        while True:
            try:
                count = int(input(f"How many {coin}?: "))
                total += count * value
                break
            except ValueError:
                print("Please enter a valid number.")
    return total


def give_change(order, money_input):
    """Give the change"""
    change = round(money_input - MENU[order]["cost"], 2)
    print(f"Here is ${change} in change.")


def make_coffee(order):
    print(f"Here is your {order}. Enjoy!")


def update_resources(order):
    """Update the resources"""
    global resources
    for ingredient, amount in MENU[order]["ingredients"].items():
        resources[ingredient] -= amount
    resources["money"] += MENU[order]["cost"]


def print_report():
    """Print the report"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


# Start the program
if __name__ == "__main__":
    main()
