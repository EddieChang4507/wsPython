import random
# a = random.randint(1,99)                         # 產生 1～99 的隨機整數
# b = int(input('輸入 1～99 的數字：'))               # 讓使用者輸入數字，使用 int 轉換成數字
# while a!=b:                                      # 使用 while 迴圈，如果 a 不等於 b，就不斷繼續
#     if b < a:
#         b = int(input('數字太小囉！再試一次吧：'))   # 如果 b<a，提示數字太小
#     elif b > a:
#         b = int(input('數字太大囉！再試一次吧：'))   # 如果 b>a，提示數字太大
# print('答對囉！')                                 # 如果 b=a 會停止 while 迴圈，顯示正確答案


a = random.randint(1,99)
b = int(input('輸入 1～99 的數字：'))
while True:
    if b < a:
        b = int(input('數字太小囉！再試一次吧：'))
    elif b > a:
        b = int(input('數字太大囉！再試一次吧：'))
    else:
        print('答對囉！')
        break;




# 猜數字 ( 猜大猜小 )
# 
# 使用 break 停止 while 迴圈 
# 
# PS C:\wsPython> python test0016.py
# 輸入 1～99 的數字：50
# 數字太大囉！再試一次吧：20
# 數字太小囉！再試一次吧：40
# 數字太小囉！再試一次吧：45
# 數字太大囉！再試一次吧：42
# 數字太小囉！再試一次吧：44
# 答對囉！
# PS C:\wsPython> python test0016.py
# 輸入 1～99 的數字：40
# 數字太小囉！再試一次吧：80
# 數字太大囉！再試一次吧：60
# 數字太小囉！再試一次吧：70
# 數字太大囉！再試一次吧：65
# 數字太小囉！再試一次吧：68
# 數字太小囉！再試一次吧：69
# 答對囉！
