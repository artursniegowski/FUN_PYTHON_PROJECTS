# class for managing
from tkinter import *
from turtle import bgcolor
from quiz_brain import QuizBrain

class QuizGUISettings:
    """
    settings fro the GUI class
    """
    THEME_COLOR = "#375362"
    WINDOW_TITLE = "Quizzler"
    WINDOW_PADDING_X = 20
    WINDOW_PADDING_Y = 20
    # buttons settings
    BUTTON_CHECK_FILE_NAME = './images/true.png'
    BUTTON_CROSS_FILE_NAME = './images/false.png'
    # cnvas settings
    CANVAS_WIDTH = 300
    CANVAS_HEIGHT = 250
    CANVAS_TEXT_WIDTH = 280
    CANVAS_BACKGROUND_COLOR = 'white'
    CANVAS_BACKGROUND_COLOR_GREEN = 'green'
    CANVAS_BACKGROUND_COLOR_RED = 'red'
    CANVAS_LANGUAGE_TEXT_FONT = ('Arial',12,'italic')
    #  label settings
    LABEL_SCORE_TEXT = lambda score : f'Score: {score}'
    LABEL_SCORE_COLOR = 'white'



class QuizInterface:
    """
    creating the user GUI
    """
    def __init__(self, quiz_brain: QuizBrain) -> None:

        # creating the instance of quiz
        self.quiz_brain = quiz_brain

        # main window
        self.window = Tk()
        self.window.title(QuizGUISettings.WINDOW_TITLE)
        self.window.config(padx=QuizGUISettings.WINDOW_PADDING_X, 
                            pady=QuizGUISettings.WINDOW_PADDING_Y,
                            bg=QuizGUISettings.THEME_COLOR)
        

        # creating score label
        self.label_score = Label(text=QuizGUISettings.LABEL_SCORE_TEXT(0), 
                bg=QuizGUISettings.THEME_COLOR, highlightthickness=0, 
                fg=QuizGUISettings.LABEL_SCORE_COLOR)
        self.label_score.grid(row=0,column=1)


        # creating white canvas
        # creating canvas flash card on the screen
        self.canvas = Canvas(width=QuizGUISettings.CANVAS_WIDTH, 
                        height=QuizGUISettings.CANVAS_HEIGHT,
                        highlightthickness=0, 
                        bg=QuizGUISettings.CANVAS_BACKGROUND_COLOR)
        self.question_text_canvas = self.canvas.create_text(
                        QuizGUISettings.CANVAS_WIDTH/2,
                        QuizGUISettings.CANVAS_HEIGHT/2,
                        text="question text",
                        width=QuizGUISettings.CANVAS_TEXT_WIDTH,
                        fill=QuizGUISettings.THEME_COLOR,
                        font=QuizGUISettings.CANVAS_LANGUAGE_TEXT_FONT)
        self.canvas.grid(row=1,column=0,columnspan=2, pady=50) 

        # creating buttons
        # green check button
        button_check_image = PhotoImage(file=QuizGUISettings.BUTTON_CHECK_FILE_NAME)
        self.button_check = Button(image=button_check_image, highlightthickness=0, 
                            command=self.check_for_true)
        self.button_check.grid(row=2,column=0) 

        # red cross button
        button_cross_image = PhotoImage(file=QuizGUISettings.BUTTON_CROSS_FILE_NAME)
        self.button_cross = Button(image=button_cross_image, highlightthickness=0, 
                            command=self.check_for_false)
        self.button_cross.grid(row=2,column=1)
        

        self.get_next_question()

        # main loop for the window so it dosent disapear
        self.window.mainloop()

        
    def get_next_question(self):
        """
        adding question to the GUI front side
        """
        self.canvas.configure(bg = QuizGUISettings.CANVAS_BACKGROUND_COLOR)

        if self.quiz_brain.still_has_questions():
            self.label_score.configure(
                text=QuizGUISettings.LABEL_SCORE_TEXT(self.quiz_brain.score))
            self.canvas.itemconfig(self.question_text_canvas, 
                                    text=self.quiz_brain.next_question())
        else:
            self.canvas.itemconfig(self.question_text_canvas, 
                                    text="You have reached the end of the quiz")
            # disable the buttons
            self.button_check.config(state="disabled")
            self.button_cross.config(state="disabled")


    def check_for_true(self) -> None:
        """
        checks for true
        """
        is_right = self.quiz_brain.check_answer('True')
        self.give_feedback(is_right)


    def check_for_false(self) -> None:
        """
        checks for true
        """
        is_right = self.quiz_brain.check_answer('False')
        self.give_feedback(is_right)


    def give_feedback(self, is_right: bool) -> None:
        """
        it gives the user feedback if it was corect or wrong
        """
        if is_right:
            # set green for right
            self.canvas.configure(bg = QuizGUISettings.CANVAS_BACKGROUND_COLOR_GREEN)
        else:
            # set red for false
            self.canvas.configure(bg = QuizGUISettings.CANVAS_BACKGROUND_COLOR_RED)

        self.window.after(1000,self.get_next_question)
