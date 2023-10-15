import json
import requests

URL = "http://127.0.0.1:8000/stucreate/"


data = {
    'name': 'Ishroop',
    'roll': 6,
    'city': 'Chandigarh',
}
headers = {
    'Content-Type': 'application/json',  # Set the Content-Type header to indicate JSON data.
}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data, headers=headers)

data = r.json()
print(data)