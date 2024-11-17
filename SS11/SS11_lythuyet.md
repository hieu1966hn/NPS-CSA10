Buổi 11: Truy xuất và xử lý dữ liệu với thư viện Pandas
- Ôn tập kiến thức
+ KDL: Series (list), DataFrame (dictionary: mỗi giá trị trong key là 1 series)
+ read_csv(): Đọc dữ liệu từ file csv
+ to_csv(): Xuất dữ liệu ra file csv
+ dtypes: Trả về kiểu dữ liệu của từng cột
+ head()/tail(): Trả về 5 hàng đầu tiên/ cuối cùng
+ info(): Tổng hợp thông tin về DF và các cột

- Truy xuất dòng và cột từ DF (Cách thông thường)
+ Truy xuất 1 cột: df['Name'] || df.Name
+ Truy xuất nhiều cột: df[['Name', 'Age']]
+ Truy xuất 1 hàng: df[1:2]
+ Truy xuất nhiều hàng: df[1:4] || df[1:]

Chú ý: 
- Nếu truy vấn là một dòng/ một cột thì kết quả trả về là một: Series
- Nếu truy vấn bao gồm nhiều hơn một dòng/ một cột thì kết quả là một: DataFrame

***** Cú pháp truy vấn LOC và ILOC
- DF hỗ trợ thuộc tính loc & iloc để truy xuất dòng và cột. Cú pháp:
df.loc[<danh_sach_dong>, <danh_sach_cot>]
df.iloc[<danh_sach_dong>, <danh_sach_cot>]
- Trong đó: ds_dong và ds_cot có thể là:
+ một dòng/cột
+ một list các dòng/cột
+ cú pháp list slicing: [<bắt đầu>:<kết thúc>]



