from turtle import Turtle, Screen
from random import choice

sam = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
print(bet)

for turtle_index in range(0, 6):
    sam = Turtle(shape="turtle")
    sam.penup()
    sam.goto(x=-230, y=y_positions[turtle_index])



screen.exitonclick()
