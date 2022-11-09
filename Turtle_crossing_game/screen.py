# class to manage the screen properties
from turtle import Screen, Turtle

class ScreenSettings:
    """
    Settings for the screen
    """
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    SCREEN_TIME_SLEEP = 0.1
    SCREEN_BACKGROUND_COLOR = 'white'
    SCREEN_TITLE = 'TURTLE CROSSING GAME'
    SCREEN_TRACER_VALUE = 0 # 0 for turning tracer off ,
                            # inorder to control animation manually
    SCREEN_GREEN_POLLY_WIDTH = 50

class MainScreen():
    """
    class for managing the main screen
    """
    def __init__(self) -> None:
        self.screen = Screen()
        self.screen.setup(width=ScreenSettings.SCREEN_WIDTH,\
            height=ScreenSettings.SCREEN_HEIGHT)
        self.screen.bgcolor(ScreenSettings.SCREEN_BACKGROUND_COLOR)
        self.screen.title(ScreenSettings.SCREEN_TITLE)
        self.screen.tracer(ScreenSettings.SCREEN_TRACER_VALUE)
        
        # creating new shape for the green fields
        self.register_green_line_polly_shape("green_fields", \
            width=ScreenSettings.SCREEN_GREEN_POLLY_WIDTH)
        self.creating_green_line("green_fields",\
            (0,ScreenSettings.SCREEN_HEIGHT/2))
        self.creating_green_line("green_fields",\
            (0,-ScreenSettings.SCREEN_HEIGHT/2))

    def register_green_line_polly_shape(self, shape_name: str, width: int ) \
        -> None:
        """
        creating the polly shape of the green line
        """
        P1 = (ScreenSettings.SCREEN_WIDTH/2,width)
        P2 = (ScreenSettings.SCREEN_WIDTH/2,-width)
        P3 = (-ScreenSettings.SCREEN_WIDTH/2,-width)
        P4 = (-ScreenSettings.SCREEN_WIDTH/2,width)
        self.screen.register_shape(shape_name,((P1),(P2),(P3),(P4)))

    def creating_green_line(self, shape_name: str, init_pos_x_y: tuple[int,int])\
         -> None:
        """
        creating green lines with a given start position
        """
        green_lline = Turtle(shape_name) 
        green_lline.penup()
        green_lline.speed('fastest')
        green_lline.setheading(90)
        green_lline.color('green')
        green_lline.goto(init_pos_x_y)