from turtle import *
import turtle

t = Turtle()

def forwards():
    t.forward(5)
def backwards():
    t.forward(-5)
def c_clock():
    t.left(5)
def clock():
    t.right(5)
def clear():
    t.clear()
    t.home()
    
turtle.onkey(forwards, 'w')
turtle.onkey(backwards, 's')
turtle.onkey(c_clock, 'a')
turtle.onkey(clock, 'd')
turtle.onkey(clear, 'c')
# to listen by the turtle
turtle.listen()

turtle.mainloop()