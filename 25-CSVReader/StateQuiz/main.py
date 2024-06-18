import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Quiz")
states_df = pandas.read_csv("50_states.csv")

#Create turtle screen with blank US map image
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

state_guess = screen.textinput(title="Guess a state", prompt="What's another state? ")

#TODO Make if statement that checks if the state guessed is in the dataframe
#If so, make state name display where the coordinates are on the map

turtle.mainloop()