# snake class for managing the snake
from turtle import Turtle


class SnakeSettings:
    """
    settings for the snake class
    """
    MOVE_DISTANCE = 20 # pixel amount by how much is the snake moving by
    UP_HEADING = 90 # angel for turning up
    RIGHT_HEADING = 0 # angel for turning righth
    DOWN_HEADING = 270 # angel for turning down
    LEFT_HEADING = 180 # angel for turning left


class Snake:
    """
    class for managing snake
    """

    def __init__(self, pos_x_y: tuple[int,int] = (0,0)) -> None:
        self.snake_segements = self.create_init_snake_segments(pos_x_y)
        self.head = self.snake_segements[0]
        self.head.color('green')


    def create_init_snake_segments(self, pos_x_y: tuple[int,int]) -> list[Turtle]:
        """
        creating the initial position and body of the snake
        """
        list_segments = []
        for num in range(3):
            self.create_segment(list_segments,(pos_x_y[0]+(-20)*num,pos_x_y[1]))

        return list_segments


    def create_segment(self, list_of_segements: list[Turtle], 
    pos_x_y: tuple[int,int]) -> None:
        """
        creating a segment with coordinates pos_x_y, and populating the 
        list_of_segements. base pixel size of the turtle oject is 20 pixels 
        it is the default size
        """
        # default shape size is 20x20 pixels
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(pos_x_y)
        list_of_segements.append(new_segment)


    def extend(self) -> None:
        """
        adding one extra segment at the end of the snake
        """
        self.create_segment(self.snake_segements,self.snake_segements[-1].position())

    def reset_snake(self) -> None:
        """
        Reseting the snake to its initial position
        """
        self.head.reset()
        for segment in self.snake_segements:
            segment.reset()

        self.__init__()

    def move(self) -> None :
        """
        moving the whole body of the snake, in reverse order. 
        Body always follows the head of the snake !
        """
        # starting with last segment and moving it into the next segment 
        # position. Revers order, the body follows the head !
        for num_segment in range(len(self.snake_segements)-1,0,-1):
            next_segment = self.snake_segements[num_segment-1]
            self.snake_segements[num_segment].goto(next_segment.position())
        # at the end moving the head
        self.snake_segements[0].forward(SnakeSettings.MOVE_DISTANCE)

    def move_up(self) -> None:
        """
        turning snakes head up
        """
        # so the snake dosent go back on itself
        if self.head.heading() != SnakeSettings.DOWN_HEADING:
            self.head.setheading(SnakeSettings.UP_HEADING)
    

    def move_down(self) -> None:
        """
        turning snakes head down
        """
        # so the snake dosent go back on itself
        if self.head.heading() != SnakeSettings.UP_HEADING:
            self.head.setheading(SnakeSettings.DOWN_HEADING)


    def move_left(self) -> None:
        """
        turning snakes head left
        """
        # so the snake dosent go back on itself
        if self.head.heading() != SnakeSettings.RIGHT_HEADING:
            self.head.setheading(SnakeSettings.LEFT_HEADING)


    def move_right(self) -> None:
        """
        turning snakes head right
        """
        # so the snake dosent go back on itself
        if self.head.heading() != SnakeSettings.LEFT_HEADING:
            self.head.setheading(SnakeSettings.RIGHT_HEADING)