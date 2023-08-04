import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("dots.jpg", 20)
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

color_list = [(205, 161, 87), (59, 89, 128), (141, 92, 43), (220, 207, 111), (136, 174, 197), (136, 28, 50), (153, 50, 85), (46, 55, 103), (133, 188, 145), (167, 159, 44), (190, 140, 162), (82, 22, 44), (183, 92, 106), (38, 43, 66), (88, 117, 174), (59, 41, 35)]

t = Turtle()
s = Screen()
t.hideturtle()
t.speed(0)
t.pu()


for j in range(10):
    for i in range(10):
        t.goto(-325 + 70 * i, -325 + 70 * j)
        t.dot(20, random.choice(color_list))

s.exitonclick()