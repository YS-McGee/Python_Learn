from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from turtle import *
import time

sc = Screen()
sc.tracer(0)                                        # Eliminate animation
sc.setup(width=800, height=600)
sc.title("Pong")
sc.bgcolor("black")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

sc.listen()
sc.onkeypress(l_paddle.up, 'w')
sc.onkeypress(l_paddle.down, 's')
sc.onkeypress(r_paddle.up, 'Up')
sc.onkeypress(r_paddle.down, 'Down')

game_on = True
while game_on:                                      # Keep refreshing screen
    time.sleep(ball.acceler)
    sc.update()
    ball.move()

    # Top and Bottom Wall Ball Collision 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Paddle Collision 
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball.acceler *= 0.6
    # Right wall Collision
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_plus()
    # Left Wall Collision
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_plus()

sc.exitonclick()