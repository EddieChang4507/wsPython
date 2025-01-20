# 計算多個數字的總和

a = input('請輸入數字 ( 格式 a,b,c... )：')   # 新增變數 a，內容是使用者輸入的多個數字，數字以逗號分隔
b = a.split(',')      # 新增變數 b，內容使用 split 根據逗號將數字拆開為串列
output = 0            # 設定 output 從 0 開始
for i in b:           # 使用 for 迴圈，依序取出 b 串列的每個項目
    output += int(i)  # 將 output 的數值加上每個項目 ( 使用 int 將項目轉換成數字 )

print(f'數字總和為：{output}')

# 使用 while 迴圈不斷計算 

while output!=0:      # 使用 while 迴圈，如果 output 等於 0 才會停止
  a = input('請輸入數字 ( 格式 a,b,c... )：')
  b = a.split(',')
  output = 0
  for i in b:
      output += int(i)
  print(f'數字總和為：{output}')
  
nums = [int(i) for i in input().split(',')]   # 使用串列生成式，將輸入的數字轉換成串列
result = sum(nums)         # 將串列內的數字加總
print(result)              # 印出結果



# PS C:\wsPython> python test0025.py
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,
# 請輸入數列產生幾個數: 30
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,
