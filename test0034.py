# 讀取 PDF 內容
# 
# pip install pdfplumber
# 

import os
import pdfplumber
import csv

file_path = 'C:\\test'
file_pdf = 'External_DGN_D_PAS_Tap_on_Mobile_Implementation_Guide_July_2022.pdf'
file_text = 'test.txt'
file_csv = 'test.csv'

pdf = pdfplumber.open(f'{file_path}\\{file_pdf}')   # 開啟 pdf
# print(pdf.pages)                          # [<Page:1>, <Page:2>, <Page:3>]，共有三頁


page = pdf.pages[0]           # 讀取第一頁
text = page.extract_text()    # 取出文字
print(text)


page = pdf.pages[13]           # 讀取第14頁 
table = page.extract_table()  # 取出表格
print(table)



page = pdf.pages[0]
text = page.extract_text()
print(text)
pdf.close()

f = open(f'{file_path}\\{file_text}','w+', encoding="utf-8")   # 使用 w+ 模式開啟 test.txt
f.write(text)               # 寫入內容
f.close()                   # 關閉 test.txt


page = pdf.pages[13]           # 讀取第14頁 
table = page.extract_table()  # 取出表格
csvfile = open(f'{file_path}\\{file_csv}', 'w+')  # 建立 CSV 檔案
write = csv.writer(csvfile)           # 建立寫入物件
for i in table:
    write.writerow(i)                 # 讀取表格每一列寫入 CSV

