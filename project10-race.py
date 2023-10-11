from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet?", prompt="Which turtle will win the race? Choose color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cord = -100
is_on_race = False

list_turtles = []
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cord)
    y_cord += 40
    list_turtles.append(new_turtle)

if user_bet:
        is_on_race = True

while is_on_race:
    for turtle in list_turtles:
        if turtle.xcor() > 230:
            is_on_race = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
        random_num = random.randint(0,10)
        turtle.forward(random_num)


screen.exitonclick()