from turtle import *

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

        self.hideturtle()
        self.color("black")
        self.update()
    def lv_plus(self):
        self.level += 1
        self.update()
    def update(self):
        self.clear()
        self.penup()
        self.goto(-240, 270)
        self.write(f"Level: {self.level}", align="center", font=FONT)
    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
