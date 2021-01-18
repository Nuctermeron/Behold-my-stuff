from tkinter import *
import requests


class Application:

    def __init__(self, master):
        self.master = master
        master.title("ISS Tracker")
        master.config(padx=100, pady=50, bg="black")
        self.label = Label(text="ISS Tracker", fg="white", bg="black", font=("Fixedsys", 35, "bold"))
        self.label.grid(column=0, row=0, columnspan=2)

        self.canvas = Canvas(width=300, height=300, bg="black", highlightthickness=0)
        ISS_image = PhotoImage(file="ISS_emblem_300x300.png")
        self.canvas.create_image(150, 150, image=ISS_image)
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.longitude = Label(text="Longitute:", bg="black", fg="white", justify=LEFT)
        self.longitude.grid(column=0, row=2)
        self.longitude_entry = Entry(width=20)
        self.longitude_entry.grid(column=0, row=3, sticky="e")
        self.longitude_entry.focus()

        self.latitude = Label(text="Latitue:", bg="black", fg="white", justify=LEFT)
        self.latitude.grid(column=1, row=2)
        self.latitude_entry = Entry(width=20)
        self.latitude_entry.grid(column=1, row=3, sticky="e")

        self.get_location_button = Button(text="Get Location", width=20, highlightthickness=0,
                                          command=self.iss_location)
        self.get_location_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)
        mainloop()

    def iss_location(self):
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        data = response.json()
        longitude_value = data["iss_position"]["longitude"]
        latitude_value = data["iss_position"]["latitude"]
        self.latitude_entry.delete(0, END)
        self.longitude_entry.delete(0, END)
        self.latitude_entry.insert(0, longitude_value)
        self.longitude_entry.insert(0, latitude_value)
