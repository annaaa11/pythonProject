-- База даних Академія (Academy) містить інформацію про
-- співробітників та внутрішній порядок академії.
-- Викладачі, які читають лекції в академії, занесені до таблиці
-- Викладачі (Teachers), в якій зібрано основну інформацію: ім’я,
-- прізвище, дані про зарплату, дата прийому на роботу.
-- Також у базі даних є інформація про групи, яка зберігається в таблиці Групи (Groups). Дані про факультети та кафедри містяться в таблицях Факультети (Faculties) та Кафедри
-- (Departments) відповідно.

-----Таблиці--------------------
--  Кафедри (Departments)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор кафедри.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Фінансування (Financing). Фонд фінансування кафедри.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Назва (Name). Назва кафедри.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною


CREATE TABLE DEPARTMENTS(
	ID SERIAL NOT NULL PRIMARY KEY,	
	FINANCING FLOAT NOT NULL CHECK(FINANCING >= 0) DEFAULT 0,
	NAME VARCHAR(100) NOT NULL CHECK(NAME != '') UNIQUE
)

INSERT INTO DEPARTMENTS (Financing, Name)
VALUES
    (140000.00, 'Department of Economics'),
    (135000.00, 'Department of Mathematics'),
    (125000.00, 'Department of Computer Science'),
    (110000.00, 'Department of Physics'),
    (105000.00, 'Department of Chemistry'),
    (95000.00,  'Department of History'),
    (100000.00, 'Department of Philosophy')
	



SELECT * 
FROM DEPARTMENTS

-- ¾ Факультети(Faculties)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор факультету.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Декан (Dean). Декан факультету.
-- ▷ Тип даних — varchar(255).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнім.
-- Назва (Name). Назва факультету.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

CREATE TABLE Faculties(
ID SERIAL NOT NULL PRIMARY KEY,
Decan VARCHAR(255) NOT NULL CHECK(NAME != ''),
NAME VARCHAR(100) NOT NULL CHECK(NAME != '') UNIQUE
)


INSERT INTO Faculties (Decan, Name)
VALUES
    ('Dr. Elizabeth Carter', 'Faculty of Economics'),
    ('Dr. James Thornton', 'Faculty of Mathematics and Informatics'),
    ('Dr. Linda Martinez', 'Faculty of Natural Sciences'),
    ('Dr. Robert Young', 'Faculty of History and Philosophy'),
    ('Dr. Susan Bennett', 'Faculty of Law'),
    ('Dr. Michael Green', 'Faculty of Social Sciences'),
    ('Dr. Karen Hughes', 'Faculty of Engineering'),
    ('Dr. Thomas Brooks', 'Faculty of Education'),
    ('Dr. Angela Simmons', 'Faculty of Medicine'),
    ('Dr. William Adams', 'Faculty of Foreign Languages')


-- Групи (Groups)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор групи.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва групи.
-- ▷ Тип даних — varchar(10).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Рейтинг (Rating). Рейтинг групи.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 0 до 5.
-- ■ Курс (Year). Курс (рік), на якому навчається група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 5.

CREATE TABLE Groups(
ID SERIAL NOT NULL PRIMARY KEY,
Year INT NOT NULL CHECK(Year >= 1 AND Year <= 5),
Rating INT NOT NULL CHECK(Rating >= 0 AND Rating <= 5),
NAME VARCHAR(10) NOT NULL CHECK(NAME != '') UNIQUE
)

INSERT INTO Groups (Year, Rating, Name)
VALUES
    (1, 4, 'ECO-101'),
    (2, 5, 'MATH-202'),
    (3, 3, 'CS-303'),
    (4, 4, 'PHYS-404'),
    (5, 2, 'CHEM-505'),
    (1, 3, 'LAW-106'),
    (2, 5, 'ENG-207'),
    (3, 4, 'MED-308'),
    (4, 5, 'HIST-409'),
    (5, 1, 'SOC-510')

-- Викладачі(Teachers)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- викладача.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- Не містить null-значення.
-- ▷ Первинний ключ.

-- ■ Дата працевлаштування (EmploymentDate). Дата працевлаштування викладача.
-- ▷ Тип даних — date.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше 01.01.1990.

-- ■ Асистент (IsAssistant). Чи є викладач асистентом.
-- ▷ Тип даних — bit.
-- ▷ Не містить null-значення.
-- ▷ Значення за замовчуванням — 0.

-- ■ Професор (IsProfessor). Чи є викладач професором.
-- ▷ Тип даних — bit.
-- ▷ Не містить null-значення.
-- ▷ Значення за замовчуванням — 0.

-- Ім’я (Name). Ім’я викладача.
-- ▷ Тип даних — nvarchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.

-- ■ Посада (Position). Посада викладача.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.

-- ■ Надбавка (Premium). Надбавка викладача.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.

-- ■ Ставка (Salary). Ставка викладача.
-- Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути меншою або дорівнювати 0.

-- ■ Прізвище (Surname). Прізвище викладача.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.

CREATE TABLE Teachers(
ID SERIAL NOT NULL PRIMARY KEY,
EmploymentDate DATE NOT NULL CHECK(EmploymentDate >= '01.01.1990'),
IsAssistant BIT NOT NULL DEFAULT '0',
IsProfessor BIT NOT NULL DEFAULT '0',
NAME varchar(20) NOT NULL CHECK(NAME != ''),
SURNAME varchar(50) NOT NULL CHECK(SURNAME != ''),
Position varchar(20) NOT NULL CHECK(Position != ''),
Premium money NOT NULL CHECK(Premium >= 0::MONEY) DEFAULT 0,
Salary money NOT NULL CHECK(Salary > 0::MONEY)
)

INSERT INTO Teachers (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position, Premium, Salary)
VALUES
('2001-09-01', B'1', B'0', 'Anna', 'Petrova', 'Assistant', 500.00::money, 2500.00::money),
('1995-02-15', B'0', B'1', 'John', 'Smith', 'Professor', 1000.00::money, 5500.00::money),
('2008-06-20', B'0', B'0', 'Daria', 'Koval', 'Lecturer', 300.00::money, 3200.00::money),
('2012-01-10', B'1', B'0', 'Ivan', 'Melnyk', 'Assistant', 200.00::money, 2200.00::money),
('1993-03-05', B'0', B'1', 'Olga', 'Ivanova', 'Professor', 1500.00::money, 6000.00::money),
('2000-09-01', B'0', B'0', 'Mark', 'Davies', 'Lecturer', 400.00::money, 3100.00::money),
('2010-10-10', B'1', B'0', 'Svitlana', 'Tkachenko', 'Assistant', 100.00::money, 2000.00::money),
('1998-04-12', B'0', B'1', 'Robert', 'Brown', 'Professor', 1200.00::money, 5700.00::money),
('2005-11-30', B'0', B'0', 'Natalia', 'Bondarenko', 'Lecturer', 250.00::money, 3300.00::money),
-- ('2018-02-18', B'1', B'0', 'Yuriy', 'Kravets', 'Assistant', 150.00::money, 2100.00::money),
('1991-07-01', B'0', B'1', 'Ludmila', 'Martynenko', 'Professor', 1300.00::money, 5900.00::money),
('2003-03-21', B'0', B'0', 'Peter', 'Green', 'Lecturer', 350.00::money, 3400.00::money),
('2007-05-14', B'1', B'0', 'Inna', 'Polishchuk', 'Assistant', 220.00::money, 2300.00::money),
('1999-12-12', B'0', B'1', 'Victor', 'Shevchenko', 'Professor', 1100.00::money, 5600.00::money),
('2002-08-25', B'0', B'0', 'Emily', 'Roberts', 'Lecturer', 300.00::money, 3100.00::money),
('2011-09-05', B'1', B'0', 'Iryna', 'Fedorova', 'Assistant', 180.00::money, 2150.00::money),
('1994-10-30', B'0', B'1', 'Sergey', 'Bondar', 'Professor', 1400.00::money, 6100.00::money),
('2006-06-06', B'0', B'0', 'Julia', 'Taylor', 'Lecturer', 275.00::money, 3350.00::money),
('2013-07-17', B'1', B'0', 'Andriy', 'Zhuk', 'Assistant', 160.00::money, 2250.00::money),
('1997-05-01', B'0', B'1', 'Maria', 'Lozynska', 'Professor', 1250.00::money, 5800.00::money);


SELECT *
FROM Teachers


-- 1. Вивести таблицю кафедр, але розташувати її поля у зворотному порядку.
SELECT NAME, FINANCING, ID
FROM DEPARTMENTS



-- 2. Вивести назви груп та їх рейтинги з уточненнями до назв
-- полів відповідно до назви таблиці.

SELECT 
NAME as "Group NAME", Rating as "Group Rating", Year as "Group Year" 
FROM Groups


-- 3. Вивести для викладачів їх прізвища, відсоток ставки по
-- відношенню до надбавки та відсоток ставки по відношенню до зарплати (сума ставки та надбавки).

SELECT SURNAME, (Salary/Premium)*100 as "Salary/Premium%", 100*Salary/(Premium+Salary) as "Salary/(Premium+Salary)%"
FROM Teachers


-- 4. Вивести таблицю факультетів одним полем у такому форматі: «The dean of faculty [faculty] is [dean].».

SELECT 
    'The dean of faculty ' || NAME || ' is ' || Decan || '.' AS Faculty_Info
FROM Faculties



-- 5. Вивести прізвища професорів, ставка яких перевищує 1050.
SELECT SURNAME, Salary
FROM Teachers
WHERE Salary > 1050::money 


-- 6. Вивести назви кафедр, фонд фінансування яких менший,
-- ніж 11000 або більший за 25000.

SELECT NAME, FINANCING
FROM DEPARTMENTS
WHERE FINANCING < 11000 OR FINANCING > 25000

-- 7. Вивести назви факультетів, окрім факультету «Computer
-- Science».
SELECT NAME
FROM DEPARTMENTS
WHERE NAME NOT LIKE '%Computer Science%'

--8. ивести прізвища та посади викладачів, які не є професорами.

SELECT SURNAME, Position 
FROM Teachers
WHERE IsProfessor = '0'


9. Вивести прізвища, посади, ставки та надбавки асистентів,
надбавка яких у діапазоні від 160 до 550.

SELECT SURNAME, Position, Salary, Premium 
FROM Teachers
WHERE IsAssistant = '1' AND (Premium BETWEEN 160::money AND 550::money)


10. Вивести прізвища та ставки асистентів.

SELECT SURNAME, Salary
FROM Teachers
WHERE IsAssistant = '1' 

11. Вивести прізвища та посади викладачів, які були прийняті
на роботу до 01.01.2000.

SELECT SURNAME, Position, EmploymentDate
FROM Teachers
WHERE EmploymentDate < '01.01.2000'


12. Вивести назви кафедр, які в алфавітному порядку розміщені до кафедри «Software Development». Виведене поле
назвіть «Name of Department».

SELECT NAME AS "Name of Department"
FROM DEPARTMENTS
WHERE NAME < 'Department of History'
ORDER BY NAME

13. Вивести прізвища асистентів із зарплатою (сума ставки
та надбавки) не більше 1200.

SELECT SURNAME
FROM Teachers
WHERE IsAssistant = '1' AND (Premium + Salary ) < 12000::money 

14. Вивести назви груп 5-го курсу з рейтингом у діапазоні
від 2 до 4.

SELECT NAME 
FROM Groups
WHERE Year = 5 AND Rating BETWEEN 2 AND 4

15. Вивести прізвища асистентів зі ставкою менше, ніж 550
або надбавкою менше, ніж 200.

SELECT SURNAME
FROM Teachers
WHERE IsAssistant = '1' AND ( Salary < 550::money OR Premium  < 200::money) 

