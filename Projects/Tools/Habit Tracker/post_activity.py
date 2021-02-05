from create_user import pixela_endpoint, USERNAME, graph_params, headers
import requests
from datetime import datetime


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}"
today = datetime.now().strftime("%Y%m%d")
qty = str(float(input("How many kilometers you accomplished today?")))
2
pixel_data = {
    "date": today,
    "quantity": qty
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)



