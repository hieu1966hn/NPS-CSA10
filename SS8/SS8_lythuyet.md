Buổi 8: Truy vấn dữ liệu từ nhiều bảng

1. INNER JOIN
- Công dụng: Kết hợp các bản ghi từ 2 bảng dựa trên giá trị chung trong một cột (shared column) của cả hai bảng.
- Cú pháp: 
SELECT Students.StudentName , Courses.CourseName
FROM Students 
INNER JOIN Courses
ON Students.CourseID = Courses.CourseID
=> Lấy ra tên học sinh và tên khóa học nếu có giá trị chung.

2. LEFT JOIN
- Công dụng: Trả về tất cả các bảng ghi từ bảng bên trái và các bản ghi khớp từ bảng bên phải. Nếu không có khớp, cột từ bảng bên phải sẽ trả về NULL.
- Cú pháp: 
SELECT table1.col1, table2.col2
FROM table1
LEFT JOIN table2
ON table1.sharedCol = table2.sharedCol;
- Ví dụ: Lấy danh sách tất cả học sinh và các khóa học, kể cả những học sinh không tham gia khóa học nào

SELECT Students.name, Courses.course_name
FROM Students
LEFT JOIN Courses
ON Students.course_id = Courses.course_id;


3. RIGHT JOIN
- Công dụng: Trả về tất cả các dữ liệu từ bảng bên phải và các bản ghi khớp từ bảng bên trái. Nếu không có bản ghi nào khớp sẽ trả về NULL.
- Cú pháp: 
SELECT table1.col1, table2.col2
FROM table1
RIGHT JOIN table2
ON table1.sharedCol = table2.sharedCol;
- Ví dụ: Lấy tất cả khóa học và những học sinh tham gia, kể cả khóa học không có học sinh tham gia.

SELECT Students.name, Courses.course_name
FROM Students
RIGHT JOIN Courses
ON Students.course_id = Courses.course_id;

4. FULL JOIN 
- Công dụng: Kết hợp kết quả của cả LEFT/ RIGHT JOIN. Trả về tất cả dữ liệu từ cả 2 bảng, với các dữ liệu không khớp sẽ được trả về NULL.
- Cú pháp: 
SELECT table1.col1, table2.col2
FROM table1
FULL JOIN table2
ON table1.sharedCol = table2.sharedCol;
- Ví dụ: Lấy ra dan sách tất cả học sinh và tất cả khóa học, dù học sinh không tham gia khóa học hay khóa học không có học sinh.

5. WITH 
- Công dụng: Dùng để định nghĩa một truy vấn phụ (subquery) tạm thời, giúp cải thiện sự rõ ràng và tối ưu hiệu năng khi làm việc với truy vấn phức tạp.
- Cú pháp: 
WITH Ten_alias AS (
    SELECT col FROM table WHERE condition
)

SELECT * FROM Ten_alias;

- Ví dụ: Lấy ra tất cả học sinh có điểm 'A'

WITH HighGrades AS (
    SELECT name, grade
    FROM Students
    WHERE grade = 'A'
)

SELECT * FROM HighGrades;