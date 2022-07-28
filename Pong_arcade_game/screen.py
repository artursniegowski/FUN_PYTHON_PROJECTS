# class for managign the screen settings
from turtle import Screen

class ScreenSettings:
    """
    Basic screen settings
    """
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_BACKGROUNDCOLOR = 'black'
    SCREEN_TITLE = 'THE PONG GAME'
    TRACER_VALUE = 0
    SLEEP_TIME = 0.1


class GamesScreen:
    """
    creating screen object and its properties
    """
    def __init__(self) -> None:
        # creating screen view
        self.screen = Screen()
        self.screen.setup(width=ScreenSettings.SCREEN_WIDTH,\
            height=ScreenSettings.SCREEN_HEIGHT)
        self.screen.bgcolor(ScreenSettings.SCREEN_BACKGROUNDCOLOR)
        self.screen.title(ScreenSettings.SCREEN_TITLE)
        # turn off tracer # so we control manually when to update the 
        # screen with update function
        self.screen.tracer(ScreenSettings.TRACER_VALUE)