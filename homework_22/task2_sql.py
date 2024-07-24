# 2) Создайте новую Базу данных. Поля: id, 2 целочисленных поля.
# Целочисленные поля заполняются рандомно от 0 до 9.
# Посчитайте среднее арифметическое всех элементов без учёта id.
# Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД

import random
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

cursor.execute("""CREATE TABLE IF NOT EXISTS table_task2 (id INT AUTO_INCREMENT PRIMARY KEY, num1 INT(9), num2 INT(9));""")
cursor.execute("""SHOW TABLES""")
print(cursor.fetchall())

x = random.randint(0, 10)
y = random.randint(0, 10)

cursor.execute("""INSERT INTO table_task2 (num1, num2) VALUES (%s, %s);""", (x, y))
connection.commit()
cursor.execute("""SELECT * FROM table_task2;""")
random_list = cursor.fetchall()
print(random_list)

cursor.execute("""SELECT COUNT(*) FROM table_task2;""")
result_count = cursor.fetchall()
count_num = list(result_count[0])
print(f'количество записей: {count_num[0]}')


cursor.execute("""SELECT AVG(num1), AVG(num2) FROM table_task2;""")
result = cursor.fetchall()
for avg_num1, avg_num2 in result:
    avg_all = (avg_num1 + avg_num2) / 2
    print(f'среднее арифметическое всех элементов: {round(avg_all)}')

if avg_all > count_num[0]:
    cursor.execute("""SELECT id FROM table_task2;""")
    list_id = cursor.fetchall()
    forth_item = list_id[3]
    cursor.execute("""DELETE FROM table_task2 WHERE id=%s;""", (forth_item))
    connection.commit()
cursor.execute("""SELECT * FROM table_task2;""")
print(cursor.fetchall())

