import time


n = 10
for i in range(n + 1):
    print(f'\r倒數 {n-i} 秒', end = '')
    time.sleep(1)
print('') # 換行
print('\r時間到')

n = 20                   # 設定進度條總長
for i in range(n+1):
    print(f'\r[{"█"*i}{" "*(n-i)}] {i*100/n}%', end='')   # 輸出不換行的內容
    time.sleep(0.2)
    
print('') # 換行

n = 100
icon = '⋮⋰⋯⋱'          # 建立旋轉的符號清單
for i in range(n+1):
    print(f'\r{icon[i%4]} {i*100/n}%', end='')
    time.sleep(0.1)

print('') # 換行


# 下載進度條
# 
# 在 Python 可以透過 print 印出結果，如果在印出的文字前方加上
# 「\r」的命令，每次印出時會將游標移動到最前方，
# 搭配 end 不換行的設定，就能做出類似「畫面更新」的效果，
# 下面的程式執行後，畫面上會顯示倒數秒數。
# 
# PS C:\wsPython> python test0013.py
# 倒數 0 秒
# 時間到
# [████████████████████] 100.0%
# ⋮ 100.0%