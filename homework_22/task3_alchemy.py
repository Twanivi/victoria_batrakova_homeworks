# 3) Создайте новую Базу данных: Поля: id, 2 целочисленных поля, Целочисленные поля
# заполняются рандомно от 0 до 9. Выберите случайную запись из БД. Если каждое число данной записи
# чётное, то удалите эту запись, если нечётное, то обновите данные в ней на(2,2)

import random
from sqlalchemy import func
import sqlalchemy as db


meta = db.MetaData()

task3_alchemy = db.Table(
    'Task3_alchemy', meta,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('num1', db.Integer, nullable=False),
    db.Column('num2', db.Integer, nullable=False)
)
print(task3_alchemy.c)

engine = db.create_engine('mysql+mysqlconnector://root:stgvj754ErEt83@localhost:3306/task3_alchemy')
meta.create_all(engine)

connection = engine.connect()

x = random.randint(0, 10)
y = random.randint(0, 10)

add_query = task3_alchemy.insert().values(num1=x, num2=y)
connection.execute(add_query)
connection.commit()
select_all_query = db.select(task3_alchemy)
print(connection.execute(select_all_query).fetchall())

random_query = db.select(task3_alchemy).order_by(func.random()).limit(1)
random_result = connection.execute(random_query).fetchall()
print(random_result)
list_random = list(random_result[0])
id_list_random = []
id_list_random.append(list_random[0])
print(id_list_random)
if list_random[1] % 2 != 0 and list_random[2] % 2 != 0:
    change_query_with_id = task3_alchemy.update().values(num1=2, num2=2).where(task3_alchemy.c.id.in_(id_list_random))
    result = connection.execute(change_query_with_id)
    connection.commit()
elif list_random[1] % 2 == 0 and list_random[2] % 2 == 0:
    delete_query_with_id = task3_alchemy.delete().where(task3_alchemy.c.id.in_(id_list_random))
    result2 = connection.execute(delete_query_with_id)
    connection.commit()
select_all_query = db.select(task3_alchemy)
print(connection.execute(select_all_query).fetchall())

connection.close()
