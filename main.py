
class Passenger():
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination #місце, куди прямує

class Transport():
    def __init__(self, speed):
        self.speed = speed

    def move(self, destination, distance):
        time = distance / self.speed
        print(f"Transport is moving to {destination}. It will take {time:.2f} hours.")

class Bus(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed)

        self.passengers = []
        self.capacity = capacity # максимальна можлива кількість пасажирів

    def board_passenger(self, passenger):

        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Пасажир {passenger.name} доданий в автобус.")
        else:
            print("Автобус переповнений! Неможливо додати більше пасажирів.")

    def move(self, destination, distance):
        departing_passengers = [p for p in self.passengers if p.destination == destination]
        self.passengers = [p for p in self.passengers if p.destination != destination]
        print(f"Висаджено {len(departing_passengers)} пасажирів у {destination}.")
        super().move(destination, distance)

    def list_passengers(self):
        print("Пасажири в автобусі:")
        for p in self.passengers:
            print(f"{p.name} -> {p.destination}")

    # Приклад використання

bus = Bus(speed=60, capacity=3)  # Створення автобуса зі швидкістю 60 км/год і місткістю 3 пасажири
p1 = Passenger("Олександр", "Київ")
p2 = Passenger("Марія", "Львів")
p3 = Passenger("Іван", "Київ")
p4 = Passenger("Анна", "Одеса")

bus.board_passenger(p1)  # Додаємо пасажирів
bus.board_passenger(p2)
bus.board_passenger(p3)
bus.board_passenger(p4)  # Цей пасажир не поміститься

bus.list_passengers()  # Виводимо список пасажирів
bus.move("Київ", 500)  # Автобус рухається до Києва, висаджує відповідних пасажирів
bus.list_passengers()  # Оновлений список пасажирів