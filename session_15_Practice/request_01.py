import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)
data = response.json()

# data={
#     "name":"sonam",
#     "username":"sonam123",
#     "email":"sonam@pw.live"
# }
# response=requests.post(BASE_URL,json=data)
# i want to register with given data in json format to this API

print(response.json())

print(data)