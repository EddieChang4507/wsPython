nums = [int(i) for i in input().split(',')]   # 使用生成式將輸入的數字變成串列
nums.sort()                         # 由小到大排序
result = nums[0]                    # 取出最小的項目當作預設的最大公因數
while result!=1:                    # 如果 result 不為 1，就不斷執行迴圈內容
    for i in range(1,len(nums)):    # 使用 for 迴圈，依序將串列元素取出執行
        r = nums[i]%result          # 取得相除後的餘數
        if r !=0:                   # 如果相除後餘數不為 0
            nums.insert(0, r)       # 將餘數插入為串列的第一個項目
            break                   # 只要遇到餘數不為 0 就跳出迴圈
    if result != nums[0]:           # 如果 result 不等於串列第一個項目 ( 餘數 )
        result = nums[0]            # 將 result 改為第一個項目 ( 餘數 )，然後重新執行 while 迴圈
    else:
        break                       # 如果相等，表示沒有餘數，得到最大公因數
print(result)