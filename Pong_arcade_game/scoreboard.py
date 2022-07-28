# class for managing the scoreboard
from turtle import Turtle

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
    def __init__(self, pos_x_y: tuple[int,int]) -> None:
        super().__init__()
        self.score = 0
        self.text = lambda score: f"Score: {score}"
        self.penup()
        self.color(ScoreBoardSettings.COLOR)
        self.goto(pos_x_y)
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

