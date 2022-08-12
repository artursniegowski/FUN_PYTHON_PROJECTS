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

# Flash_card_program
The flash card program is used to help you study foreign languages. You can learn the most frequently used words in any language. It will show the user the front and back of each flash card. So, for example, one side will show you the desired language to learn with a word from this language, and after three seconds, the program will flip the card and show the same word in English on the other side, and the user has to make a choice whether the foreign word was known or not. If the user knew the meaning of the word, then the green check button should be pressed, and if the user was not familiar with it, the red cross button should be pressed. So whenever the user confirms that the word is known, the program will take out this word from the list of flash cards to learn and keep showing only the flashcards that were chosen as unknown (red cross button pressed, or the card is shown for the very first time).

# Guess_The_Number
Guess the secret number in the range 1-100 (including endpoints).
If your guess is too high or too low, you'll get a hint.
The user has a limited amount of attempts to guess the right number,
based on the level they choose to play.

# GUI_Quiz_app
This is a quiz app using the data from the open trivia database API, https://opentdb.com/. 
On the GUI, the user will find a true / false question and the aim is to guess whether it is right or false, with the two buttons on the bottom of the application. For true, the user should press the green check button and for false the red cross button.   

# Hangman
Hangman is a guessing game where the player has to guess the whole word,
letter by letter. Every time the guess is wrong,  the player loses a life and 
a "Hangman" ASCI art will be progressive, drawn out. In order to win, the player 
has to guess all the letters before the hangman is drawn. 

# Happy_Birthday_automatic_email_sender
This is a python program that is an automated email birthday wish sender. It uses a spreadsheet with a list of birthdays, names, and emails, and based on the list, the program will check the current date. If that date matches someone's birthday from the file 'birthdays.csv' the program will extract the data and choose one of the random letters from the letter_templates directory and replace the name tag ([NAME]) with the matching name from birthdays.csv. At the end, the program will use a Gmail account to send a happy birthday email to this person.

# Higher_Lower_game
The program compares one search term against another search term. 
It retrieves data from a JSON file with usernames from Instagram and its followers. 
The user is given a choice between two randomly selected Instagram names, to decide who has more followers.
For a correct guess the score will be adjusted by 1, otherwise the user will lose 
and will be prompted the amount of points collected so far. Each decision is worth 1 point.
  
# Hirst_painting
It is a project where we try to recreate some art of the famous Damien Hirst random spot paintings. First, using python library colorgram for defining color palette from a painting (color_palette.jpg). 
Next, we use the library Turtel and the extracted colors to draw a random spot painting. 

# ISS_tracker
This program tracks the position of the International Space Station (https://en.wikipedia.org/wiki/International_Space_Station), and once the station is visible at our location, it will send an automatic email reminding us to look up and search for the station.

# Kanye_quotes
Every time we press the button with the emoji of Kanye West, we will get a new quote fetched from the https://kanye.rest/ API and display it on the GUI main screen. 

# Mail_merging
The program takes a template.txt, which contains a default message and names.json file, with a list of names, we want to send the template message to. The program will loop through each of the names from the input folder names.json file and will replace the [name] in the template message with the names in the json file and save for each name a separate file customized to the name in the output folder. It is an example where we can use python for writing multiple messages to different people, and let the  program do the repetitive task of adjusts the names for us.

# Miles_Kilometers_converter_GUI
This is a unit converter program using Tkinter. This program has a graphical interface and is used to convert miles to kilometers or can be easily adjusted to convert liters to gallons (or whatever little conversion that you might often use).
A fully-fledge Python graphical user interface program.

# NATO_phonetic_alphabet_converter
This program converts the given word to the NATO phonetic alphabet. The NATO phonetic alphabet is read from a file 'nato_phonetic_alphabet.csv' using Pandas library. The user has to type down a word in the console, and it returns a list of phonetic alphabet that matches each of the letters in the given word. 

# Password_manager
This program is used to store and generate passwords. It requires filling few fields, like:
Website - this is used only as description for future identification. So it is easier to deduct what this password is for.
Email/Username - which is prepopulated but can be change to any username / email address.
Password - here we fill in the password we want to store, or we can choose to autogenerate a password with the Generate Password button, which results also in copying the newly generated password into our clipboard and be ready to use it right away. 
After completing the form, we can add the password to our list of passwords, which will be saved in a data.JSON file. Hitting the Add button will result in another pop up window asking for confirmation of adding a new password to the list. 
There is also the search button which will look for the given website name, and retrieve the data from the data.json file (if it exists)
and populate the password and email/username fields. If an error occurs or the user will submit an invalid input, the program will indicate this with a pop-up message box.  

# Pokemon_Search_API
It is a program which uses the API https://pokeapi.co/ to look through the database of the pokemons. 
The user is asked about the name of the pokemon and after entering it the program will show some detailed information about his choice. 

# Pomodoro_app
This is a famous technique that helps people time-manage and to get more stuff done.
If you're figuring out a time-consuming task, then you can set your timer to 25 minutes and then work on the task for 25 mins and after that you take a short five-minute break. After doing four of these sequence repetitions called pomodoros, you take a longer break between 15-30 mins. This way you can break your work into intervals, which arguably helps with information retention and to stay motivated. This program will help you keep track of time according to the famous pomodoro technique. It is a timer with a tomato on it, and when you click start, it is going to tell you to work for 25 minutes. Then that window can go into background and while you are working on your task, when the timer's up it will pop to the very front of the screen above all the other windows and tell you to take a break. So the first break is for 5 mins, and you will notice the program will mark which pomodoro cycle was completed. Once you're done with the break, it's going to go back to work, and it's going to continue until you reach the longer break or until you click to stop or reset the timer. This program will help you to do these Pomodoro where you have 25 minute work, 5 mins break. You do four of these 25 mins sessions, and you get a 20-minute break.

# Pong_arcade_game
The Pong game it is a classic arcade game and probably one of the first one. It has a really simple premise. It's basically just a ball that is going across a table and two players each control a paddle bouncing the ball back and forth. If you miss the ball, then the other player scores a point. The right player controls the right paddle with the arrow keyboards: 'UP' and 'DOWN', and the left player controls left paddle with the keyboard 'W' and 'S'. In order to increase the difficulty of the game, each time the ball bounces from one of the paddles, it will increase its speed. 

# Quiz_game
It is a quiz game, where the user has to answer some True/False questions.
Based on the answer a total score is calculated where for each question the user
is rewarded with one point. 
The questions / data is read from JSON files (they can be generated using the API https://opentdb.com/).

# Rain_alarm_app
This is an API driven application that will monitor the weather in the given location, and if it's going to rain, it will send automatically an SMS text in the morning to the defined number. 

# Snake_game
Snake game has, a moving snake, which you control using your arrow keyboards (UP, RIGHT, DOWN, LEFT). The aim is to collect food objects that appear randomly on the screen. It will grow in length as it eats more food. You have to make sure that you don't end up getting tangled or hitting the wall, which would result in Game Over. 
The goal is to eat as much food as you can while staying alive.
YYou'll be able to see your score on the scoreboard located on the top of your screen, as well as the high score that will be stored in a file and loaded at the beginning of each game.

# Stock_news_monitoring_project
This program monitors the prices of a given stock and notifies the user via email if there is a good chance for investing, like big fluctuation in price. The threshold of fluctuation can be adjusted. By default, it is set to 5%. 
1. First, the program pulls out the data of the stock price that we are interested in. For the two previous days, the closing prices of the given company will be compared. Whether it went up or down and by how much. 
Here we will use the API: https://www.alphavantage.co/ </br>
2. Next, the program will fetch three news data regarding this company, which should make it easier to understand the reason for the fluctuation. 
Here we will use the API: https://newsapi.org/ </br>
3. At the end, the data is put together, and the program will send the user an email about the new finding. (this can be easily adjusted to send an SMS text instead with the help of https://www.twilio.com/) </br>

# Turtle_crossing_game
In the Turtle crossing game, we have a bunch of cars spawning randomly on the right side of the screen and going across a super busy multilane highway. The player controls the turtle on the bottom side of the road with arrow keyboard 'Up', which can only go forwards. The aim is to cross the road without being hit by the cars driving on it.
Once the player reaches the other side of the screen, the cars speed up (next level), but the player goes back to the starting position, ready to cross the screen again. 
At any point when a car hits the player turtle, the game ends with a Game Over.

# Turtle_racing_game
This program utilizes the python library Turtle, in order to draw turtles on the display.
At the beginning, the user is supposed to place a bet, which turtle is going to win. 
Next the race starts and the turtles race each other, with random speeds. The turtle that reaches first the edge of the right screen is the winner, and determines whether the bet was lost or won.  

# US_States_map_quiz
This game tests you on your knowledge of the names of the 50 states in the USA. Every time we guess the correct state name, it will appear on the map at the location of the state. The aim of the game is to remember all the names of the states and to name as many as you can. This is an interactive and educational game. At any time, the user can write in the box "Exit" instead of a state name, and the game will terminate, and output all the missed states to a new file 'states_to_learn.csv'.