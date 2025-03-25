
"""
 Напишіть програму для збереження даних про музичні
групи у вигляді словника, де ключ – назва групи, значення –
список альбомів.
Напишіть функціонал:
 додати новий гурт
 додати новий альбом
 зберегти дані через json
 зберегти дані через pickle
 завантажити дані через json
 завантажити дані через pickle

"""
import json
import pickle


class MusicLibrary:
    def __init__(self):
        self.bands = {}

    def add_band(self, band_name):
        if band_name not in self.bands:
            self.bands[band_name] = []
        else:
            print("Гурт вже існує!")

    def add_album(self, band_name, album_name):
        if band_name in self.bands:
            if album_name not in self.bands[band_name]:
                self.bands[band_name].append(album_name)
            else:
                print("Альбом вже існує у гурту!")
        else:
            print("Гурт не знайдено!")

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.bands, f)

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as f:
                self.bands = json.load(f)
        except FileNotFoundError:
            print("Файл не знайдено!")

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.bands, f)

    def load_from_pickle(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.bands = pickle.load(f)
        except FileNotFoundError:
            print("Файл не знайдено!")


# Приклад

library = MusicLibrary()

library.add_band("ABBA")
library.add_album("ABBA", "Merry Crist")
library.add_album("ABBA", "Money")
library.save_to_json("bands.json")
library.save_to_pickle("bands.pkl")

new_library = MusicLibrary()
new_library.load_from_json("bands.json")
print(new_library.bands)

new_library.load_from_pickle("bands.pkl")
print(new_library.bands)
