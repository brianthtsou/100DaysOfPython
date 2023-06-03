from turtle import Turtle, Screen
import random


race_finished = False
turtles = []
winning_turtle = None
colors = ["red", "green", "blue", "purple", "black"]
for i in range(5):
    turtles.append(Turtle())
    turtles[i].color(colors[i])
    turtles[i].shape("turtle")
    turtles[i].penup()
    turtles[i].setx(-200)
    turtles[i].sety(250 - (i+1) * 75)
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win? Enter the color of the turtle: ")
#print(user_bet)

while not race_finished:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= 230:
            winning_turtle = turtle
            race_finished = True
            break
print(winning_turtle.color()[0])
if user_bet == winning_turtle.color()[0]:
    print(f"The winner was {winning_turtle.color()[0]}, you win!")
else:
    print(f"The winner was {winning_turtle.color()[0]}, you lose.")
screen.exitonclick()