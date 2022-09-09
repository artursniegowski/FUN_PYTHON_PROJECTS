# logic for the quizbrain
from question_model import Question

class QuizBrain:
    """
    class managing the whole game
    """
    ASK_QUESTION = lambda  self, q_number, q_text : f"Q.{q_number}: {q_text} (True/False): "
    WRONG_MESSAGE = lambda  self, answer, score, q_num : f"That's wrong.\nThe correct answer was {answer}.\nYour current score is: {score}/{q_num}"
    CORRECT_MESSAGE = lambda  self, answer, score, q_num : f"You got it right!\nThe correct answer was {answer}.\nYour current score is: {score}/{q_num}"


    def __init__(self, question_list: list[Question]) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def take_user_answer(self, message: str, options: list[str]) -> str :
        """
        takes user input. and returns only if the user choose the correct respond.
        Return only : a string ; True or False
        """ 
        while not (user_choice := input(message).strip().lower()) in options:
            print(f"{user_choice} is not a valid choice! Only {options} are valid")

        return user_choice.capitalize()

    def next_question(self) -> None:
        """
        showing the question to the user, based on the question number
        """
        max_questions = len(self.question_list)
        if 0 <= self.question_number < max_questions:
            current_question = self.question_list[self.question_number]
            
            user_answer = self.take_user_answer(self.ASK_QUESTION(self.question_number+1, current_question.text), ['true', 'false'])

            if user_answer == current_question.answer:
                self.score += 1
                print(self.CORRECT_MESSAGE(current_question.answer,self.score,self.question_number+1))
            else: 
                print(self.WRONG_MESSAGE(current_question.answer,self.score,self.question_number+1))

            self.question_number += 1
            print("\n")
        else:
            print("You have exhausted all the questions passed to the list!")


    def still_has_question(self) -> bool :
        """
        Checks if we still have a question to ask. if we reached the end of 
        our questions bank list it will return false
        """
        return 0 <= self.question_number < len(self.question_list)

    def end_message_score(self) -> str :
        """
        end message - end quiz
        """
        message = f"You've completed the quiz.\nYour score was: {self.score}/{len(self.question_list)}"
        print(message)