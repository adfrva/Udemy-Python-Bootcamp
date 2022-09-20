from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)

def turn_left():
    turtle.left(10)

def turn_right():
    turtle.right(10)

def toggle_pen():
    if turtle.isdown():
        turtle.penup()
    else:
        turtle.pendown()

screen.onkey(move_forward, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(toggle_pen, "space")
screen.listen()
screen.exitonclick()