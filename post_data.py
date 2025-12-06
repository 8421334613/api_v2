import requests
import os

url="https://jsonplaceholder.typicode.com/users"

data={'id': 101,
     'name': 'Leanne Graham', 
     'username': 'Bret', 
     'email': 'Sincere@april.biz'
    }



data=requests.post(url, json=data)

if data.status_code == 201:
    print("Data posted successfully:", data.json())

else:
    print(f"Failed to post data. Status code: {data.status_code}")