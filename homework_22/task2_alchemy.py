# 2) Создайте новую Базу данных. Поля: id, 2 целочисленных поля.
# Целочисленные поля заполняются рандомно от 0 до 9.
# Посчитайте среднее арифметическое всех элементов без учёта id.
# Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД

import random
import sqlalchemy as db

meta = db.MetaData()

task2_alchemy = db.Table(
    'Task2_alchemy', meta,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('num1', db.Integer, nullable=False),
    db.Column('num2', db.Integer, nullable=False)
)
print(task2_alchemy.c)

engine = db.create_engine('mysql+mysqlconnector://root:stgvj754ErEt83@localhost:3306/task2_alchemy')
meta.create_all(engine)

connection = engine.connect()

x = random.randint(0, 10)
y = random.randint(0, 10)

add_query = task2_alchemy.insert().values(num1=x, num2=y)
connection.execute(add_query)
connection.commit()
select_all_query = db.select(task2_alchemy)
list_of_query = connection.execute(select_all_query).fetchall()
print(list_of_query)
count_of_list = len(list_of_query)
print(f'количество записей: {count_of_list}')

list_of_sum = []
sum_of_elements = 0
all_sum = 0
for i in list_of_query:
    sum_of_elements = i[1] + i[2]
    print(f'сумма каждого кортежа = {sum_of_elements}')
    list_of_sum.append(sum_of_elements)
for j in list_of_sum:
    all_sum += j
print(f'общая сумма = {all_sum}')

average = round(all_sum / count_of_list)
print(f'Среднее арифметическое = {average}')
if average > count_of_list:
    forth_element = list_of_query[3]
    forth_element_id = forth_element[0]
    delete_forth_elem = task2_alchemy.delete().where(task2_alchemy.c.id.in_([forth_element_id]))
    result = connection.execute(delete_forth_elem)
    connection.commit()
    select_all_query = db.select(task2_alchemy)
print(connection.execute(select_all_query).fetchall())

connection.close()
