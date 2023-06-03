from turtle import Turtle, Screen

point = Turtle()
screen = Screen()
angle = 0
def move_forward():
    point.forward(20)

def move_backward():
    point.backward(20)

def rotate_cw():
    global angle
    angle -= 10
    point.setheading(angle)

def rotate_ccw():
    global angle
    angle += 10
    point.setheading(angle)

def reset():
    point.clear()
    point.penup()
    point.home()
    point.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_ccw)
screen.onkey(key="d", fun=rotate_cw)
screen.onkey(key="c", fun=reset)

screen.exitonclick()