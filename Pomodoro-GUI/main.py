from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Work Timer")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
title_label.grid(column=1, row=0)

canvs = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvs.create_image(100, 112, image=tomato)
canvs.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 36, 'bold'))
canvs.grid(row=1, column=1)

start = Button(text='Start',highlightthickness=0, command=None)
start.grid(column=0, row=2)
reset = Button(text='Reset', highlightthickness=0,command=None)
reset.grid(column=2, row=2)

check_marks = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
check_marks.grid(column=1, row=3)













window.mainloop()