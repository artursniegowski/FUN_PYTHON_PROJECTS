# Main program
import json
from question_model import Question
from quiz_brain import QuizBrain


# loading json.data into a file
def load_json_data(file_name: str) -> dict[str,bool]:
    """
    function for reading json data file
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

# populating our question bank
def return_question_bank(file_name: str, main_atribute: str, attribute_text: str, attribute_answer: str) -> list[Question] :
    """
    function for populating our question bank.
    Returning a list of Questions (text, answer)
    """
    question_bank = []

    data = load_json_data(file_name)
    if data:
        for question_data in data[main_atribute]:
            question_bank.append(Question(question_data[attribute_text],question_data[attribute_answer]))

    return question_bank


#question_bank = return_question_bank("data.json", main_atribute = "question_data", attribute_text = "text", attribute_answer = "answer")
# https://opentdb.com/api_config.php
# https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean
# OPEN TRIVIA DATABASE
# https://opentdb.com/
question_bank = return_question_bank("data_new.json", main_atribute = "results", attribute_text = "question", attribute_answer = "correct_answer")

if question_bank:
    new_quiz = QuizBrain(question_bank)
else:
    raise Exception("Question bank is empty!! In order for the porgram to run question bank needs to be populated with class Question")
    exit(0)

while new_quiz.still_has_question():
    new_quiz.next_question()


new_quiz.end_message_score()