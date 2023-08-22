import turtle
import pandas

states_data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

game_is_on = True
guessed_states = set()


def append_state(state, x, y):
    t = turtle.Turtle()
    t.pu()
    t.hideturtle()
    t.goto((x, y))
    t.write(state)


while len(guessed_states) < 50:
    #  Get user input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "name?").strip().title()
    if answer_state == "Exit":
        # Save not guessed to csv "learn.csv"
        states_list = set(states_data.state.to_list())
        not_guessed = states_list.difference(guessed_states)
        df = pandas.DataFrame(not_guessed)
        df.to_csv("learn.csv")
        break
    if answer_state in states_data.state.values:
        guessed_states.add(answer_state)
        state_to_write = states_data[states_data.state == answer_state].values
        append_state(state_to_write[0][0], state_to_write[0][1], state_to_write[0][2])

#  Check win
if len(guessed_states) == 50:
    t = turtle.Turtle()
    t.pu()
    t.hideturtle()
    t.write("YOU WON!", font=("Verdana", 32, "bold"), align="center")

turtle.mainloop()
