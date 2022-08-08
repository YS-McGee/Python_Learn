import random
from turtle import *

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
            # Default is 20x20
        self.color("blue")
        self.speed(0)
    def relocate(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
            # sc size is 600x600
        self.goto(rand_x, rand_y)
    