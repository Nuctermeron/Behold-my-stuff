from tkinter import *


class Application:

    def __init__(self, master):
        self.master = master
        master.title("D'Hondt Calculator")
        master.config(padx=10, pady=10, bg="green")
        self.label = Label(text="D'Hondt seats Calculator for Sejm", fg="white", bg="green",
                           font=("Courier", 20, "bold"), anchor= "w")
        self.label.grid(column=0, row=0, columnspan=4)

        """Column labels"""
        labels = ["Party name","Percentage","Seats"]
        column_no = 1
        for label in labels:
            l = Label(text=f"{label}", fg="white", bg="green", font=("Courier", 10, "bold"))
            l.grid(column=column_no,row=1)
            column_no += 1


        """Number labels"""
        for i in range(2, 12):
            label = Label(text=f"{i-1}. ", fg="white", bg="green", font=("Courier", 10, "bold"))
            label.grid(column=0, row=i)

        self.entry_party = []
        for i in range(2, 12):
            entry = Entry(justify="left", width=15)
            entry.grid(column=1, row=i)
            self.entry_party.append(entry)

        self.entry_score = []
        for i in range(2, 12):
            entry = Entry(justify="left", width=15)
            entry.grid(column=2, row=i)
            self.entry_score.append(entry)

        self.entry_seats = []
        for i in range(2, 12):
            entry = Entry(justify="left", width=15)
            entry.grid(column=3, row=i)
            self.entry_seats.append(entry)

        self.calculate_button = Button( text="Calculate seats", width = 20, command= self.calculate_seats)
        self.calculate_button.grid(padx=10, pady=10,column=1,row = 12, columnspan=3)

    def calculate_seats(self):
        for entry in self.entry_party:
            entry.get()
            print(entry)

