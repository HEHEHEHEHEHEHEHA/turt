
#Connor Kilmer-Setrakian
#9/15/25
#turt


import turtle

# Set up the screen and turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.pendown()
def bullet():
    turt = turtle.Turtle()
    for i in range(30):
        turt.forward(20)
# Define the movement functions
def move_forward():
    my_turtle.forward(4)
    screen.ontimer(move_forward, 20)

def turn_left():
    my_turtle.left(15)

def turn_right():
    my_turtle.right(15)

# Listen for key presses
screen.listen()

# Bind the keys to the functions
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(bullet, "Down")

#Makes Turtle Move
move_forward()

# Keep the window open
turtle.done()
