# # винятки у функціях
#
# def get_name():
#     name = input('Введіть ім\'я: ')
#
#     # перевірка порожнього імені
#     if name == '':
#         # викликає виняток з повідомлення про проблему
#         raise Exception("ім'я не може бути порожнім")
#
#     # ім'я не з літер
#     if not name.isalpha():
#         raise Exception("ім'я має складатися лише з літер")
#
#     print(name[0]) # перша літера імені
#
#     return name
#
#
# try:
#     user = get_name()
#     print(user)
# except Exception as error:
#     print(f'Помилка: {error}')
#
# ##2###
#
# # Напишіть функцію, яка приймає список і елемент,
# # який слід видалити зі списку. Обробіть можливий виняток,
# # коли такого елементу немає у списку.
#
#
# def remove_item1(items, item):
#     if item not in items:
#         raise Exception(f"Елемента {item} немає в списку")
#
#     items.remove(item)
#
#
# def remove_item2(items, item):
#     try:
#         items.remove(item)
#     except Exception:
#         raise Exception(f"Елемента {item} немає в списку")
#
#
# nums = [1, 2, 6]
#
# try:
#     remove_item2(nums, -2)
#     print(nums)
# except Exception as error:
#     print(f"Помилка {error}")

# def get_user_pas():
#     try:
#         pas = input("Ведіть пароль ")
#     except ValueError:
#         raise ValueError("Некоректний пароль")
#
#     if len(pas) < 8:
#         raise ValueError("пароль не може бути менше 8 символів")
#
#     if len(pas)>len(set(pas)):
#         raise ValueError("пароль не може містить однакові символи ")
#     return pas
#
#
# try:
#     pas = get_user_pas()
#     print(pas)
# except ValueError as error:
#     print(error)
#users={}
# users={"user1":"password123","admin":"securePass!","john_doe":"qwerty2024"}
#
#
# def get_log_pas(users):
#
#     login = input("Введіть логін: ")
#     password = input("Введіть пароль: ")
#
#     if not login or not password:
#         raise ValueError("невірна кількість символів")
#
#     if not login in users:
#         raise ValueError("логіна немає в словнику")
#
#     if password != users[login]:
#         raise ValueError("невірний пароль")
#     print("Успішний вхід!")
#
# try:
#     get_log_pas(users)
#
# except ValueError as err:
#     print(f"Помилка: {err}")

# Створіть програму, яка дозволяє користувачеві ввести дані
# та записує їх у файл.
#
# filename = input('Введіть назву файла: ')
# data = input('Введіть текстові дані: ')
#
# with open(filename, 'w') as file:
#     # file.write(data)
#     print(data, file=file, end='') # без переходу на новий рядок
#
# # Напишіть програму, яка здійснює пошук та заміна слів у
# # текстовому файлі.
#
# filename = input('Введіть назву файла: ')
# old_word = input('Введіть старе слово: ')
# new_word = input('Введіть нове слово: ')
#
# with open(filename, 'r') as file:
#     data = file.read()
#
# new_data = data.replace(old_word, new_word)
#
# with open(filename, 'w') as file:
#     print(new_data, file=file, end='')


# #Користувач вводить літеру та назву файлу. Виведіть усі
# #слова з файлу, які починаються на цю літеру.
#
# liter = input("вводить літеру ").lower()
# file_name = input("вводить назву файлу ")
#
# with open(file_name, 'r', encoding="utf-8") as file:
#     text = file.read()
#
# text = text.replace("\n",' ')
# words = text.split(' ')
# print(words)
#
# for word in words:
#     if word.lower().startswith(liter):
#         print(word)
#



# filename = "dd"
# filename2 = "dd.txt"
# vowels = "aeuioAEUIO"
#
 #with open(filename, "r", encoding='utf-8') as file:
      #lines = file.
#      count = 0
#      count_symb = 0
#      count_digits=0
#      count_vowels=0
#
#      for line in lines:
#          count += 1
#          count_symb += len(line)
#          for char in line:
#             if char.isdigit():
#                 count_digits += 1
#             if char in vowels:
#                 count_vowels += 1
#
#
# with open(filename2, 'w', encoding='utf-8') as file:
#     print(f"Загальна кількість рядків - {count}. \n Загальна кількість символів в файлі {count_symb}", file=file)
#     file.write(f"Кількість цифр: {count_digits}\n")
#     file.write(f"Кількість голосних літер: {count_vowels}\n")

# word = input("вводить слово ").lower()
# file_name = input("вводить назву файлу ")
#
# with open(file_name, 'r', encoding="utf-8") as file:
#     words = file.read().lower()
#     print(f"Слово '{word}' зустрічається {words.count(word.lower())} раз(и) у файлі '{file_name}'.")
#
# #print(words)

#for word in words:

file_name = input("вводить назву файлу ")

with open(file_name, 'r', encoding="utf-8") as file:
    lines = file.readlines()
    #print(type(lines))
    # Видаляємо останній рядок
    lines = lines[:-1]

# Перезаписуємо файл без останнього рядка
with open(file_name, 'w', encoding='utf-8') as file:
    file.writelines(lines)