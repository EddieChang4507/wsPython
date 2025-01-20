
import calendar       # import calendar 模組

import datetime                                   # import datetime 標準函式
today = datetime.date.today()                     # 使用 datetime.date 取得今天的日期
age = input('輸入生日 ( YYYY/MM/DD )：')            # 讓使用者輸入生日，格式為 YYYY/MM/DD
age_list = age.split('/')                         # 將使用者輸入的日期，使用「/」拆成串列
year = today.year - int(age_list[0])              # 用今天的年份，減去使用者的生日年份 ( 年份差 )
month = today.month - int(age_list[1])            # 用今天的月份，減去使用者生日的月份 ( 月份差 )
if month<0:                                       # 如果月份差的數字小於零，表示生日還沒到
    year = year - 1                               # 將年份差減少 1 ( 表示跨了一年 )
    month = 12 + month                            # 將月份差改成 12 + 月份差
day_list = [31,28,31,30,31,30,31,31,30,31,30,31]  # 建立一個每個月有多少天的串列
day = today.day - int(age_list[2])                # 用今天的日期，點去使用者生日的日期 ( 月份差 )
if day<0:                                         # 如果月份差的數字小於 0，表示生日還沒到
    month = month - 1                             # 將月份差減少 1
    if month<0:                                   # 如果月份差減少後小於 0
        year = year - 1                           # 再將年份差減少 1 ( 表示跨了一年 )
        month = 12 + month                        # 將月份差改成 12 + 月份差
    day = day_list[month] + day       # 將日期差改成該月的天數 + 日期差

print(f'{year} 歲 {month} 個月 {day} 天')    # 印出現在幾歲幾個月又幾天

today = datetime.date.today()
age = input('輸入生日 ( YYYY/MM/DD )：')
age_list = age.split('/')
year = today.year - int(age_list[0])
month = today.month - int(age_list[1])
if month<0:
    year = year - 1
    month = 12 + month
day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
if calendar.isleap(today.year):         # 判斷如果是閏年
    day_list[1] = 29                    # 就將二月份的天數改成 29 天
day = today.day - int(age_list[2])
if day<0:
    month = month - 1
    if month<0:
        year = year - 1
        month = 12 + month
    day = day_list[month] + day

print(f'{year} 歲 {month} 個月 {day} 天')

# 計算年紀 ( 幾歲幾個月幾天 )
# 加入閏年的判斷 
# 
# 日期輸入錯誤的狀況無檢核