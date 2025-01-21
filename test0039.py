# 您可以使用 Python 的 Flask 或 Django 等框架，從 HTTP 請求中提取 User-Agent：

# Flask 範例
# python
# 複製
# 編輯
# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/')
# def get_user_agent():
#     user_agent = request.headers.get('User-Agent')
#     return f"Your User-Agent is: {user_agent}"

# if __name__ == '__main__':
#     app.run()
# 啟動後訪問 http://127.0.0.1:5000/，可以看到您的 User-Agent。

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_user_agent():
    user_agent = request.headers.get('User-Agent')
    return f"Your User-Agent is: {user_agent}"

if __name__ == '__main__':
    app.run()