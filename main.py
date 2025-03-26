
"""
Програма складається з трьох потоків. Перший
просить в користувача вводити числа, поки не введено
порожній рядок, та зберігає числа в список.
Інші два потоки чекають поки перший завершить
роботу, і вже потім запускаються. 

Один рахує суму чисел в
списку, інший рахує середнє арифметичне.
Список чисел, сума та середнє виводяться на екран

"""
import threading

numbers = []


def sum_numbers(numbers):
    print(f"Сума чисел: {sum(numbers)}")


def avg_numbers(numbers):
    if len(numbers) == 0:
        print("Середнє арифметичне неможливо обчислити (список пустий).")
        return
    avg = sum(numbers) / len(numbers)
    print(f"Середнє арифметичне: {avg}")


def read_numbers():
    while True:
        input_number = input("number: ")
        if input_number == "":
            break  # Завершаем ввод чисел
        try:
            numbers.append(int(input_number))
        except ValueError:
            print("Помилка: введіть ціле число.")

    print(f"Список чисел: {numbers}")


# Создаем и запускаем поток для ввода чисел
read_thread = threading.Thread(target=read_numbers)
read_thread.start()
read_thread.join()  # Дожидаемся завершения потока

# Создаем потоки для вычислений
sum_thread = threading.Thread(target=sum_numbers, args=(numbers,))
avg_thread = threading.Thread(target=avg_numbers, args=(numbers,))

sum_thread.start()
avg_thread.start()

sum_thread.join()
avg_thread.join()