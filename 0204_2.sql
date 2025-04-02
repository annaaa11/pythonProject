-- Створіть однотабличну базу даних «Овочі та фрукти»,
-- яка зберігатиме таку інформацію:
-- ■ Назва;
-- ■ Тип (овоч або фрукт);
-- ■ Колір;
-- ■ Калорійність;
-- ■ Короткий опис.

CREATE TABLE Vegetables_Fruits (
	Veg_Fr_ID SERIAL PRIMARY KEY,
	Veg_Fr_Name VARCHAR(30),
	Veg_Fr_Type VARCHAR(10),	
	Calories FLOAT,
	Short_description VARCHAR(100)	
	)
	
ALTER TABLE Vegetables_Fruits  
ADD COLUMN Color VARCHAR(15);

--DELETE FROM Vegetables_Fruits;

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

-- Створіть наступні запити для таблиці з інформацією про
-- овочі та фрукти із попереднього завдання:
-- ■ Відображення всієї інформації з таблиці овочів та фруктів;
-- ■ Відображення усіх овочів;
-- ■ Відображення усіх фруктів;
-- ■ Відображення усіх назв овочів та фруктів;
-- ■ Відображення усіх кольорів. Кольори мають бути унікальними;
-- ■ Відображення фруктів певного кольору;
-- ■ Відображення овочів певного кольору.

--Відображення всієї інформації з таблиці овочів та фруктів;
SELECT * 
FROM Vegetables_Fruits

--Відображення усіх овочів;
SELECT * 
FROM Vegetables_Fruits
WHERE Veg_Fr_Type = 'Vegetable'

--Відображення усіх фруктів;
SELECT * 
FROM Vegetables_Fruits
WHERE Veg_Fr_Type = 'Fruit'

-- ■ Відображення усіх назв овочів та фруктів;
SELECT Veg_Fr_Name 
FROM Vegetables_Fruits

--Відображення усіх кольорів. Кольори мають бути унікальними;
SELECT DISTINCT Color
 FROM Vegetables_Fruits

--Відображення фруктів певного кольору
SELECT * 
FROM Vegetables_Fruits
WHERE Veg_Fr_Type = 'Fruit' AND Color='Red'

--Відображення овочів певного кольору.
SELECT * 
FROM Vegetables_Fruits
WHERE Veg_Fr_Type = 'Vegetable' AND Color='Brown'


