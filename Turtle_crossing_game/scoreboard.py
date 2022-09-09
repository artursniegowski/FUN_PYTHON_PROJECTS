# class for managing the score / level
from turtle import Turtle

class ScoreBoardSettings:
    """
    settings for Scoreboard
    """
    ALIGMENT = 'center'
    FONT = ('Courier',20,'normal')
    COLOR = 'black'


class ScoreBoard(Turtle):
    """
    class to manage the score on the screen
    """
    def __init__(self, pos_x_y: tuple[int,int]) -> None:
        super().__init__()
        self.level = 1
        self.text = lambda score: f"Level: {score}"
        self.penup()
        self.color(ScoreBoardSettings.COLOR)
        self.goto(pos_x_y)
        self.draw_score()
        self.hideturtle()

    def add_level(self) -> None:
        """
        increassing the score by 1, and redrawing the score
        """
        self.clear()
        self.level += 1
        self.draw_score()

    def draw_score(self) -> None:
        """
        draw the score on the screen
        """
        self.write(self.text(self.level),align=ScoreBoardSettings.ALIGMENT,
        font=ScoreBoardSettings.FONT)

    def game_over(self) -> None:
        """
        game over message 
        """
        self.goto(0,0)
        self.write("GAME OVER",align=ScoreBoardSettings.ALIGMENT,
        font=ScoreBoardSettings.FONT)
