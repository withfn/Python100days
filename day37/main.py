import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "withfn"
TOKEN = "k1j2k3jslk21uwahuspsstw"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Time Reading",
    "unit": "Min",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.put(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "180",
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_endpoint = f"{pixel_endpoint}/{pixel_config['date']}"

update_pixel_config = {
    "quantity": "120"
}

# response = requests.put(url=update_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)