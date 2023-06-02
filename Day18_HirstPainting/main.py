import colorgram
from turtle import Turtle, Screen
import random

# colors = colorgram.extract('image.jpg', 20)
# color_list = []
# for i in range(len(colors)):
#     red = colors[i].rgb.r
#     blue = colors[i].rgb.b
#     green = colors[i].rgb.g
#     tup = (red, blue, green)
#     color_list.append(tup)

color_list = [(208, 96, 158), (234, 101, 213), (41, 144, 104), (149, 57, 78), (130, 194, 168), (202, 162, 137), (148, 83, 65), (24, 55, 40), (204, 68, 90), (169, 55, 159), (139, 152, 180), (193, 121, 89), (59, 93, 117), (26, 36, 44), (223, 187, 171), (63, 34, 46)]

dot = Turtle()
dot.penup()
dot.speed(0)
screen = Screen()
screen.setup(1000, 1000)
screen.colormode(255)
dot.setx(-250)
dot.sety(-250)

for i in range(10):
    for _ in range(10):
        dot.color(random.choice(color_list))
        dot.dot(20)
        dot.forward(50)
    dot.setx(-250)
    dot.sety(50*(i+1) - 250)

dot.ht()
screen.exitonclick()