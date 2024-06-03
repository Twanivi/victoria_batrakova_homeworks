# 1) Установить Postman и попробовать отправить запросы для получения ответа через него

import requests
from fake_useragent import UserAgent

user = UserAgent().random

url = 'https://reqres.in/api/users?page=2'

# GET
#
response = requests.get(url)
# print(response.json())

# POST
data = {
    "id": "735",
    "createdAt": "2024-06-02T18:09:15.634Z"
}

response_post = requests.post(url,  json=data)
print(response_post.json())
print(response.json())
