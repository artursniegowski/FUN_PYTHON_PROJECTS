# class that mangaes the food on the screen
from turtle import Turtle
from random import randint
from screen import ScreenSettings

class Food(Turtle):
    """
    managing the food on the screen
    """
    def __init__(self, screen_settings: ScreenSettings) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        # default size is 20 x 20 pixel
        # we are making it smaller to 10 x 10 pixels
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        # so the animation of creating new food object is instantaneous
        self.speed('fastest')
        self.screen_settings = screen_settings
        self.refresh()
    
    
    def refresh(self):
        """
        create a new random position for the food object
        """
        # moving it to a random location
        x_position = randint(30-self.screen_settings.SCREEN_WIDTH/2,self.screen_settings.SCREEN_WIDTH/2 - 30)
        y_position = randint(30-self.screen_settings.SCREEN_HEIGHT/2,self.screen_settings.SCREEN_HEIGHT/2 - 30)
        self.goto(x_position,y_position)