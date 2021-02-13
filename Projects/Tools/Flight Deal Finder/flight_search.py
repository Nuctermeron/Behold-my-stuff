import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "EzUXfPpqRsU2KyHYhZ0uc6-xz9CU2pF_"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term":city_name, "location_types":"city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query )
        data = response.json()
        code = data["locations"][0]["code"]
        return code
