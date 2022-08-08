from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import *
import time


sc = Screen()
sc.tracer(0)
sc.setup(width=600, height=600)
sc.title("Snake Game")
sc.bgcolor("black")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

sc.listen()
sc.onkey(snake.up, 'w')
sc.onkey(snake.down, 's')
sc.onkey(snake.left, 'a')
sc.onkey(snake.right, 'd')

game_on = True
while game_on:
    sc.update()
    time.sleep(0.08)
    # Loop from the last segment, and go to the position of the next segment
    snake.move()

    # Collision Detect
    if snake.head.distance(food) < 15:
        # print("Yumi")
        food.relocate()
        snake.extend()
        scoreboard.point_gain()
    # Wall Collision Detect
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
         game_on = False
         scoreboard.game_over()
    # Snake Body Collision Detect
    for seg in snake.segment[1:]:
        # if seg == snake.head:
        #     pass
        if snake.head.distance(seg) < 10:
            game_one = False
            scoreboard.game_over()

sc.exitonclick()