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

def is_enought_resource(ingredients):
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"We don't have enough {ingredient}")
            return(False)
    return(True)

def money(cost):
    print(f"Please,pay for coffee {cost}")
    quarters = int(input("How many quarters"))
    dimes = int(input("How many dimes"))
    nickels = int(input("How many nickels"))
    pennies = int(input("How many pennies"))
    money_amounght = (quarters*0.25)+(dimes*0.1)+(nickels*0.05)+(pennies*0.01)
    if money_amounght < cost:
        print(f"Sorry, you don't have enough")
        return False
    else:
        print(f"Here is your charge {money_amounght - cost}")
        return True



def makeCoffee (CoffeType):
    if CoffeType == 'resources':
        print(resources)
        return('')
    if not money(MENU[CoffeType]["cost"]) :
        return('')
    else:
        print(f'Here are your {CoffeType}')
        for resourse in MENU[CoffeType]["ingredients"]:
            resources[resourse] = resources[resourse] - MENU[CoffeType]['ingredients'][resourse]





coffee_client = input("What kind of coffee(espresso/latte/cappuccino)")
if coffee_client == 'resources':
    makeCoffee (coffee_client)
else:
    if is_enought_resource(MENU[coffee_client]["ingredients"]):
        makeCoffee (coffee_client)
