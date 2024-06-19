import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Quiz")
states_df = pandas.read_csv("50_states.csv")

#Create turtle screen with blank US map image
screen.addshape("blank_states_img.gif")
screen.setup(height=481, width=725)
turtle.shape("blank_states_img.gif")


def check_guess(guess):
    cap_guess = guess.title()

    if states_df['state'].str.contains(cap_guess).any():
        row_match = states_df.loc[states_df['state'] == cap_guess]
        x_coord = row_match['x'].item()
        y_coord = row_match['y'].item()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_coord, y_coord)
        t.write(cap_guess)
        print(cap_guess)


end_quiz = 0
while not end_quiz:
    state_guess = screen.textinput(title="Guess a state", prompt="What's another state? ")

    if state_guess.lower() == "exit":
        end_quiz = 1
        turtle.bye()
    else:
        check_guess(state_guess)
