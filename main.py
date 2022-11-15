from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def move_counter_clock():
    t.left(10)


def move_clock_wise():
    t.right(10)


def clear():
    t.reset()


s.listen()
s.onkey(key="w", fun=move_forward)
s.onkey(key="s", fun=move_backward)
s.onkey(key="a", fun=move_counter_clock)
s.onkey(key="d", fun=move_clock_wise)
s.onkey(key="c", fun=clear)

s.exitonclick()
