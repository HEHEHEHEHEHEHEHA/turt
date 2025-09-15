#Connor Kilmer-Setrakian
#9/15/25
#turt


import turtle

# Set up the screen and turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.pendown()

# Define the movement functions
def move_forward():
    my_turtle.forward(4)
    screen.ontimer(move_forward, 20)

def move_backward():
    my_turtle.backward(10)

def turn_left():
    my_turtle.left(15)

def turn_right():
    my_turtle.right(15)

# Listen for key presses
screen.listen()

# Bind the keys to the functions
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

#Makes Turtle Move
move_forward()

# Keep the window open
turtle.done()

