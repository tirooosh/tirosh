# tirosh tayouri 1/26/22
# bulls and cows

import random

chosen_colors = []
pc_chosen_colors = []
last_colors = []
last_grades = []
recorder = []
turn = 0


def color_rand():  # the pc choosing colors
    global pc_chosen_colors

    colors = ["blue", "light_blue", "yellow", "green", "red", "orange"]
    pc_chosen_colors = []

    for i in range(4):
        color = random.randint(0, 5-i)
        pc_chosen_colors.append(colors[color])
        colors.remove(colors[color])

    print(pc_chosen_colors)


def input_p():  # the input the user gives
    global chosen_colors, turn

    colors = ["blue", "light_blue", "yellow", "green", "red", "orange"]
    chosen_colors = []
    i = 0

    while i != 4 and turn <= 10:
        print(colors, "enter index of color")
        color = int(input())-1
        if 0 <= color < len(colors):
            chosen_colors.append(colors[color])
            colors.remove(colors[color])
            i += 1
        else:
            print("not legal")
    if turn <= 10:
        turn += 1
        compair()


def compair():  # calculating the result of the colors the user inputed
    global last_grades, last_colors
    white = 0
    black = 0
    win = False
    if pc_chosen_colors == chosen_colors:
        print("good job you won")
        win = True
    if not win:
        for i in range(4):
            if chosen_colors[i] == pc_chosen_colors[i]:
                    black += 1
            for j in range(4):
                if chosen_colors[i] == pc_chosen_colors[j] and i != j:
                    white += 1

        last_grades.append("white= "+str(white)+" black= "+str(black))
        last_colors.append(str(chosen_colors))
        print(white, " ", black)
        print("\n" * 100)
        recorder.append(str(chosen_colors) + " " + "white= "+str(white)+" black= "+str(black) + " turn= " + str(turn))
        for i in range(turn):
            print(recorder[i])
        input_p()


def loose():  # checking if the user lost
    if turn > 10:
        print("you lost")
        exit()


color_rand()
input_p()
