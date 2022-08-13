import pandas

# settings for the program
FILE_NAME_NATO_ALPHABET = 'nato_phonetic_alphabet.csv'
USER_PROMPT = 'Input a word that you wish to spell out in NATO alphabet: '


# readinding the csv file into a DataFrame
data = pandas.read_csv(FILE_NAME_NATO_ALPHABET)

# creating the Nato dictionary from csv file
Nato_dictionary = {row.letter: row.code for index, row in data.iterrows()}

# the main loop of the porgram
while True:
    user_word = input(USER_PROMPT)
    user_word = user_word.upper()
    if user_word == "EXIT":
        break
    # creating the NATO alphabet based on the input
    NATO_spelled_word = [Nato_dictionary[letter] for letter in user_word if letter in Nato_dictionary]
    print(NATO_spelled_word)