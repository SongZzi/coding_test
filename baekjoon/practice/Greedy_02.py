#1이 될 때까지

#n,k 공백을 기준으로 구분하여 입력받기
n,k=map(int, input().split())
cnt=0

while n!=1:
    if n%k==0: #n이 k로 나누어 떨어지는 경우
        n=n//k
    else:
        n-=1
    cnt+=1

print(cnt)