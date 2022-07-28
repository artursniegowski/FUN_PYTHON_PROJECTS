# class for managing the score
from turtle import Turtle
from screen import ScreenSettings

class ScoreBoardSettings:
    """
    settings for Scoreboard
    """
    ALIGMENT = 'center'
    FONT = ('Courier',20,'normal')
    COLOR = 'white'


class ScoreBoard(Turtle):
    """
    class to manage the score on the screen
    """
    def __init__(self, screen_settings: ScreenSettings) -> None:
        super().__init__()
        self.score = 0
        self.text = lambda score: f"Score: {score}"
        self.penup()
        self.color(ScoreBoardSettings.COLOR)
        self.goto(0,screen_settings.SCREEN_HEIGHT/2-30)
        self.hideturtle()
        self.draw_score()


    def add_score(self) -> None:
        """
        increassing the score by 1, and redrawing the score
        """
        self.clear()
        self.score += 1
        self.draw_score()


    def draw_score(self) -> None:
        """
        draw the score on the screen
        """
        self.write(self.text(self.score),align=ScoreBoardSettings.ALIGMENT,
        font=ScoreBoardSettings.FONT)

    
    def game_over(self) -> None :
        """
        Info on the screen - Game Over
        """
        # write teh message in the center
        self.goto(0,0)
        self.write("GAME OVER",align=ScoreBoardSettings.ALIGMENT,font=ScoreBoardSettings.FONT)