## Small Fun Python Projects


# Banking_APP
The program will track the balance of the given account based on the user choices,
and all the transactions will be logged into a txt file. It's a program to simulate basic banking transactions like depositing or withdrawing money.
  
# Blackjack
Blackjack is the most widely played casino banking game in the world. 
It uses decks of 52 cards. It's also known as Twenty-One. In the game, 
the players compete only against the dealer. The aim is to get a sum of all cards 
totaling as close as possible to 21 (including). With the combination of an ace and 
another 10 value card called "blackjack".
This is a simplified version of the popular game Blackjack, written in Python. 
The game keeps track of the probability of cards based on the decks played 
and cards removed from them. The base scenario is with 8 decks of cards and 
after playing 2 decks of cards, all decks will get reshuffled, in order to 
reset the probabilities.  

# Caesar Cipher
A Caesar cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, A would be replaced by D, E would become H, and so on. The method is named after Julius Caesar, who used it in his private correspondence. The program encrypts and decrypts the given text according to the Caesar Cipher. 

# Coffee_machine_simulation
It's a simple digital version of a coffee machine (based on OOP principles), simulating the option of buying one of three available coffees: espresso, latte, or cappuccino. It keeps track of the coffee machine's resources and gives a prompt accordingly if it is lacking any of them. The user can check the remaining resources with the command 'report' and shuts the machine down for maintenance with the command 'off'. The machine also keeps track of the money made from the coffee sold (accepted coins: penny (1 cent), nickel (5 cents), dime (10 cents), quarter (25 cents)). It calculates the inserted coins and gives back change if there is any.

# Guess_The_Number
Guess the secret number in the range 1-100 (including endpoints).
If your guess is too high or too low, you'll get a hint.
The user has a limited amount of attempts to guess the right number,
based on the level they choose to play.

# Hangman
Hangman is a guessing game where the player has to guess the whole word,
letter by letter. Every time the guess is wrong,  the player loses a life and 
a "Hangman" ASCI art will be progressive, drawn out. In order to win, the player 
has to guess all the letters before the hangman is drawn. 

# Higher_Lower_game
The program compares one search term against another search term. 
It retrieves data from a JSON file with usernames from Instagram and its followers. 
The user is given a choice between two randomly selected Instagram names, to decide who has more followers.
For a correct guess the score will be adjusted by 1, otherwise the user will lose 
and will be prompted the amount of points collected so far. Each decision is worth 1 point.
  
# Hirst_painting
It is a project where we try to recreate some art of the famous Damien Hirst random spot paintings. First, using python library colorgram for defining color palette from a painting (color_palette.jpg). 
Next, we use the library Turtel and the extracted colors to draw a random spot painting. 

# Mail_merging
The program takes a template.txt, which contains a default message and names.json file, with a list of names, we want to send the template message to. The program will loop through each of the names from the input folder names.json file and will replace the [name] in the template message with the names in the json file and save for each name a separate file customized to the name in the output folder. It is an example where we can use python for writing multiple messages to different people, and let the  program do the repetitive task of adjusts the names for us.

# Pokemon_Search_API
It is a program which uses the API https://pokeapi.co/ to look through the database of the pokemons. 
The user is asked about the name of the pokemon and after entering it the program will show some detailed information about his choice. 

# Pong_arcade_game
The Pong game it is a classic arcade game and probably one of the first one. It has a really simple premise. It's basically just a ball that is going across a table and two players each control a paddle bouncing the ball back and forth. If you miss the ball, then the other player scores a point. The right player controls the right paddle with the arrow keyboards: 'UP' and 'DOWN', and the left player controls left paddle with the keyboard 'W' and 'S'. In order to increase the difficulty of the game, each time the ball bounces from one of the paddles, it will increase its speed. 

# Quiz_game
It is a quiz game, where the user has to answer some True/False questions.
Based on the answer a total score is calculated where for each question the user
is rewarded with one point. 
The questions / data is read from JSON files (they can be generated using the API https://opentdb.com/).

# Snake_game
Snake game has, a moving snake, which you control using your arrow keyboards (UP, RIGHT, DOWN, LEFT). The aim is to collect food objects that appear randomly on the screen. It will grow in length as it eats more food. You have to make sure that you don't end up getting tangled or hitting the wall, which would result in Game Over. 
The goal is to eat as much food as you can while staying alive.
YYou'll be able to see your score on the scoreboard located on the top of your screen, as well as the high score that will be stored in a file and loaded at the beginning of each game.

# Turtle_crossing_game
In the Turtle crossing game, we have a bunch of cars spawning randomly on the right side of the screen and going across a super busy multilane highway. The player controls the turtle on the bottom side of the road with arrow keyboard 'Up', which can only go forwards. The aim is to cross the road without being hit by the cars driving on it.
Once the player reaches the other side of the screen, the cars speed up (next level), but the player goes back to the starting position, ready to cross the screen again. 
At any point when a car hits the player turtle, the game ends with a Game Over.

# Turtle_racing_game
This program utilizes the python library Turtle, in order to draw turtles on the display.
At the beginning, the user is supposed to place a bet, which turtle is going to win. 
Next the race starts and the turtles race each other, with random speeds. The turtle that reaches first the edge of the right screen is the winner, and determines whether the bet was lost or won.  