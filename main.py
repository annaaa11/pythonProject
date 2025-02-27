

class Pet:
    def __init__(self, name, satiety=50, energy=50):
        self.name = name

        self.satiety = max(0, min(satiety, 100))  # Обмеження від 0 до 100
        self.energy = max(0, min(energy, 100))  # Обмеження від 0 до 100

    def sleep(self):
        self.energy = 100

    def eat(self, food_amont):
        self.satiety += food_amont

    def play(activity_level):
        pass

    def make_sound(self):
        pass

class Cat(Pet):

    def play(self, activity_level):     #якщо    satiety > 60, зменшує    energy     на
        if self.satiety > 60:
            self.satiety -= activity_level
            self.energy -= 2*activity_level
            print(f"рівень ситості= {self.satiety} рівень енергії= {self.energy} ")

    def make_sound(self):
        print("Мяу")

    def catch_mouse(self):
        if self.energy > 30:
            print("ловить мишу")
        if self.satiety > 40:
            print("грається з мишею")
        else:
            print("їсть")

# class Dog(Pet):
#     def play(self, activity_level):
#         if self.satiety >15:
#             self.satiety -= activity_level//2
#             self.energy -= activity_level//2
#         print(f"рівень ситості= {self.satiety} рівень енергії= {self.energy} ")
#
#     def make_sound(self):
#         print("Гав")
#
#     def fetch_ball(self):
#         print("ловить м’яча")
#         if self.satiety > 10:
#             self.energy -= 5
#
# dog1 = Dog("Bim")
# dog1.make_sound()
# dog1.play(20)
# dog1.fetch_ball()
#
# cat1 = Cat("mura")
# cat1.make_sound()
# cat1.eat(30)
# cat1.sleep()
# cat1.catch_mouse()
# cat1.play(30)
#
# Створіть абстрактний клас Robot з атрибутами:
#  name – назва робота або id
#  battery_level – рівень заряду(за замовчуванням 100%)
#  status – поточний стан (один з on, off, working)
# Методи:
#  info() – виводить інформацію
#  charge() – відновлює заряд до 100%
#  turn_on() – змінює стан на on
#  turn_off() – змінює стан на of

from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, name, battery_level=100, status="off"):
        self.name = name
        self.battery_level = battery_level
        self.status = status

    @abstractmethod
    def info(self):
        print(f"назва робота або id: {self.name}")
        print(f"рівень заряду: {self.battery_level}%")
        print(f"поточний стан: {self.status}")

    def charge(self):
        self.battery_level = 100

    def turn_on(self):
        self.status = "on"

    def turn_off(self):
        self.status = "off"

# robot1 = Robot("abs", 90)
# robot1.info()

# Створіть дочірній клас CleaningRobot
# Додаткові атрибути:
#  dust_capacity – ємність контейнеру для пилу(за
# замовчуванням 0%)
#  water_capacity – ємність контейнеру для води(за
# замовчуванням 100%)
#  cleaning_mode – тип прибирання(вологе або сухе)
# Методи:
#  info() – додатково виводить інформацію про робота

#  turn_on() – якщо контейнер для пилу повний або
# контейнер для води порожній то виводить повідомлення,
# інакше запускається turn_on() з класу Robot

#  empty_dustbin() – очищає контейнер для пилу
#  fill_water() – заповнює контейнер для води
#  swap_mode() – змінює тип прибирання на протилежний
#  clean(energy, dust, water=None) – чистить поверхню,
# якщо прибирання сухе, то просто перенести пил у
# контейнер(якщо місця не достатньо вивести помилку),
# якщо прибирання вологе то додатково витратити воду.
# Також зменшує рівень заряду на energy

class CleaningRobot(Robot):
    def __init__(self, name, battery_level=100, status="off", dust_capacity=0,
                 water_capacity=100, cleaning_mode="wet"):
        super().__init__(name, battery_level, status)
        self.dust_capacity = dust_capacity
        self.water_capacity = water_capacity
        self.cleaning_mode = cleaning_mode

    def info(self):
        super().info()
        print(f"ємність контейнеру для пилу: {self.dust_capacity}%")
        print(f"ємність контейнеру для води: {self.water_capacity}%")
        print(f"тип прибирання: {self.cleaning_mode}")

#  turn_on() – якщо контейнер для пилу повний або
# контейнер для води порожній то виводить повідомлення,
# інакше запускається turn_on() з класу Robot
    def turn_on(self):
        if self.dust_capacity == 100 or self.water_capacity == 0:
            print("контейнер для пилу повний або контейнер для води порожній")
        else:
            super().turn_on()

    def empty_dustbin(self):
        self.dust_capacity = 0

    def fill_water(self):
        self.water_capacity = 100

    def swap_mode(self):
        if self.cleaning_mode == 'wet':
            self.cleaning_mode = "dry"
        else:
            self.cleaning_mode = "wet"

#  clean(energy, dust, water=None) – чистить поверхню,
# якщо прибирання сухе, то просто перенести пил у
# контейнер(якщо місця не достатньо вивести помилку),
# якщо прибирання вологе то додатково витратити воду.
# Також зменшує рівень заряду на energy

    def clean(self, energy, dust, water=None):
        if self.status =="off":
            print("Robot is off!")
            return


        if self.battery_level < energy:
            print("Low battery_level!")
            return


        if self.dust_capacity + dust > 100:
            print("Empty dust_capacity!")
            return

        if self.cleaning_mode =="wet":
            if self.water_capacity < water:
                print("Nor Enough water!")
                return

        print("Working!")
        self.battery_level -= energy
        self.dust_capacity += dust

        if self.cleaning_mode == "wet":
            self.water_capacity -= water


robot2 = CleaningRobot("Abs")
robot2.turn_on()
robot2.clean(50, 20, 20)
robot2.info()







