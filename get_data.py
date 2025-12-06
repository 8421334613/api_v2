# import requests
# import os

# url="https://jsonplaceholder.typicode.com/todos"
# df=requests.get(url)
# data = df.json()
# print(data)



import requests
import os

url="https://jsonplaceholder.typicode.com/todos"
df=requests.get(url)

if source := df.status_code == 200:
    data = df.json()
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {df.status_code}")