# class for managing the Paddle
from turtle import Turtle


class PaddleSettings:
    """
    Paddle settings
    """
    PADDLE_WIDTH = 20 # this is the default size for square
    PADDLE_HEIHGT = 100
    PADDLE_COLOR = 'white'
    # basic size 20x20 pixels
    PADDLE_SHAPE = 'square'
    PADDLE_DEFAULT_SIZE = 20
    PADDLE_MOVE_DISTANCE = 20


class Paddle(Turtle):
    """
    class managing the paddle
    """
    def __init__(self, start_pos_x_y: tuple[int,int]) -> None:
        """
        creating the paddle object based on the height,
        """
        super().__init__()
        stretch_width = PaddleSettings.PADDLE_HEIHGT / \
            PaddleSettings.PADDLE_DEFAULT_SIZE
        # default size is 20x20 pixels
        self.shape(PaddleSettings.PADDLE_SHAPE)
        self.color(PaddleSettings.PADDLE_COLOR)
        self.shapesize(stretch_wid=stretch_width,stretch_len=1)
        self.penup()
        self.goto(start_pos_x_y)

    def move_up(self) -> None:
        """
        moving the paddle up
        """
        self.sety(self.ycor() + \
            PaddleSettings.PADDLE_MOVE_DISTANCE)

    def move_down(self) -> None:
        """
        moving the paddle down
        """
        self.sety(self.ycor() - \
            PaddleSettings.PADDLE_MOVE_DISTANCE)