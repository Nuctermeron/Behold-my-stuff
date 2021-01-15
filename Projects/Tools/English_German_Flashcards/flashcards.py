from tkinter import *
import pandas
import random

COLOR = "#B1DDC6"
card = {}
try:
    DATA = pandas.read_csv("To_Learn.csv")
except FileNotFoundError:
    DATA = pandas.read_csv("English-German dictionary.csv")
    to_learn = DATA.to_dict(orient="records")
else:
    to_learn = DATA.to_dict(orient="records")

class Flashcards(Tk):
    def __init__(self):
        super().__init__()

        """Methods"""

        def next_card():
            global card, flip
            self.after_cancel(flip)
            card = random.choice(to_learn)
            self.flashcard.itemconfig(card_title, text="English", fill="black")
            self.flashcard.itemconfig(card_word, text=card["English"], fill="black")
            self.flashcard.itemconfig(card_image, image=self.front_image)
            flip = self.after(3000,func=flip_card)

        def flip_card():
            global card, flip
            self.flashcard.itemconfig(card_title, text="German", fill="white")
            self.flashcard.itemconfig(card_word, text=card["German"], fill="white")
            self.flashcard.itemconfig(card_image, image=self.back_image)

        def next_card_known():
            global card
            to_learn.remove(card)
            pandas.DataFrame(to_learn)
            data = pandas.DataFrame(to_learn)
            data.to_csv("To_Learn.csv")
            next_card()


        """Skeleton of app"""
        self.title("Flashcards")
        self.configure(background=COLOR, padx=50, pady=50)
        global flip
        flip = self.after(3000, func=flip_card)
        self.grid()

        """Images"""
        self.front_image = PhotoImage(file="./images/card_front.png")
        self.back_image = PhotoImage(file="./images/card_back.png")
        self.right_answer_image = PhotoImage(file="./images/right.png")
        self.wrong_answer_image = PhotoImage(file="./images/wrong.png")

        """Placing elements"""
        """Card"""
        self.flashcard = Canvas(width=800, height=526)
        card_image = self.flashcard.create_image(400, 263, image=self.front_image)
        card_title = self.flashcard.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
        card_word = self.flashcard.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
        self.flashcard.config(bg=COLOR, highlightthickness=0)
        self.flashcard.grid(row=0, column=0, columnspan=2)

        """Wrong"""
        self.wrong_answer = Button(image=self.wrong_answer_image, highlightthickness=0, command=next_card)
        self.wrong_answer.grid(row=1, column=0)

        """Right"""
        self.right_answer = Button(image=self.right_answer_image, highlightthickness=0, command=next_card_known)
        self.right_answer.grid(row=1, column=1)

        next_card()
