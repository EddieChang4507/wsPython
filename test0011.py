import re


text = '''請 求 您 幫 我 oxxo.studio 去 除 空 白 ok ？
但是要保留換行 可以 嗎 ，(        哈哈哈 )( 啊哈)
統一便利超商 (711) 的括號之間也要有空白喔！
寫作規    範就是這 麼 100% 的龜毛～
'''
# 取得中文字和英文單字的正規表達式
# [a-zA-Z0-9]+ 表示開頭是英文字母後面連接一串字母或數字
regex= re.compile(r'[\u4E00-\u9FFF\uFF00-\uFFFF\u0021-\u002F\n]|[a-zA-Z0-9]+')

# 根據正規表達式，將每個中文字、標點符號和英文單字變成串列
arr = re.findall(regex, text)

# 使用空格合併串列
text = ' '.join(arr)
print(text)

regex= re.compile(r'(?<=[^a-zA-Z0-9\u0021-\u002E])(\x20)(?=[^a-zA-Z0-9\u0021-\u002E])')
text = re.sub(regex, '', text)
print(text)

regex= re.compile(r'(\x20)(?=[\(\%\uFF00-\uFFFF])')
text = re.sub(regex, '', text)
print(text)

text = text.replace(' . ','.')
print(text)


# 去除中英文夾雜的空白
# 
# 基本規則
# 中文字和英文字中間要有空白。
# 除了括號外，其他標點符號使用「全形標點符號」。
# 括號左右需要有空白，括號和括號之間不留空白。
# 全形標點符號左右不留空白。
# 
# 步驟 1，在所有的中文字中間加上空白 
# 步驟 2，根據規則移除空白 
# 步驟 3，最後修飾 

# 匹配	說明
# \u4E00-\u9FFF	所有中文字。
# \uFF00-\uFFFF	所有全形標點符號。
# \u0021-\u002F	所有半形標點符號。
# \n	結尾換行。
# a-zA-Z0-9	所有英文字母和阿拉伯數字。
# 
# PS C:\wsPython> python test0011.py
# 請 求 您 幫 我 oxxo . studio 去 除 空 白 ok ？ 
#  但 是 要 保 留 換 行 可 以 嗎 ， ( 哈 哈 哈 ) ( 啊 哈 ) 
#  統 一 便 利 超 商 ( 711 ) 的 括 號 之 間 也 要 有 空 白 喔 ！ 
#  寫 作 規 範 就 是 這 麼 100 % 的 龜 毛 ～ 

# 請求您幫我 oxxo . studio 去除空白 ok ？
# 但是要保留換行可以嗎， ( 哈哈哈 ) ( 啊哈 ) 
# 統一便利超商 ( 711 ) 的括號之間也要有空白喔！
# 寫作規範就是這麼 100 % 的龜毛～

# 請求您幫我 oxxo . studio 去除空白 ok？
# 但是要保留換行可以嗎，( 哈哈哈 )( 啊哈 ) 
# 統一便利超商( 711 ) 的括號之間也要有空白喔！
# 寫作規範就是這麼 100% 的龜毛～

# 請求您幫我 oxxo.studio 去除空白 ok？
# 但是要保留換行可以嗎，( 哈哈哈 )( 啊哈 ) 
# 統一便利超商( 711 ) 的括號之間也要有空白喔！
# 寫作規範就是這麼 100% 的龜毛～