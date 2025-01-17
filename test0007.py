year = int(input('請輸入年份: '))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(f'{year} 是閏年')
        else:
            print(f'{year} 是平年')
    else:
        print(f'{year} 是閏年')
else:
    print(f'{year} 是平年')
            



# 判斷平年與閏年
# 
# 公元年份非4的倍數，為365天平年。
# 公元年份為4的倍數但非100的倍數，為366天閏年。
# 公元年份為100的倍數但非400的倍數（1700年、1800年及1900年）為平年。
# 公元年份為400的倍數（1600年及2000年）為閏年。
# 
# PS C:\wsPython> python test0007.py
# 請輸入年份: 1000
# 1000 是平年
# PS C:\wsPython> python test0007.py
# 請輸入年份: 2024
# 2024 是閏年
# PS C:\wsPython> python test0007.py
# 請輸入年份: 2023
# 2023 是平年
# PS C:\wsPython> python test0007.py
# 請輸入年份: 2300
# 2300 是平年