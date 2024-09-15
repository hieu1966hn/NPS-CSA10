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



#### Bài thực hành với kế thừa:
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
    
#     def make_sound(self):
#         return f'{self.name} makes a sound'
        
### Tạo ra một bản thiết kế cừu từ Animal
# class Sheep(Animal):
#     def __init__(self, name, species, breed):
#         ## Gọi làm hàm khởi tạo của lớp cha và kế thừa chúng: super()
#         super().__init__(name, species)
#         self.breed = breed

#     ### Mặc định có phương thức make_sound(). tuy nhiên muốn bổ sung thêm 
#     def make_sound(self):
#         ## Sử dụng phương thức kế thừa super().phương_thức muốn kế thừa
#         return super().make_sound() + f". {self.name} Beeee"
    
### Tạo ra một bản thiết kế chó từ Animal
# class Dog(Animal):
#     def __init__(self, name, species, breed):
#         ## Gọi làm hàm khởi tạo của lớp cha và kế thừa chúng: super()
#         super().__init__(name, species)
#         self.breed = breed

#     ### Mặc định có phương thức make_sound(). tuy nhiên muốn bổ sung thêm 
#     def make_sound(self):
#         ## Sử dụng phương thức kế thừa super().phương_thức muốn kế thừa
#         return super().make_sound() + f". {self.name} Barks"




### Tạo một đối tượng cừu: 
# sheep1 = Sheep("Blue", "Sheep", "Cừu Beltex")
# print(sheep1.make_sound())

# ### Tạo một đối tượng chó: 
# dog1 = Dog("mic", "Dog", "Béc giê")
# print(dog1.make_sound())



######### Kế thừa nhiều lớp
# class Bird:
#     def __init__(self, name):
#         self.name = name
    
#     def eat(self):
#         return f'{self.name} is eating'


# class Flyer:
#     def __init__(self, wing_span):
#         self.wing_span = wing_span
    
#     def fly(self):
#         return f"fly with a wingspan of {self.wing_span} meters"

# class FlyingBird(Bird, Flyer):
#     def __init__(self, name, wing_span):
#         ### Gọi hàm khởi tạo của cả 2 lớp
#         Bird.__init__(self, name)
#         Flyer.__init__(self, wing_span)

#     def show_info(self):
#         return f'{self.name} can ' + Flyer.fly(self)



# ### sử dụng lớp FlyingBird
# eagle = FlyingBird("Eagle", 2.5)

# print(eagle.eat())
# print(eagle.fly())
# print(eagle.show_info())


### chữa bài luyện tập số 1
class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    
    def area(self):
        return self.lenght * self.width
    
    def perimeter(self):
        return (self.lenght + self.width) * 2
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    
### test hình vuông
s = Square(5)
print(s.area())
print(s.perimeter())