from turtle import Turtle,Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=800,height=600)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle win the race? chose a color: ")
color = ["red","yellow","green","purple","orange","blue","black","hot pink","tan","silver"]
y_direction = [-180,-140,-100,-60,-20,20,60,100,140,180]

all_turtle = []
for turtle_index in range(0,10):
    Participate = Turtle(shape="turtle")
    Participate.color(color[turtle_index])
    Participate.penup()
    Participate.goto(x=-325,y=y_direction[turtle_index])
    all_turtle.append(Participate)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        # 380 is 400 - half the width of the turtle
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've win! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        # Make each turtle move a random amount.
        distance = random.randint(0,20)
        turtle.forward(distance)

screen.exitonclick()
