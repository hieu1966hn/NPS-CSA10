Buổi 7: Truy vấn & các hàm trong SQL (phần 2)
- C, U, D


C: Create

CREATE DATABASE ten_database; Tạo cơ sở dữ liệu (DB)

USE ten_database; chọn CSDL để sử dụng

CREATE TABLE ten_bang (...); Tạo bảng mới trong cơ sở dữ liệu
 
INSERT INTO ten_bang (cot1, cot2, ..) VALUES (gia_tri1, gia_tri2, ...); Thêm dữ liệu vào bảng


/////////////
R: Read 
SELECT cot1, cot2, ... (*) FROM ten_bang; Để lấy dữ liệu từ bảng


/////////////
U: Update

UPDATE ten_bang SET cot1 = gia_tri_moi WHERE dieu_kien ; Cập nhật dữ liệu trong bảng

/////////////
D: Delete
DELETE FROM ten_bang WHERE dieu_kien;

////////////: Cú pháp Thêm
ALTER TABLE ten_bang ADD cot_moi kieu_du_lieu; Thêm cột vào bảng 

ALTER TABLE ten_bang DROP COLUMN ten_cot; Xóa cột khỏi bảng

DROP TABLE ten_bang; Xóa bảng

DROP DATABASE ten_database; Xóa cơ sở dữ liệu (DB)



; 