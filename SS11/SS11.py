import pandas as pd

### Tạo DF về học sinh lớp CSA10
# data_student_csa10 = [    
#     ['STT', 'Name', 'Age', 'Score', 'Attempts', 'Qualify'],
#     [1, 'Hà Anh', 17, 8, 1, 'yes'],
#     [2, 'Minh Khuê', 17, 9.0, 3, 'no'],
#     [3, 'Lê Anh', 16, 7.0, 2, 'yes'],
#     [4, 'Quang Anh', 17, 6.0, 3, 'no'],
#     [5, 'Đức Trí', 16, 5.0, 4, 'no'],
# ]

data_student_csa10 = {
    'STT': [1, 2, 3, 4, 5],
    'Name': ['Hà Anh', 'Minh Khuê', 'Lê Anh', 'Quang Anh', 'Đức Trí'],
    'Age': [17, 17, 16, 17, 16],
    'Score': [8, 9, 7.0, 6.5, 4],
    'Attempts': [1, 3, 2, 3 ,4],
    'Qualify': ['yes', 'no', 'yes', 'no', 'no']    
}    
    


### Chuyển data => DF 
df_csa10 = pd.DataFrame(data_student_csa10)
# print(df_csa10['Name']) 

###### Ví dụ với iloc
## Truy xuất 1 dòng (hàng)
# print(df_csa10.iloc[1]) # => 1: vị trí hàng (thường bắt đầu từ hàng số 0)

## Truy xuất 1 cột 
# print(df_csa10.iloc[:, 1]) # => Lấy ra toàn bộ giá trị của cột ở vị trí số 1 "Name"

## Truy xuất 1 ô dữ liệu
# print(df_csa10.iloc[2, 2]) # => dòng 2, cột 2

## Truy xuất nhiều dòng
# print(df_csa10.iloc[1: 3]) # => lấy ra dòng 1 và 2
# print(df_csa10.iloc[[0, 2, 3]]) => lấy ra dòng 0, 2, 3

## Truy xuất nhiều cột
# print(df_csa10.iloc[:, 1:3]) # => lấy ra cột 1 và 2
# print(df_csa10.iloc[:, [0, 2, 3]]) # => lấy ra cột 0, 2, 3

## Truy xuất nhiều dòng và cột
# print(df_csa10.iloc[1:, [0, 1, 2, 3]]) # => Lấy ra hàng và cột số: 0, 1, 2, 3


####### Thực hành bài tập cơ bản
### 1. Tìm các học sinh có score >= 5
rows = df_csa10['Score'] >= 5 
# => rows là một Series chứa các giá trị boolean với True & False 
# lần lượt tương ứng với các dòng thỏa & không thỏa điều kiện.

print(df_csa10[rows])


#### Sử dụng iloc để tìm các học sinh có score >= 5