from turtle import colormode ,Screen, Turtle
from random import choice
import colorgram

# extracting colors from the picture, using colorgram
# and storing them into a list color_palette
color_palette = []
color_palette_extracted = colorgram.extract('color_palette.jpg',25)
for color in color_palette_extracted:
    color_palette.append((color.rgb[0],color.rgb[1],color.rgb[2]))

# creating turtle object
turtle_object = Turtle()
# hidding the turtle
turtle_object.hideturtle()
# making sure the simulation is drawn out as fast as possible
turtle_object.speed("fastest")
# setting the colors to r,g,b - 255
colormode(255)

# function for drawing a circle and filling it with radom color
def drawn_circle(turtle_object: Turtle,size: int, pos: tuple[int,int] = (0,0)) -> None:
    """
    drawing a random color circle with radius of 20
    """
    random_RGB_color = choice(color_palette)
    turtle_object.penup()
    turtle_object.color(random_RGB_color)
    turtle_object.fillcolor(random_RGB_color)

    turtle_object.goto(pos)

    turtle_object.begin_fill()
    turtle_object.circle(size)
    turtle_object.end_fill()

# function for drawing the grid
def draw_grid(size: int, gap: int, offset: int = 0) -> None:
    """
    function for drawing the grid based on the size of the grid,
    distance between the dots and offset for the startign position
    """
    for rows in range(size):
        for columns in range(size):
            drawn_circle(turtle_object,20,(offset+rows*gap,offset+columns*gap))

##########################
# main content - program #
##########################
draw_grid(10,70,-300)


# wait for a click to exit the Turtle simulation
screen = Screen()
screen.exitonclick()
