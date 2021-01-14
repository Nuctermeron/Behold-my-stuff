from tkinter import *

COLOR = "#B1DDC6"

class Flashcards(Tk):
    def __init__(self):
        super().__init__()

        """Skeleton of app"""
        self.title("Flashcards")
        self.configure(background=COLOR, padx=50, pady=50)
        self.grid()

        """Images"""
        self.front_image = PhotoImage(file="./images/card_front.png")
        self.back_image = PhotoImage(file="./images/card_back.png")
        self.right_answer_image = PhotoImage(file="./images/right.png")
        self.wrong_answer_image = PhotoImage(file="./images/wrong.png")

        """Placing elements"""
        """Front"""
        self.front = Canvas(width=800, height=526)
        self.front.create_image(400, 263, image=self.front_image)
        self.front.create_text(400, 150, text="Title", font= ("Ariel", 40, "italic"))
        self.front.create_text(400, 263, text="Word", font= ("Ariel", 60, "bold"))
        self.front.config(bg=COLOR, highlightthickness=0)
        self.front.grid(row=0, column=0, columnspan=2)

        """Wrong"""
        self.wrong_answer = Button(image= self.wrong_answer_image, highlightthickness=0)
        self.wrong_answer.grid(row=1, column=0)

        """Right"""
        self.right_answer = Button(image= self.right_answer_image, highlightthickness=0)
        self.right_answer.grid(row=1, column=1)

