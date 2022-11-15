import turtle
from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["crimson", "navy", "darkcyan", "darkkhaki", "darkorange", "magenta"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []
is_race_on = False
print(bet)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)


if bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == bet:
                print(f"You've won, The {win_color} turtle is the winner!")
            else:
                print(f"You've lost! The {win_color} turtle is the winner!")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
