from tkinter import *
import converters

def converter():
    miles = float(input_window.get())
    km = miles * 1.609
    output_window.config(text=f"{km} km")

window = Tk()
window.title("Converter")
window.config(padx=20,pady=20)

input_window = Entry(width=5)
input_window.grid(column=1 , row=0)

input_label = Label(text="Miles")
input_label.grid(column=2 , row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0 , row=1)

output_window = Label(text="0")
output_window.grid(column=1 , row=1)

output_label = Label(text="Km")
output_label.grid(column=2 , row=1)

calculate_button = Button(text="Calculate", command=converter)
calculate_button.grid(column=1 , row=2)




window.mainloop()





