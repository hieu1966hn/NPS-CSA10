-- Xử lý các thao tác với CSDL tại đây
USE NPS_CSA10;

-- Đọc toàn bộ dữ liệu trong bảng Student
-- SELECT * FROM Students;

-- 1. Cập nhật độ tuổi học sinh có ID = 1 thành 28 tuổi
-- UPDATE Students SET Age = 28 WHERE studentId = 1;
-- SELECT * FROM Students;

-- 2. Xóa học sinh có tên 'Lê Anh'
-- DELETE FROM Students WHERE Name = 'Lê Anh';


-- 3. Thêm cột email vào bảng Students
-- ALTER TABLE Students ADD Email VARCHAR(100);


-- 4. Xóa cột email khỏi bảng Students
-- ALTER TABLE Students DROP COLUMN Email;
-- SELECT * FROM Students;

-- 5. Xóa bảng Students
-- DROP TABLE Students;
-- 6. Xóa cơ sở dữ liệu NPS_CSA10
-- DROP DATABASE NPS_CSA10;
