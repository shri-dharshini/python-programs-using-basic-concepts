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


# function to check if the resources in the machiene are sufficient or not
def sufficient_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


#quarter=0.25, dime=0.10, nickles=0.05, pennies=0.01
#function to calculate amount paid by the user
def process_coins():
    print('Insert coins.')
    quarters=int(input('How many quarters?: '))
    dimes=int(input('How many dimes?: '))
    nickles=int(input('How many nickles?: '))
    pennies=int(input('How many pennies?: '))
    total= quarters*0.25 + dimes*0.1 + nickles*0.05 +pennies*0.01
    return total
    

#function to check if entered money is sufficient to proces order, return changes if exists
def success_transac(amount, cost):
    global profit
    if amount==cost:
        profit+= cost
        return True
    elif amount <cost:
        print('Money entered is not sufficient, try again.')
        return False
    else:
        change=amount-cost
        print(f'Change amount: {round(change,2)}')
        profit+=cost
        return True
    

def make_coffee(choice, ingredients):
    for item in ingredients:
        resources[item]-= ingredients[item]
    print(f'Here is your {choice}, Enjoy!')



while True:
    choice=input('What would you like? (espresso/latte/cappuccino): ').lower()
    if choice=='off':
        break
    elif choice=='report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        if sufficient_resources(drink['ingredients']):
            payment=process_coins()
            if success_transac(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
