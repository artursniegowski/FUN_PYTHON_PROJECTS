# banking managing app
from Bank import User
import os

# to close the system
def exit_system() -> None:
    print("Closing the system ...")

# depositing money
def deposit(Object: User, amount: float = 0.0):
    print(f"Depositing ${amount:.2f} ...")
    Object.deposit(amount)

# Withdrawing money
def withdraw(Object: User, amount: float = 0.0):
    print(f"Withdrawing ${amount:.2f} ...")
    Object.withdraw(amount)

options = {
    'deposit': deposit,
    'withdraw': withdraw,
    'quit': exit_system,
}

print("Welcome to the pyhton transaction system")
first_name = input("First name: ")
last_name = input("Last name: ")
new_client = User(first_name,last_name,0)


while True:
    print(new_client)
    clients_choice = input("Choose your option: 'deposit', 'withdraw', 'quit':\n")    
    clients_choice = clients_choice.lower().strip()


    if clients_choice in options:
        command = options[clients_choice]
        if clients_choice == 'quit':
            command()
            break
        else:
            amount = input(f"How much $ do you want to {clients_choice}: $")
            try:
                amount = float(int(float(amount)*100)/100)
            except ValueError:
                print(f"{amount} This is not a valid number !!")
            except Exception as e:
                print(f"Exception {e} was caught")
                print(type(e))
            else : # if no exception caught
                command(new_client,amount)
    else:
        print(f"{clients_choice} is not a valid option. Try again!")