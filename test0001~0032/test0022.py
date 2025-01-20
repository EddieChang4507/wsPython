# table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}  # 轉換對照表
# roman = [i for i in input()]             # 將輸入的羅馬數字變成串列
# r = roman[::-1]                          # 反轉串列
# output = table[r[0]]                     # 讓 output 先等於第一個數字
# for i in range(1, len(r)):               # 從第二個數字開始依序取到最後一個數字
#     if table[r[i]] < table[r[i-1]]:      # 如果後面數字比較小
#         output = output - table[r[i]]    # 讓 output 減去後面的數字
#     else:
#         output = output + table[r[i]]    # 如果後面數字比較大，讓 output 加上後面的數字
# print(output)


num_table = [
    [1000,'M'],
    [900,'CM'],
    [500,'D'],
    [400,'CD'],
    [100,'C'],
    [90,'XC'],
    [50,'L'],
    [40,'XL'],
    [10,'X'],
    [9,'IX'],
    [5,'V'],
    [4,'IV'],
    [1,'I']]                          # 建立對照表
num = int(input())                    # 將輸入的文字轉換成數字
output = ''                           # 設定輸出的 output 字串
for i in num_table:                   # 依序判斷對照表中每個數字
    a = divmod(num, i[0])             # 取得商 ( a[0] ) 和餘數 ( a[1] )
    if a[0]!=0:                       # 如果 a[0] 不為 0
        num = a[1]                    # 取得餘數繼續往下除
        output = output + i[1]*a[0]   # 組合字串
print(output)


# 羅馬數字轉換
