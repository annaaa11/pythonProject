
from sqlalchemy import create_engine, MetaData, insert, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json

save_to_file = False

# завантажуємо логін та пароль
with open('config.json', 'r') as file:
    data = json.load(file)
    login = data['login']
    password = data['password']

# підключаємось до бд itstep
db_url = f"postgresql+pg8000://{login}:{password}@localhost:5432/Academy2"
engine = create_engine(db_url)

metadata = MetaData()
metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# вивести назви доступних таблиць
# for table_name in metadata.tables:
#     print(table_name)
# print(metadata.tables)
'''
Завдання
Для бази даних Академія, яку ви розробили в рамках
курсу «Теорія Баз Даних», створіть додаток для взаємодії
з базою даних, який дозволяє:
■ вставляти рядки в таблиці бази даних;
■ оновлювати рядків у таблицях бази даних;
■ видаляти рядки з таблиць бази даних;
передбачити можливість збереження звітів з результатів роботи на екран або у файл (встановлюється в
налаштуваннях додатку);
створювати звіти:
print("4 -  відобразити кафедру з максимальною кількістю груп")
    print("5 -  вивести назви кафедр і груп, які до них відносяться")
    print("6 -  вивести імена та прізвища викладачів, які читають лекції в конкретній групі")
    print("7 -  вивести інформацію про всіх викладачів")
    print("8 -  вивести    назви  предметів, які   викладає конкретний  викладач,")
'''

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


def update_row():
    # теж саме але без запиту
    table_name = get_table()

    # отримуємо саму таблицю по її назві
    table = metadata.tables[table_name]

    # показати таблицю
    show_table(table_name)

    id = int(input('Виберіть id рядка: '))

    print('Виберіть назву стовпчика')
    for column in table.columns:
        print(f"\t{column.name}")

    column_name = input('Ваша відповідь: ')
    value = input('Ведіть нове значення: ')

    # запит для зміни рядка
    query = f"""
    UPDATE {table_name}
    SET {column_name} = '{value}'
    WHERE id = {id}
    """

    # виконати запит та обробити помилки
    try:
        query = text(query)
        session.execute(query)
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")


def show_table(table_name):
    table = metadata.tables[table_name]

    query = f"""
    SELECT *
    FROM {table_name}
    """

    query = text(query)
    rows = session.execute(query)
    rows = rows.fetchall()

    # вивід назв стовпчиків
    for column in table.columns:
        print(column.name, end='\t\t')
    print()

    for row in rows:
        for value in row:
            print(value, end='\t\t')
        print()

def delete_row():
    # теж саме але без запиту
    table_name = get_table()

    # отримуємо саму таблицю по її назві
    table = metadata.tables[table_name]

    # показати таблицю
    show_table(table_name)

    id = int(input('Виберіть id рядка: '))

    # запит для видалення рядка
    query = f"""
    DELETE
    FROM {table_name}
    WHERE id = {id}
    """

    # query = delete(table).where(table.c.id == id) - другий варіант (через делете)

    # виконати запит та обробити помилки
    try:
        query = text(query) #- закоментується для другого варіанту (делете)
        session.execute(query)
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")


def Teacher_grup(): ## вивести імена та прізвища викладачів, які читають лекції в конкретній групі

    grup_name = input("Введіть групу ")
    # запит
    query = f""" SELECT T.NAME AS TeacherName, T.SURNAME AS TeacherSurname    
FROM GroupsLectures GL
	JOIN Groups G ON GL.GroupId = G.ID
	JOIN Lectures L ON GL.LectureId = L.ID
	JOIN Teachers T ON L.TeacherId = T.ID
WHERE G.NAME = '{grup_name}' """


    # виконати запит та обробити помилки
    try:
        query = text(query) #- закоментується для другого варіанту (делете)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    if save_to_file == 'y':
        try:
            with open("result.txt", "w", encoding="utf-8") as f:
                for row in rows:
                    f.write(f"{row}\n")
            print("Результат збережено у 'result.txt'")
        except Exception as err:
            print(f"Помилка при збереженні у файл: {err}")
    else:
        for row in rows:
            print(row)

def show_depart_grup(): ##вивести назви кафедр і груп, які до них відносяться

    # запит
    query = f"""
   SELECT DEPARTMENTS.NAME AS DEPARTMENT, G.NAME As Group   
FROM DEPARTMENTS 
JOIN Groups G ON G.DepartmentId = DEPARTMENTS.ID
    """

    # виконати запит та обробити помилки
    try:
        query = text(query) #- закоментується для другого варіанту (делете)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    if save_to_file=='y':
        try:
            with open("result.txt", "w", encoding="utf-8") as f:
                for row in rows:
                    f.write(f"{row}\n")
            print("Результат збережено у 'result.txt'")
        except Exception as err:
            print(f"Помилка при збереженні у файл: {err}")
    else:
        for row in rows:
            print(row)

def depart_maxgrup(): ##  відобразити кафедру з максимальною кількістю груп

    # запит
    query = f"""
   SELECT D.NAME AS DEPARTMENT, COUNT(G.ID) AS GroupCount
FROM DEPARTMENTS D
JOIN Groups G ON G.DepartmentId = D.ID
GROUP BY D.ID, D.NAME
HAVING COUNT(G.ID) = (
    SELECT MAX(GroupCount) 
    FROM (
        SELECT COUNT(G2.ID) AS GroupCount
        FROM Groups G2
        GROUP BY G2.DepartmentId
    ) AS Counts
)
    """

    # виконати запит та обробити помилки
    try:
        query = text(query) #- закоментується для другого варіанту (делете)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    if save_to_file=='y':
        try:
            with open("result.txt", "w", encoding="utf-8") as f:
                for row in rows:
                    f.write(f"{row}\n")
            print("Результат збережено у 'result.txt'")
        except Exception as err:
            print(f"Помилка при збереженні у файл: {err}")
    else:
        for row in rows:
            print(row)

def show_depart_grup(): ##вивести назви кафедр і груп, які до них відносяться

    # запит
    query = f"""
   SELECT DEPARTMENTS.NAME AS DEPARTMENT, G.NAME As Group   
FROM DEPARTMENTS 
JOIN Groups G ON G.DepartmentId = DEPARTMENTS.ID
    """

    # виконати запит та обробити помилки
    try:
        query = text(query) #- закоментується для другого варіанту (делете)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    if save_to_file=='y':
        try:
            with open("result.txt", "w", encoding="utf-8") as f:
                for row in rows:
                    f.write(f"{row}\n")
            print("Результат збережено у 'result.txt'")
        except Exception as err:
            print(f"Помилка при збереженні у файл: {err}")
    else:
        for row in rows:
            print(row)

def show_teachers(): ##вивести інформацію про всіх викладачів

    # запит
    query = f"""
   SELECT * 
FROM Teachers
    """

    # виконати запит та обробити помилки
    try:
        query = text(query) #- закоментується для другого варіанту (делете)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    if save_to_file=='y':
        try:
            with open("result.txt", "w", encoding="utf-8") as f:
                for row in rows:
                    f.write(f"{row}\n")
            print("Результат збережено у 'result.txt'")
        except Exception as err:
            print(f"Помилка при збереженні у файл: {err}")
    else:
        for row in rows:
            print(row)

def show_Subject_teachers(): ##вивести назви предметів, які викладає конкретний викладач,

    show_teachers()

    name = input("Введіть ім'я викладача ")
    surname = input("Введіть прізвище викладача ")

    # запит
    query = f"""SELECT S.NAME AS SubjectsName   
FROM GroupsLectures GL
	JOIN Groups G ON GL.GroupId = G.ID
	JOIN Lectures L ON GL.LectureId = L.ID
	JOIN Teachers T ON L.TeacherId = T.ID
	JOIN Subjects S ON L.SubjectId = S.ID
WHERE T.NAME = '{name}' AND T.SURNAME = '{surname}'
    """

    # виконати запит та обробити помилки
    try:
        query = text(query) #- закоментується для другого варіанту (делете)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    if save_to_file=='y':
        try:
            with open("result.txt", "w", encoding="utf-8") as f:
                for row in rows:
                    f.write(f"{row}\n")
            print("Результат збережено у 'result.txt'")
        except Exception as err:
            print(f"Помилка при збереженні у файл: {err}")
    else:
        for row in rows:
            print(row)


while True:
    print("1 - вставити рядок в таблицю")
    print("2 - змінити рядок в таблиці")
    print("3 - Видалити рядок в таблиці")
    print("4 -  відобразити кафедру з максимальною кількістю груп")
    print("5 -  вивести назви кафедр і груп, які до них відносяться")
    print("6 -  вивести імена та прізвища викладачів, які читають лекції в конкретній групі")
    print("7 -  вивести інформацію про всіх викладачів")
    print("8 -  вивести    назви  предметів, які   викладає конкретний  викладач,")

    print("0 - Вийти")

    save_to_file = input("Зберігати результати у файл 'result.txt'? (y/n): ").lower()

    command = input('Введіть номер команди: ')
    if command == '1':
        insert_row()
    elif command == '2':
        update_row()
    elif command == '3':
        delete_row()
    elif command == '4':
        depart_maxgrup()

    elif command == '5':
        show_depart_grup()

    elif command == '6':
        Teacher_grup()
    elif command == '7':
        show_teachers()

    elif command == '8':
        show_Subject_teachers()

    elif command == '0':
        break
    else:
        print('невірна команда')