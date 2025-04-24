from sqlalchemy import create_engine, MetaData, insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json

# завантажуємо логін та пароль
with open('config.json', 'r') as file:
    data = json.load(file)
    login = data['login']
    password = data['password']

# підключаємось до бд itstep
db_url = f"postgresql+pg8000://{login}:{password}@localhost:5432/itstep2"
engine = create_engine(db_url)

metadata = MetaData()
metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# вивести назви доступних таблиць
# for table_name in metadata.tables:
#     print(table_name)


# print(metadata.tables)

# Вставляти рядки в таблиці бази даних.
# ■ Оновлення рядків у таблицях бази даних. При спробі
# оновлення усіх рядків в одній таблиці надайте запит на
# підтвердження користувачеві. Оновлювати усі рядки
# можна лише після підтвердження користувачем.
# ■ Видалення рядків з таблиць баз даних. При спробі видалити
# усі рядки в одній таблиці потрібно видавати користувачу
# запит на підтвердження. Видаляти усі рядки, можна тільки
# після підтвердження користувачем.

def get_table():
    print('Виберіть таблицю з бази')

    for table_name in metadata.tables:
        print(f'\t{table_name}')

    user_table_name = input('Ваша відповідь: ')

    return user_table_name

def insert_row():
    table_name = get_table()

    # отримуємо саму таблицю по її назві
    table = metadata.tables[table_name]

    # список з даними рядка
    values = []

    # список з назвами стовпців
    column_names = []

    for column in table.columns:
        # пропускаємо стовпчик id
        if column.name == 'id':
            continue

        value = input(f'{column.name} = ')

        values.append(value)
        column_names.append(column.name)

    # назви стовпців без лапок
    new_column_names = tuple(column_names)
    new_column_names = str(new_column_names)
    new_column_names = new_column_names.replace('\'', '')

    # запит по добавлянню рядка

    query = f"""
    INSERT INTO {table_name}
    {new_column_names}
    VALUES {tuple(values)}
    """

    # print(query)

    # виконати запит та обробити помилки
    try:
        query = text(query)
        session.execute(query)
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")


def insert_row2():
    # теж саме але без запиту
    table_name = get_table()

    # отримуємо саму таблицю по її назві
    table = metadata.tables[table_name]

    # словник: ключ - назва стовпця, значення - те що ввів користувач
    values = {}


    for column in table.columns:
        # пропускаємо стовпчик id
        if column.name == 'id':
            continue

        value = input(f'{column.name} = ')

        values[column.name] = value

    # добавляємо рядок
    query = insert(table).values(values)

    try:
        session.execute(query)
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

# Вивести прізвища та зарплати (сума ставки та надбавки)
# лікарів, які не перебувають у відпустці;

def doctors_notvac():

    # запит
    query = f"""
    SELECT DOCTORS.SURNAME,  (DOCTORS.SALARY+DOCTORS.premium) as ZP
FROM DOCTORS
JOIN Vacations on Vacations.doctorid = doctors.id 
WHERE now() NOT BETWEEN Vacations.startdate and Vacations.enddate
    """

    # виконати запит та обробити помилки
    try:
        query = text(query) #- закоментується для другого варіанту (делете)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    for row in rows:
        print(row)


# ▷ Вивести назви палат, які знаходяться у певному відділенні;

def wards_depart():

    show_depart()

    depart_name = input("відділенні ")
    # запит
    query = f"""
   SELECT WARDS.NAME 
FROM WARDS
JOIN Departments on Departments.id = WARDS.Departmentid
WHERE Departments.NAME = '{depart_name}'
    """

    # виконати запит та обробити помилки
    try:
        query = text(query) #- закоментується для другого варіанту (делете)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    for row in rows:
        print(row)

def show_depart():

    # запит
    query = f"""
   SELECT Departments.NAME 
FROM Departments 
    """

    # виконати запит та обробити помилки
    try:
        query = text(query) #- закоментується для другого варіанту (делете)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    for row in rows:
        print(row)

while True:
    print("1 - вставити рядок в таблицю")
    print("2 - Вивести прізвища та зарплати лікарів, які не перебувають у відпустці")
    print("3 - Вивести назви палат, які знаходяться у певному відділенні")

    command = input('Введіть номер команди: ')

    if command == '1':
        insert_row2()
    elif command == '2':
        doctors_notvac()
    elif command == '3':
        wards_depart()
    else:
        print('невірна команда')