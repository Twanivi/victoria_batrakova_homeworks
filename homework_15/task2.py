# 2) Создайте функцию, которая принимает на вход список словарей и сохраняет его в CSV файл.
# Каждый словарь представляет собой строку данных, а ключи словарей - названия столбцов.
import csv

lines = [
    {'name': 'Alexander Melnikov', 'age': 38, 'sex': 'm'},
    {'name': 'Mihail Tolstoy', 'age': 28, 'sex': 'm'},
    {'name': 'Elena Ivanova', 'age': 22, 'sex': 'w'},
]

def lines_csv(lines):
    with open('table_task2.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(lines[0].keys())
        for i in lines:
            writer.writerow(i.values())

lines_csv(lines)
