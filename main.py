# Створіть клас Recipe з атрибутами
#  name – назва страви
#  ingredients – список продуктів
#  text – текст рецепту
#  time – час приготування


class Recipe:
    def __init__(self, name, ingredients, text, time):
        self.name = name
        self.ingredients = ingredients
        self.text = text
        self.time = time

 #   – повертає     назву     страви
    def __str__(self):
        return f"назва страви - {self.name} "

    def __gt__(self, other): # – перевіряє чи є час приготування self більшим за other
        return len(self) > len(other)

    #  перевіряє     чи     є     інгредієнт     в     рецепті
    def __contains__(self, ingredient): #
        return ingredient in self.ingredients

    def display_info(self): # виводить всю інформацію про рецепт
        print (f"назва страви: {self.name}")
        print(f"список продуктів: {self.ingredients}")
        print(f"текст рецепту: {self.text}")
        print(f"час приготування: {self.time}  хвилин")


#Приклад рецептів:
Recipe1 = Recipe("Піца",
["борошно", "вода", "дріжджі", "томат", "сир"],
"Готуємо тісто, додаємо інгредієнти та запікаємо",
30)

Recipe2 = Recipe("Салат",
       ["томат", "огірок", "зелень", "олія"],
       "Нарізаємо овочі, додаємо зелень та поливаємо олією ",
10)

Recipe3 = Recipe("Суп",
       ["вода", "картопля", "морква", "м'ясо"],
       "Варимо всі інгредієнти до готовності",
       45)

recipes = [Recipe1, Recipe2, Recipe3]


# Виведення рецептів з інгредієнтом "томат"
print("Рецепти з томатом:")
for recipe in recipes:
    if "томат" in recipe:
        print(f"- {recipe}")

# Рецепт з найменшим часом приготування
fastest_recipe = recipes[0]
for recipe in recipes[1:]:
    if recipe.time < fastest_recipe.time:
        fastest_recipe = recipe

print("\nРецепт з найменшим часом приготування:")
fastest_recipe.display_info()