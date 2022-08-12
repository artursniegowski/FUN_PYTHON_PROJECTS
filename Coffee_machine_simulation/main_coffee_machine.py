from coffee_machine import CoffeeMachine



STARTER_CHOICE = 'What would you like? "espresso","latte","cappuccino": '


# to close the system
def off(object: CoffeeMachine) -> None:
    """shuting down the system"""
    object.shutting_down_maintenance()

def report(object: CoffeeMachine) -> None:
    """coffie machine reports its status"""
    object.make_report()

def espresso(object: CoffeeMachine) -> None:
    """coffee machine - prepares espresso"""
    object.order_coffee('espresso')

def latte(object: CoffeeMachine) -> None:
    """coffee machine - prepares latte"""
    object.order_coffee('latte')

def cappuccino(object: CoffeeMachine) -> None:
    """coffee machine - prepares cappuccino"""
    object.order_coffee('cappuccino')


options = {
    'off': off,
    'report': report,
    'espresso': espresso,
    'latte': latte,
    'cappuccino': cappuccino,
}


coffee_machine = CoffeeMachine()

while True:
        while not (user_coffee := input(STARTER_CHOICE).strip().lower()) in options:
            print(f"{user_coffee} is not a valid choice.")
        else:
            choice = user_coffee

        if choice in options:
            action = options[choice]

            action(coffee_machine)

            if choice == 'off':
                break
