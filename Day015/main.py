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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def change(quarters, dimes, nickles, penny, choice):
    total = quarters*0.25 + dimes*0.10 + nickels*0.05 + penny*0.01
    return total

coins = [0.01, 0.05, 0.10, 0.35]

choice = input("What would you like? (espresso/latte/cappuccino): ")
print("Please insert coins.")

quarters = int(input("How many quarters?: "))
dimes = int(input("How many dimes?: "))
nickels = int(input("How many nickles?: "))
penny = int(input("How many pennies?: "))

print(f"Heree is {change(quarters, dimes, nickels, penny, choice)} in change.")
print(f"Here is your {choice}. Enjoy!")
