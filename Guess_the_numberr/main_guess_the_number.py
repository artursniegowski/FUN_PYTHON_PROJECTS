from random import randint
from main_ASCI_ART import LOGO_GUESS_THE_NUMBER_ASCII

# Main variables
WELCOME_PROMPT = 'Welcome to the Number Guessing Game!'
INFO_PROMPT = 'I\'m thinking of a number between 1 and 100.'
CHOOSE_DIFICULTY_PROMPT = 'Choose a difficulty. Type \'easy\' or \'hard\': '
MAKE_A_GUESS = 'Make a guess: '
REMAINING_ATTEMPTS_PROMPT = lambda attemps_re : f'You have {attemps_re} attempts remaining to guess the number'
EASY_ATTEMPTS_LEVEL = 10
HARD_ATTEMPTS_LEVEL = 5

# functions for the game 
def propmpt(message: str = '') -> None:
    """function for printing the message to the consol"""
    print(message)

def take_input(message: str = '') -> str:
    """function for taking the user input"""
    return input(message)

def take_difficulty_input(message: str = '', easy_level_attempts: int = 10, hard_level_attempts: int = 5) -> int:
    """ function for taking the user input 
    as two options, 'hard', 'easy'
    and return the number of attempts
    """
    while not (user_difficulty := take_input(message)).strip().lower() in ['easy','hard']:
        print(f"{user_difficulty} is not a valid option. Try 'hard' or 'easy'.")
    else:
        if user_difficulty == 'easy':
            user_attempts = easy_level_attempts
        elif user_difficulty == 'hard':
            user_attempts = hard_level_attempts

    return user_attempts

def take_number_input(message: str = '') -> int:
    """function for taking the user input
    expecting to be an int 
    in range of range
    """
    number = input(message)
    try:
        number = int(number)
    except ValueError:
        print(f'{number} is not a valid integer number. Try AGAIN !!')
        number = take_number_input(message)
    except Exception as e:
        print(f"Exception {e} was caught")
        print(type(e))
    else:
        if 1 <= number <= 100:
            print(f'your guess is {number}')
        else:
            print(f'{number} is not in range 1-100 (including)')
            number = take_number_input(message)

    return number

def return_random_number(start_range: int = 1, end_range: int = 100) -> int:
    """Returning random number in range od start and end (including)"""
    return randint(start_range,end_range)


# Main content
propmpt(LOGO_GUESS_THE_NUMBER_ASCII)
propmpt(WELCOME_PROMPT)
propmpt(INFO_PROMPT)
user_attempts = take_difficulty_input(CHOOSE_DIFICULTY_PROMPT,EASY_ATTEMPTS_LEVEL,HARD_ATTEMPTS_LEVEL)
random_number = return_random_number()

# Main guessing game loop
while True:
    propmpt(REMAINING_ATTEMPTS_PROMPT(user_attempts))
    guessed_number = take_number_input(MAKE_A_GUESS)

    if guessed_number == random_number:
        print("\nCongratulations you guessed the right number !!")
        print(f"Random number was: {random_number}")
        print(f"Your guess was: {guessed_number}")
        break
    elif guessed_number > random_number:
        print("Too high.")
        user_attempts  -= 1
    else:
        print("Too low.")
        user_attempts -= 1

    if user_attempts <= 0:
        print("You've run out of guesses, you lose.")
        break
    else:
        print("Guess again.")