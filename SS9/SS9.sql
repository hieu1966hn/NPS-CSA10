-- Truy vấn dữ liệu nhiều bảng
USE NPS_CSA10;

-- 1. Lấy tên học sinh và khóa học họ tham gia
-- SELECT Students.StudentName, Courses.CourseName
-- FROM Students
-- INNER JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
-- INNER JOIN Courses ON Enrollments.CourseID = Courses.CourseID;

-- 2. Lấy danh sách học sinh kèm điểm số của họ trong từng khóa học
-- SELECT Students.StudentName, Courses.CourseName, Enrollments.Grade
-- FROM Students
-- INNER JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
-- INNER JOIN Courses ON Enrollments.CourseID = Courses.CourseID;

-- 3. Liệt kê tất cả các giáo viên và khóa học mà họ giảng dạy
-- SELECT Teachers.TeacherName, Courses.CourseName
-- FROM Teachers
-- INNER JOIN CourseAssignments ON Teachers.TeacherID = CourseAssignments.TeacherID
-- INNER JOIN Courses ON CourseAssignments.CourseID = Courses.CourseID;


-- 4. Tìm các học sinh đăng ký khóa học 'Math' và điểm của họ
-- SELECT Students.StudentName, Courses.CourseName, Enrollments.Grade
-- FROM Students
-- INNER JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
-- INNER JOIN Courses ON Enrollments.CourseID = Courses.CourseID
-- WHERE Courses.CourseName =  'Math';


-- 5. Lấy tên và độ tuổi của các học sinh đã đạt điểm 'A' trong bất kỳ khóa học nào
-- SELECT Students.StudentName, Students.Age, Enrollments.Grade
-- FROM Students 
-- INNER JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
-- WHERE Enrollments.Grade = 'A';

-- 6. Liệt kê học sinh, khóa học và giáo viên giảng dạy khóa học đó
-- SELECT Students.StudentName, Courses.CourseName, Teachers.TeacherName
-- FROM Students
-- INNER JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
-- INNER JOIN Courses ON Enrollments.CourseID = Courses.CourseID
-- INNER JOIN CourseAssignments ON Courses.CourseID = CourseAssignments.CourseID
-- INNER JOIN Teachers ON CourseAssignments.TeacherID = Teachers.TeacherID;

-- 7. Lấy thông tin học sinh từ 'New York' tham gia vào khóa học 'Science';
-- SELECT Students.StudentName, Students.City, Courses.CourseName
-- FROM Students
-- INNER JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
-- INNER JOIN Courses ON Enrollments.CourseID = Courses.CourseID
-- WHERE Students.City = 'New York' AND Courses.CourseName = 'Science';

-- 8. Đếm số học sinh trong mỗi khóa học
-- SELECT Courses.CourseName, COUNT(Enrollments.StudentID) AS StudentCount
-- FROM Courses
-- LEFT JOIN Enrollments ON Courses.CourseID = Enrollments.CourseID
-- GROUP BY Courses.CourseName;

-- 9. Lấy danh sách tất cả các học sinh chưa đăng ký vào khóa học nào?
-- SELECT Students.StudentName
-- FROM Students
-- LEFT JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
-- WHERE Enrollments.StudentID IS NULL;

-- 10. Lấy danh sách học sinh và tổng số tín chỉ của các khóa học mà họ đang tham gia.
-- SELECT Students.StudentName, SUM(Courses.Credits) AS TotalCredis
-- FROM Students
-- INNER JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
-- INNER JOIN Courses ON Enrollments.CourseID = Courses.CourseID
-- GROUP BY Students.StudentName



