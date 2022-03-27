# tirosh tayouri
# bulls and cows

import random
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.simpledialog import askstring

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
win = False
name = StringVar()
names = []
wins = []
turns = []


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
    file_menu.add_command(label='reset', command=reset)
    file_menu.add_command(label='rules', command=rules)
    file_menu.add_command(label='top 10', command=top_10)

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
    while not pc_chosen_colors:
        colors = ["blue", "light blue", "yellow", "green", "red", "orange"]
        pc_chosen_colors = []

        for i in range(4):
            color = random.randint(0, 5 - i)
            pc_chosen_colors.append(colors[color])
            colors.remove(colors[color])

        print(pc_chosen_colors)


def input_p():  # the input the user gives
    global chosen_colors, turn

    colors = ["blue", "light blue", "yellow", "green", "red", "orange"]
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
    global last_grades, last_colors, black, white, win
    white = 0
    black = 0
    if pc_chosen_colors == chosen_colors or black == 4:
        winer()
    if not win:
        counter = 0
        for i in chosen_colors:

            if i == pc_chosen_colors[counter]:
                black += 1
            elif i in pc_chosen_colors:
                white += 1
            counter += 1

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
        if askyesno("you lost", "continue?"):
            continu()
        else:
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
        score_displayer()
        exit()


def reset():  # going a turn back
    global temp_chosen_colors, already_used, color_press
    temp_chosen_colors = []
    already_used = []
    print(already_used)

    while color_press > 0:
        color_press -= 1
        lbl_crl = Label(root, height=2, width=5, bg="white")
        lbl_crl.place(x=52 + 50 * color_press, y=52 + 50 * turn)


def winer():  # if win
    global win
    print("good job you won")
    win = True
    if askyesno("you won", "continue?"):
        continu()
    else:
        exit()


def rules():
    messagebox.showinfo("rules", """
    on a sheet of paper,
    the players each write a 4-digit secret number.
    The digits must be all different. Then, in turn,
    the players try to guess their opponent's
    number who gives the number of matches.
    If the matching digits are in their right positions,
    they are "bulls",
    if in different positions, they are "cows""")


def continu():
    global chosen_colors, temp_chosen_colors, already_used, color_press, win, wins
    global pc_chosen_colors, last_colors, last_grades, recorder, turn, black, names
    name2 = enter_name()
    names.append(name2)
    if win:
        wins.append("Win")
    else:
        wins.append("lost")
    turns.append(turn)
    print(names)
    to_file()
    chosen_colors = []
    temp_chosen_colors = []
    already_used = []
    color_press = 0
    pc_chosen_colors = []
    last_colors = []
    last_grades = []
    recorder = []
    turn = 0
    black = 0
    win = False
    board_creator()


def enter_name():
    prompt = askstring("name", "Input name")
    return prompt


def top_10():
    def creator():
        top_10_page = tk.Tk()
        top_10_page.geometry("325x550")
        canvas1 = Canvas(top_10_page, width=300, height=550)
        canvas1.create_line(0, 50, 400, 50, fill="black", width=2)
        for i in range(13):
            canvas1.create_line(0, i * 50 + 100, 400, i * 50 + 100, fill="black", width=2)
            lbl = Label(top_10_page, text=i)
            if 0 < i < 11:
                lbl = Label(top_10_page, text=i)
            if i == 0:
                lbl = Label(top_10_page, text="turn")
            lbl.place(x=25, y=i * 50 + 25)
            counter = 0
            for j in names:
                counter += 1
                lbl = Label(top_10_page, text=j)
                lbl.place(x=100, y=counter * 50 + 25)

            counter = 0
            for j in wins:
                counter += 1
                lbl = Label(top_10_page, text=j)
                lbl.place(x=200, y=counter * 50 + 25)

            counter = 0
            for j in turns:
                counter += 1
                lbl = Label(top_10_page, text=j)
                lbl.place(x=270, y=counter * 50 + 25)

        for i in range(5):
            canvas1.create_line(i * 80, 0, i * 80, 600, fill="black", width=2)

        lbl = Label(top_10_page, text="name")
        lbl.place(x=100, y=25)
        lbl = Label(top_10_page, text="state")
        lbl.place(x=200, y=25)
        lbl = Label(top_10_page, text="turns")
        lbl.place(x=265, y=25)

        canvas1.pack()

    creator()


def to_file():
    file = open('text.txt', 'a')
    for i in range(len(names)):
        file.write(str(names[i]))
        file.write("\n")
        file.write(str(wins[i]))
        file.write("\n")
        file.write(str(turns[i]))
        file.write("\n")


board_creator()
root.mainloop()
