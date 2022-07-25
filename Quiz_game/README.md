# Quiz_game

It is a quiz game, where the user has to answer some True/False questions.
Based on the answer a total score is calculated where for each question the user
is rewarded with one point. 
The questions / data is read from JSON files. With the example files data_new.json and
data.json. 
data_new.json is a file created with the use of the API https://opentdb.com/.
The program main, has a function that can easily covert any JSON file to required
Question class, which is later used as data for our quiz. 
This program was written based on an OOP principles with the main classes
being Question (question_model.py - model), and QuizBrain (quiz_brain.py - the
main quiz functionality)

To run the program, simply execute main.py.

