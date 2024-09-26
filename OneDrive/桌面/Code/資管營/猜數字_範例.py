import random
#生成題目
def generate_unique_number():
    digits = list(range(10))
    unique_number = []
    
    for i in range(4):
        digit = random.choice(digits)
        unique_number.append(digit)
        digits.remove(digit)
    
    return unique_number
#幾A幾B
def get_feedback(secret, guess):
    a = 0
    b = 0
    for i in range(4):
        if guess[i] in secret:
            if guess[i] == secret[i]:
                a += 1
            else:
                b += 1
    feedback = str(a) + "A" + str(b) + "B"  # 將數字轉為字串並拼接
    return feedback

#主程式
while True:
    target = generate_unique_number()
    times = 0
    print("電腦已經生成了一個不重複的四位數字。")
    
    while True:
        try:
            print("")
            print("請輸入四個不重複的數字，中間使用空格隔開 (或輸入 'exit' 退出):")
            user_input = input().strip() # 去頭去尾

            parts = user_input.split() #分割空格

            guess = []
            
            if user_input.lower() == 'exit':
                print("遊戲結束。謝謝你遊玩！")
                exit()
            
            if user_input.lower() == 'answer':
                print("偷偷告訴你，這次的答案是：",target)
                continue
            
            # 處理每一部分，如果某個部分包含多個字符，將其拆分
            for part in parts:
                if part.isdigit():
                    guess.extend(map(int, part))  # 將部分中的每個字符轉換為數字並加入列表            

            
            if len(guess) != 4 or len(set(guess)) != 4:
                print("您的輸入有誤，請輸入四個不重複的數字。")
                continue
            
            if any(i < 0 or i > 9 for i in guess):
                print("您的輸入有誤，數字必須在0到9之間。")
                continue
            
            times += 1
            feedback = get_feedback(target, guess)
            print(f"這次的結果是: {feedback}")
            
            if feedback == "4A0B":
                print(f"恭喜你！你在 {times} 次嘗試中猜對了數字。")
                break
            
        except ValueError:
            print("您的輸入有誤，請看清楚下面的規則。")

    play_again = input("你想再玩一次嗎？(輸入 'yes' 再玩一次，或輸入 'exit' 退出): ").strip().lower()
    if play_again == 'exit':
        print("遊戲結束。謝謝你遊玩！")
        break
