import random
import blackjack

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def enough_resources(drink_ingredients):
    """ Checks machine for sufficient resources and returns T/F """
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f'Sorry, there is not enough {ingredient}.')
            return False
    return True


def insert_coins(drink_cost):
    """ Asks user to insert coins and returns amount they paid"""
    print(f'Your drink costs ${drink_cost}.')
    quarters = int(input('Please insert quarters: '))
    dimes = int(input('Please insert dimes: '))
    nickels = int(input('Please insert nickels: '))
    pennies = int(input('Please insert pennies: '))
    total_paid = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total_paid


def enough_money(user_paid, drink_cost):
    """ Check if user inserted enough money and show change -- return T/F """
    global profit
    if user_paid >= drink_cost:
        change = round(user_paid - drink_cost, 2)
        print(f'Your change is : ${change}')
        profit += drink_cost
        return True
    else:
        print('Sorry, you didn\'t put in enough money. Please try again.')
        return False


def make_coffee(user_drink, drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f'Here is your {user_drink}, enjoy!')


def play_blackjack():
    blackjack.play()


profit = 0

done = False
while not done:

    user_choice = input('\n What kind of coffee would you like: espresso, latte, or cappuccino? ')

    if user_choice == 'off':
        print('Thanks for using the coffee machine!')
        done = True

    elif user_choice == 'status':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Profit: ${profit}')

    elif user_choice == 'refill':
        random_num = random.randint(1, 10)
        if random_num >= 7:
            resources["water"] += 500
            resources["milk"] += 400
            resources["coffee"] += 300
            print('The machine has been refilled!')
        else:
            print('You\'re out of supplies!')
            print('You\'ll need to win some money in blackjack before you can get more...')
            play_blackjack()
            resources["water"] += 500
            resources["milk"] += 400
            resources["coffee"] += 300
            print('The machine has been refilled!')

    elif user_choice == 'latte' or user_choice == 'espresso' or user_choice == 'cappuccino':
        drink = MENU[user_choice]
        resource_check = (enough_resources(drink["ingredients"]))
        if resource_check:
            user_paid = insert_coins(drink["cost"])
            money_check = (enough_money(user_paid, drink["cost"]))
            if money_check:
                make_coffee(user_choice, drink["ingredients"])

    else:
        print('Sorry, that isn\'t a valid input.')
