MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "coffee": 100
}

is_machine_off = False


def coffee_machine():
    def resources_management(coffee):
        if coffee in MENU:
            if coffee == 'espresso':
                for i in resources:
                    resources[i] -= MENU['espresso']['ingredients'][i]
            elif coffee == 'latte':
                for i in resources:
                    resources[i] -= MENU['latte']['ingredients'][i]
            elif coffee == 'cappuccino':
                for i in resources:
                    resources[i] -= MENU['cappuccino']['ingredients'][i]
            for i in resources:
                if resources[i] < 0:
                    print("Sorry, coffee machine is out of resources currently 😔")
                    coffee_machine()

    def resource_remaining():
        for i in resources:
            if resources[i] < 0:
                resources[i] = "0"
            else:
                print(i, resources[i])

    def transactions():
        total = 0
        print("please insert coins 🪙: ")
        total += int(input("How many quarters: ")) * 0.25
        total += int(input("How many dimes: ")) * 0.1
        total += int(input("How many nickles: ")) * 0.05
        total += int(input("How many pennies: ")) * 0.01

        global profit
        if total != 0:
            if user_selected_coffee == 'espresso' and total >= MENU['espresso']['cost']:
                profit += MENU['espresso']['cost']
                total -= MENU['espresso']['cost']
                print(f"{round(total, 2)}$ is your change")
                print(f"Enjoy Your {user_selected_coffee} ☕️")

            elif user_selected_coffee == 'latte' and total >= MENU['latte']['cost']:
                profit += MENU['espresso']['cost']
                total -= MENU['latte']['cost']
                print(f"{round(total, 2)}$ is your change")
                print(f"Enjoy Your {user_selected_coffee} ☕️")

            elif user_selected_coffee == 'cappuccino' and total >= MENU['cappuccino']['cost']:
                profit += MENU['espresso']['cost']
                total -= MENU['cappuccino']['cost']
                print(f"{round(total, 2)}$ is your change")
                print(f"Enjoy Your {user_selected_coffee} ☕️")
            else:
                print("Coins are not sufficient. Try again 🙅‍")
                coffee_machine()

    user_selected_coffee = input("What would you like? (espresso/latte/cappuccino) 👉 ").lower()

    if user_selected_coffee == 'off':
        return True
    elif user_selected_coffee == "report":
        print("Resources: ")
        resource_remaining()
        global profit
        print(f"Income {profit}$")
    else:
        resources_management(user_selected_coffee)
        transactions()


while not is_machine_off:
    if coffee_machine() == True:
        print("Thank You 🙂")
        break

