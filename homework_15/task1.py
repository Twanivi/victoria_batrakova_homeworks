#Файл "books.csv" содержит информацию о книгах в следующем формате:

# Название,Автор,Год издания,Жанр,Цена
# Мастер и Маргарита,Михаил Булгаков,1967,Фэнтези,500
# Преступление и наказание,Фёдор Достоевский,1866,Классика,400
# 1984,Джордж Оруэлл,1949,Научная фантастика,350
# Тень горы,Грегори Дэвид Робертс,2007,Триллер,600
#
# Реализовать функцию load_books(file_path), которая загружает данные из файла "books.csv"
# и возвращает список словарей, где каждый словарь представляет информацию о книге.
# Написать функцию total_price(books), которая принимает на вход список книг и
# возвращает общую стоимость всех книг.
# Создать функцию books_by_genre(books, genre), которая выводит на экран названия
# и авторов книг определенного жанра.
# Разработать скрипт, который загружает данные о книгах, вычисляет и выводит их
# общую стоимость, а также список книг определенного жанра, например, "Фэнтези".

import csv

with open('books.csv', 'w', newline='', encoding='cp1251') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Автор', 'Год издания', 'Жанр', 'Цена'])
    writer.writerow(['Мастер и Маргарита', 'Михаил Булгаков', 1967, 'Фэнтези', 500])
    writer.writerow(['Преступление и наказание', 'Фёдор Достоевский', 1866, 'Классика', 400])
    writer.writerow(['1984', 'Джордж Оруэлл', 1949, 'Научная фантастика', 350])
    writer.writerow(['Тень горы', 'Грегори Дэвид Робертс', 2007, 'Триллер', 600])


# Реализовать функцию load_books(file_path), которая загружает данные из файла "books.csv"
# и возвращает список словарей, где каждый словарь представляет информацию о книге.

def load_books(file_path):
    books = []
    with open(file_path, 'r', encoding='cp1251') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            books.append(row)
        # print(books)
    return books


load_books('books.csv')


# Написать функцию total_price(books), которая принимает на вход список книг и
# возвращает общую стоимость всех книг.

def total_price(books):
    # print(books)
    result = 0
    for i in books:
        for key, value in i.items():
            if key == 'Цена':
                result += int(value)
    # print(result)
    return result


total_price(load_books('books.csv'))

# Создать функцию books_by_genre(books, genre), которая выводит на экран названия
# и авторов книг определенного жанра.

def books_by_genre(books, genre):
    print(books)
    for i in books:
        if i['Жанр'] == genre:
            i['Жанр'] = genre
            print(f'По жанру {genre} найдена книга {i['Название']}, автор {i['Автор']}')


books_by_genre(load_books('books.csv'), 'Фэнтези')