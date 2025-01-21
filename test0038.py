# 常見的反爬蟲方式

import requests

# url = '要爬的網址'
# # 假的 headers 資訊
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
# # 加入 headers 資訊
# web = requests.get(url, headers=headers)
# web.encoding = 'utf8'
# print(web.text)


import pandas as pd
import re, time, requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# 開啟瀏覽器
driver = webdriver.Chrome()

# 進入PTT首頁
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")

# 找到進入滿18歲的按鈕，並點擊
enter_button = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[1]/button")
enter_button.click()
time.sleep(2)

# 設置滿18歲的Cookies，這取決於PTT網站具體的Cookies名稱和值
over_18_cookie = {'over18': '_gat', '1': '1'}  # over_18_cookie = {'Name': 'your_cookies_name', 'Value': 'your_value'}
driver.add_cookie(over_18_cookie)

# 重新刷新頁面，確保Cookies生效
driver.refresh()