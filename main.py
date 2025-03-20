import json


data = [1, 2, 3, 4]

# JSON
# збереження у файл
# filename = 'data.json'
# with open(filename, 'w') as file:
#     json.dump(data, file)
#
#
# # завантаження з файла
# with open(filename, 'r') as file:
#     new_data = json.load(file)
#
#
# print(new_data)

#Pickle
import pickle


data = [1, 2, 3, 4]

# encoded = pickle.dumps(data)
# print(encoded)

# збереження у файл
# w -- відкрити для запису
# b -- відкрити як двійковий файл(файл з байтами)

# with open('data.pkl', 'wb') as file:
#    pickle.dump(data, file)
#     #file.write('data')

#
# # завантаження з файла
# with open('data.pkl', 'rb') as file:
#     new_data = pickle.load(file)
#
# print(new_data)

# dump -- робота з файлом
# dumps -- робота без файла


# класи

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"{self.name}, {self.age} років")

    def __repr__(self):
        return f"{self.name}, {self.age} років"


# person1 = Person('Mary', 27)
# person2 = Person("John", 34)
# person3 = Person('Jack', 42)
#
# persons = [person1, person2, person3]
#
# with open('data.pkl', 'wb') as file:
#     pickle.dump(persons, file)
#
#
# with open("data.pkl", 'rb') as file:
#     data = pickle.load(file)
#
#
# print(data)
# jack = data[2]
#
#jack.print_info()



# gzip
import gzip


# data = [1, 2, 3, 4]
#
# with gzip.open('data.zip', 'wb') as file:
#     # кодуємо дані у байти
#     encoded_data = pickle.dumps(data)
#
#     # зберігаємо закодовані дані у файл
#     file.write(encoded_data)
#
#
# with gzip.open('data.zip', 'rb') as file:
#     # читаємо закодовані дані
#     encoded_data = file.read()
#
#     # розшифровуємо дані
#     new_data = pickle.loads(encoded_data)
#
#
# print(encoded_data)
# print(new_data)

# Напишіть програму для заповнення списку товарів.
# Назви товарів вводить користувач. Реалізуйте функціонал:
#  додати новий товар
#  вивести список товарів
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle

# import json
# import pickle
#
# def add_item(items):
#     item = input('Введіть назву товару: ')
#     items.append(item)
#
#
# def print_items(items):
#     print('Товари: ')
#     for item in items:
#         print('   ', item)
#
#
# def save_json(items, filename='items.json'):
#     with open(filename, 'w') as file:
#         json.dump(items, file)
#
#
# def save_pickle(items, filename='items.pkl'):
#     with open(filename, 'wb') as file:
#         pickle.dump(items, file)
#
#
# def load_json(filename='items.json'):
#     try:
#         with open(filename, 'r') as file:
#             return json.load(file)
#     except Exception:
#         print('Невдалось завантажити')
#         return []
#
#
#
# def load_pickle(filename='items.pkl'):
#      try:
#         with open(filename, 'rb') as file:
#             return pickle.load(file)
#      except Exception:
#         print('Невдалось завантажити')
#         return []
#
#
#
# def main():
#     items = []
#     while True:
#         print('''Виберіть:
#             1. Додати товар.
#             2. Вивести список товарів
#             3. Зберегти Json
#             4. Зберегти Pickle
#             5. Завантажити Json
#             6. Завантажити Pickle''')
#
#         user_choice = input('Введіть команду: ')
#
#         if user_choice == '1':
#             add_item(items)
#
#         elif user_choice == '2':
#             print_items(items)
#
#         elif user_choice == '3':
#             save_json(items)
#
#         elif user_choice == '4':
#             save_pickle(items)
#
#         elif user_choice == '5':
#             items = load_json()
#
#         elif user_choice == '6':
#             items = load_pickle()
#
#         else:
#             break
#
#
# if __name__ == '__main__':
#     main()



##############3
# Напишіть клас Student
# Атрибути:
#  name – ім’я
#  specialization – спеціалізація
#  grades – список оцінок
# Методи:
#  add_grade(grade) – додати нову оцінку
#  show_info() – вивести ім’я, спеціалізацію та середню
# оцінку

# Створіть список з трьох студентів. Збережіть цей список
# використовуючи pickle та json.
# Завантажте дані за допомогою pickle та json

import json
import pickle


class Student:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def show_info(self):
        print()
        print()
        print(self.name)
        print(self.specialization)
        av_grade = sum(self.grades)/len(self.grades)
        print(av_grade)

student1 = Student("Jonh","Art")
student2 = Student("Anna","Art")
student3 = Student("Mary","Music")
students = [student1, student2, student3]

students[0].add_grade(5)
students[1].add_grade(8)
students[2].add_grade(11)
students[2].add_grade(9)

#Збережіть цей список
# використовуючи pickle та json.

with open("students.pcl", "wb") as file:
    pickle.dump(students, file)

with open("students.pcl", "rb") as file:
    new_students = pickle.load(file)

new_students[2].show_info()
