import random 
from turtle import Turtle,Screen 
tinny = Turtle ()
colours = ["CornflowerBlue", "DarkOrchid",
"IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(angle):
    for _ in range(angle):
        number_of_draws = 360/angle
        tinny.forward(100)
        tinny.right(number_of_draws)

for i in range(3,11):
    tinny.color(random.choice(colours))
    draw_shape(i)

screen = Screen()
screen.exitonclick()