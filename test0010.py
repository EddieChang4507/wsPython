import math


text = input('輸入文字: ')
length = len(text)
center = math.floor(length/2)

if length%2 == 0:
    print(f'{text[center - 1 : center + 1]}') #取出中間兩個字元
else:
    print(f'{text[center]}')




# 找出中間的字元
# 
# PS C:\wsPython> python test0010.py
# 輸入文字: asd
# s
# PS C:\wsPython> python test0010.py
# 輸入文字: asdf
# sd