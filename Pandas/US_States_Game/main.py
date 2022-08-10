from turtle import *
import turtle
import pandas

IMAGE = 'blank_states_img.gif'
df = pandas.read_csv('50_states.csv')

state_list = df['state'].to_list()
guess_cnt = 0
guess_list = []

sc = Screen()
sc.title("U.S. States Game")
sc.addshape(IMAGE)

turtle.shape(IMAGE)
t = Turtle()
t.hideturtle()

def add_state(usr_answer):
    row_ds = df[df["state"] == usr_answer]
    x = int(row_ds.x)
    y = int(row_ds.y)   
    t.penup()
    t.goto(x,y)
    t.write(usr_answer)
def csv_gen():
    missing_state_list = []
    for state in state_list:
        if state not in guess_list:
            missing_state_list.append(state)
    missing_state_dict = {'States':missing_state_list}
    new_csv = pandas.DataFrame(missing_state_dict)
    new_csv.to_csv('missing_states.csv')
    # print(new_csv)

while guess_cnt < 50:
    usr_answer = sc.textinput(
        title=f"{guess_cnt}/50 States Correct", 
        prompt="What's another state's name?"
    ).title()                                       # Convert to title case
    # print(df[df["state"] == usr_answer])
    if usr_answer == "Exit":
        csv_gen()
        break
    if usr_answer in state_list:
        guess_cnt += 1
        guess_list.append(usr_answer)
        add_state(usr_answer)

sc.exitonclick()
