first_number = int(input("請輸入第一個數字："))
second_number = int(input("請輸入第二個數字："))

operation = input("請輸入加、減、乘、除、次方、取餘數、取商數其中之一：")
if operation == "加":
    result = first_number + second_number
    print("運算結果為：",result)
elif operation == "減":
    result = first_number - second_number
    print("運算結果為：",result)
elif operation == "乘":
    result = first_number - second_number
    print("運算結果為：",result)
elif operation == "除":
    result = first_number / second_number
    print("運算結果為：",result)
elif operation == "次方":
    result = first_number ** second_number
    print("運算結果為：",result)
elif operation == "取餘數":
    result = first_number % second_number
    print("運算結果為：",result)
elif operation == "取商數":
    result = first_number // second_number
    print("運算結果為：",result)
else: #當都不是該寫上甚麼呢???
    print("無效的運算符號(文字)")
