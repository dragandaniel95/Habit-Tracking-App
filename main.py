import requests
from datetime import datetime

USERNAME = "daniel1409"
PASSWORD = "Cenaraw1"
GRAPH_ID = "graph1"

# Creare username pixela
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": PASSWORD,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)  # Printeaza raspunsul primit de la API

# Creare grafic pixela
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Steps Graph",
    "unit": "steps",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": PASSWORD
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Creare post pixela
today = datetime.now()
yesterday = datetime(year=2023, month=1, day=17)
yesterday_formatted = yesterday.strftime("%Y%m%d")
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
post_params = {
    "date": today,  # Functie cu care obtinem data in ce format dorim.
    # Daca schimbam data (ex:yesterday) putem face un post pentru ieri
    "quantity": input("How many steps did you do today?")
}
# response = requests.post(url=post_endpoint, json=post_params, headers=headers)
# print(response.text)

# Updatare postare pixela - PUT method
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday_formatted}"
update_params = {
    "quantity": "10000"
}
# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

# Delete postare pixela - DELETE method
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday_formatted}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)