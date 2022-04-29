#거스름 돈

n=int(input())
#큰 단위의 화폐부터 차례대로 확인하기
coin=[500,100,50,10]
cnt=0

for i in range(4):
    cnt+=n//coin[i] #필요한 동전 개수
    n=n%coin[i]

print(cnt)