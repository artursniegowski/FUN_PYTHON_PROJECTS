from food import Food
from screen import ScreenSettings
from scoreboard import ScoreBoard
from snake import Snake
from turtle import Screen
import time


# creating screen view
screen = Screen()
screen.setup(width=ScreenSettings.SCREEN_WIDTH,height=ScreenSettings.SCREEN_HEIGHT)
screen.bgcolor(ScreenSettings.SCREEN_BACKGROUNDCOLOR)
screen.title(ScreenSettings.SCREEN_TITLE)
# turn off tracer # so we control manually when to update the 
# screen with update function
screen.tracer(ScreenSettings.TRACER_VALUE) 

# creating sneak object
new_snake = Snake()
# creating food class
new_food = Food(ScreenSettings)
# creating Scoreboard object
new_scoreboard = ScoreBoard(ScreenSettings)

# creating the screen listener - watching for any events:
screen.listen()

# differe direction for the snake base on the key pressed
screen.onkey(key="Up", fun=new_snake.move_up)
screen.onkey(key="Down", fun=new_snake.move_down)
screen.onkey(key="Right", fun=new_snake.move_right)
screen.onkey(key="Left", fun=new_snake.move_left)


game_is_on = True
while game_is_on:
    
    screen.update()
    time.sleep(ScreenSettings.SLEEP_TIME)

    new_snake.move()

    # detect collision with food.
    if new_snake.head.distance(new_food) < 15:
        new_food.refresh()
        new_snake.extend()
        new_scoreboard.add_score()
        

    # detect colision with wall
    if (ScreenSettings.SCREEN_WIDTH/2 - 15) < new_snake.head.xcor() or \
        new_snake.head.xcor() <  (5 - ScreenSettings.SCREEN_WIDTH/2) or \
            (ScreenSettings.SCREEN_HEIGHT/2 - 5) < new_snake.head.ycor() or \
                new_snake.head.ycor() <  (15 - ScreenSettings.SCREEN_HEIGHT/2):
        # Game OVER
        new_scoreboard.game_over()
        game_is_on = False

    # detect colision with tail
    # baypassing the checking of the head
    for segment in new_snake.snake_segements[1:]:
        if new_snake.head.distance(segment) < 10:
            # Game OVER
            # if head collides with any segment in the tail:
            new_scoreboard.game_over()
            game_is_on = False
    

# wait for the scree to disapear fro a click
screen.exitonclick()
