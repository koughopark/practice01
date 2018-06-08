str = input("문자열을 입력하세요 : ")

for i in range(len(str), 0, -1):
    print(str[i-1:i])