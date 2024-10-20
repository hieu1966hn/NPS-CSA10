Buổi 6: Cài đặt, Truy vấn và hàm trong SQL
1. Cài đặt mySQL
2. Cài đặt SQL Workbench (Done).


Syntax chi tiết

SELECT
- Công dụng: Dùng để chọn và truy xuất dữ liệu từ bảng
- Cú pháp: SELECT ten_cot1, ten_cot2, ..
Chú ý: nếu chọn tất cả các cột thì sử dụng dấu *

FROM
- Công dụng: Chỉ định bảng chứa dữ liệu cần truy vấn
- Cú pháp: FROM ten_bảng

WHERE
- Công dụng: Dùng để lọc dữ liệu theo điều kiện cụ thể
- Cú pháp: WHERE ten_cot "=, <, >, ..." value

DISTINCT
- Công dụng: Loại bỏ các giá trị trùng lặp trong kết quả truy vấn
- Cú pháp: SELECT DISTINCT ten_cot FROM ten_bảng

AS
- Công dụng: Đặt tên mới (bí danh) cho cột hoặc bảng để hiểu hơn
- Cú pháp: Đặt tên cột Name là StudentName
SELECT Name AS StudentName, Age FROM Students; 

LIKE 
- Công dụng: Tìm kiếm dữ liệu khớp với mẫu ký tự
- Cú pháp: Tìm loại hoa có tên bắt đầu bằng chữ "R"
SELECT * FROM Flowers_table WHERE Name LIKE "R%";


BETWEEN
- Công dụng: Lọc dữ liệu trong một khoảng giá trị nhất đinh.
- Ví dụ: Lấy tất cả hoa có giá từ 20 - 25$
SELECT * FROM Flowers_table WHERE Price BETWEEN 20 AND 25;

ORDER BY
- Công dụng: Sắp xếp kết quả truy vấn theo cột cụ thể
- Ví dụ: Sắp xếp danh sách các loại hoa có giá tiền tăng dần.
SELECT * FROM Flowers_table ORDER BY Price ASC/DESC;

LIMIT
- Công dụng: Giới hạn số lượng kết quả trả về
- Ví dụ: Lấy ra 3 hoa đầu tiên trong bảng Flowers_table
SELECT * FROM Flowers_table LIMIT 3;

AND
- Công dụng: Điều kiện đồng thời (hoạt động giống and của Python)



Bài tập thực hành: 
Đề bài thực hành:

Sử dụng câu lệnh SELECT, liệt kê tất cả tên học sinh và thành phố của họ.
Sử dụng WHERE để lọc danh sách học sinh có điểm Grade là "A".
Sử dụng DISTINCT để liệt kê các giá trị khác nhau trong cột Grade.
Sử dụng LIKE để tìm học sinh có tên chứa từ khóa "Lee".
Sử dụng ORDER BY để sắp xếp danh sách học sinh theo tên.
Sử dụng BETWEEN AND để tìm các học sinh có độ tuổi từ 14 - 16


Bài nâng cao: Bài 1: Truy vấn nâng cao với WHERE, BETWEEN, LIKE và ORDER BY

Lấy tên tất cả học sinh có tuổi từ 15 - 17 và sống ở thành phố "Chicago"
Tìm kiếm học sinh có tên chứa chữ "a" (khong phân biệt hoa thường) và sắp xếp theo Grade giảm dần
Liệt kê danh sách học sinh có điểm Grade là "B" hoặc "C", sắp xếp theo tuổi giảm dần.
Sử dụng LIMIT đẻ chỉ hiển thị 2 học sinh có tuổi nhỏ nhất.
Bài 2: (về nhà làm)