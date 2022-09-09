# class responsible for the player
from turtle import Turtle

class PlayerSettings:
    """
    Managing the settings of the player
    """
    PLAYER_SHAPE = 'turtle'
    PLAYER_COLOR = 'black'
    PLAYER_MOVE_DISTANCE = 10
    PLAYER_HEADING_UP = 90

class Player(Turtle):
    """
    class for managing the player
    """
    def __init__(self, start_pos_x_y: tuple[int,int]) -> None:
        super().__init__()
        self.shape(PlayerSettings.PLAYER_SHAPE)
        self.color(PlayerSettings.PLAYER_COLOR)
        self.setheading(PlayerSettings.PLAYER_HEADING_UP)
        self.penup()
        self.start_pos_x_y = start_pos_x_y
        self.goto(start_pos_x_y)

    def move_up(self) -> None:
        """
        moving the turtle object up
        """
        self.sety(self.ycor()+PlayerSettings.PLAYER_MOVE_DISTANCE)


    def back_to_start_position(self) -> None:
        """
        moving the turtle object back to its start position
        """
        self.goto(self.start_pos_x_y)

    def turtle_passed_the_road(self, upper_limit: int = 100) -> bool:
        """
        returns true if the turtle 'y' coordinate is pass the upper limit
        else returns false
        """
        return self.ycor() > upper_limit