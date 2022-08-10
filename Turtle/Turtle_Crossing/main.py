import time
import random
from turtle import Screen, clear
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.up,'w')

scoreboard = Scoreboard()

car_man = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_man.create_car()
    car_man.move_cars()

    for car in car_man.all_car:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.reset()
        scoreboard.lv_plus()
        car_man.speedup()

screen.exitonclick()