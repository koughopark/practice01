money = input("금액을 입력하세요 :")

c50000 = 0
c10000 = 0
c5000 = 0
c1000 = 0
c500 = 0
c100 = 0
c50 = 0
c10 = 0
c5 = 0
c1 = 0

c50000 = int(money)//50000
c10000 = int(money)%50000//10000
c5000 = int(money)%50000%10000//5000
c1000 = int(money)%50000%10000%5000//1000
c500 = int(money)%50000%10000%5000%1000//500
c100 = int(money)%50000%10000%5000%1000%500//100
c50 = int(money)%50000%10000%5000%1000%500%100//50
c10 = int(money)%50000%10000%5000%1000%500%100%50//10
c5 = int(money)%50000%10000%5000%1000%500%100%50%10//5
c1 = int(money)%50000%10000%5000%1000%500%100%50%10%5//1

print("50000원 : ",c50000)
print("10000원 : ",c10000)
print("5000원 : ",c5000)
print("1000원 : ",c1000)
print("500원 : ",c500)
print("100원 : ",c100)
print("50원 : ",c50)
print("10원 : ",c10)
print("5원 : ",c5)
print("1원 : ",c1)