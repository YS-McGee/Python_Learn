# import colorgram

# colors = colorgram.extract('img.png', 30)
# color_list = []
# for c in colors:
#     color_t = (c.rgb.r, c.rgb.g, c.rgb.b)
#     color_list.append(color_t)
# print(color_list)

from turtle import *
import turtle as tur
import random

color_list = [(125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205), (109, 67, 85), (39, 35, 34), 
(223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47), (65, 154, 134), (132, 41, 43), 
(184, 98, 81), (183, 180, 181), (210, 200, 108), (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59), 
(193, 190, 192), (17, 78, 98), (215, 184, 172), (190, 190, 195), (78, 72, 31)]

t = Turtle()
tur.colormode(255)
t.hideturtle()
t.speed(0)

t.penup()
t.goto(t.pos() + (-300, -300))
for _ in range(10):
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        # t.penup()
        # t.forward(50)
        t.goto(t.pos() + (50, 0))
    # t.forward(-500)
    # t.left(90)
    # t.up()
    # t.forward(50)
    # t.right(90)
    t.goto(t.pos() + (-500, 50))


screen = Screen(width=300)
screen.exitonclick()