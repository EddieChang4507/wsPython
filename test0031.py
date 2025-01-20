# 定時自動螢幕截圖
# pip install pyautogui
# 


from time import sleep
import pyautogui
from datetime import datetime



pic_path = 'C:\\Users\\kenco\\OneDrive\\桌面'
for i in range(5):
    now = datetime.now()
    pic_name = now.strftime("%Y-%m-%d-%H-%M-%S") + f"_{i}.png"
    myScreenshot = pyautogui.screenshot(region=(20, 20, 500, 500))
    myScreenshot.save(f'{pic_path}\\{pic_name}')
    sleep(1)

