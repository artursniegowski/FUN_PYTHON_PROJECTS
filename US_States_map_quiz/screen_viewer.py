# class for managing the screen settings
from turtle import Screen, shape, Turtle


class ScreenSettings:
    """
    Basic screen settings
    """ 
    SCREEN_TITLE = 'U.S. States Game'
    SCREEN_BACKGROUND = 'blank_states_img.gif'
    SCREEN_TITLE_PROMPT_STATE = lambda correct_guess : \
        f'{correct_guess}/50 States Corect'
    SCREEN_QUESTION_PROMPT_STATE = 'What\'s another state\'s name?'


class ScreenView:
    """
    managing screen
    """
    def __init__(self) -> None:
        self.screen = Screen()
        self.screen.title(ScreenSettings.SCREEN_TITLE) 
        #self.screen.addshape(ScreenSettings.SCREEN_BACKGROUND)
        #shape(ScreenSettings.SCREEN_BACKGROUND)
        self.screen.bgpic(ScreenSettings.SCREEN_BACKGROUND)


    def prompt_user_input(self, state_guess: int = 1) -> str:
        """
        ask the user for thr state and return the given answer
        """
        return self.screen.textinput(
                    title=ScreenSettings.SCREEN_TITLE_PROMPT_STATE(state_guess),
                    prompt=ScreenSettings.SCREEN_QUESTION_PROMPT_STATE
                            )


    def draw_state_name(self, name: str, x_position: int, y_position: int) \
        -> None:
        """
        draws the turtel object as state text in the given cordinates
        """
        new_txt_turtle = Turtle(shape='circle')
        new_txt_turtle.color('red')
        new_txt_turtle.shapesize(0.2,0.2,1)
        new_txt_turtle.penup()
        new_txt_turtle.goto(x_position,y_position)
        new_txt_turtle.write(name,align='left',font=('Arial', 8, 'normal'))
