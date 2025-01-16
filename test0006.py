c = int(input('輸入 1(公分) 或 2(英吋): '))
length = int(input('輸入長度數值: '))

print('|cm   |m    |ich  |foot |yd   |')
print('|-----|-----|-----|-----|-----|')

if c == 1:
    print('|', end = '')
    print(f'{str(length):<5.5s}', end='|')
    print(f'{str(length*0.01):<5.5s}', end='|')
    print(f'{str(length*0.394):<5.5s}', end='|')
    print(f'{str(length*0.03281):<5.5s}', end='|')
    print(f'{str(length*0.01094):<5.5s}', end='|')
else:
    print('|', end='')
    print(f'{str(length*2.54):<5.5s}', end='|')
    print(f'{str(length*0.0254):<5.5s}', end='|')
    print(f'{str(length):<5.5s}', end='|')
    print(f'{str(length/12):<5.5s}', end='|')
    print(f'{str(length/36):<5.5s}', end='|')


# 公分/英吋換算 加上文字格式化

# PS C:\wsPython> python test0006.py
# 輸入 1(公分) 或 2(英吋): 1
# 輸入長度數值: 10
# |cm   |m    |ich  |foot |yd   |
# |-----|-----|-----|-----|-----|
# |10   |0.1  |3.940|0.328|0.109|
# PS C:\wsPython> python test0006.py
# 輸入 1(公分) 或 2(英吋): 2
# 輸入長度數值: 20
# |cm   |m    |ich  |foot |yd   |
# |-----|-----|-----|-----|-----|
# |50.8 |0.508|20   |1.666|0.555|