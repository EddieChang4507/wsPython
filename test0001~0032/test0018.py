h = float(input('請輸入身高(cm)：'))/100
# 使用 float 轉換成浮點數後除以 100 ( 因為身高可能會有小數點 )

w = float(input('請輸入體重(kg)：'))
# 使用 float 轉換成浮點數 ( 因為體重可能會有小數點 )

bmi = w/(h*h)                           # 套用公式計算
print(f'你的 BMI 數值為：{bmi}')          # 你的 BMI 數值為：23.044982698961938

h = float(input('請輸入身高(cm)：'))/100
w = float(input('請輸入體重(kg)：'))
bmi = round(w/(h*h),3)                  # 使用 round 四捨五入到小數點三位
if bmi<18.5:                            # 使用邏輯判斷
    note = '你太輕囉！'
elif bmi>=18.5 and bmi<=25:
    note = '你的體重正常！'
else:
    note = '你有點太重囉～'
print(f'你的 BMI 數值為：{bmi}，{note}')



# 計算 BMI 數值
# 
# 輸入身高體重，計算 BMI
# 
# 加上邏輯判斷與四捨五入 
# 
# PS C:\wsPython> python test0018.py
# 請輸入身高(cm)：168
# 請輸入體重(kg)：75
# 你的 BMI 數值為：26.573129251700685
# PS C:\wsPython> python test0018.py
# 請輸入身高(cm)：168
# 請輸入體重(kg)：79
# 你的 BMI 數值為：27.99，你有點太重囉～
# PS C:\wsPython> python test0018.py
# 請輸入身高(cm)：120
# 請輸入體重(kg)：10
# 你的 BMI 數值為：6.944，你太輕囉！
# PS C:\wsPython> python test0018.py
# 請輸入身高(cm)：168
# 請輸入體重(kg)：50
# 你的 BMI 數值為：17.715，你太輕囉！
# PS C:\wsPython> python test0018.py
# 請輸入身高(cm)：168
# 請輸入體重(kg)：60
# 你的 BMI 數值為：21.259，你的體重正常！