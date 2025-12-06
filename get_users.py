import requests
import os

data=requests.get("https://jsonplaceholder.typicode.com/users")

if data.status_code == 200:
    users = data.json()
    print(users[0])
else:
    print(f"Failed to retrieve data. Status code: {data.status_code}")