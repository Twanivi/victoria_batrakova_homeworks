# 2) https://rapidapi.com/collection/list-of-free-apis - берёте любую api и пробуете обращаться к endpoint-ам для
# получения ответа, чем больше сделаете запросов, тем лучше

import requests

url = 'https://mashape-community-urban-dictionary.p.rapidapi.com/define'
headers = {
    'X-RapidAPI-Key': '9bff569308msh75be96ad4492c48p139ba2jsn1256011dbfc4',
    'X-RapidAPI-Host': 'mashape-community-urban-dictionary.p.rapidapi.com',

}
data = {
    'term': 'Привет'
}
response = requests.get(url, headers=headers,  params=data)
# print(response.json())
dictionary_info = response.json()
# print(dictionary_info.values())
dict_values = list(dictionary_info.values())
# print(dict_values[0])
first_elem = dict_values[0]
# print(first_elem[0])
dict_end = first_elem[0]
print(dict_end.keys())
print(dict_end.values())
print(dict_end['permalink'])
