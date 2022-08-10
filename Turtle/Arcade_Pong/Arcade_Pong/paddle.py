from turtle import *

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.goto(pos)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
    def up(self):
        self.penup()
        self.goto(self.xcor(), self.ycor()+20)
    def down(self):
        self.penup()
        self.goto(self.xcor(), self.ycor()-20)    