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

import sqlalchemy as db

meta = db.MetaData()

table_task1_alchemy = db.Table(
    'Table_task1_alchemy', meta,
    db.Column('string1', db.String(150), nullable=False),
    db.Column('string2', db.String(150), nullable=False),
    db.Column('num1', db.Integer, nullable=False)
)
print(table_task1_alchemy.c)

engine = db.create_engine('mysql+mysqlconnector://root:stgvj754ErEt83@localhost:3306/task1_alchemy')
meta.create_all(engine)

connection = engine.connect()

i = int(input('Введите число: '))

add_query = table_task1_alchemy.insert().values(string1='text1', string2='text2', num1=i)
connection.execute(add_query)
connection.commit()
select_all_query = db.select(table_task1_alchemy)

for row in connection.execute(select_all_query).fetchall():
    row = str(row)
    row1 = row.replace('(', '')
    row2 = row1.replace(')', '')
    print(row2)

connection.close()
