# from MODULE import CLASS
import turtle as t
from turtle import Screen, Turtle
import random

obj = Turtle()
t.colormode(255)
obj.speed(0) 

# for _ in range(4):
#     obj.forward(200)
#     obj.left(90)

# for _ in range(20):
#     # obj.pencolor("gold1")
#     obj.forward(10)
#     obj.penup()
#     obj.forward(10)
#     obj.pendown()

"""  Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon """
def draw_shapes():
    for i in range(3, 11):
        for _ in range(i):
            obj.forward(100)
            obj.right(360/i)
# draw_shapes()

def random_walk():
    color = ["blueviolet", "cadetblue", "chartreuse", "chocolate", "cornflowerblue", "crimson", "darkgoldenrod", "darkred", "darkturquoise", "floralwhite", "green"]
    obj.pensize(9)                                      # line thickness
    obj.speed(0)                                        # draw speed = max
    direction = [0, 90, 180, 270]
    while 1:
        # obj.color(random.choice(color))
        obj.color(random_color())
        obj.forward(30*random.randint(0,2))
        obj.setheading(random.choice(direction))        # set random direction

def random_color():
    r = random.randint(0,255)        
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)
# random_walk()

def circles():
    for _ in range(72):
        obj.color(random_color())
        obj.circle(80)
        # obj.left(5)
        obj.setheading(obj.heading() + 5)

circles()


screen = Screen()
screen.exitonclick()