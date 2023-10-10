import turtle
from random import choice
import colorgram

# list_of_colors = []
# colors = colorgram.extract('spots.jpg', 20)
# for color in colors:
#     tuples_of_colors = (color.rgb[0], color.rgb[1], color.rgb[2])
#     list_of_colors.append(tuples_of_colors)
# print(list_of_colors)

timmy = turtle.Turtle()
turtle.colormode(255)
colors_list = [(199, 12, 32), (250, 237, 19), (39, 76, 189), (238, 228, 5), (38, 217, 68), (228, 159, 48), (28, 40, 157), (215, 75, 13), (15, 154, 15), (198, 15, 11), (243, 33, 166), (68, 10, 30), (228, 18, 120), (60, 15, 8), (224, 141, 209), (11, 97, 62)]
timmy.penup()
timmy.hideturtle()
timmy.speed(0)
x_pos = -250
y_pos = 200
timmy.goto(x_pos, y_pos)

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, choice(colors_list))
        timmy.forward(50)
    y_pos -= 40
    timmy.goto(x_pos, y_pos)

screen = turtle.Screen()
screen.exitonclick()


