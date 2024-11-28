### Sử dụng thư viện Matplotlib
import matplotlib as plt
import matplotlib.pyplot as plt 

### Ví dụ với biểu đồ đường
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# plt.plot(x, y, label='Dữ liệu mẫu')
# plt.xlabel('Thời gian')
# plt.ylabel('Giá trị')
# plt.title("Biểu đồ tăng trưởng")

# plt.show()


### Ví dụ với Figure
# plt.figure(figsize=(10,5))
# plt.plot([1,2,3], [4,5,6])
# plt.show()

### Biểu đồ histtogram: Biểu diễn tần suất dữ liệu
# data = [1,2,2,3,3,3,4,4,4,4] ## Tập dữ liệu
# plt.hist(data, bins=10) ## bins=4 chia thành 4 cột dựa trên tần suất của các giá trị từ 1 đến 4
# plt.show()

### Biểu đồ tròn pie
# sizes = [20, 30, 25, 25]
# labelNames = ['Trí', 'Khuê', 'Lê Anh', 'Quang Anh']
# plt.pie(sizes, labels=labelNames)
# # plt.show()

# ### Xuất biểu đồ dưới dạng hình ảnh
# plt.savefig('./SS12/bieudohinhtron.jpg')




###### Chữa bài thực hành 1
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 
# temperatures = [25, 27, 26, 28, 29, 30, 31]

# plt.plot(days, temperatures, label="Nhiệt độ trung bình trong tuần")
# plt.xlabel('Ngày')
# plt.ylabel('Nhiệt độ')
# plt.legend("T")
# plt.show()


###### Chữa bài thực hành 2:
subjects = ["Math", "Science", "History", "Art", "PE"] 
students = [15, 20, 10, 5, 25]

### Vẽ biểu đồ cột
# plt.figure(figsize=(10,5))
# plt.bar(subjects, students, color='green')
# plt.xlabel('Môn học')
# plt.ylabel('Số lượng học sinh')
# plt.title("Số lượng học sinh thích các môn học")
# plt.show()

### Vẽ biểu đồ tròn
plt.figure(figsize=(10,10))
plt.pie(students, labels=subjects, autopct="%1.1f%%", startangle=90)
plt.title("Số lượng học sinh thích các môn học")
plt.show()