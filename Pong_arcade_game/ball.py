# class for managing the ball
from turtle import Turtle
from screen import ScreenSettings

class BallSettings:
    """
    class for managing the class ball settings
    """
    #BALL_WIDTH = 20
    #BALL_HEIGHT = 20
    BALL_COLOR = 'white'
    # basic size 20x20 pixels
    BALL_SHAPE = 'circle'
    BALL_START_VELOCITY_X = 8.0
    BALL_START_VELOCITY_Y = 8.0


class Ball(Turtle):
    """
    class for managing the ball
    """
    def __init__(self, start_pos_x_y: tuple[int,int]) -> None:
        super().__init__()
        self.shape(BallSettings.BALL_SHAPE)
        self.color(BallSettings.BALL_COLOR)
        self.penup()
        self.goto(start_pos_x_y)
        self.velocity_x = BallSettings.BALL_START_VELOCITY_X
        self.velocity_y = BallSettings.BALL_START_VELOCITY_Y
        self.enable_bounce_paddle = True
        self.x_padle_bounce_location = 0.0
        self.time_step_simulation = ScreenSettings.SLEEP_TIME

    def start_moving(self) -> None:
        """
        start moving the ball
        """
        self.setx(self.xcor() + self.velocity_x)
        self.sety(self.ycor() + self.velocity_y)

        # reactivating the option for bouncing again
        if (abs(self.x_padle_bounce_location) - abs(self.xcor())) > 50:
            self.enable_bounce_paddle = True


    def bounce_from_wall(self) -> None:
        """
        defining the behavious for bouncing from the walls
        """
        self.velocity_y = -self.velocity_y

    
    def bounce_from_paddle(self) -> None:
        """
        defining the behavious for bouncing from the paddle
        """
        if self.enable_bounce_paddle: # so each bounce happens only once 
                                    # and a delay for the next bounce to happen
            self.enable_bounce_paddle = False
            self.x_padle_bounce_location = self.xcor()
            self.velocity_x = -self.velocity_x

            # increasing the speed of the ball / simulation
            self.time_step_simulation *= 0.8

    def reset_position(self) -> None:
        """
        Reseting the positin of the ball
        """
        # go to starting position
        self.goto(0,0)
        self.time_step_simulation = ScreenSettings.SLEEP_TIME
        self.velocity_x = -self.velocity_x