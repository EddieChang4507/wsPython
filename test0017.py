import datetime
import time

now = datetime.datetime.now().strftime('%H:%M:%S')
print(now)


while True:
    now = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'\r{now}', end = '')     # 前方加上 \r
    time.sleep(1)

def timezone(h):
    GMT = datetime.timezone(datetime.timedelta(hours=h))       # 取得時區
    return datetime.datetime.now(tz=GMT).strftime('%H:%M:%S')  # 回傳該時區的時間

# 六個時區的名稱與時差
local = {'倫敦':1,
        '台灣':8,
        '日本':9,
        '紐約':-4,
        '洛杉磯':-7,
        '紐西蘭':12 }

while True:
    print('\r',end='')   # 開始時將游標移到開頭
    # 讀取 local 的 key
    for i in local:
        now = timezone(local[i])   # 根據 key 的 value 取得時間
        print(f'{i}>{timezone(local[i])}  ', end='')
    time.sleep(1)

# 簡單時鐘 ( 世界時間 )

# 每秒更新並顯示時間

# 顯示世界時間 ( 同時顯示六個時區 ) 

# PS C:\wsPython> python test0017.py
# 10:43:35
# PS C:\wsPython> python test0017.py
# 10:44:09Traceback (most recent call last):
#   File "C:\wsPython\test0017.py", line 11, in <module>
#     time.sleep(1)
# KeyboardInterrupt
# PS C:\wsPython> python test0017.py
# 倫敦>03:44:22  台灣>10:44:22  日本>11:44:22  紐約>22:44:22  洛杉磯>19:44:22  紐西蘭>14:4倫敦>03:44:23  台灣>10:44:23  日本>11:44:23  紐約>22:44:23  洛杉磯>19:44:23  紐西蘭>14:4倫敦>03:44:24  台灣>10:44:24  日本>11:44:24  紐約>22:44:24  洛杉磯>19:44:24  紐西蘭>14:4倫敦>03:44:25  台灣>10:44:25  日本>11:44:25  紐約>22:44:25  洛杉磯>19:44:25  紐西蘭>14:4倫敦>03:44:26  台灣>10:44:26  日本>11:44:26  紐約>22:44:26  洛杉磯>19:44:26  紐西蘭>14:4倫敦>03:44:27  台灣>10:44:27  日本>11:44:27  紐約>22:44:27  洛杉磯>19:44:27  紐西蘭>14:44:27  Traceback (most recent call last):
#   File "C:\wsPython\test0017.py", line 31, in <module>
#     time.sleep(1)
# KeyboardInterrupt