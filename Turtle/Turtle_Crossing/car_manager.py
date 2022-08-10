from turtle import *
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_SPEED = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_car = []
        self.speed = STARTING_SPEED
    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            rand_y = 20 * random.randint(-12, 12)
            new_car.goto(300, rand_y)
            self.all_car.append(new_car)
    def move_cars(self):
        for car in self.all_car:
            car.backward(self.speed)
    def speedup(self):
        self.speed += MOVE_INCREMENT
