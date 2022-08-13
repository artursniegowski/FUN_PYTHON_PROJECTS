# Program for generating strong random passwords
from random import randint

def generate_random_password(number_of_letters: int, number_of_symbols: int,\
    number_of_numbers: int) -> str:
    """
    function for generating random password with the given number of letters,
    symbols and numbers
    """

    # Main
    numberOfLetters = number_of_letters
    numberOfSymbols = number_of_symbols
    numberOfNumbers = number_of_numbers

    possibleLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    possibleSymbols = "~`!@#$%^&*()-_+={[}]|\\:;\"'<,.>?/"
    possibleNumbers = "0123456789"

    newPassword = ""


    #init values
    options = ['letters', 'symbols', 'numbers']
    choice = -1

    # brewing the password - random from all characters with random choices
    while numberOfLetters or numberOfSymbols or numberOfNumbers :


        #updating options
        if not numberOfLetters and 'letters' in options:
            options.remove('letters')

        if not numberOfSymbols and 'symbols' in options:
            options.remove('symbols')

        if not numberOfNumbers and 'numbers' in options:
            options.remove('numbers')


        # we coudl also use random.shuffle()
        if options : # if list is not empty
            choice = randint(0,len(options)-1)

            if options[choice] == 'letters':
                if (numberOfLetters > 0):
                    # we coudl also use random.choice(possibleLetter)
                    newPassword += possibleLetter[randint(0,len(possibleLetter)-1)]
                    numberOfLetters -= 1

            elif options[choice] == 'symbols':
                if (numberOfSymbols > 0):
                    newPassword += possibleSymbols[randint(0,len(possibleSymbols)-1)]
                    numberOfSymbols -= 1

            elif options[choice] == 'numbers':
                if (numberOfNumbers > 0):
                    newPassword += possibleNumbers[randint(0,len(possibleNumbers)-1)]
                    numberOfNumbers -= 1


    return newPassword