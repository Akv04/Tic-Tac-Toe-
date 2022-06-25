import tkinter as tk
from tkinter import ttk
import time
from sys import argv,exit

def press(i):
    global turn, root
    cur = "X" if turn else "O"
    board[i//3][i%3] = cur
    print(cur)
    button_texts[i].set(cur)
    turn = not turn
    check = checkGameWon()
    if not check=="-":
        if check=="X":
            status_text.set("You Won!")
        elif check=="O":
            status_text.set("You Lost!")
        elif check=="D":
            status_text.set("Draw!")
        disable()
    
    elif not turn:
        playComputerTurn()

def checkGameWon():
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and not board[i][0]=="":
            return board[i][0]
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i] and not board[0][i]=="":
            return board[0][i]
    if board[0][0]==board[1][1]==board[2][2] and not board[0][0]=="":
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0] and not board[0][2]=="":
        return board[0][2]

    for i in range(9):
        if not board[i//3][i%3]:
            return "-"
    return "D"

def playComputerTurn():
    maxi = -20
    toPlay = 0
    score = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                board[i][j] = 'O'
                score[i][j] = minimax(False, 1)
                board[i][j] = ""
                if score[i][j]>maxi:
                    maxi = score[i][j]
                    toPlay = i*3 + j
    press(toPlay)
    
def minimax(chance, level):
    check = checkGameWon()
    if check=="X":
        return -1.0/level
    elif check=="O":
        return 1.0/level
    elif check=="D":
        return 0

    if chance:
        maxi = -20
        score = [[0 for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                if not board[i][j]:
                    board[i][j] = 'O'
                    score[i][j] = minimax(False, level+1)
                    board[i][j] = ""
                    if score[i][j]>maxi:
                        maxi = score[i][j]
        return maxi
    else:
        mini = 20
        score = [[0 for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                if not board[i][j]:
                    board[i][j] = 'X'
                    score[i][j] = minimax(True, level+1)
                    board[i][j] = ""
                    if score[i][j]<mini:
                        mini = score[i][j]
        return mini

def restart(i):
    global turn
    turn = not i
    status_text.set("")
    for i in range(9):
        buttons[i]["state"] = "enabled"
        button_texts[i].set("")
        board[i//3][i%3] = ""
    if not turn:
        playComputerTurn()

def disable():
    for button in buttons:
        button["state"] = "disabled"

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.grid(columnspan=3, rowspan=6)

status_text = tk.StringVar()
status_label = tk.Label(root, textvariable=status_text)
status_label.grid(column=1, row=4)

restart_button = ttk.Button(root, text="Restart as 1st Player", command=lambda: restart(0))
restart_button.grid(column=0, row=5)
restart_button_2 = ttk.Button(root, text="Restart as 2nd Player", command=lambda: restart(1))
restart_button_2.grid(column=1, row=5)
quit_button = ttk.Button(root, text="Quit", command=lambda: exit())
quit_button.grid(column=2, row=5)

board = [["" for i in range(3)] for j in range(3)]
turn = True

button_texts = []
buttons = []

button_text_0 = tk.StringVar()
button_0 = ttk.Button(root, textvariable=button_text_0, command=lambda: press(0))
button_0.grid(column=0, row=0, ipady=30, ipadx=20)
button_texts.append(button_text_0)
buttons.append(button_0)

button_text_1 = tk.StringVar()
button_1 = ttk.Button(root, textvariable=button_text_1, command=lambda: press(1))
button_1.grid(column=1, row=0, ipady=30, ipadx=20)
button_texts.append(button_text_1)
buttons.append(button_1)

button_text_2 = tk.StringVar()
button_2 = ttk.Button(root, textvariable=button_text_2, command=lambda: press(2))
button_2.grid(column=2, row=0, ipady=30, ipadx=20)
button_texts.append(button_text_2)
buttons.append(button_2)

button_text_3 = tk.StringVar()
button_3 = ttk.Button(root, textvariable=button_text_3, command=lambda: press(3))
button_3.grid(column=0, row=1, ipady=30, ipadx=20)
button_texts.append(button_text_3)
buttons.append(button_3)

button_text_4 = tk.StringVar()
button_4 = ttk.Button(root, textvariable=button_text_4, command=lambda: press(4))
button_4.grid(column=1, row=1, ipady=30, ipadx=20)
button_texts.append(button_text_4)
buttons.append(button_4)

button_text_5 = tk.StringVar()
button_5 = ttk.Button(root, textvariable=button_text_5, command=lambda: press(5))
button_5.grid(column=2, row=1, ipady=30, ipadx=20)
button_texts.append(button_text_5)
buttons.append(button_5)

button_text_6 = tk.StringVar()
button_6 = ttk.Button(root, textvariable=button_text_6, command=lambda: press(6))
button_6.grid(column=0, row=2, ipady=30, ipadx=20)
button_texts.append(button_text_6)
buttons.append(button_6)

button_text_7 = tk.StringVar()
button_7 = ttk.Button(root, textvariable=button_text_7, command=lambda: press(7))
button_7.grid(column=1, row=2, ipady=30, ipadx=20)
button_texts.append(button_text_7)
buttons.append(button_7)

button_text_8 = tk.StringVar()
button_8 = ttk.Button(root, textvariable=button_text_8, command=lambda: press(8))
button_8.grid(column=2, row=2, ipady=30, ipadx=20)
button_texts.append(button_text_8)
buttons.append(button_8)

root.mainloop()