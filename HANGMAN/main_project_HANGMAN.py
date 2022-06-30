# game hangman
from main_project_data import INTRO, HANGMANPICS, WORDS
from random import choice
import os

# Init 
# keep  playing
gameOn = True

# asking user for a letter
def askForLetter () -> str :
    """
    Ask the user fro an input , and retursn the 
    inputed letter
    """
    return (input("Guess a letter: ")).lower()

# return obscure word
def obscureWord (wordToGuess: str, guessedLetters: list[str]) -> list[str] :
    """
    replece the amoun of characters in the word with undescores
    and if the letter is alredy guessed than the letter
    """
    return [character if character in guessedLetters else '_'  for character in wordToGuess]

# ============================================
# GAME ON
# ============================================


while gameOn:

    # INIT
    # hangman status
    STATUS = 0
    # choosing a random word to start with
    wordToGuess = choice(WORDS).lower()
    # lives 
    lives = len(HANGMANPICS) - 1
    # for history of guesses 
    history = []
    os.system('cls') #os.system('clear')

    print(INTRO)


    while STATUS <= lives: 

        wordGuessed = obscureWord(wordToGuess,history)
        if '_' in wordGuessed:
            print(' '.join(wordGuessed)+'\n') # printing the word / progress
        else: # you won the game !!
            print("You Guessed all the letters")
            print("You have won !!")
            print("{} was the word".format((' '.join(wordGuessed)).upper()))
            print("You have won !!")
            break # while loop

        if history: # display history if it exists
            history.sort()
            print("You have tried so far: {}".format(history))
        quessedLetter = askForLetter() # asks for a new letter
        
        
        if quessedLetter in wordToGuess and not quessedLetter in history:
            os.system('cls') #os.system('clear')
            print("GOOD JOB! The {} letter is in the word".format(quessedLetter))
        elif quessedLetter in history:
            os.system('cls') #os.system('clear')
            print("You already guessed {}".format(quessedLetter))
        else:
            os.system('cls') #os.system('clear')
            STATUS += 1
            print("You guessed {}, that's not in the word. You lose a life.".format(quessedLetter))
            
        if STATUS <= lives:
            print(HANGMANPICS[STATUS]+'\n')

        if STATUS == lives:
            print("GAME OVER !!!")
            print("You have died !!!")
            print("GAME OVER !!!")
            break # break the while loop


        if not quessedLetter in history:
            history.append(quessedLetter) # add the letter to the history

    if 'n' == (input("Do you want to play again ? (Y/N) : ")).lower():
        gameOn = False