# . Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.

#
# start = int(input("Введіть перше ціле число: "))
# end = int(input("Введіть друге ціле число: "))
#
# min_val = min(start, end)
# max_val = max(start, end)
# range_sum = 0
#
# # Обчислюємо суму чисел у діапазоні, включаючи обидва числа
# for i in range(min_val, max_val + 1):
#     range_sum += i
#
# print(f"Сума чисел від {min_val} до {max_val} дорівнює: {range_sum}")


# 2. Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.

#
# sum = 0
#
# # Перебираємо числа від 1 до 100 включно
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum += i

# print("Сума всіх парних чисел від 1 до 100 дорівнює:", sum)

# 3. Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.

# str = input("Введіть рядок: ")
#
# # Виводимо кожну літеру на окремому рядку
# for char in str:
#     print(char)

# 4. Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.

import random

# Початковий список з 10 випадкових цілих чисел від 1 до 100
# original_list = [random.randint(1, 100) for _ in range(10)]
#
# new_list = []
#
# for num in original_list:
#     if num % 2 == 0:
#         new_list.append(num)
#
#
# print("Початковий список:", original_list)
# print("Список парних чисел:", new_list)

# 5. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.

# def big_lit(strings):
#     # Створюємо новий список лише з тих рядків, які починаються з великої літери
#     big_lit_list = []
#     for s in strings:
#         if s[0].isupper():
#             big_lit_list.append(s)
#     return big_lit_list
#
# # Ввід рядків від користувача через кому
# user_input = input("Введіть кілька рядків через кому: ")
# input_list = []
#
# # Розділяємо введений рядок за комами та додаємо до списку, обрізаючи пробіли
# for s in user_input.split(","):
#     input_list.append(s.strip())
#
# result = big_lit(input_list)
# print("Рядки, що починаються з великої літери:", result)


# 6. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".

# def Python_lit(strings):
#     # Створюємо новий список, що містить лише
#     # # рядки, які містять слово "Python".
#
#     Python_lit_list = []
#     for s in strings:
#         if "Python" in s:
#             Python_lit_list.append(s)
#     return Python_lit_list

# Ввід рядків від користувача через кому
# user_input = input("Введіть кілька рядків через кому: ")
# input_list = []

# Розділяємо введений рядок за комами та додаємо до списку, обрізаючи пробіли
# for s in user_input.split(","):
#     input_list.append(s.strip())
#
# result = Python_lit(input_list)
# print("рядки, які містять слово Python: ", result)

# (додаткове на кристалики)Напишіть програму, яка
# створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти
# та шукати слова у цьому словнику

# def add_word(dictionary):
#     # Додаємо слово та визначення до словника
#     word = input("Введіть слово: ")
#     definition = input("Введіть визначення: ")
#     dictionary[word] = definition
#
#
# def delete_word(dictionary):
#     # Видаляємо слово зі словника
#     word = input("Введіть слово для видалення: ")
#     if word in dictionary:
#         del dictionary[word]
#         print(f"Слово '{word}' видалено зі словника.")
#     else:
#         print(f"Слово '{word}' не знайдено в словнику.")
#
# def search_word(dictionary):
#     # Шукаємо слово в словнику
#     word = input("Введіть слово для пошуку: ")
#     if word in dictionary:
#         print(f"Визначення слова '{word}': {dictionary[word]}")
#     else:
#         print(f"Слово '{word}' не знайдено в словнику.")
#
#
# def main():
#     # порожній словник
#     dictionary = {}
#
#     # Меню
#     while True:
#         print("\nМеню:")
#         print("1. Додати слово та визначення")
#         print("2. Видалити слово")
#         print("3. Шукати слово")
#         print("5. Вийти")
#
#         choice = input("Виберіть (1-4): ")
#
#         if choice == '1':
#             add_word(dictionary)
#         elif choice == '2':
#             delete_word(dictionary)
#         elif choice == '3':
#             search_word(dictionary)
#         elif choice == '4':
#             print("Пока!")
#             break
#         else:
#             print("Невірний вибір, спробуйте ще раз.")
#
# # Запуск програми
# main()

# Використовуючи лямбдафункцію, напишіть вираз, який сортує список кортежів
# за другим елементом кожного кортежу (наприклад, [(1,
# 3), (3, 2), (2, 1)])

# Список кортежів
# tuples = [(1, 8), (3, 9), (2, 1), (2.2, 2.22)]
# sorted_t = sorted(tuples, key=lambda x: x[1])
# print(sorted_t)

######################3

### cимулятор роботи сайту
'''
Симулятор роботи сайту
WebSite: Основний клас, який представляє вебсайт.
Атрибути: назва сайту, URL, список сторінок.
Методи: додавання/видалення сторінок, відображення
інформації про сайт.
WebPage: Клас, який представляє окрему сторінку на сайті.
Атрибути: заголовок сторінки, вміст, дата публікації.
Методи: відображення деталей сторінки.
Реалізація функціональності:
Дозвольте користувачеві створювати новий сайт з
певною назвою та URL. Додайте можливість створювати нові
сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
функцію для видалення сторінок з сайту. Включіть функцію
для відображення всієї інформації про сайт, включаючи
список усіх сторінок.
Розробіть простий текстовий інтерфейс для взаємодії з
користувачем. Користувач повинен мати змогу вибирати дії,
такі як створення сайту, додавання/видалення сторінок,
перегляд інформації про сайт.
'''

from datetime import datetime

# Клас, який представляє окрему сторінку на сайті.
class WebPage:
    def __init__(self, title, content): # Атрибути:
        self.title = title  # Заголовок сторінки
        self.content = content  # Вміст
        self.date_published = datetime.now()  # Дата публікації сторінки

    def display_details(self):  # Виведення деталей сторінки

        print(f"Заголовок: {self.title}")
        print(f"Вміст: {self.content}")
        print(f"Дата публікації: {self.date_published}")

    def edit_content(self, new_content): # *Редагування вмісту сторінки

        self.content = new_content
        self.date_published = datetime.now()  # date Редагування
        print(f"Сторінка {self.title} відредагована")

# Клас, який представляє вебсайт
class WebSite:
    def __init__(self, name, url): # Атрибути:
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, title, content):# Додавання нової сторінки на сайт
        page = WebPage(title, content)
        self.pages.append(page)
        print(f"Сторінка {title} додана!")

    def remove_page(self, title): # Видалення сторінки за заголовком

        page_to_remove = None
        for page in self.pages:
            if page.title == title:
                page_to_remove = page
                break
        if page_to_remove:
            self.pages.remove(page_to_remove)
            print(f"Сторінка {title} видалена!")
        else:
            print(f"Сторінка {title} не знайдена")

    def display_info(self):

        print(f"\nІнформація про сайт:")
        print(f"Назва сайту: {self.name}")
        print(f"URL: {self.url}")
        print(f"Кількість сторінок: {len(self.pages)}")

        if self.pages:
            print("\nСписок сторінок:")
            for page in self.pages:
                page.display_details()

    def search_pages(self, keyword): # *Пошук сторінок за ключовим словом у заголовку чи вмісті

        found_pages = []
        for page in self.pages:
            if keyword.lower() in page.title.lower() or keyword.lower() in page.content.lower():
                found_pages.append(page)

        if found_pages:
            print(f"\nСторінки за словом {keyword} у заголовку чи вмісті :")
            for page in found_pages:
                page.display_details()
        else:
            print(f"Не знайдено сторінок з словом {keyword}")


# Клас для користувачів- логіну/реєстрації для керування  сайтом
class User:
    def __init__(self):
        self.users = {}  # Словник користувачів: {username: password}

    def reg_user(self, username, password):
        # Реєстрація нового користувача
        if username in self.users:
            print(f"Користувач {username} вже існує.")
        else:
            self.users[username] = password
            print(f"Користувач {username} зареєстрован!")

    def login_user(self, username, password):
        # Логін користувача
        if username in self.users and self.users[username] == password:
            print(f"Користувач {username} увійшов!")
            return True
        else:
            print("Невірне ім'я користувача або пароль.")
            return False

def main_menu():
    website = None
    user_site = User()
    try:

        while True:

            print("\nМеню:")
            print("1. Створити сайт")
            print("2. Додати сторінку")
            print("3. Видалити сторінку")
            print("4. Переглянути інформацію про сайт")
            print("5. Вийти")

            print("6. Зареєструватися")
            print("7. Увійти")
            print("8. Пошук сторінок")



            choice = input("Виберіть (1-8): ")

            if choice == '1':
                if website:
                    print("Сайт вже створено.")
                else:
                # Створення нового сайту
                    name = input("Введіть назву сайту: ")
                    url = input("Введіть URL сайту: ")
                    website = WebSite(name, url)
                    print(f"Сайт {name} з URL {url} створен!")

            elif choice == '2':
                if website:
                    # Додавання нової сторінки на сайт
                    title = input("Введіть заголовок сторінки: ")
                    content = input("Введіть вміст сторінки: ")
                    website.add_page(title, content)
                else:
                    print("нема сайту")

            elif choice == '3':
                if website:
                    # Видалення сторінки з сайту
                    title = input("Введіть заголовок сторінки, яку видалити: ")
                    website.remove_page(title)
                else:
                    print("Нема сторінки.")

            elif choice == '4':
                if website:
                    # Перегляд інформації про сайт
                    website.display_info()
                else:
                    print("Треба створіть сайт.")

            elif choice == '5':
                print("Пока!")
                break

            elif choice == '6':
                # Реєстрація користувача
                username = input("Введіть ім'я користувача: ")
                password = input("Введіть пароль: ")
                user_site.reg_user(username, password)

            elif choice == '7':
                # Логін користувача
                username = input("Введіть ім'я користувача: ")
                password = input("Введіть пароль: ")
                if user_site.login_user(username, password):
                    print("Тепер ви можете керувати сайтом.")

            elif choice == '8':  # *Пошук сторінок
                if website:
                    key_word = input("Введіть слово для пошуку: ")
                    website.search_pages(key_word)
                else:
                    print("Треба створіть сайт")

            else:
                print("Невірний вибір, спробуйте ще раз.")


    except Exception as e:
            print(f"Виникла помилка: {e}")

main_menu()


