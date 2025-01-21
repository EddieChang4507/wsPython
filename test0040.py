#  Python 建立 TXT 檔案並寫入內容的範例
# 

# 定義要寫入的內容
content = "這是範例內容，用來測試建立 TXT 檔案。"

# 指定檔案名稱

file_path = 'C:\\test'
file_name = "example.txt"

# 使用 with 語法開啟檔案並寫入內容
with open(f'{file_path}\\{file_name}', "w", encoding="utf-8") as file:
    file.write(content)

print(f"檔案 {file_name} 已成功建立並寫入內容。")



