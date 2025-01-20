
# 列出字母對應的數字
import random


local_table = {
    'A': 1, 'B': 0, 'C': 9, 'D': 8, 'E': 7, 'F': 6, 'G': 5, 'H': 4, 'I': 9,
    'J': 3, 'K': 2, 'L': 2, 'M': 1, 'N': 0, 'O': 8, 'P': 9, 'Q': 8, 'R': 7,
    'S': 6, 'T': 5, 'U': 4, 'V': 3, 'W': 1, 'X': 3, 'Y': 2, 'Z': 0
}

for i in range(10):
        local = random.choice(list(local_table.keys())) # 取得隨機字母
        sex = random.randint(1,2)                       # 性別
        total = local_table[local]+sex*8                # 先將前兩個數字換算成的數字加總
        result = f'{local}{sex}'                        # 結果使用 f-string 來組合字串

        for i in range(1,8):
                num = random.randint(0,9)                   # 重複八次每次都取出 0~9 隨機數字
                total = total + num*(8-i)                   # 根據公式計算數值並加總到 total
                result = f'{result}{num}'                   # 結果使用 f-string 來組合字串

        num10 = 10 - total%10                 # 最後一碼根據總值除以十是否整除來決定，如果不能整除，就是 10-餘數
        if num10 == 10 : num10 = 0            # 如果能整除，最後一碼就是 0
        result = f'{result}{num10}'           # 結果使用 f-string 來組合字串
        print(result)                         # 印出結果


local_table = {
    'A': 1, 'B': 0, 'C': 9, 'D': 8, 'E': 7, 'F': 6, 'G': 5, 'H': 4, 'I': 9,
    'J': 3, 'K': 2, 'L': 2, 'M': 1, 'N': 0, 'O': 8, 'P': 9, 'Q': 8, 'R': 7,
    'S': 6, 'T': 5, 'U': 4, 'V': 3, 'W': 1, 'X': 3, 'Y': 2, 'Z': 0
}

# 使用 for 迴圈
for i in range(20):
        local = random.choice(list(local_table.keys()))
        sex = random.randint(1,2)
        total = local_table[local]+sex*8
        result = f'{local}{sex}'

        for i in range(1,8):
                num = random.randint(0,9)
                total = total + num*(8-i)
                result = f'{result}{num}'

        num10 = 10 - total%10
        if num10 == 10 : num10 = 0
        result = f'{result}{num10}'
        print(result)
            

# 產生身分證字號 ( 隨機 )
# 身分證字號編碼規則
# 
# 第 2 碼：性別代碼，1 表示男生，2 表示女生。
# 第 3 碼～第 10 碼：八個 0～9 數字組成的流水號。