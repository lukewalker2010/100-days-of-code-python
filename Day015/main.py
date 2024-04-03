 # Coffee Machine Code

# 3 Hot Flavores

# Coin Opperated

# Espresso - 50ml Water, 19g coffee, 0 Milk - $1.50

# Latte - 200ml Water, 24g, Coffee, 150ml Milk - $2.50

# Cappuccion - 250ml Water, 24g Coffee, 100ml Milk - $3.00

# Resources - Water 300ml, Milk 200ml, Coffee 100g, Money

# Print report on resources

# Check resources are sufficent

# check if money is sufficent

# check transaction successful

# make drink and deduct resources

# Coins, Penny, Nickle, Dime, Quarter

# TODO: 1. Print a report of all the coffee machine resoucres.
# TODO: 2. Check resources sufficent to make drink order.

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

def is_resource_sufficent(order_ingredients):
    """"Returns True when order can be made and False if incredients are insufficent"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or false if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Detuct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficent(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])