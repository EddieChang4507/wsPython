# 快速找出質數
# 


a = range(2, 1000)        # 產生 2～100 的串列
p = 0                    # 設定 p 從 0 開始 ( 從 a[p] 也就是第一個項目開始 )
def g():                 # 定義一個函式 g
    global p, a            # 設定 p 和 a 是全域變數
    if p<len(a):           # 如果 p 小於 a 的長度 ( 依序取值到 a 的最後一個項目 )
        a = [i for i in a if i==a[p] or i%a[p]>0]  # 重新設定 a 為移除倍數後的串列
        p = p + 1            # p 增加 1
        g()                  # 重新執行函式 g
g()                      # 執行函式 g
print(*a)                # 印出 a ( 使用 * 將串列打散印出 )


def gg(max):                   # 定義一個 gg 函式
    s = set()                    # 設定一個空集合
    for n in range(2,max):       # 從 range(2, max) 當中開始依序找質數
        if all(n%i>0 for i in s):  # 判斷如果 i 已經存在於集合，且除以集合中的值會有餘數 ( 整除表示非質數 )
            s.add(n)                 # 將該數字加入集合 ( 表示質數 )
            yield n                  # 使用 yield 記錄狀態
print(*gg(10000))                # 印出結果