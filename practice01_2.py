
while True:    
    num = input("숫자를 입력하세요 :")
    if num.isdigit():
        if int(num) == 0:
            break
        elif int(num) % 2 == 0:
            print("짝수 입니다.")
        else:
            print("홀수 입니다.")

    else :
        print("숫자가 아닙니다.")
    
    print("다시 입력 하세요!")
    print("Process finished with exit code 0")