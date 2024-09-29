### Bài tập phân số
class PhanSo:
    ## Hàm khởi tạo
    def __init__(self, tuso, mauso):
        self.tuso = tuso
        self.mauso = mauso
    
    ##### Phương thức đi kèm với Phanso

    ## Hàm hiển thị phân số ra ngoài màn hình terminal => Hàm này sẽ được tự động gọi ra để hiển thị trên terminal
    def __str__(self):
        return f'{self.tuso}/{self.mauso}' ### 3/2

    ##### Rút gọn phân số => Phải tìm được UCLN của 2 số a và b
    ## Hàm tìm UCLN
    def find_UCLN(self, a, b):
        ucln = 1
        smaller = min(abs(a), abs(b))
        for i in range(1, smaller + 1):
            if a % i == 0 and b % i == 0:
                ucln = i
        return ucln

    def rutGonPhanSo(self):
        ucln  = self.find_UCLN(self.tuso, self.mauso)
        self.tuso = self.tuso // ucln ## // Chia lấy phần nguyên
        self.mauso = self.mauso // ucln
        return PhanSo(self.tuso, self.mauso)





    ## Cộng 2 phân số 
    def add(self, other):
        new_tuso = self.tuso * other.mauso + other.tuso * self.mauso
        new_mauso = self.mauso * other.mauso
        result = PhanSo(new_tuso, new_mauso)
        return result

    ## Trừ 2 phân số 
    def subtract(self, other):
        new_tuso = self.tuso * other.mauso - other.tuso * self.mauso
        new_mauso = self.mauso * other.mauso
        result = PhanSo(new_tuso, new_mauso)
        return result

    ## Nhân 2 phân số 
    def multiply(self, other):
        new_tuso = self.tuso * other.tuso 
        new_mauso = self.mauso * other.mauso
        result = PhanSo(new_tuso, new_mauso)
        return result
    
    ## Chia 2 phân số 
    def divide(self, other):
        new_tuso = self.tuso * other.mauso 
        new_mauso = self.mauso * other.tuso
        result = PhanSo(new_tuso, new_mauso)
        return result

### Khởi tạo 2 đối tượng Phân số mới gồm:
phanso1 = PhanSo(1, 2)
phanso2 = PhanSo(4, 8)

#### Cộng 2 phân số
print(f'Cộng 2 phân số: {phanso1.add(phanso2).rutGonPhanSo()}') ### Output: ...