
# Напишіть "гру вгадати число": комп’ютер загадує число
# від 1 до 100. Користувач вводить свої відповіді на що
# отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг
# користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
#  почати нову гру – користувач вводить числа до
# правильної відповіді
#  вивести результат – кількість перемог та програшів
#  зберегти дані – зберегти кількості перемог та
# програшів у файл
#  завантажити дані – завантажити кількості перемог
# та програшів
# Реалізуйте все функціями

import json
import random

# Файл для збереження статистики
file_stat = "game_stats1.json"

def load_stats():
    try:
        with open(file_stat, "r") as file:
            return json.load(file)
    except Exception as ex:
        print(ex)
        return {"wins": 0, "losses": 0}


def save_stats(stats):
    with open(file_stat, "w") as file:
        json.dump(stats, file)


def play_game():

    number = random.randint(1, 100)
    attempts = 0
    stats = load_stats()

    while True:
        if attempts < 5 :

            guess = int(input("Вгадайте число від 1 до 100: "))
            if guess < 1 or guess > 100:
                print("Будь ласка, введіть коректне число! ")
                break

            attempts += 1

            if guess < number:
                print("Більше Вгадайте! ")
            elif guess > number:
                print("Менше Вгадайте!")
            else:
                print(f"Ви вгадали число {number} за {attempts} спроб!")

                stats["wins"] += 1
                save_stats(stats)
                break

        else:
            print(f"Комп'ютер переміг! число {number}")
            stats["losses"] += 1
            save_stats(stats)
            break


def show_stats():
    stats = load_stats()
    print(f"Перемог: {stats['wins']}, Програшів: {stats['losses']}")

def main():
    while True:
        print("""Можливі дії: 
                  1. Почати нову гру
                  2. Вивести статистику
                  3. Вийти.
                  """)

        choice = input("Оберіть дію: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            print("До побачення!")
            break
        else:
            print("Невідома опція, спробуйте ще раз.")

main()