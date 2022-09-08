from carmanagment import CarManagment
from player import Player
from scoreboard import ScoreBoard
from screen import MainScreen, ScreenSettings
from time import sleep

# creating screen object, init all the necessary settings
game_screen = MainScreen()

# creating the player object
player_turtle = Player((0,20-ScreenSettings.SCREEN_HEIGHT/2))

# creating the scoreboard
score_board = ScoreBoard((80-ScreenSettings.SCREEN_WIDTH/2, \
    ScreenSettings.SCREEN_HEIGHT/2-40))

# start car-managment
car_managment = CarManagment(ScreenSettings.SCREEN_WIDTH/2, \
    -ScreenSettings.SCREEN_HEIGHT/2+70,ScreenSettings.SCREEN_HEIGHT/2-70)

# starting to listen for key events
game_screen.screen.listen()
# binding the key arrow Up to the player function
game_screen.screen.onkeypress(key="Up",fun=player_turtle.move_up)


# Main game loop
game_is_on = True
while game_is_on:
    # setting the default sleep time for tha animation
    sleep(ScreenSettings.SCREEN_TIME_SLEEP)
    # updating the screen , since tracer is off
    game_screen.screen.update()
    # update the score on the screen
    score_board.draw_score()

    # creat reandomly cars
    car_managment.create_random_cars()
    # move the cars
    car_managment.move_cars(-ScreenSettings.SCREEN_WIDTH/2)

    # detecting - getting over the street
    if player_turtle.turtle_passed_the_road(ScreenSettings.SCREEN_HEIGHT/2-30):
        # level up
        score_board.add_level()
        # reset the player to start position
        player_turtle.back_to_start_position()
        # increase the difficulty
        car_managment.level_up()
        
    # detecting colision with a car    
    for car in car_managment.car_list:
        if car.distance(player_turtle) < 20:
            # game over   
            score_board.game_over()
            game_is_on = False


# wait for a user click to make the screen disappear
game_screen.screen.exitonclick()