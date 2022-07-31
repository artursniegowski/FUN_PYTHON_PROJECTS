# class for managin the cars on the screen
from random import choice, randint
from turtle import Turtle


class CarManagmentSettings:
    """
    Main settings for the car managment
    """
    CAR_SIZE_WIDTH = 20
    CAR_SIZE_LENGTH = 40
    CAR_HEADING_EAST = 0
    CAR_SPEED = 8
    CAR_COLORS_LIST = ['blue4','brown4','chocolate4','DarkGreen','orange','red',
                        'red4','purple4','RoyalBlue4','yellow']

class CarManagment:
    """
    class for managing the cars on the screen
    """
    def __init__(self, start_pos_x: int, lower_limit: int, upper_limit: int) \
        -> None:
        self.car_list = []
        self.car_speed = CarManagmentSettings.CAR_SPEED
        self.start_pos_x = start_pos_x
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit

    def create_car(self, start_pos_x_y: tuple[int,int], color: str) -> Turtle:
        """
        creates a car, and returns an instace of Turtle for the car
        """
        # creates a basic square - default size 20x20 pixel
        new_car = Turtle('square')
        new_car.color(color)
        new_car.penup()
        # new_car.speed('fastest')
        new_car.setheading(CarManagmentSettings.CAR_HEADING_EAST)
        new_car.shapesize(stretch_wid=1.0, \
            stretch_len=CarManagmentSettings.CAR_SIZE_LENGTH/20)
        new_car.goto(start_pos_x_y)
        return new_car

    def create_random_car(self, start_pos_x: int, lower_limit: int, \
        upper_limit: int) -> None:
        """
        creating random car
        """
        random_pos = randint(lower_limit,upper_limit)
        new_car = self.create_car((start_pos_x,random_pos),\
            choice(CarManagmentSettings.CAR_COLORS_LIST))
        self.car_list.append(new_car)


    def create_random_cars(self) -> None:
        """
        careating randomly cars
        """
        random_choice = randint(1,6)
        if random_choice == 1:
            self.create_random_car(self.start_pos_x,\
                self.lower_limit,self.upper_limit)


    def move_cars(self, lef_end_line: int) -> None:
        """
        Moving all the cars, and deleting the cars from the screen that are pass 
        the left line
        """
        if self.car_list:
            for car in self.car_list:
                car.setx(car.xcor() - self.car_speed)
            
            # removing elemnts that are pass the left line
            for car in self.car_list:
                if car.xcor() < lef_end_line-50:
                    car.clear()
            # # updating the list - only cars that are on the screen
            self.car_list = [car for car in self.car_list \
                if car.xcor() > (lef_end_line-50)]


    def level_up(self) -> None:
        """
        Increase the difficulty by increasing the car moving speed
        """
        self.car_speed *= 1.25