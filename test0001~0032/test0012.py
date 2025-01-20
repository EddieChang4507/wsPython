import random

# 方法一、串列判斷
a = []
while len(a) < 6:
    b = random.randint(1, 49)
    if b not in a:
        a.append(b)
print(a)

# 方法二、搭配集合 set 
a = set()
while len(a) < 6:
    b = random.randint(1, 49)
    a.add(b)
print(a)


# 方法三、使用 random.sample
a = random.sample(range(1, 50), 6)
# 從包含 1～49 數字的串列中，取出六個不重複的數字變成串列
print(a)



# 大樂透電腦選號
# 
# PS C:\wsPython> python test0012.py
# [47, 27, 28, 23, 36, 5]
# PS C:\wsPython> python test0012.py
# [49, 39, 2, 43, 13, 37]
# PS C:\wsPython> python test0012.py
# [6, 33, 3, 35, 38, 20]
# PS C:\wsPython> python test0012.py
# [36, 49, 15, 26, 41, 6]