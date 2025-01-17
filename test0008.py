year = int(input('請輸入年份: '))

text = '平年'
if year%4 == 0:
    text = '閏年'
if year%100 == 0:
    text = '平年'
if year%400 == 0:
    text = '閏年'
print(f'{year} 是 {text}')




# 判斷平年與閏年2
# 編輯程式 ( 非巢狀判斷 ) 
# 
# PS C:\wsPython> python test0007.py
# 請輸入年份: 2023
# 2023 是平年
# PS C:\wsPython> python test0007.py
# 請輸入年份: 2024
# 2024 是閏年
# PS C:\wsPython> python test0007.py
# 請輸入年份: 2100
# 2100 是平年
# PS C:\wsPython> python test0007.py
# 請輸入年份: 2400
# 2400 是閏年