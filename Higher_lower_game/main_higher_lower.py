from random import randint
from main_ASCI_ART import LOGO_HIGHER_LOWER, VS_LOGO
import json
from os import system


FILE_NAME_DATA = 'data.json'
MAIN_QUESTION = 'Who has more followers? '
PERSON_INFO = lambda info_person : f" {info_person['name']}, a {info_person['description']}, from {info_person['country']}."
MESSAGE_COMPARE_A = 'Compare A:'
MESSAGE_AGAINST_B = 'Against B:'
MESSAGE_WHO_HAS_MORE_FOLLOWERS = "Who has more followers? Type 'A' or 'B': "
MESSAGE_YOU_ARE_RIGHT = lambda user_score : f"You are right!! Current Score: {user_score}"
MESSAGE_YOU_ARE_WRONG = lambda user_score : f"Sorry that's wrong. Your final Score is: {user_score}"
score = 0

# gettin json data as dict
def get_data(file_name: str) -> dict:
    """reading the json file and returning it as a dictionarym
    if a error occurs during reading return None
    """
    data = {}
    try:
        with open(file_name,'r') as f:
            data = json.loads(f.read())
    except FileNotFoundError:
        print(f"File {file_name} dosent exists? or wrong directory?")
        return None
    except Exception as e:
        print(type(e))
        print(f"Exception {e} was caught!")
        return None

    return data

# printing message to the consol
def prompt(message: str) -> None:
    """Printing the message to the consol"""
    if message:
        print(message)

# get random number
def get_random_number(start: int, end: int, excluding_number: int = -1) -> int:
    """Returns a random number from start to end including,
    it will look for a random number as long as it is not equel to excluding_number
    """
    random_number = randint(start,end)
   
    if random_number != excluding_number:
        return random_number
    else :
        return get_random_number(start,end,excluding_number)

# getting user choice A or B
def get_user_choice(message: str) -> str:
    """function for getting input from user, choice"""
    while not (choice := input(message).strip().lower()) in ['a','b']:
        print(f"{choice} is not a valid choice. It has to be 'A' or 'B'. TRY AGAIN !!")
    
    return choice


# saving data in a dictionary
data = get_data(FILE_NAME_DATA)['data']
end_number = len(data)-1

# starting random number for data from json
compare_a_number = get_random_number(1,end_number)

# Main content for the game
while True:

    print(LOGO_HIGHER_LOWER)
    prompt(MAIN_QUESTION)
    prompt("\n")
    if score:
        prompt(MESSAGE_YOU_ARE_RIGHT(score))

    
    compare_b_number = get_random_number(0,end_number,compare_a_number)
    
    followers_a = data[compare_a_number]['follower_count']
    followers_b = data[compare_b_number]['follower_count']


    prompt(MESSAGE_COMPARE_A+PERSON_INFO(data[compare_a_number]))
    prompt(VS_LOGO)
    prompt(MESSAGE_AGAINST_B+PERSON_INFO(data[compare_b_number]))
    choice = get_user_choice(MESSAGE_WHO_HAS_MORE_FOLLOWERS)

    if choice == 'a':
        if followers_a >= followers_b:
            score += 1
            system('cls')
        else:
            system('cls')
            prompt(MESSAGE_YOU_ARE_WRONG(score))
            break

    elif choice == 'b':
        if followers_b >= followers_a:
            score += 1
            system('cls')
        else:
            system('cls')
            prompt(MESSAGE_YOU_ARE_WRONG(score))
            break

    compare_a_number = compare_b_number