import requests

"""Use it only once when you create profile"""

USERNAME = "nuctermeron"  # Write your user name
TOKEN = "fasfafwafawfaw"  # Create your own token
GRAPH_COLORS = {
    "green": "shibafu",
    "red": "momiji",
    "blue": "sora",
    "yellow": "ichou",
    "purple": "ajisai",
    "black": "kura"
}
COLOR_CHOICE = "green"  # Pick your color: green, red, blue, yellow, purple, black

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_params = {
    "id": "graph1",
    "name": "activity graph",
    "unit": "km",
    "type": "float",
    "color": GRAPH_COLORS[COLOR_CHOICE]
}
headers = {
    "X-USER-TOKEN": TOKEN
}

## POST
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

YOUR_PAGE = f"https://pixe.la/@{USERNAME}"
YOUR_GRAPH = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_params['id']}.html"
print(YOUR_PAGE)
print(YOUR_GRAPH)
