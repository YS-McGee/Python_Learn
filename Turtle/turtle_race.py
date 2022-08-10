from turtle import *
import turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue']
usr_bet = textinput(title='Your Bet!', prompt="What's Your Bet?")

t = []
sc = turtle.Screen()
sc.setup(500, 400)
for i in range(5):
    t.append(Turtle(shape='turtle'))
    t[i].color(colors[i])
    t[i].up()
    t[i].goto(-240, -60+i*30)

not_finish = 1
while not_finish:
    for tur in t:
        tur.forward(random.randint(0,10))
        if tur.xcor() > 230:
            if tur.pencolor == usr_bet:
                print("You Win!")
            else:
                print("You Lose......")
            not_finish = 0
            break


turtle.mainloop()
