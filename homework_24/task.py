# С сайта https://www.21vek.by/mobile/iphone_12_mini/ спарсить все названия смартфонов с их ценами, только те телефоны,
# которые можно добавить в корзину.
# записать в csv файл: 1 колонка - названия телефонов, 2 колонка - на сколько GB, 3 колонка - стоимость
# Обработать файл и выяснить какой телефон с наименьшей стоимостью(вывести имя-GB-стоимость)

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv

user = UserAgent().random
url = 'https://www.21vek.by/mobile/iphone_12_mini/'
headers = {
    'user-agent': user
}
response = requests.get(url, headers=headers)
with open('21vek.html', 'w', encoding='utf-8') as file:
    file.write(response.text)

soup = BeautifulSoup(response.text, 'lxml')
main_block = soup.find('div', {'data-testid': 'product-list'})
list_of_name = []
list_of_price = []
list_of_gb = []
new_list_of_gb = []

for i in main_block:
    button_block = i.find_all('button', {'data-testid': 'in-basket-button'})
    # print(button_block)
    for j in button_block:
        # print(i.text)
        if j.text == 'В корзину':
            name_phone = i.find_all('a', {'data-testid': 'card-info-a'})
            price_phone = i.find_all('p', {'data-testid': 'card-current-price'})
    # print(name_phone)
    # print(price_phone)
    for c in name_phone:
        # print(c.text)
        list_of_name.append(c.text)
    for n in price_phone:
        list_of_price.append(n.text)
        # print(n.text)

# print(list_of_name)
# print(list_of_price)

for i in list_of_name:
    # print(i)
    i = i.split()
    # print(i)
    list_of_gb.append(i[5])

# print(list_of_gb)
for i in list_of_gb:
    i = i.partition('B')[0] + i.partition('B')[1]
    new_list_of_gb.append(i)

# print(new_list_of_gb)

with open('21vek.csv', 'w', encoding='cp1251') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Название', 'GB', 'Цена'])
    writer.writerow(list_of_name)
    writer.writerow(list_of_gb)
    writer.writerow(list_of_price)