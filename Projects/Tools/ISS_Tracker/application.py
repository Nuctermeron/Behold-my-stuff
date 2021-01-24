from tkinter import *
from tkinter import messagebox
import requests
from datetime import datetime

"""Change only these parameters"""
MY_LAT = 50.264893  # example latitude
MY_LONG = 19.023781  # example longitude
"""----------------------------"""

MY_PARAMETERS = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
LONGITUDE_VALUE = 0.0
LATITUDE_VALUE = 0.0


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

        self.iss_passing = Button(text="Is ISS near my location?", width=20, highlightthickness=0,
                                  command=self.is_iss_flying_over)
        self.iss_passing.grid(column=0, row=5, columnspan=2, padx=10, pady=10)
        mainloop()

        self.passing_by = ""
        self.visibility = ""
        self.passing = False

    def iss_location(self):
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        data = response.json()
        global LONGITUDE_VALUE, LATITUDE_VALUE
        LONGITUDE_VALUE = float(data["iss_position"]["longitude"])
        LATITUDE_VALUE = float(data["iss_position"]["latitude"])
        self.latitude_entry.delete(0, END)
        self.longitude_entry.delete(0, END)
        self.latitude_entry.insert(0, LONGITUDE_VALUE)
        self.longitude_entry.insert(0, LATITUDE_VALUE)

    def is_iss_flying_over(self):
        response = requests.get(url="http://api.sunrise-sunset.org/json", params=MY_PARAMETERS)
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        self.iss_location()
        time_now = datetime.now().hour
        self.visibility = ""

        if MY_LAT - 5 <= LATITUDE_VALUE <= MY_LAT + 5 and MY_LONG - 5 <= LONGITUDE_VALUE <= MY_LONG + 5:
            self.passing_by = "ISS is passing by."
            self.passing = True
        else:
            self.passing_by = "ISS is not passing by."
            self.passing = False

        if self.passing == True:
            if time_now >= sunset or time_now <= sunrise:
                self.visibility = "If not cloudy, station should be visible."
            else:
                None

        return messagebox.showinfo(title= "Info", message= f"{self.passing_by} {self.visibility}")
