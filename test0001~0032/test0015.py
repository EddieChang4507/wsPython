a = 10                                # 要產生的金字塔層數
for i in range(1,a+1):                # 使用 for 迴圈，重複 1～10 ( a+1 ) 的數字
    print(' '*3*(a-i),end='')         # 根據不同的層數，讓第一個數字前方增加指定的空白字元 ( 後方不換行 )
    for j in range(1, i+1):           # 第二層 for 迴圈，重複不同層內的數字
        if j==1:                      # 如果是第一個數字
            print(j, end='')          # 單純印出數字即可 ( 後方不換行 )
        else:                         # 如果是第二個以後的數字
            print(f'{j:>3d}', end='') # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
    for j in range(i-1, 0, -1):       # 剛剛的 for 迴圈是由小到大，加入另外一個由大到小的迴圈
        print(f'{j:>3d}', end='')     # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
    print('')                         # 最後執行換行的 print



a = 10
for i in range(1,a+1):
    print(' '*3*(a-i),end='')
    for j in range(0, i):            # ragne 改成從 0 開始，因為 2 的 0 次方等於 1
        k = 2 ** j                   # 計算 2 的幾次方
        if k==1:
            print(k, end='')
        else:
            print(f'{k:>3d}', end='')
    for j in range(i-2, -1, -1):     # 修改 range，使其最後一位數為 0
        k = 2 ** j                   # 計算 2 的幾次方
        print(f'{k:>3d}', end='')
    print('')
    
    
    
    # 方法二、使用 while 迴圈 
    
a = 10                                # 要產生的金字塔層數
b = 1                                 # 提供 while 迴圈停止的依據
while b<=a:                           # 如果 b <= a 就讓 while 迴圈繼續
    n = 1                             # 設定從 1 開始
    print(' '*3*(a-b),end='')         # 根據不同的層數，讓第一個數字前方增加指定的空白字元 ( 後方不換行 )
    while n<=b:                       # 第二層 while 迴圈，如果 n <= b 就讓 while 迴圈繼續
        if n==1:                      # 如果是第一個數字
            print(n, end='')          # 單純印出數字即可 ( 後方不換行 )
        else:                         # 如果是第二個以後的數字
            print(f'{n:>3d}', end='') # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
        n = n + 1                     # 將 n 增加 1
    while n>2:                        # 剛剛的 while 迴圈是由小到大，加入另外一個由大到小的迴圈
        print(f'{n-2:>3d}', end='')   # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
        n = n - 1                     # 將 n 減少 1
    print('')                         # 最後執行換行的 print
    b = b + 1                         # 將 b 增加 1

# 數字金字塔
# PS C:\wsPython> python test0015.py
#                            1
#                         1  2  1
#                      1  2  3  2  1
#                   1  2  3  4  3  2  1
#                1  2  3  4  5  4  3  2  1
#             1  2  3  4  5  6  5  4  3  2  1
#          1  2  3  4  5  6  7  6  5  4  3  2  1
#       1  2  3  4  5  6  7  8  7  6  5  4  3  2  1
#    1  2  3  4  5  6  7  8  9  8  7  6  5  4  3  2  1
# 1  2  3  4  5  6  7  8  9 10  9  8  7  6  5  4  3  2  1
#                            1
#                         1  2  1
#                      1  2  4  2  1
#                   1  2  4  8  4  2  1
#                1  2  4  8 16  8  4  2  1
#             1  2  4  8 16 32 16  8  4  2  1
#          1  2  4  8 16 32 64 32 16  8  4  2  1
#       1  2  4  8 16 32 64128 64 32 16  8  4  2  1
#    1  2  4  8 16 32 64128256128 64 32 16  8  4  2  1
# 1  2  4  8 16 32 64128256512256128 64 32 16  8  4  2  1
#                            1
#                         1  2  1
#                      1  2  3  2  1
#                   1  2  3  4  3  2  1
#                1  2  3  4  5  4  3  2  1
#             1  2  3  4  5  6  5  4  3  2  1
#          1  2  3  4  5  6  7  6  5  4  3  2  1
#       1  2  3  4  5  6  7  8  7  6  5  4  3  2  1
#    1  2  3  4  5  6  7  8  9  8  7  6  5  4  3  2  1
# 1  2  3  4  5  6  7  8  9 10  9  8  7  6  5  4  3  2  1    