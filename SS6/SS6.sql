-- CREATE DATABASE NPS_CSA10;


USE NPS_CSA10;

CREATE TABLE Students 
(
StudentId INT PRIMARY KEY,
Name VARCHAR(50),
Age INT,
Grade VARCHAR(5),
City VARCHAR(50)
);

INSERT INTO Students (StudentId, Name, Age, Grade, City)
VALUES 
(1, 'Đinh Hoàng Hà Anh', 17, 'B', 'Hà Nội'),
(2, 'Vũ Đức Trí', 16, 'C', 'Hà Nội'),
(3, 'Đào Quang Anh', 17, 'A', 'Hà Nội'),
(4, 'Lê Anh', 16, 'D', 'Hà Nội'),
(5, 'Bùi Minh Khuê', 17, 'A', 'Hà Nội');



