import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("35e67c5300a0eb6cf4c2854188903185") # Use yours API key
account_sid = "YOUR ACCOUNT SID" #get it from twilio
auth_token = os.environ.get("AUTH_TOKEN") #get it from twilio

#  export API_KEY "35e67c5300a0eb6cf4c2854188903185"


parameters = {
    "lat": 50.264893,
    "lon": 19.023781,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)
