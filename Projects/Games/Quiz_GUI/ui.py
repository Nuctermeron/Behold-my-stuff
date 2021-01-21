from tkinter import *
from quiz_brain import QuizBrain
from data import question_data

BG_COLOR = "#375362"
FONT_NAME = "Courier"


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        """Window"""
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=BG_COLOR)

        """Score label"""
        self.score_label = Label(text=f"Score: 0", fg="white", bg=BG_COLOR, font=(FONT_NAME, 15, "bold"))
        self.score_label.grid(column=1, row=0)

        """Card canvas"""
        self.card = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.card.create_text(150, 125, text="Placeholder", fill="black", font=(FONT_NAME, 15, "bold"),
                                              width=280)
        self.card.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        """Buttons"""
        self.true_answer = PhotoImage(file="./images/true.png")
        self.false_answer = PhotoImage(file="./images/false.png")

        """True"""
        self.true_button = Button(image=self.true_answer, highlightthickness=0, command=self.true_command)
        self.true_button.grid(row=2, column=0)

        """False"""
        self.false_button = Button(image=self.false_answer, highlightthickness=0, command=self.false_command)
        self.false_button.grid(row=2, column=1)

        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.card.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.card.itemconfig(self.question, text=q_text)
        else:
            self.card.itemconfig(self.question, text="You've reached end of a quiz!")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")

    def true_command(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_command(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.card.config(bg="green")
            self.window.after(1000, self.get_question)
        else:
            self.card.config(bg="red")
            self.window.after(1000, self.get_question)
