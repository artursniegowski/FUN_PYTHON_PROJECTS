from main_project_ASCI_art import Intro

# init variables
# starting option prompt
start_message = "Type 'encode' to encrypt, type 'decode' to decrypt:\n"

# cipher helper function for the main cipherResult
def cipherHelper (message : str, listLetters : list[str], shift : int, option : str = 'decode') -> str : 
    """
    Helper function for cipherResult,
    - message - str to be ENCRYPTED or DECRYPTED
    - listLetters - list of string , posible letters
    - shift - int  by how many psotions should the ext be shifted in the algorithm
    - option - 'decode' or 'encode' for DECRYPTING , ENCRYPTING respectively
    """
    cipherResult = ''

    # depending on decode or encode we change the direction of shit
    if option == 'decode':
        shiftAdjuster = 1
    elif option == 'encode':
        shiftAdjuster = -1
    else:
        raise Exception("Option {} is not valid !!".format(option))
    
    # adjusting direction of our shift
    shift *= shiftAdjuster

    for character in message:
        # and the cipher will also deal with white spaces
        if character.upper() in listLetters:
            # to make the algorithm case sensitive
            # For lowercase letters 
            if character == character.lower():
                index = listLetters.index(character.upper())
                new_index = (index - shift) % len(listLetters)
                cipherResult += listLetters[new_index].lower()
            # For capital letters
            else: 
                index = listLetters.index(character)
                new_index = (index - shift) % len(listLetters)
                cipherResult += listLetters[new_index]
        else:
            cipherResult += character

    return cipherResult

# encrytpting / decrypting - Caeser Cipher
def cipherResult(message: str, shift : int = 0, option : str = 'encode') -> str :
    """
    This function is used to either encode or decode the caeser cipher.
    option : a string , either 'encode' or 'decode' (choice for the flow of algorithm)
    shift : by how many psotions should the ext be shifted in the algorithm
    message : a string that will be adjusted with the cipher algorithm
    output : str as a result
    """
    # all letters 
    listLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # starting value - empty string
    cipherResult = ''
    # if shift is greater than than the lengt of letters we have to roll over
    shift = shift % len(listLetters)
    # reducing the spaces at the begingin and end of the message
    message = message.strip()

    # encrypting
    if option == 'decode':
        cipherResult = cipherHelper(message,listLetters,shift,option)

    # decrypting
    elif option == 'encode':
        cipherResult = cipherHelper(message,listLetters,shift,option)

    else:
        print("!! Wrong option choice !!")
        raise Exception("Sorry, {} is not a valid option choice in the function".format(option))

    return cipherResult


# ASCI ART INTRO
print(Intro)

# Start the program
while True:
    userOption = (input(start_message)).lower()

    if userOption == 'encode': # encrypting
        messageToEncrypt = input("Type your message:\n")
        shiftEncrypt = input("Type the shift number:\n")
        result = cipherResult(messageToEncrypt,int(shiftEncrypt))
        print("Her's the encoded result: {}".format(result))
    elif userOption == 'decode': # decoding
        messageToDecode = input("Type your message:\n")
        shiftDecode = input("Type the shift number:\n")
        result = cipherResult(messageToDecode,int(shiftDecode),option=userOption)
        print("Her's the decoded result: {}".format(result))
    else : # no valid option
        print("Not a valid input!")

    # option for exiting the loop
    choiceToQuit = input("Do you want to quit (Y/N): ")
    if choiceToQuit.lower() == 'y':
        break # breaking while loop