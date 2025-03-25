"""
Використовуючи бінарні дерева, організуйте роботу
автопарку, де зберігаються автомобілі, відсортовані за
маркою
Клас Car
Атрибути:
 brand – модель автомобіля
 model – марка автомобіля
 year – рік випуску
Клас CarPark
Атрибути:
 cars – дерево з автомобілями
Методи:
 add(car) – добавити автомобіль
 remove(model) – видалити автомобіль
 search(model) – пошук автомобіля за маркою, якщо є
то повертає книгу інакше None
 __len__() – кількість автомобілів
 sell_car(client, model) – продати автомобіль клієнту,
якщо така марка присутня
"""
import bintrees
from bintrees import AVLTree

class Car:
    def __init__(self, brand , model, year):
        self.brand = brand
        self.model = model
        self.year = year

# Атрибути:
#  brand – модель автомобіля
#  model – марка автомобіля
#  year – рік випуску

class CarPark:
    def __init__(self):
        self.cars = bintrees.AVLTree()    # cars – дерево з     автомобілями

    def add(self, car):
        self.cars.insert(key=car.model, value=car)

    def remove(self, model):
        if model in self.cars:
            self.cars.remove(model)
        else:
            print(f'автомобіля "{model}" немає!')

    def search(self, model):   #пошук автомобіля за маркою

        if model in self.cars:
            return self.cars[model]
        else:
            return None

    def __len__(self): #кількість автомобілів
        return len(self.cars)

    def sell_car(self, client, model): #продати автомобіль клієнту,
#якщо така марка присутня
        car = self.search(model)
        if not car:
            print(f'автомобіля "{model}" немає!')
            return
        self.remove(model)

        print(f'Клієнт {client} купив автомобіль  {model}')

    def display_info(self, model):
        car = self.search(model)
        print(f'''
модель автомобіля - {car.brand}
марка автомобіля - {car.model}
рік випуску - {car.year}
''')

park_cars = CarPark()
cars = [
    Car("x032", "BMW", 2003),
    Car("nn889", "Audi", 2022),
    Car("nn8890", "Cherry", 2021),
]

for car in cars:
    park_cars.add(car)

print(f"📚 кількість автомобілів {len(park_cars)} автопарку ")
park_cars.display_info("Audi")
park_cars.sell_car("Anna","Audi")
#park_cars.display_info("Audi")

print(f"📚 кількість автомобілів {len(park_cars)} автопарку ")