

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

class Dog(Pet):
    def play(self, activity_level):
        if self.satiety >15:
            self.satiety -= activity_level//2
            self.energy -= activity_level//2
        print(f"рівень ситості= {self.satiety} рівень енергії= {self.energy} ")

    def make_sound(self):
        print("Гав")

    def fetch_ball(self):
        print("ловить м’яча")
        if self.satiety > 10:
            self.energy -= 5

dog1 = Dog("Bim")
dog1.make_sound()
dog1.play(20)
dog1.fetch_ball()

cat1 = Cat("mura")
cat1.make_sound()
cat1.eat(30)
cat1.sleep()
cat1.catch_mouse()
cat1.play(30)







