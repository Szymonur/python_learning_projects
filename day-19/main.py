from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_back():
    tim.back(10)
def turn_right():
    tim.right(10)
def turn_left():
    tim.left(10)

def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.pd()

screen.onkey(move_forwards, "w")
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()