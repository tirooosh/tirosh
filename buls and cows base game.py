# tirosh tayouri 1/26/22
# bulls and cows

import random
from tkinter import *
import tkinter as tk

chosen_colors = []
temp_chosen_colors = []
already_used = []
color_press = 0
pc_chosen_colors = []
last_colors = []
last_grades = []
recorder = []
turn = 0
root = tk.Tk()
root.title("bulls and cows")
root.geometry("300x550")
black = 0
white = 0


def board_creator():  # creats the board
    canvas1 = Canvas(root, width=300, height=550)
    canvas1.create_line(50, 50, 50, 550, fill="black", width=2)
    canvas1.create_line(250, 50, 250, 550, fill="black", width=2)
    canvas1.create_line(0, 50, 300, 50, fill="black", width=2)
    canvas1.grid(row=1)

    btn_green = Button(root, height=2, width=5, bg="green", command=lambda color="green": clr_btn_prs(color))
    btn_green.place(x=0, y=0)

    btn_blue = Button(root, height=2, width=5, bg="blue", command=lambda color="blue": clr_btn_prs(color))
    btn_blue.place(x=50, y=0)

    btn_light_blue = Button(root, height=2, width=5, bg="light blue",
                            command=lambda color="light blue": clr_btn_prs(color))
    btn_light_blue.place(x=100, y=0)

    btn_yellow = Button(root, height=2, width=5, bg="yellow", command=lambda color="yellow": clr_btn_prs(color))
    btn_yellow.place(x=150, y=0)

    btn_red = Button(root, height=2, width=5, bg="red", command=lambda color="red": clr_btn_prs(color))
    btn_red.place(x=200, y=0)

    btn_orange = Button(root, height=2, width=5, bg="orange", command=lambda color="orange": clr_btn_prs(color))
    btn_orange.place(x=250, y=0)

    menu = Menu(root)
    root.config(menu=menu)
    file_menu = Menu(menu)
    menu.add_cascade(label='menu', menu=file_menu)
    file_menu.add_command(label='submit', command=submit_btn)

    for i in range(10):
        lbl_num = Label(root, text=i + 1)
        lbl_num.place(x=0, y=i * 50 + 51)

    pc_color_rand()


def clr_btn_prs(color):  # changes the color that will be displayed
    global color_press, temp_chosen_colors, already_used
    if len(already_used) == 4:
        already_used = []
    keep = True
    if color_press < 4 and turn <= 11:
        for i in already_used:
            if i == color:
                print("in use")
                keep = False
        if keep:
            already_used.append(color)
            print(already_used)
            lbl_crl = Label(root, height=2, width=5, bg=color)
            lbl_crl.place(x=52 + 50 * color_press, y=52 + 50 * turn)
            color_press += 1
            temp_chosen_colors.append(color)


def score_displayer():
    x_place1 = 1
    x_place2 = 1
    for i in range(black):
        lbl_score = Label(root, bg="black", height=1, borderwidth=1, width=2)
        if x_place1 <= 2:
            lbl_score.place(x=227 + x_place1 * 25, y=turn * 50 + 2)
            x_place1 += 1
        elif x_place1 >= 3:
            lbl_score.place(x=227 + x_place2 * 25, y=25 + turn * 50)
            x_place2 += 1
    for i in range(white):
        lbl_score = Label(root, bg="white", borderwidth=1, height=1, width=2)
        if x_place1 <= 2:
            lbl_score.place(x=227 + x_place1 * 25, y=turn * 50 + 2)
            x_place1 += 1
        elif x_place1 >= 3:
            lbl_score.place(x=227 + x_place2 * 25, y=25 + turn * 50)
            x_place2 += 1


def pc_color_rand():  # the pc choosing colors
    global pc_chosen_colors

    colors = ["blue", "light_blue", "yellow", "green", "red", "orange"]
    pc_chosen_colors = []

    for i in range(4):
        color = random.randint(0, 5 - i)
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
        color = int(input()) - 1
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
    global last_grades, last_colors, black, white
    white = 0
    black = 0
    win = False
    if pc_chosen_colors == chosen_colors or black == 4:
        print("good job you won")
        win = True
        black = 4
    if not win:
        for i in range(4):
            if chosen_colors[i] == pc_chosen_colors[i]:
                black += 1
            elif chosen_colors[i] in pc_chosen_colors:
                white += 1

        last_grades.append("white= " + str(white) + " black= " + str(black))
        last_colors.append(str(chosen_colors))
        print(white, " ", black)
        print("\n" * 100)
        recorder.append(
            str(chosen_colors) + " " + "white= " + str(white) + " black= " + str(black) + " turn= " + str(turn))
        for i in range(turn):
            print(recorder[i])
        score_displayer()


def loose():  # checking if the user lost
    if turn > 10:
        print("you lost")
        exit()


def submit_btn():  # the submit button affects
    global chosen_colors, temp_chosen_colors, turn, color_press
    if temp_chosen_colors[3] != "":
        chosen_colors = temp_chosen_colors
        temp_chosen_colors = []
        color_press = 0
        turn += 1
        compair()
    if turn == 10:
        exit()


board_creator()
root.mainloop()
