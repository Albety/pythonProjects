from turtle import Turtle, Screen

timmy = Turtle()

screen = Screen()

def move_forward():
    timmy.forward(10)
def move_backward():
    timmy.backward(10)
def clockwise():
    timmy.right(10)
def counter_clockwise():
    timmy.left(10)
def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(clockwise, "d")
screen.onkey(counter_clockwise, "a")
screen.onkey(clear_screen, "c")

screen.exitonclick()
