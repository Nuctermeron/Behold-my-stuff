from tkinter import *

"""Funtions for updating and clearing input window and solving equations"""
def input_update(item):
    """Function takes another argument and adds it to the input window"""
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def input_clear():
    """Function makes empty string and replace text window"""
    global expression
    expression = ""
    input_text.set("")


def equality():
    """Function takes expression and using eval keyword it makes calculations and then cast it into string"""
    global expression
    result = str(eval(expression))
    input_text.set(result)


"""Screen setup"""
window = Tk()
window.geometry("312x324")
window.resizable(0, 0)
window.title("Simple Calculator")

expression = ""

input_text = StringVar()  # It allows creating instance of selected number, could be solved by *args but would require additional functions

"""Input window setup"""
input_window_frame = Frame(window, width=312, height=50, bd=10, highlightbackground="black", highlightcolor="black",
                           highlightthickness=2)
input_window_frame.pack(side=TOP)
input_field = Entry(input_window_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

"""Button frame setup"""
button_frame = Frame(window, width=312, height=272.5, bg="grey")
button_frame.pack()

"""First row"""
clear = Button(button_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: input_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(button_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: input_update("/")).grid(row=0, column=3, padx=1, pady=1)

"""Second row"""
seven = Button(button_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: input_update(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(button_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: input_update(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(button_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: input_update(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(button_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: input_update("*")).grid(row=1, column=3, padx=1, pady=1)

"""Third row"""
four = Button(button_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: input_update(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(button_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: input_update(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(button_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: input_update(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(button_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: input_update("-")).grid(row=2, column=3, padx=1, pady=1)

"""Fourth row"""
one = Button(button_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: input_update(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(button_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: input_update(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(button_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: input_update(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(button_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
              command=lambda: input_update("+")).grid(row=3, column=3, padx=1, pady=1)

"""Fifth row"""
zero = Button(button_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: input_update(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(button_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: input_update(".")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(button_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: equality()).grid(row=4, column=3, padx=1, pady=1)

window.mainloop()
