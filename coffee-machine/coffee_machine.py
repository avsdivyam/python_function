resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

money_collected = 0

def report(resources, money_collected):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money_collected:.2f}")

def check_resources(coffee_type, resources):
    if coffee_type == "espresso":
        return resources["water"] >= 50 and resources["coffee"] >= 18
    elif coffee_type == "latte":
        return resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24
    elif coffee_type == "cappuccino":
        return resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24
    return False

def generate_bill(coffee_type):
    if coffee_type == "espresso":
        return 1.5
    elif coffee_type == "latte":
        return 2.5
    elif coffee_type == "cappuccino":
        return 3.0
    return 0

def process_payment(coffee_type, money_collected):
    cost = generate_bill(coffee_type)
    print(f"Your bill is ${cost:.2f}")
    money_collected += cost
    return money_collected

def process_coffee(coffee_type, resources, money_collected):
    if coffee_type == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
    elif coffee_type == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
    elif coffee_type == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24

    money_collected = process_payment(coffee_type, money_collected)
    print(f"Here is your {coffee_type}. Enjoy!")
    return resources, money_collected

while True:
    user_input = input("What would you like? (coffee/report/off): ").strip().lower()

    if user_input == "coffee":
        prompt = int(input("What would you like? \n 1: espresso\n 2: latte\n 3: cappuccino\n"))

        if prompt == 1:
            user_input = "espresso"
        elif prompt == 2:
            user_input = "latte"
        elif prompt == 3:
            user_input = "cappuccino"
        else:
            print("Invalid selection. Please try again.")
            continue


    if user_input == "off":
        print("Turning off the coffee machine. Goodbye!")
        break

    if user_input == "report":
        report(resources, money_collected)
        continue

    if user_input in ["espresso", "latte", "cappuccino"]:
        if check_resources(user_input, resources):
            resources, money_collected = process_coffee(user_input, resources, money_collected)
        else:
            print("Sorry, not enough resources to make your drink.")
    else:
        print("Invalid selection. Please try again.")
