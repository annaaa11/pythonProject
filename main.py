

# 1. Створіть клас Cart(кошик клієнта магазину) з атрибутами
#client(ім’я клієнта) та items(список товарів).
#Додайте метод який додає новий товар до кошика
#Додайте метод який видаляє товар з кошика
#Додайте метод для виведення інформації про кошик

class Cart:
    def __init__(self, client):
        self.client = client
        self.items = []

    def add_item(self):
        self.items.append(input("новий товар: "))

    def clear(self):
        self.items.clear()


    def print_items(self):
        print(f"список товарів: {self.items} клієнта магазину {self.client}")


cart1 = Cart(client = input("ім’я клієнта: "))

cart1.add_item()
cart1.add_item()

cart1.print_items()
cart1.clear()
cart1.print_items()

# 2.Створіть клас Phone з атрибутами number та battery_level.
#Додайте метод який зменшує заряд телефона(на скільки
#зменшити відсотків передається як параметр), якщо він
#опуститься нижче 20%, вивести повідомлення
#Додайте метод для виведення інформації про телефон.

class Phone():
    def __init__(self, number, battery_level):
        self.number = number
        self.battery_level = battery_level


    def low_balance(self, procent):
        self.battery_level -= procent
        if self.battery_level < 20:
            print("заряд телефона опуститься нижче 20%")

    def print_info(self):
        print(f"заряд телефона {self.number}  складає {self.battery_level} %")


phone1 = Phone("098889900", 100)
phone1.low_balance(82)
phone1.print_info()

# Завдання 1
# Створіть клас Проект з атрибутами:
#  назва
#  виділений кошторис
#  загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні
# задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі
# та список під-задач
#  виконати задачу, передається назва, час та ціна
# виконання
#  поповнення кошторису


class Project:
    def __init__(self, name, budget, tasks):
        self.name = name
        self.budget = budget
        self.tasks = tasks

        self.expenses = 0
        self.is_finished = False
        self.spent_time = 0  # місяці

    def display_info(self):
        print(f"Проєкт {self.name}")
        print(f'Час виконання {self.spent_time} місяців')
        print(f'Витрачено {self.expenses}/{self.budget}$')
        print(f'Залишилось {self.budget - self.expenses}$')

        if self.is_finished: # якщо проект завершений
            print("Стан проекту: завершений")
        else:
            print("Стан проекту: незавершений")

            print('Задачі що залишились:')
            for task in self.tasks:
                print(f'   - {task}')


project = Project(name='Ігрушка',
                  budget=10_000,
                  tasks=['Знайти інвесторів',
                         'Придумати загальну ідею'])

project.display_info()

# Завдання 2
# Створіть клас Телефон з атрибутами:
#  максимальний обсяг пам’яті
# Практичне завдання
#  зайнята пам’ять
#  чи включений(за замовчуванням False)
#  встановлені додатки у вигляді словника, де ключ –
# назва додатку, значення – обсяг пам’яті
# Додайте методи:
#  вивести інформацію про використання пам’яті
#  видалити додаток
#  встановити новий додаток, якщо пам’яті достатньо
#  оновити додаток(нова версія може займати іншу
# кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон
# вкючений
#  включити телефон
#  виключити телефон

class Phone:
    def __init__(self, max_memory, apps):
        self.max_memory = max_memory
        self.is_on = False
        self.apps = apps

        self.used_memory = 0 # рахуємо память
        for app_name in self.apps:
            self.used_memory += self.apps[app_name]

    def display_info(self):
        print(f'використана память {self.used_memory}/{self.max_memory}ГБ')
        print(f'встановлені додатки')
        for app_name in self.apps:
            print(f'встановлений додаток {app_name} -{self.apps [app_name]} ГБ')
        print()
        print()

    def delete_app(self, app_name):
        if app_name not in self.apps:
            print('немає такого додатку')
            return

        app_memory = self.apps.pop(app_name)
        self.used_memory -= app_memory

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

phone = Phone(128,
              {'Google': 30,
              'Ytube': 20,
               'Telegram':5})

phone.display_info()

phone.delete_app('Ytube')

phone.display_info()