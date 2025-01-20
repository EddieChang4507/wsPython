# import pyautogui
import requests

# myScreenshot = pyautogui.screenshot()   # 截圖
# myScreenshot.save('./test.png')         # 儲存為 test.png

# url = 'https://notify-api.line.me/api/notify'
# token = ''
# headers = {
#     'Authorization': 'Bearer ' + token    # 設定 LINE Notify 權杖
# }
# data = {
#     'message':'測試一下！'      # 設定 LINE Notify message ( 不可少 )
# }
# image = open('./test.png', 'rb')    # 以二進位方式開啟圖片
# imageFile = {'imageFile' : image}   # 設定圖片資訊
# data = requests.post(url, headers=headers, data=data, files=imageFile)   # 發送 LINE Notify


url = 'https://notify-api.line.me/api/notify'
token = ''

headers = {
    'Authorization': 'Bearer ' + token    # 設定權杖
}
data = {
    'message':'測試一下！'     # 設定要發送的訊息
}
data = requests.post(url, headers=headers, data=data)   # 使用 POST 方法