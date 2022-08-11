from operator import truediv
from turtle import colormode ,Screen, Turtle, goto, shape
from random import randint

# basic settings for the game
SCREE_WIDTH = 500
SCREE_HEIGHT = 500

# posible players
colors = ["red","orange","yellow","green","blue","purple"]

# setting up the scree
screen = Screen()
screen.setup(width=SCREE_WIDTH, height=SCREE_HEIGHT)

# the user is palcing his bet
# expecting the right color,
# otherwise keep asking for the right color
user_bet = ""
while not user_bet in colors:
    user_bet = screen.textinput(title="Place the BET", prompt=f"Which turtle do you bet on? \nEnter a color one of {colors}: ")
    user_bet = user_bet.lower().strip()

# list with all players
racing_turtels = []
# creating players
def create_turtel_objects(racing_turtels: list[Turtle], players: list[str]) -> None:
    """
    Creating a list of turtles with predefined settings
    """
    for player in players:
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.color(player)
        new_turtle.shape("turtle")
        racing_turtels.append(new_turtle)

# moving to startin position
def move_start_position(racing_turtels: list[Turtle], screen_width: int = SCREE_WIDTH) -> None:
    """
    Moving to starting position
    """
    vertical_aligment = 0
    for turtle in racing_turtels:
        turtle.goto(20-screen_width/2,-60+30*vertical_aligment)
        vertical_aligment += 1

# moving the turtle by a random number
def rand_forward(turtle: Turtle) -> None:
    """
    move forward by a radom number
    """
    turtle.forward(randint(0,10))

# start the race
def start_race(racing_turtels: list[Turtle], width: int) -> None:
    """
    strating the raace
    """
    winner = False
    while not winner:
        for turtle in racing_turtels:
            rand_forward(turtle)

            if turtle.pos()[0] >= width/2 - (40/2):
                winner = True
                break

    return turtle

# creating turtel players
create_turtel_objects(racing_turtels, colors)
# setting the starting position for each turtle
move_start_position(racing_turtels,SCREE_WIDTH)
# startin the race
turtle_who_won = start_race(racing_turtels,SCREE_WIDTH)


print(f"{turtle_who_won.color()[0]} won the race!")
if user_bet == turtle_who_won.color()[0] :
    print("You have won the bet! Congratulations")
else:
    print("You have lost the bet!")



# wait for a click to exit the Turtle simulation
screen.exitonclick()