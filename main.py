#
#
# # Створіть дочірні класи від Zone та перевизначте метод
# # serve_passenger() щоб він повертав пару: пасажир та True/False
# # в залежності від успішності перевірки.
# # Перевірки:
# #  реєстрація – наявність білету(у багажі)
# #  безпека – відсутність небезпечних предметів у багажі:
# # ніж, зброя, вибухівка
# #  посадка – перевірка не потрібна
# # Для цього скористайтесь класом Passenger
# # Атрибути:
# #  name – ім’я
# #  priority – пріоритет
# #  baggage – список з предметами в багажі
#

from queue import PriorityQueue

class Passenger:
    def __init__(self, name, priority, baggage):
        self.name = name
        self.priority = priority
        self.baggage = baggage  # список предметів у багажі


class Zone:
    def __init__(self, name):
        self.name = name
        self.passengers = PriorityQueue()

    def add_passenger(self, passenger):
        priority = passenger.priority
        pair = (priority, passenger)
        self.passengers.put(pair)

    def serve_passenger(self):
        #if not self.passengers.empty():
        priority, passenger = self.passengers.get()
        return passenger
        #return None


class RegistrationZone(Zone):
    def serve_passenger(self):
        #if not self.passengers.empty():
        priority, passenger = self.passengers.get()
            # Перевірка наявності квитка в багажі
        has_ticket = "ticket" in passenger.baggage
        return passenger, has_ticket
        #return None, False


class ControlZone(Zone):
    def serve_passenger(self):
        if not self.passengers.empty():
            priority, passenger = self.passengers.get()
            # Перевірка на небезпечні предмети
            dangerous_items = ["knife", "weapon", "explosive"]
            for item in passenger.baggage:
                if item in dangerous_items:
                    return passenger, False
            return passenger, True
        return None, False


class BoardingZone(Zone):
    def serve_passenger(self):
        if not self.passengers.empty():
            priority, passenger = self.passengers.get()
            # Для посадки перевірка не потрібна
            return passenger, True
        return None, False


class Airport:
    def __init__(self):
        self.zones = {
            "Registration": RegistrationZone("Реєстрація"),
            "Control": ControlZone("Контроль"),
            "Board": BoardingZone("Посадка")
        }
        self.passengers = []

    def add(self, passenger):
        self.zones["Registration"].add_passenger(passenger)

    def serve_registration(self):
        passenger, has_ticket = self.zones["Registration"].serve_passenger()
        if passenger and has_ticket:
            self.zones["Control"].add_passenger(passenger)

    def serve_security_control(self):
        passenger, passed_security = self.zones["Control"].serve_passenger()
        if passenger and passed_security:
            self.zones["Board"].add_passenger(passenger)

    def serve_boarding(self):
        passenger, ch = self.zones["Board"].serve_passenger()
        if passenger:
            self.passengers.append(passenger)

    def show_statistics(self):
        print(f"Кількість пасажирів, які пройшли всі зони: {len(self.passengers)}")
        print("Список пасажирів на борту:")
        for p in self.passengers:
            print(f"Пасажир {p.name}")


# Тестування
airport = Airport()
passengers = [
    Passenger("Олег", 3, ["ticket", "clothes"]),
    Passenger("Анна", 1, ["ticket", "knife"]),
    Passenger("Марія", 4, ["clothes"]),  # немає квитка
    Passenger("Сергій", 2, ["ticket", "book"])
]

for p in passengers:
    airport.add(p)
    airport.serve_registration()
    airport.serve_security_control()
    airport.serve_boarding()

airport.show_statistics()
