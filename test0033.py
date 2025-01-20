# 批次重新命名檔案
# 

import glob
import os

file_path = 'C:\\test'

images = glob.glob(f'{file_path}\\*')
print(images)


n = 1          # 設定名稱從 1 開始
for i in images:
    os.rename(i, f'{file_path}\\img-{n:03d}.jpg')   # 改名時，使用字串格式化的方式進行三位數補零
    n = n + 1    # 每次重複時將 n 增加 1