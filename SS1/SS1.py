# ### Khởi tạo một bản thiết kế con người.
# class Human:
#     ## Khởi tạo thuộc tính cơ bản cho con người
#     def __init__(self, name, age):
#         ## Gán giá trị cho thuộc tính của Human
#         self.name = name
#         self.age = age
    
#     ### Khởi tạo hành vi (phương thức)
#     def move(self):
#         print(f"{self.name} can move with 2 leg on the ground")
    
#     def greet(self):
#         print(f'Hello, my name is {self.name} and I am {self.age} years old')


# ### Khai báo 1 biến (đối tượng) là thực thể của lớp Human
# Hieu = Human("Nguyễn Trung Hiếu", 30)

# print(Hieu.name) ###
# print(Hieu.age) ###

# Hieu.move()
# Hieu.greet()



### Chữa bài luyện tập 1
# class Counter:
#     def __init__(self):
#         self.count = 0

#     def tick(self):
#         self.count += 1
#         # self.count = self.count + 1

#     def reset(self):
#         self.count = 0

# counter1 = Counter()
# counter1.tick()
# counter1.tick()
# counter1.tick()
# print(counter1.count) #### Ouput: 3
# counter1.reset()
# print(counter1.count) #### Ouput: 0


### Chữa bài luyện tập số 2
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
    
#     def display_info(self):
#         print(f'Model: {self.model} , Color: {self.color}, Year: {self.year}')

        
# car1 = Car("Toyota Camry", "White", 2020)
# car2 = Car("Honda Civic", "Black", 2019)

# ### Gọi hàm hiển thị thông tin xe
# car1.display_info()
# car2.display_info()

### Chữa bài luyện tập số 3
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade): 
        self.grades.append(grade)
    
    def calculate_average(self):
        if len(self.grades) == 0:
            return 0 
        return sum(self.grades)/len(self.grades)

### Tạo đối tượng học viên và thêm điểm
student1 = Student("Nguyễn Trung Hiếu", "$123456")
student1.add_grade(8)
student1.add_grade(7)
student1.add_grade(9)

print(f"Average grade for {student1.name}: {student1.calculate_average()}")

        
