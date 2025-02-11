# class Dog

# опис класу, шаблон
# class Dog:
#     # конструктор для створення об'єктів класу
#     def __init__(self, name, age, weight):
#         # self -- обєкт класу(конкретний пес)
#         if age < 0:
#             raise ValueError("вік пса неможе бути від'ємні")
#
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     # можливість гавкати
#     # метод
#     def make_sound(self):
#         print("Гав")
#
#
#     def print_info(self):
#         # вивід інформації про песика
#         print(self.name, self.age, self.weight)


# конкретні песики
# dog1 = Dog()  # об'єкт клас Dog
#
# print(dog1.name)
# print(dog1.age)
# print(dog1.weight)
#
# dog2 = Dog()
#
# dog2.name = 'Lev' # зміна
#
# print(dog2.name)
# print(dog2.age)
# print(dog2.weight)
#
# # використання метода
# dog1.make_sound()


# dog1 = Dog(name='Lev', age=3, weight=7)
# print(dog1.name)
#
# dog2 = Dog(name='Carl', age=5, weight=10)
# print(dog2.name)
#
#
# dog1.print_info()  # self = dog1
# dog2.print_info()  # self = dog2


# Створіть список з 3-ма студентами, дані вводить
# користувач. Після чого для кожного студента виведіть
# інформацію про нього за допомогою метода

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Імя: {self.name}")
        print(f"Вік: {self.age}")
        print()


students = []
for _ in range(3):
    name = input("Імя: ")
    age = int(input("Вік: "))

    student = Student(name, age)
    students.append(student)

for student in students:
    student.print_info()






