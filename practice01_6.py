
print("키보드에서 5개 정수를 입력받아 리스트에 저장하고 평균을 구하는 프로그램을 만드시오")

data = []
total = 0

while True:
    
    

    if len(data) != 5:
        num = input("숫자를 입력하세요 : ")        
        if num.isdigit():                
            data.append(num)
            total += int(num)
            print(data)
            print(total)
        else:
            print("숫자가 아닙니다.")            
    else:
         break    
                
    print("다시 입력하세요")

print("data[] : ", data)
print("total : ", total)
 