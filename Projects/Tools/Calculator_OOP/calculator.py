from tkinter import *


class Calculator:
    def __init__(self, parent, x, y):
        """Calculator skeleton"""
        self.parent = parent
        self.container = Frame(self.parent)
        self.container.grid(row=x, column=y)

        """Attributes for buttons"""
        self.button_font = ('Verdana', 15)
        self.entry_font = ('Verdana', 20)
        self.button_width = 4
        self.button_height = 1

        """String inside input window"""
        self.string = ""

        """Calculator elements"""
        """Input window"""
        self.entry(0, 0)

        """Upper row"""
        self.button('7', 1, 0)
        self.button('8', 1, 1)
        self.button('9', 1, 2)

        """Middle row"""
        self.button('4', 2, 0)
        self.button('5', 2, 1)
        self.button('6', 2, 2)

        """Lower row"""
        self.button('1', 3, 0)
        self.button('2', 3, 1)
        self.button('3', 3, 2)

        """0"""
        self.button('0', 4, 0)

        """Function buttons"""
        self.button('+', 1, 3)
        self.button('-', 1, 4)
        self.button('*', 2, 3)
        self.button('/', 2, 4)
        self.button('(', 3, 3)
        self.button(')', 3, 4)
        self.evauluate('=', 4, 1)
        self.remove('<x', 4, 4)
        self.clear("C", 4, 3)

    def button(self, char_, x, y):  # button configuration
        self.b = Button(self.container,
                        text=char_, width=self.button_width, height=self.button_height, font=self.entry_font,
                        command=lambda: self.button_click(char_))
        self.b.grid(row=x, column=y)

    def entry(self, x_, y_):
        self.entry = Text(
            self.container, font=self.entry_font, state=DISABLED,
            height=self.button_height//2, width=self.button_width*5)
        self.entry.grid(row=x_, column=y_, columnspan=5, sticky='we')

    def evauluate(self, char_, x, y):  # evauluating expression
        self.b = Button(self.container,
                        text=char_, width=self.button_width, height=self.button_height, font=self.entry_font,
                        command=self.evaluate_click)
        self.b.grid(row=x, column=y, columnspan=2, sticky='we')

    def remove(self, char_, x, y):  # remove character
        self.b = Button(self.container,
                        text=char_, width=self.button_width, height=self.button_height, font=self.entry_font,
                        command=self.remove_click)
        self.b.grid(row=x, column=y)

    def clear(self, char_, x, y):  # clear window
        self.b = Button(self.container,
                        text=char_, width=self.button_width, height=self.button_height, font=self.entry_font,
                        command=self.clear_click)
        self.b.grid(row=x, column=y)

    def display(self, text):  # displaying characters
        self.entry.config(state=NORMAL)
        self.entry.delete('1.0', END)
        self.entry.insert('1.0', text)
        self.entry.config(state=DISABLED)

    def button_click(self, text):
        self.string = '' + self.string + text
        self.display(self.string)

    def evaluate_click(self):
        self.display(eval(self.string))
        self.string = ''

    def remove_click(self):
        self.string = '' + self.string[0:-1]
        self.display(self.string)

    def clear_click(self):
        self.display('')
        self.string = ''
