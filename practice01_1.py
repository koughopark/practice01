
while True:    
    num = input("3의 배수를 입력하세요 :")
    if num.isdigit():
        if int(num) % 3 == 0:
            print("정답입니다.")
            break
        else :
            print("3의 배수가 아닙니다.")
    else :
        print("숫자가 아닙니다.")
    
    print("다시 입력 하세요!")
