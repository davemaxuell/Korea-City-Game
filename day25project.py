import csv
import pandas
import turtle
from answer_text import Answer

screen = turtle.Screen()
screen.title("Korea City Names")
image_bg = "map.gif"
screen.bgpic(image_bg)

data = pandas.read_csv("대한민국_행정구역.csv")

# def get_mouse_click_coor(x,y):
#     print(x,y)
# 
# turtle.onscreenclick(get_mouse_click_coor)

total = len(data.region.values)
guessed = 0

while guessed != total:
    answer_state = screen.textinput(title="Guess the city! ", prompt="Type your guess!")
    print(answer_state)
    if answer_state in data["region"].values:
        x = data[data.region == answer_state].coorx.values[0]
        y = data[data.region == answer_state].coory.values[0]
        print(x, y)
        answer = Answer()
        answer.goto(x=x, y=y)
        answer.write(f"{answer_state}")
        guessed += 1

turtle.mainloop()