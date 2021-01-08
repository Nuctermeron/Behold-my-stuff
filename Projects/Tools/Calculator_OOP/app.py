from tkinter import *
from calculator import Calculator

class App:
    def __init__(self, master):
        self.master = master #Main GUI object e.g. root
        Calculator(self.master, 300, 350)
