# class Point:
#     ## Viết hàm khởi tạo thuộc tính
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     ### Viết phương thức với điểm
#     def add(self, point):
#         return Point(self.x + point.x, self.y + point.y)
    
#     def sub(self, point):
#         return Point(self.x - point.x, self.y - point.y)
    

    
#     ## Phương thức hiển thị (Cách viết điểm dạng chữ):
#     #### Phương thức này giúp định dạng đầu ra khi in một đối tượng point
#     def __str__(self):
#         ### Khi gọi hàm print(point1), phương thức này sẽ được tự động gọi ra để hiển thị theo định dạng
#         return f'({self.x},{self.y})'



# ### Ví dụ
# point1 = Point(2, 0)
# point2 = Point(0, 1)

# ### Cộng 2 điểm trên
# print("Cộng 2 điểm point1 và point2", point1.add(point2))

# ### Trừ 2 điểm trên
# print("Trừ 2 điểm point1 và point2", point1.sub(point2))

# ### 