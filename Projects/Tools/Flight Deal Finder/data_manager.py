import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d139c8f1f6ed0fe1784f116499fa7d6f/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """With use of Sheety, below code takes data from pricing sheet"""
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"] #prices is name of sheet, dict contains all rows from xlsx
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
