# Components
# TODO 
# 1. Screen - create 
# 2. paddle - create and move 
# 3. create another paddle so we can have a two player game
# 4. Create a ball and make it move
# 5. detects collisions with wall and bounce
# 6. detect colision with the padle
# 7. detect when the paddle misses the ball
# 8. Scoreboards

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
from screen import GamesScreen, ScreenSettings
import time

# creating the screen object
game_screen = GamesScreen()

# creating paddle for right palyer
right_paddle = Paddle((350,0))
# creating paddle for the left player
left_paddle = Paddle((-350,0))

# creating left score object
left_scoreboard = ScoreBoard((-ScreenSettings.SCREEN_WIDTH/4,ScreenSettings.SCREEN_HEIGHT/2-50))
# creating right score object
right_scoreboard = ScoreBoard((ScreenSettings.SCREEN_WIDTH/4,ScreenSettings.SCREEN_HEIGHT/2-50))

# creating the ball
pong_ball = Ball((0,0))

# activating event listeners
game_screen.screen.listen()

# binding functions to the keys
# for the right paddle
game_screen.screen.onkeypress(key="Up",fun=right_paddle.move_up)
game_screen.screen.onkeypress(key="Down",fun=right_paddle.move_down)
# for the left paddle
game_screen.screen.onkeypress(key="w",fun=left_paddle.move_up)
game_screen.screen.onkeypress(key="s",fun=left_paddle.move_down)


# main game loop
game_on = True
while game_on:
    time.sleep(pong_ball.time_step_simulation)
    game_screen.screen.update()
    

    # updaiting position of the ball
    pong_ball.start_moving()

    # detecting collision with the wall
    if pong_ball.ycor() > (ScreenSettings.SCREEN_HEIGHT/2-20) or \
        pong_ball.ycor() < (20-ScreenSettings.SCREEN_HEIGHT/2) :

        pong_ball.bounce_from_wall()

    # detecting collision with both paddles
    
    if (right_paddle.xcor() + 15) > (pong_ball.xcor()) and (right_paddle.xcor() - 15) < (pong_ball.xcor()) and \
        (right_paddle.ycor() + 55) > (pong_ball.ycor()) and (right_paddle.ycor() - 55) < (pong_ball.ycor()):
        pong_ball.bounce_from_paddle()

    if (left_paddle.xcor() + 15) > (pong_ball.xcor()) and (left_paddle.xcor() - 15) < (pong_ball.xcor()) and \
        (left_paddle.ycor() + 55) > (pong_ball.ycor()) and (left_paddle.ycor() - 55) < (pong_ball.ycor()):
        pong_ball.bounce_from_paddle()

    # if pong_ball.distance(right_paddle) < 50 and pong_ball.xcor() > 320.00 or \
    #     pong_ball.distance(left_paddle) < 50 and pong_ball.xcor() < -320.00:

    #     pong_ball.bounce_from_paddle()
    
    # detecting if the ball went pass the left side
    if pong_ball.xcor() < -ScreenSettings.SCREEN_WIDTH/2:
        # right paddle player won, add score
        right_scoreboard.add_score()
        # reset the position of the ball
        pong_ball.reset_position()
    # detecting if the ball went pass the right side
    if pong_ball.xcor() > ScreenSettings.SCREEN_WIDTH/2:
        # left paddle palyer won, add score
        left_scoreboard.add_score()
        # reset the position of the ball
        pong_ball.reset_position()

# wait for the scree to disapear after a click
game_screen.screen.exitonclick()