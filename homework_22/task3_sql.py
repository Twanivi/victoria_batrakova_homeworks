# 3) Создайте новую Базу данных: Поля: id, 2 целочисленных поля, Целочисленные поля
# заполняются рандомно от 0 до 9. Выберите случайную запись из БД. Если каждое число данной записи
# чётное, то удалите эту запись, если нечётное, то обновите данные в ней на(2,2)

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

cursor.execute("""CREATE TABLE IF NOT EXISTS table_task3 (id INT AUTO_INCREMENT PRIMARY KEY, num1 INT(9), num2 INT(9));""")
cursor.execute("""SHOW TABLES""")
print(cursor.fetchall())

x = random.randint(0, 10)
y = random.randint(0, 10)

cursor.execute("""INSERT INTO table_task3 (num1, num2) VALUES (%s, %s);""", (x, y))
connection.commit()
cursor.execute("""SELECT * FROM table_task3;""")
print(cursor.fetchall())

cursor.execute("""SELECT * FROM table_task3 ORDER BY RAND() LIMIT 1;""")
random_result = cursor.fetchall()
print(random_result)
list_random = list(random_result[0])
id_list_random = []
id_list_random.append(list_random[0])
print(id_list_random)
if list_random[1] % 2 != 0 and list_random[2] % 2 != 0:
    cursor.execute("""UPDATE table_task3 SET num1=2, num2=2 WHERE id=%s;""", (id_list_random))
    connection.commit()
elif list_random[1] % 2 == 0 and list_random[2] % 2 == 0:
    cursor.execute("""DELETE FROM table_task3 WHERE id=%s;""", (id_list_random))
    connection.commit()
cursor.execute("""SELECT * FROM table_task3;""")
print(cursor.fetchall())


