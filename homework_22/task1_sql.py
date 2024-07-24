# 1) первая задача из класса
# Создайте новую Базу данных.
# В ней создайте таблицу с тремя полями, два текстовых, одно - целое число.
# Число запрашивается с клавиатуры, а слова задаются статически.
# * Выведите каждую запись в отдельную строку
# пример
# [(hello, world, 2), (hello2, world2, 3)]
# Результат работы нашей программы
# hello, world, 2
# hello2, world2, 3

import mysql.connector as mysql

connection = mysql.connect(
    host='localhost',
    user='root',
    password='stgvj754ErEt83',
    database='test_db'
)
cursor = connection.cursor()
cursor.execute("""CREATE DATABASE IF NOT EXISTS test_db""")
cursor.execute("""SHOW DATABASES""")
print(cursor.fetchall())

cursor.execute("""CREATE TABLE IF NOT EXISTS table_task1 (id INT AUTO_INCREMENT PRIMARY KEY, string1 TEXT,
    string2 TEXT, num1 INT);"""
               )
cursor.execute("""SHOW TABLES""")
print(cursor.fetchall())


list_of_num = []
i = int(input('Введите число: '))
list_of_num.append(i)
cursor.execute("""INSERT INTO table_task1 (string1, string2, num1) VALUES ("text1", "text2", %s)""", (list_of_num))
connection.commit()
cursor.execute("""SELECT * FROM table_task1;""")

for row in cursor.fetchall():
    row = str(row)
    row1 = row.replace('(', '')
    row2 = row1.replace(')', '')
    print(row2)
