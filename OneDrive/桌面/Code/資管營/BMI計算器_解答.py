# BMI 計算器
height = float(input("輸入你的身高（公尺）: "))
weight = float(input("輸入你的體重（公斤）: "))


# BMI 的公式為 體重（公斤）除以 身高（公尺）的平方
bmi = weight / (height ** 2)
print("你的 BMI 值是:", bmi)

# 當BMI小於18.5時 過輕 當BMI介於 18.5 & 24.9 時 正常 當BMI介於 25 & 29.9時 過重 其餘為肥胖
if bmi < 18.5:
    print("體重過輕")
elif 18.5 <= bmi < 25:
    print("體重正常")
elif 25 <= bmi < 30:
    print("體重過重")
else:
    print("肥胖")
