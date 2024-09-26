first_number = int(空格("請輸入第一個數字："))  #int() 可把中間的東西換成int
second_number = int(空格("請輸入第二個數字：")) #int() 可把中間的東西換成int
operation = 空格("請輸入加、減、乘、除、次方、取餘數、取商數其中之一：") #使用 operation 來存取使用者的輸入

if operation == "加":
    result = first_number 空格 second_number
    print("運算結果為：",result)
elif operation == "減":
    result = first_number 空格 second_number
    print("運算結果為：",result)
elif operation == "乘":
    result = first_number 空格 second_number
    print("運算結果為：",result)
elif operation == "除":
    result = first_number 空格 second_number
    print("運算結果為：",result)
elif operation == "次方":
    result = first_number 空格 second_number
    print("運算結果為：",result)
elif operation == "取餘數":
    result = first_number 空格 second_number
    print("運算結果為：",result)
elif operation == "取商數":
    result = first_number 空格 second_number
    print("運算結果為：",result)
空格: #當都不是該寫上甚麼呢???
    print("無效的運算符號(文字)")
