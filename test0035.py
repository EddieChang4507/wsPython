import os
from pikepdf import Pdf, Permissions, Encryption


file_path = 'C:\\test'
file_pdf_A = 'April 2022 Codes Reference Guide.pdf'
file_pdf_B = 'External_DGN_D_PAS_Tap_on_Mobile_Implementation_Guide_July_2022.pdf'
file_pdf_C = 'AAA.pdf'
file_pdf_D = 'BBB.pdf'

pdf = Pdf.open(f'{file_path}\\{file_pdf_A}', password='')         # 開啟 pdf
pdf_pwd = Pdf.open(f'{file_path}\\{file_pdf_A}', password='') # 開啟需要密碼的 pdf

print(pdf)
print(pdf_pwd)

no_extracting = Permissions(extract=False)
# 儲存為密碼是 qqqq 的 pdf
pdf.save(f'{file_path}\\{file_pdf_C}', encryption = Encryption(user="qqqq", owner="qqqq", allow=no_extracting))


pdf = Pdf.open(f'{file_path}\\{file_pdf_C}', password="qqqq")   # 開啟 pdf
pages = pdf.pages                  # 將每一頁的內容變成串列
output = Pdf.new()                 # 建立新的 pdf 物件
# output.pages.append(pages[0])      # 添加頁面內容
output.pages.extend(pages[1:3])   # 改用 extend，放入特定範圍的頁面
output.pages.reverse()           # 反轉 pdf
del output.pages[1:2]                # 刪除第二頁
output.save(f'{file_path}\\{file_pdf_D}')             # 儲存為新的 pdf