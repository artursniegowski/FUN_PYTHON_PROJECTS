# class for managing the score
import json
from select import select
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
    def __init__(self, screen_settings: ScreenSettings, file_name: str) -> None:
        super().__init__()
        self.score = 0
        self.file_name = file_name
        self.high_score = self.read_high_score(self.file_name)
        self.text = lambda score, high_score: f"Score: {score} High Score: {high_score}"
        self.penup()
        self.color(ScoreBoardSettings.COLOR)
        self.goto(0,screen_settings.SCREEN_HEIGHT/2-30)
        self.hideturtle()
        self.draw_score()


    def read_high_score(self, file_name:str) -> int : 
        """
        reads the highscore value from a json file data and returns its value
        if the file dosent exists , it will return 0
        """
        data = 0
        try:
            with open(file_name,'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"{file_name} dosent exists or wrong directory!")
        except Exception as e:
            print(type(e))
            print(f"{e} An exception was caught")
        else:
            return data['high_score']

        return 0

    def write_high_score(self) -> None:
        """
        write the high score to a file
        """
        try:
            data = {'high_score':self.high_score}
            json_data = json.dumps(data)
            with open(self.file_name,'w') as f:
                f.write(json_data)
        except FileNotFoundError:
            print(f"{self.file_name} error writing")
        except Exception as e:
            print(type(e))
            print(f"{e} An exception occured during writing {data} to {self.file_name}")
        else:
            print("High score was successfully written into a file.")


    def add_score(self) -> None:
        """
        increassing the score by 1, and redrawing the score
        """
        self.score += 1
        self.draw_score()

    def draw_score(self) -> None:
        """
        draw the score on the screen
        """
        self.clear()
        self.write(self.text(self.score,self.high_score), \
            align=ScoreBoardSettings.ALIGMENT,
        font=ScoreBoardSettings.FONT)

    def reset_score(self) :
        """
        Updating the valu of high score with our current score
        """
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.draw_score()
    # def game_over(self) -> None :
    #     """
    #     Info on the screen - Game Over
    #     """
    #     # write teh message in the center
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ScoreBoardSettings.ALIGMENT,font=ScoreBoardSettings.FONT)