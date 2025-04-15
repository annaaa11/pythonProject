
Куратори (Curators)
■ Ідентифікатор (Id). Унікальний ідентифікатор куратора.
▷ Тип даних — int.
▷ Автоприріст.
▷ Не містить null-значення.
▷ Первинний ключ.
Ім’я (Name). Ім’я куратора.
▷ Тип даних — varchar(max).
▷ Не містить null-значення.
▷ Не може бути порожнє.
■ Прізвище (Surname). Прізвище куратора.
▷ Тип даних — varchar(max).
▷ Не містить null-значення.
▷ Не може бути порожнє


CREATE TABLE Curators(
ID SERIAL NOT NULL PRIMARY KEY,
Name VARCHAR(50) NOT NULL CHECK(NAME != ''),
Surname VARCHAR(50) NOT NULL CHECK(NAME != '') 
)



Факультети (Faculties)
■ Ідентифікатор (Id). Унікальний ідентифікатор
факультету.
▷ Тип даних — int.
▷ Автоприріст.
▷ Не містить null-значення.
▷ Первинний ключ.
■ Фінансування (Financing). Фонд фінансування факультету.
▷ Тип даних — DECIMAL(10, 2).
▷ Не містить null-значення.
▷ Не може бути менше, ніж 0.
▷ Значення за замовчуванням — 0.
■ Назва (Name). Назва факультету.
▷ Тип даних — varchar(100).
▷ Не містить null-значення.
▷ Не може бути порожньою.
▷ Має бути унікальною.


CREATE TABLE Faculties(
ID SERIAL NOT NULL PRIMARY KEY,
FINANCING DECIMAL(10, 2) NOT NULL CHECK(FINANCING >= 0) DEFAULT 0,
NAME VARCHAR(100) NOT NULL CHECK(NAME != '') UNIQUE
)

Кафедри (Departments)
■ Ідентифікатор (Id). Унікальний ідентифікатор кафедри.
▷ Тип даних — int.
▷ Автоприріст.
▷ Не містить null-значення.
▷ Первинний ключ.
■ Фінансування (Financing). Фонд фінансування кафедри.
▷ Тип даних — DECIMAL(10, 2).
▷ Не містить null-значення.
▷ Не може бути менше, ніж 0.
▷ Значення за замовчуванням — 0.
■ Назва (Name). Назва кафедри.
▷ Тип даних — varchar(100).
▷ Не містить null-значення.
▷ Не може бути порожньою.
▷ Має бути унікальною.
Ідентифікатор факультету (FacultyId). Факультет, до складу
якого належить кафедра.
▷ Тип даних — int.
▷ Не містить null-значення.
▷ Зовнішній ключ.




CREATE TABLE DEPARTMENTS(
	ID SERIAL NOT NULL PRIMARY KEY,	
	FINANCING DECIMAL(10, 2) NOT NULL CHECK(FINANCING >= 0) DEFAULT 0,
	NAME VARCHAR(100) NOT NULL CHECK(NAME != '') UNIQUE,
	FacultyId INT NOT NULL REFERENCES Faculties(ID)
)



Групи (Groups)
■ Ідентифікатор (Id). Унікальний ідентифікатор групи.
▷ Тип даних — int.
▷ Автоприріст.
▷ Не містить null-значення.
▷ Первинний ключ.
■ Назва (Name). Назва групи.
▷ Тип даних — varchar(10).
▷ Не містить null-значення.
▷ Не може бути порожньою.
▷ Має бути унікальною.
■ Курс (Year). Курс (рік), на якому навчається група.
▷ Тип даних — int.
Не містить null-значення.
▷ Має бути в діапазоні від 1 до 5.
■ Ідентифікатор кафедри (DepartmentId). Кафедра, до складу
якої належить група.
▷ Тип даних — int.
▷ Не містить null-значення.
▷ Зовнішній ключ.

CREATE TABLE Groups(
ID SERIAL NOT NULL PRIMARY KEY,
Year INT NOT NULL CHECK(Year >= 1 AND Year <= 5),
NAME VARCHAR(10) NOT NULL CHECK(NAME != '') UNIQUE,
DepartmentId INT NOT NULL REFERENCES DEPARTMENTS(ID)
)

Групи та куратори (GroupsCurators)
■ Ідентифікатор (Id). Унікальний ідентифікатор групи та
куратора.
▷ Тип даних — int.
▷ Автоприріст.
▷ Не містить null-значення.
▷ Первинний ключ.
■ Ідентифікатор куратора (CuratorId). Куратор.
▷ Тип даних — int.
▷ Не містить null-значення.
▷ Зовнішній ключ.
■ Ідентифікатор групи (GroupId). Група.
▷ Тип даних — int.
▷ Не містить null-значення.
▷ Зовнішній ключ.


CREATE TABLE GroupsCurators(
ID SERIAL NOT NULL PRIMARY KEY,
CuratorId INT NOT NULL REFERENCES Curators(ID),
GroupId INT NOT NULL REFERENCES Groups(ID)
)




¾ Предмети (Subjects)
■ Ідентифікатор (Id). Унікальний ідентифікатор предмета.
▷ Тип даних — int.
▷ Автоприріст.
▷ Не містить null-значення.
▷ Первинний ключ.
■ Назва (Name). Назва предмета.
▷ Тип даних — varchar(100).
▷ Не містить null-значення.
▷ Не може бути порожньою.
▷ Має бути унікальною.

CREATE TABLE Subjects(
ID SERIAL NOT NULL PRIMARY KEY,
NAME VARCHAR(100) NOT NULL CHECK(NAME != '') UNIQUE
)


Викладачі(Teachers)
■ Ідентифікатор (Id). Унікальний ідентифікатор
викладача.
▷ Тип даних — int.
▷ Автоприріст.
▷ Не містить null-значення.
▷ Первинний ключ.
■ Ім’я (Name). Ім’я викладача.
▷ Тип даних — varchar(max).
▷ Не містить null-значення.
▷ Не може бути порожньою.
■ Ставка (Salary). Ставка викладача.
▷ Тип даних — DECIMAL(10, 2).
▷ Не містить null-значення.
▷ Не може бути меншою або дорівнювати 0.
■ Прізвище (Surname). Прізвище викладача.
▷ Тип даних — varchar(max).
▷ Не містить null-значення.
▷ Не може бути порожнє.

CREATE TABLE Teachers(
ID SERIAL NOT NULL PRIMARY KEY,
NAME varchar(20) NOT NULL CHECK(NAME != ''),
SURNAME varchar(50) NOT NULL CHECK(SURNAME != ''),
Salary DECIMAL(10, 2) NOT NULL CHECK(Salary > 0)
)

Лекції (Lectures)
■ Ідентифікатор (Id). Унікальний ідентифікатор лекції.
▷ Тип даних — int.
▷ Автоприріст.
▷ Не містить null-значення.
▷ Первинний ключ.
■ Аудиторія (LectureRoom). Аудиторія, в якій проходить
лекція.
▷ Тип даних — varchar(max).
▷ Не містить null-значення.
▷ Не може бути порожньою.
■ Ідентифікатор предмета (SubjectId). Предмет, з якого читається лекція.
▷ Тип даних — int.
▷ Не містить null-значення.
▷ Зовнішній ключ.
■ Ідентифікатор викладача (TeacherId). Викладач, який веде
лекцію.
▷ Тип даних — int.
▷ Не містить null-значення.
Зовнішній ключ.

CREATE TABLE Lectures(
ID SERIAL NOT NULL PRIMARY KEY,
Year INT NOT NULL CHECK(Year >= 1 AND Year <= 5),
LectureRoom VARCHAR(10) NOT NULL CHECK(LectureRoom != ''),
SubjectId INT NOT NULL REFERENCES Subjects(ID),
TeacherId INT NOT NULL REFERENCES Teachers(ID)
)


Групи та лекції (GroupsLectures)
■ Ідентифікатор (Id). Унікальний ідентифікатор групи та
лекції.
▷ Тип даних — int.
▷ Автоприріст.
▷ Не містить null-значення.
▷ Первинний ключ
Ідентифікатор групи (GroupId). Група.
▷ Тип даних — int.
▷ Не містить null-значення.
▷ Зовнішній ключ.
■ Ідентифікатор лекції (LectureId). Лекція.
▷ Тип даних — int.
▷ Не містить null-значення.
▷ Зовнішній ключ.

CREATE TABLE GroupsLectures(
ID SERIAL NOT NULL PRIMARY KEY,
GroupId INT NOT NULL REFERENCES Groups(ID),
LectureId INT NOT NULL REFERENCES Lectures(ID)
)


-- INSERT

INSERT INTO Curators (Name, Surname) VALUES
('Olena', 'Shevchenko'),
('Ihor', 'Kovalenko'),
('Nadiya', 'Petrenko'),
('Serhiy', 'Boyko'),
('Larysa', 'Tkachenko'),
('Oleh', 'Melnyk'),
('Kateryna', 'Kravchenko'),
('Andriy', 'Bondarenko'),
('Yuliya', 'Marchenko'),
('Viktor', 'Polishchuk'),
('Iryna', 'Hnatenko'),
('Denys', 'Shulha'),
('Svitlana', 'Moroz'),
('Oleksandr', 'Pavlenko'),
('Mariya', 'Danylenko'),
('Roman', 'Zinchenko'),
('Tetiana', 'Kutsenko'),
('Dmytro', 'Lysenko'),
('Halyna', 'Savchenko'),
('Mykola', 'Chernenko')


INSERT INTO Faculties (FINANCING, NAME) VALUES
(150000.00, 'Faculty of Economics'),
(120000.00, 'Faculty of Mathematics'),
(130000.00, 'Faculty of Computer Science'),
(110000.00, 'Faculty of Management'),
(140000.00, 'Faculty of Physics'),
(125000.00, 'Faculty of Biology'),
(135000.00, 'Faculty of Chemistry'),
(118000.00, 'Faculty of Engineering'),
(127000.00, 'Faculty of Philosophy'),
(123000.00, 'Faculty of Sociology'),
(119000.00, 'Faculty of Psychology'),
(145000.00, 'Faculty of Law'),
(138000.00, 'Faculty of History'),
(117000.00, 'Faculty of Geography'),
(113000.00, 'Faculty of Foreign Languages'),
(129000.00, 'Faculty of Journalism'),
(121000.00, 'Faculty of Medicine'),
(122000.00, 'Faculty of Art and Culture'),
(132000.00, 'Faculty of Information Systems'),
(124000.00, 'Faculty of Environmental Science')


INSERT INTO DEPARTMENTS (FINANCING, NAME, FacultyId) VALUES
(50000.00, 'Mathematical Analysis', 1),
(48000.00, 'Applied Economics', 1),
(62000.00, 'Software Development', 2),
(41000.00, 'Cybersecurity', 2),
(47000.00, 'Theoretical Physics', 3),
(39000.00, 'Accounting and Audit', 1),
(51000.00, 'Marketing Technologies', 4),
(55000.00, 'Data Science', 2),
(60000.00, 'Artificial Intelligence', 2),
(45000.00, 'Mechanical Engineering', 5),
(52000.00, 'Biophysics', 3),
(43000.00, 'Ecology and Nature Protection', 3),
(49000.00, 'Genetics and Biotechnology', 3),
(58000.00, 'Finance and Credit', 1),
(44000.00, 'Transport Systems', 5),
(46500.00, 'Construction Engineering', 5),
(52500.00, 'Web Engineering', 2),
(63000.00, 'Quantitative Methods', 1),
(47000.00, 'Human Resource Management', 4),
(41500.00, 'Digital Marketing', 4);

INSERT INTO DEPARTMENTS (FINANCING, NAME, FacultyId) VALUES
(415000.00, 'Digital', 4)

INSERT INTO Groups (Year, NAME, DepartmentId) VALUES
(1, 'CS101', 3),
(2, 'CS102', 3),
(3, 'CS201', 3),
(1, 'ECO101', 1),
(2, 'ECO202', 1),
(3, 'FIN301', 14),
(4, 'MATH401', 2),
(1, 'PHY101', 5),
(2, 'BIO102', 12),
(3, 'LAW301', 13),
(1, 'MGMT101', 4),
(2, 'AI202', 9),
(3, 'WEB301', 17),
(4, 'DS401', 8),
(1, 'HRM101', 19),
(2, 'MARK202', 7),
(3, 'AUD301', 6),
(4, 'ENGR401', 10),
(5, 'CON502', 16),
(1, 'GEN101', 13)

INSERT INTO GroupsCurators (CuratorId, GroupId) VALUES
(1, 1), (2, 2), (3, 3), (4, 4),
(5, 5), (6, 6), (7, 7), (8, 8),
(9, 9), (10, 10), (11, 11), (12, 12),
(13, 13), (14, 14), (15, 15), (16, 16),
(17, 17), (18, 18), (19, 19), (20, 20)

INSERT INTO Subjects (NAME) VALUES
('Microeconomics'),
('Macroeconomics'),
('Linear Algebra'),
('Discrete Mathematics'),
('Software Engineering'),
('Cybersecurity Basics'),
('Financial Accounting'),
('Marketing Management'),
('Machine Learning'),
('Artificial Intelligence'),
('Ecology'),
('Genetics'),
('Physics Fundamentals'),
('Organic Chemistry'),
('Constitutional Law'),
('Sociology'),
('Philosophy of Science'),
('Cultural Studies'),
('History of Ukraine'),
('Human Psychology')

INSERT INTO Teachers (NAME, SURNAME, Salary) VALUES
('Ivan', 'Kovalenko', 1500.00),
('Olga', 'Shevchenko', 1600.00),
('Andriy', 'Petrenko', 1400.00),
('Svitlana', 'Tkachenko', 1450.00),
('Oleh', 'Melnyk', 1550.00),
('Kateryna', 'Kravchenko', 1600.00),
('Denys', 'Bondarenko', 1580.00),
('Yuliya', 'Marchenko', 1520.00),
('Viktor', 'Polishchuk', 1590.00),
('Iryna', 'Hnatenko', 1510.00),
('Dmytro', 'Shulha', 1490.00),
('Larysa', 'Moroz', 1500.00),
('Oleksandr', 'Pavlenko', 1530.00),
('Mariya', 'Danylenko', 1560.00),
('Roman', 'Zinchenko', 1540.00),
('Tetiana', 'Kutsenko', 1570.00),
('Mykola', 'Lysenko', 1500.00),
('Halyna', 'Savchenko', 1525.00),
('Bohdan', 'Chernenko', 1480.00),
('Nadiya', 'Stasenko', 1460.00)

INSERT INTO Lectures (Year, LectureRoom, SubjectId, TeacherId) VALUES
(1, 'A101', 1, 1),
(1, 'A102', 2, 2),
(2, 'B201', 3, 3),
(2, 'B202', 4, 4),
(3, 'C301', 5, 5),
(3, 'C302', 6, 6),
(4, 'D401', 7, 7),
(4, 'D402', 8, 8),
(5, 'E501', 9, 9),
(5, 'E502', 10, 10),
(1, 'F103', 11, 11),
(2, 'G203', 12, 12),
(3, 'H303', 13, 13),
(4, 'I403', 14, 14),
(5, 'J503', 15, 15),
(1, 'K104', 16, 16),
(2, 'L204', 17, 17),
(3, 'M304', 18, 18),
(4, 'N404', 19, 19),
(5, 'O504', 20, 20)

INSERT INTO GroupsLectures (GroupId, LectureId) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14),
(15, 15),
(16, 16),
(17, 17),
(18, 18),
(19, 19),
(20, 20);

---SELECT---------------

1. Виведіть усі можливі пари рядків викладачів і груп.


SELECT T.NAME AS TeacherName, T.SURNAME AS TeacherSurname, G.NAME AS GroupName    
FROM GroupsLectures GL
	JOIN Groups G ON GL.GroupId = G.ID
	JOIN Lectures L ON GL.LectureId = L.ID
	JOIN Teachers T ON L.TeacherId = T.ID

	
2. Виведіть назви факультетів, фонд фінансування кафедр
яких перевищує фонд фінансування факультету.


SELECT F.NAME AS FacultName   
FROM Faculties F
	JOIN DEPARTMENTS D ON D.FacultyId = F.ID
WHERE D.FINANCING > F.FINANCING
	
	

3. Виведіть прізвища кураторів груп і назви груп, які вони
курирують.
 
SELECT Curators.Surname as CuratorsSurname, Groups.NAME as  GroupsNAME  
FROM GroupsCurators 
	JOIN Groups ON Groups.Id = GroupsCurators.GroupId
	JOIN Curators ON Curators.Id = GroupsCurators.CuratorId


4. Виведіть імена та прізвища викладачів, які читають лекції
у групі «P107». FIN301

SELECT T.NAME AS TeacherName, T.SURNAME AS TeacherSurname    
FROM GroupsLectures GL
	JOIN Groups G ON GL.GroupId = G.ID
	JOIN Lectures L ON GL.LectureId = L.ID
	JOIN Teachers T ON L.TeacherId = T.ID
WHERE G.NAME = 'FIN301'

5. Виведіть прізвища викладачів і назви факультетів, на яких
вони читають лекції.

SELECT T.SURNAME AS TeachersName, F.NAME As FacultiesName   
FROM GroupsLectures GL
	JOIN Groups G ON GL.GroupId = G.ID
	JOIN Lectures L ON GL.LectureId = L.ID
	JOIN Teachers T ON L.TeacherId = T.ID
	JOIN DEPARTMENTS D ON G.DepartmentId = D.ID
	JOIN Faculties F ON D.FacultyId = F.ID



6. Виведіть назви кафедр і назви груп, які до них належать.

SELECT D.NAME AS DEPARTMENT, G.NAME As Group   
FROM GroupsLectures GL
	JOIN Groups G ON GL.GroupId = G.ID	
	JOIN DEPARTMENTS D ON G.DepartmentId = D.ID
	JOIN Faculties F ON D.FacultyId = F.ID

	

7. Виведіть назви предметів, які викладає викладач «Samantha
Adams». Kateryna Kravchenko

SELECT S.NAME AS SubjectsName   
FROM GroupsLectures GL
	JOIN Groups G ON GL.GroupId = G.ID
	JOIN Lectures L ON GL.LectureId = L.ID
	JOIN Teachers T ON L.TeacherId = T.ID
	JOIN Subjects S ON L.SubjectId = S.ID
WHERE T.NAME = 'Kateryna' AND T.SURNAME = 'Kravchenko'

8. Виведіть назви кафедр, на яких викладається дисципліна
«Database Theory». Software Engineering

SELECT D.NAME AS DEPARTMENT   
FROM GroupsLectures GL
	JOIN Groups G ON GL.GroupId = G.ID
	JOIN Lectures L ON GL.LectureId = L.ID
	JOIN Teachers T ON L.TeacherId = T.ID
	JOIN DEPARTMENTS D ON G.DepartmentId = D.ID
	JOIN Faculties F ON D.FacultyId = F.ID 	
	JOIN Subjects S ON L.SubjectId = S.ID
WHERE S.NAME = 'Software Engineering'


9. Виведіть назви груп, що належать до факультету «Computer
Science».

SELECT G.NAME As Group   
FROM GroupsLectures GL
	JOIN Groups G ON GL.GroupId = G.ID	
	JOIN DEPARTMENTS D ON G.DepartmentId = D.ID
	JOIN Faculties F ON D.FacultyId = F.ID
WHERE F.NAME LIKE '%Computer Science%'

10. Виведіть назви груп 5-го курсу, а також назви факультетів,
до яких вони належать.

SELECT G.NAME As Group, F.NAME as Faculties  
FROM GroupsLectures GL
	JOIN Groups G ON GL.GroupId = G.ID	
	JOIN DEPARTMENTS D ON G.DepartmentId = D.ID
	JOIN Faculties F ON D.FacultyId = F.ID
WHERE G.YEAR = 5


11. Виведіть повні імена викладачів і лекції, які вони читають
(назви предметів та груп). Зробіть відбір по тим лекціям,
які проходять в аудиторії «B103». A101

SELECT T.NAME ||' '|| T.SURNAME AS Teachers, S.NAME as Subjects, G.NAME as Groups
FROM GroupsLectures GL
	JOIN Groups G ON GL.GroupId = G.ID
	JOIN Lectures L ON GL.LectureId = L.ID
	JOIN Teachers T ON L.TeacherId = T.ID
	JOIN DEPARTMENTS D ON G.DepartmentId = D.ID
	JOIN Faculties F ON D.FacultyId = F.ID 	
	JOIN Subjects S ON L.SubjectId = S.ID
WHERE L.LectureRoom = 'A101'

