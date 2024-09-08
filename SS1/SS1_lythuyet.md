Khóa học CSA:
- Lập trình hướng đối tượng (OOP)
- Xử lý, hệ thống dữ liệu SQL, Pandas

Buổi 1: Giới thiệu về lập trình hướng đối tượng
- Lập trình hướng đối tượng OOP(): Tạo ra các đối tượng và trừu tượng hóa chúng
- Ý bổ sung: Cách tiếp cận lập trình dựa trên việc sử dụng "đối tượng" và "lớp" để tổ chức và quản lý mã nguồn => Giúp dễ dàng quản lý các chương trình phức tạp bằng cách chia thành các đối tượng có thuộc tính và hành vi riêng.

- Lớp (class): Là bản thiết kế đối tượng, định nghĩa các thuộc tính (dữ liệu) và phương thức (hành vi) của đối tượng.

- Đối tượng (Object/ Dictionary): Là một thực thể cụ thể của lớp (class). Đối tượng được tạo ra từ lớp và có thể có dữ liệu và hành vi riêng.

- Thuộc tính (Attributes): là các biến được lưu trữ trong đối tượng. Mối đối tượng sẽ có các thuộc tính riêng được định nghĩa trong class.

- Phương thức (Methods): Là các hàm được định nghĩa bên trong lớp(class), mô tả các hành vi của đối tượng.


### Khởi tạo một bản thiết kế con người.



Bài tập thực hành: 
Bài luyện tập 1: Viết class  có tên Counter(), gồm 1 thuộc tính là count và 2 phương thức tick() và reset().
Yêu cầu: 
- Hàm khởi tạo cho count bằng 0
- phương thức tick() tăng count 1 đơn vị
- phương thức reset() cho count về 0


Bài luyện tập số 2: 
Yêu cầu: Tạo 1 Car với các thuộc tính như model, color, year và phương thức display_info() để in ra thông tin của xe. Sau đó tạo một vài đối tượng của lớp Car và gọi phương thức display_info().


Bài luyện tập số 3: Quản lý học viên
Yêu cầu: 
- Tạo 1 lớp Student với các thuộc tính như: name, student_id, grades (danh sách điểm số).
- Thêm phương thức calculate_average() để tính trung bình điểm 
- Thêm phương thức add_grade() để thêm điểm mới vào danh sách điểm số.