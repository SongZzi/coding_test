#시각

#n입력 받기
n=int(input())
#00시00분00초 ~ n시59분59초

cnt=0 #3이 하나라도 포함되어 있는 시각 개수

for i in range(0,n+1): #0시~n시
    for j in range(0,60): #00분~59분
        for k in range(0,60): #00초~59초
            if '3' in str(i) or '3' in str(j) or '3' in str(k): #3이 하나라도 포함되어 있는 경우
                cnt+=1

print(cnt)