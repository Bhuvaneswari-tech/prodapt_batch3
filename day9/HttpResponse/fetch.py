#GET - fetch a user

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

#Get - fetch a user
response = requests.get(f"{BASE_URL}/users/1")
print(response.status_code) #200
print(response.json())

#POST - Create a new user
new_post = {"title":"Hello", "body":" World","userId":50}
response = requests.post(f"{BASE_URL}/posts", json=new_post)
print(response.status_code) #201
print(response.json())

#PUT, PATCH - partial update
response = requests.patch(f"{BASE_URL}/posts/1",json={"title":"Updated!"})
print(response.status_code) #200
print(response.json())

#DELETE
response = requests.delete(f"{BASE_URL}/posts/1")
print(response.status_code)
print(response.json())
