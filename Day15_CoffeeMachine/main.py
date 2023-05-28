from menu import *

def orderRequest():
    global order
    order = input("What would you like? (espresso/latte/cappuccino): ")

def printReport():
    global resources
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${money:.2f}")

def checkResources():
    global order, MENU
    ingredientList = ["water", "milk", "coffee"]
    if order == "espresso":
        ingredientList = ["water", "coffee"]
    for i in ingredientList:
        if MENU[order]["ingredients"][i] > resources[i]:
            print(f"Sorry, not enough {i}.")
            return False
    return True

def checkCoins():
    global order, change
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    sum = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if sum > MENU[order]["cost"]:
        change = sum - MENU[order]["cost"]
        return True
    else:
        return False

def useResources():
    global order, resources
    ingredientList = ["water", "milk", "coffee"]
    if order == "espresso":
        ingredientList = ["water", "coffee"]
    for i in ingredientList:
        resources[i] = resources[i] - MENU[order]["ingredients"][i]

status = "on"
money = 0.0
# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while status == "on":
    order = ""
    change = 0.0
    orderRequest()

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.


# TODO: 3. Print report. When the user enters “report” to the prompt, a report should be
#  generated that shows the current resource values
    while order != "espresso" and order != "latte" and order != "cappuccino":
        if order == "report":
            printReport()
            orderRequest()
        elif order == "off":
            status = "off"
            break
        else:
            print("Please enter in a valid order.")
            order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "off":
        status = "off"
        break

# TODO: 4. Check resources sufficient?
    if checkResources() == True:
        if checkCoins() == True:
            useResources()
            money = money + MENU[order]["cost"]
            print(f"Here is {change:.2f} in change.")
            print(f"Here is your {order}. Enjoy!")


# TODO: 5. Process coins. a. If there are sufficient resources to make the drink selected, then the program should
#  prompt the user to insert coins

# TODO: 6. Check transaction successful?

# TODO: 7. Make Coffee
