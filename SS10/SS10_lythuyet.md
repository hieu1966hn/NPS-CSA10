Buổi 10: Truy xuất dữ liệu với Pandas
- Chữa bài Kiểm tra giữa khóa lần II (Done)
- Cài đặt thư viện Pandas 
- Kiểu dữ liệu trong Pandas: dataframe và series

Pandas chỉ có 2 KDL chính: 
1. Series: Một cột (1 chiều)
2. DataFrame: Nhiều cột (2 chiều), tương tự như một dictionary với key là tên cột và value là series.

Giới thiệu các hàm đọc file của Pandas: 
- read_csv(): Đọc dữ liệu từ file CSV
+ Cú pháp:
df = pd.read_csv('ten_file.csv')
print(df.head())

Chú ý: head() để xem trước ít nhất 5 hàng đầu tiên của df

Export Data bằng Pandas
- to_csv():
- Cú pháp: df.to_csv('output_ten.csv', index = False)
Giải thích: tham số index = False sẽ loại bỏ cột chỉ mục khi xuất ra file.

Đề bài thực hành 
1. Tạo một DF chứa thông tin về tên, tuổi, điểm số của từng học viên lớp mình
2. Đọc dữ liệu từ 1 file csv có sẵn
