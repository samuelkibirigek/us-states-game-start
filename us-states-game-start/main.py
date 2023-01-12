import turtle
import pandas

screen = turtle.Screen()
screen.title("The U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
state_list = states.state.to_list()


correct_states = 0
correct_guesses = []
states_to_learn = []

while len(correct_guesses) < 50:
    answer = screen.textinput(title="Guess the State", prompt=f"{correct_states}/50 States Correct")
    answer_state = answer.title()
    if answer_state == "Exit":
        break
    for any_state in state_list:
        if answer_state == any_state and answer_state not in correct_guesses:
            correct_states += 1
            state_details = states[states["state"] == answer_state]
            x_pos = int(state_details["x"])
            y_pos = int(state_details["y"])
            state_obj = turtle.Turtle()
            state_obj.penup()
            state_obj.hideturtle()
            state_obj.goto(x_pos, y_pos)
            state_obj.write(answer_state)
            correct_guesses.append(answer_state)


for the_states in states["state"].to_list():
    if the_states not in correct_guesses:
        states_to_learn.append(the_states)
        learning_dict = {"states": states_to_learn}
        learning_df = pandas.DataFrame(learning_dict)
        learning_df.to_csv("states_to_learn.csv")


turtle.mainloop()


