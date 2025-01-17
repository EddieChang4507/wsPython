text = input('請輸入一串英文或數字: ')
repeat = []
not_repeat = []

for i in text: # 逐一字元判斷
    a = text.count(i, 0, len(text)) # 判斷字元在字串中出現的次數
    if a > 1 and i not in repeat: # 此為重複字元，且尚未紀錄
        repeat.append(i)
    if a == 1 and i not in not_repeat: # 此為非重複字元，且尚未紀錄
        not_repeat.append(i)

print(f'重複字元 : {repeat}')
print(f'非重複字元 : {not_repeat}')



# 找出不重複字元
# 
# 判斷每個字元在字串中出現的次數
# 出現的次數大於 1 表示有重複
# 出現次數等於 1 表示沒有重複
# PS C:\wsPython> python test0009.py
# 請輸入一串英文或數字: dsadisaoi4325
# 重複字元 : ['d', 's', 'a', 'i']
# 非重複字元 : ['o', '4', '3', '2', '5']
# PS C:\wsPython> python test0009.py
# 請輸入一串英文或數字: hello world
# 重複字元 : ['l', 'o']
# 非重複字元 : ['h', 'e', ' ', 'w', 'r', 'd']
# PS C:\wsPython> 