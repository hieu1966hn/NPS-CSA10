# Nhúng thư viện Pandas
import pandas as pd ## Viết tắt lại để dễ dùng hơn

## Ví dụ một series trong Pandas
csa10 = [
    ['STT', 'Name', 'Age'],
    [1, 'Hà Anh', 17],
    [2, 'Minh Khuê', 17],
]

### VD Series là cấu trúc một chiều
# STT = pd.Series([1,2])
# print(STT)

### 1. 
df_Students = pd.DataFrame(csa10)
## Hiển thị DF
print(df_Students)