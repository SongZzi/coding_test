#효율적인 화폐 구성

#정수 N,M 입력받기
N,M=map(int, input().split())
#N개의 화폐 단위 정보 입력받기
array=[]
for i in range(N):
    array.append(int(input()))
#한번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d=[10001]*(M+1)
#DP 진행 (bottom up)
d[0]=0
for i in range(N):
    for j in range(array[i], M+1):
        if d[j-array[i]]!=10001: #(i-k)원을 만드는 방법이 존재하는 경우
            d[j]=min(d[j], d[j-array[i]]+1)
#계산된 결과 출력
if d[M]==10001:
    print(-1)
else:
    print(d[M])

