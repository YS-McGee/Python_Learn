from turtle import *
FONT = ("Courier",15,"normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 275)
        self.color("white")
        self.write(f"Score: {self.score}", 
                    font=FONT, 
                    align=ALIGNMENT)
    def point_gain(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", 
                    font=FONT, 
                    align=ALIGNMENT)
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER", 
                    font=FONT, 
                    align=ALIGNMENT)