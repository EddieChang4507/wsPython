# 兩個數字的四則運算
# 
a = input('請輸入兩個數字 ( 格式 a,b )：')  # 新增變數 a，內容是使用者輸入的兩個數字，數字以逗號分隔
b = a.split(',')                  # 新增變數 b，內容使用 split 根據逗號將數字拆開為串列
b1 = int(b[0])                    # 使用 int 將第一個值轉換為「數字」
b2 = int(b[1])                    # 使用 int 將第二個值轉換為「數字」
print(f'{b1} + {b2} = {b1+b2}')   # 印出四則運算的結果
print(f'{b1} - {b2} = {b1-b2}')
print(f'{b1} x {b2} = {b1*b2}')
print(f'{b1} / {b2} = {b1/b2}')

# 加入更多內容
a = input('請輸入兩個數字 ( 格式 a,b )：')
b = a.split(',')
b1 = int(b[0])
b2 = int(b[1])
print(f'{b1} + {b2} = {b1+b2}')
print(f'{b1} - {b2} = {b1-b2}')
print(f'{b1} x {b2} = {b1*b2}')
print(f'{b1} / {b2} = {round(b1/b2,3)}')    # 使用 round 四捨五入到小數點三位
print(f'{b2} + {b1} = {b2+b1}')
print(f'{b2} - {b1} = {b2-b1}')
print(f'{b2} x {b1} = {b2*b1}')
print(f'{b2} / {b1} = {round(b2/b1,3)}')


# 
# PS C:\wsPython> python test0023.py
# 請輸入兩個數字 ( 格式 a,b )：12,23
# 12 + 23 = 35
# 12 - 23 = -11
# 12 x 23 = 276
# 12 / 23 = 0.5217391304347826
# PS C:\wsPython> python test0023.py
# 請輸入兩個數字 ( 格式 a,b )：23  , 85 
# 23 + 85 = 108
# 23 - 85 = -62
# 23 x 85 = 1955
# 23 / 85 = 0.271
# 85 + 23 = 108
# 85 - 23 = 62
# 85 x 23 = 1955
# 85 / 23 = 3.696