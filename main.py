

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

