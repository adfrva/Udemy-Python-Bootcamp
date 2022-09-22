from turtle import Turtle, Screen
import random

def rand_forward(turtle):
    random_forward = random.randint(0, 10)
    turtle.forward(random_forward)

green_turtle = Turtle(shape="turtle")
green_turtle.color("green")
green_turtle.penup()

red_turtle = Turtle(shape="turtle")
red_turtle.color("red")
red_turtle.penup()


blue_turtle = Turtle(shape="turtle")
blue_turtle.color("blue")
blue_turtle.penup()


purple_turtle = Turtle(shape="turtle")
purple_turtle.color("purple")
purple_turtle.penup()


yellow_turtle = Turtle(shape="turtle")
yellow_turtle.color("yellow")
yellow_turtle.penup()


orange_turtle = Turtle(shape="turtle")
orange_turtle.color("orange")
orange_turtle.penup()

screen = Screen()
screen.setup(height=400, width=500)

user_pick = screen.textinput(title="Pick Your Turtle", prompt="Who will win the race? Enter a color")

green_turtle.goto(x=-240, y=50)
red_turtle.goto(x=-240, y=25)
blue_turtle.goto(x=-240, y=0)
yellow_turtle.goto(x=-240, y=-25)
orange_turtle.goto(x=-240, y=-50)
purple_turtle.goto(x=-240, y=-75)

race_finished = False

while not race_finished:
    turtles = [green_turtle, red_turtle, blue_turtle, yellow_turtle, orange_turtle, purple_turtle]

    for turtle in turtles:
        if turtle.xcor() >= 225:
            winning_turtle = turtle.pencolor()
            print(f"The {winning_turtle} turtle is the winner!")

            if winning_turtle == user_pick:
                print("You Win!")
            else:
                print("You lose :(")

            race_finished = True
        
        else:
            rand_forward(turtle)


screen.exitonclick()