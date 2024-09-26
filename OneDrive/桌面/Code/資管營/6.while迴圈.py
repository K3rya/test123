# While Loop 累加
# total = 0
# number = 1
# while number <= 3:
#     print("total =", total)
#     print("number =",number)
#     temp = total + number   # 用 temp 存取 total + number
#     total = temp            # 將 temp 轉存到 total 中
#     number = number + 1     # 將 number 增加 1
# print("1到3的累加和是:", total)


# 重複輸入 密碼直到正確
correct_password = "python123"
password = ""
while password != correct_password:
    password = input("請輸入密碼: ")
print("密碼正確！")

# 無限迴圈 & Break
while True:
    user_input = input("輸入 '退出' 來退出: ")
    if user_input == "退出":
        break
