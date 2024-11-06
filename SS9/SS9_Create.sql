CREATE DATABASE NPS_CSA10;

USE NPS_CSA10;


-- Tạo bảng Students
CREATE TABLE Students (
	StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50),
    Age INT,
    City VARCHAR(50)
);

CREATE TABLE Courses(
	CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50),
    Credits INT
);


CREATE TABLE Enrollments(
	EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    Grade CHAR(1),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

CREATE TABLE Teachers (
	TeacherID INT PRIMARY KEY,
    TeacherName VARCHAR(50),
    Department VARCHAR(50)
);

CREATE TABLE CourseAssignments(
	AssignmentID INT PRIMARY KEY,
    CourseID INT,
    TeacherID INT,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
);


-- Thêm dữ liệu mẫu
INSERT INTO Students VALUES (1, 'Alice', 20, 'New York');
INSERT INTO Students VALUES (2, 'Bob', 21, 'Los Angeles');
INSERT INTO Students VALUES (3, 'Charlie', 22, 'Chicago');
INSERT INTO Students VALUES (4, 'David', 23, 'Houston');
INSERT INTO Students VALUES (5, 'Eve', 20, 'Phoenix');

INSERT INTO Courses VALUES (101, 'Math', 3);
INSERT INTO Courses VALUES (102, 'Science', 4);
INSERT INTO Courses VALUES (103, 'Literature', 2);
INSERT INTO Courses VALUES (104, 'History', 3);
INSERT INTO Courses VALUES (105, 'Art', 2);

INSERT INTO Enrollments VALUES (1, 1, 101, 'A');
INSERT INTO Enrollments VALUES (2, 2, 102, 'B');
INSERT INTO Enrollments VALUES (3, 3, 103, 'C');
INSERT INTO Enrollments VALUES (4, 4, 104, 'A');
INSERT INTO Enrollments VALUES (5, 5, 105, 'B');
INSERT INTO Enrollments VALUES (6, 1, 102, 'A');
INSERT INTO Enrollments VALUES (7, 2, 103, 'C');
INSERT INTO Enrollments VALUES (8, 3, 104, 'B');

INSERT INTO Teachers VALUES (1, 'Prof. Smith', 'Mathematics');
INSERT INTO Teachers VALUES (2, 'Prof. Johnson', 'Science');
INSERT INTO Teachers VALUES (3, 'Prof. Lee', 'Literature');
INSERT INTO Teachers VALUES (4, 'Prof. Brown', 'History');
INSERT INTO Teachers VALUES (5, 'Prof. White', 'Art');

INSERT INTO CourseAssignments VALUES (1, 101, 1);
INSERT INTO CourseAssignments VALUES (2, 102, 2);
INSERT INTO CourseAssignments VALUES (3, 103, 3);
INSERT INTO CourseAssignments VALUES (4, 104, 4);
INSERT INTO CourseAssignments VALUES (5, 105, 5);










