import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50. Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_state = list(set(all_states) - set(guessed_states))
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        check = df[df["state"] == answer_state]
        timmy.goto(int(check.x), int(check.y))
        timmy.write(answer_state)
