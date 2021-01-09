from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
repeat_count = 0
timer = None

"""Functions"""
"""Countdown"""


def countdown(time):
    minutes = math.floor(time / 60)
    seconds = time % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if time > 0:
        global timer
        timer = window.after(1000, countdown, time - 1)
    else:
        start_timer()
        marks = ""
        for n in range(math.floor(repeat_count / 2)):
            marks += "✓"
        check_mark.config(text=marks)


def start_timer():
    global repeat_count
    repeat_count += 1

    if repeat_count % 8 == 0:
        countdown(20 * 60)
        label.config(text="Break", fg=RED)
    elif repeat_count % 2 == 0:
        countdown(5 * 60)
        label.config(text="Break", fg=YELLOW)
    else:
        countdown(25 * 60)
        label.config(text="Break", fg=PINK)


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Pomodoro timer")
    check_mark.config(text="")


"""Window setup"""
window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=GREEN)
label = Label(text="Pomodorro Timer", fg=RED, bg=GREEN, font=(FONT_NAME, 35, "bold"))
label.grid(column=1, row=0)

"""Canvas setup"""
canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.gif")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

"""GUI"""
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(bg=GREEN, fg=RED)
check_mark.grid(column=1, row=3)

window.mainloop()
