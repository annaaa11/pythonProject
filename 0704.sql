INSERT INTO Vegetables_Fruits (Veg_Fr_Name, Veg_Fr_Type, Calories, Short_description, Color)  
VALUES  
('Apple', 'Fruit', 52, 'A sweet, crunchy fruit rich in fiber and vitamins.', 'Red'),  
('Banana', 'Fruit', 89, 'A soft, energy-rich fruit high in potassium.', 'Yellow'),  
('Carrot', 'Vegetable', 41, 'A crunchy, orange vegetable good for eyesight.', 'Orange'),  
('Tomato', 'Vegetable', 18, 'A juicy red vegetable, often used in salads and sauces.', 'Red'),  
('Strawberry', 'Fruit', 32, 'A small, red, sweet fruit rich in vitamin C.', 'Red'),  
('Broccoli', 'Vegetable', 55, 'A green vegetable packed with vitamins and fiber.', 'Green'),  
('Orange', 'Fruit', 47, 'A citrus fruit high in vitamin C and antioxidants.', 'Orange'),  
('Potato', 'Vegetable', 77, 'A starchy root vegetable used in many dishes.', 'Brown'),  
('Watermelon', 'Fruit', 30, 'A juicy, hydrating fruit with a sweet taste.', 'Green'),  
('Cucumber', 'Vegetable', 16, 'A refreshing, low-calorie vegetable mostly made of water.', 'Green')

Створіть наступні запити для бази даних з інформацією
про овочі та фрукти з попереднього домашнього завдання:
■ Відображення усіх овочів з калорійністю, менше вказаної.
■ Відображення усіх фруктів з калорійністю у вказаному
діапазоні.
■ Відображення усіх овочів, у назві яких є вказане слово.
Наприклад, слово: капуста.
■ Відображення усіх овочів та фруктів, у короткому описі
яких є вказане слово. Наприклад, слово: гемоглобін.
■ Показати усі овочі та фрукти жовтого або червоного
кольору

SELECT *
FROM Vegetables_Fruits 
WHERE Veg_Fr_Type = 'Vegetable' AND Calories < 500

SELECT *
FROM Vegetables_Fruits 
WHERE Veg_Fr_Type = 'Fruit' AND Calories BETWEEN 40 AND 500

SELECT *
FROM Vegetables_Fruits 
WHERE Veg_Fr_Type = 'Vegetable' AND Veg_Fr_Name LIKE '%Potato%'

SELECT *
FROM Vegetables_Fruits 
WHERE Short_description LIKE '%vitamin%'

SELECT *
FROM Vegetables_Fruits 
WHERE Color = 'Red' OR Color = 'Yellow'

Завдання 2
Створіть наступні запити для бази даних з інформацією
про овочі та фрукти з попереднього домашнього завдання:
■ Показати кількість овочів.
■ Показати кількість фруктів.
■ Показати кількість овочів та фруктів заданого кольору.
■ Показати кількість овочів та фруктів кожного кольору.
■ Показати колір мінімальної кількості овочів та фруктів.++
■ Показати колір максимальної кількості овочів та фруктів.++
■ Показати мінімальну калорійність овочів та фруктів.
■ Показати максимальну калорійність овочів та фруктів.
■ Показати середню калорійність овочів та фруктів.
■ Показати фрукт з мінімальною калорійністю.
■ Показати фрукт з максимальною калорійністю.

SELECT COUNT(*) AS SUM_Fruit
FROM Vegetables_Fruits
WHERE Veg_Fr_Type = 'Fruit'

SELECT COUNT(*) AS SUM_Vegetable
FROM Vegetables_Fruits
WHERE Veg_Fr_Type = 'Vegetable'

SELECT COUNT(*) AS SUM_
FROM Vegetables_Fruits
WHERE Color = 'Red'

SELECT Color, COUNT(*) AS SUM_
FROM Vegetables_Fruits
GROUP BY Color

-- Показати колір максимальної кількості овочів та фруктів.++
WITH Color_STATISTICS AS (
SELECT Color, COUNT(*) AS SUM_
FROM Vegetables_Fruits
GROUP BY Color
)
SELECT Color, SUM_
FROM Color_STATISTICS
WHERE SUM_ = (
	SELECT MAX(SUM_)
	FROM Color_STATISTICS
)

--■ Показати колір мінімальної кількості овочів та фруктів.++

WITH Color_STATISTICS AS (
SELECT Color, COUNT(*) AS SUM_
FROM Vegetables_Fruits
GROUP BY Color
)
SELECT Color, SUM_
FROM Color_STATISTICS
WHERE SUM_ = (
	SELECT MIN(SUM_)
	FROM Color_STATISTICS
)

SELECT MIN(Calories)
FROM Vegetables_Fruits

SELECT MAX(Calories)
FROM Vegetables_Fruits

SELECT AVG(Calories)
FROM Vegetables_Fruits

SELECT *
FROM Vegetables_Fruits
WHERE Calories = (
	SELECT MAX(Calories)
FROM Vegetables_Fruits
WHERE Veg_Fr_Type = 'Fruit'
)

SELECT *
FROM Vegetables_Fruits
WHERE Calories = (
	SELECT MIN(Calories)
FROM Vegetables_Fruits 
WHERE Veg_Fr_Type = 'Fruit'
)

  


