#왕실의 나이트

#현재 나이트의 위치 입력받기
s=input()
x=int(s[1])-1 #행
y=ord(s[0])-ord('a') #열

#나이트가 이동할 수 있는 8가지 방향
dx=[-1,-2,-2,-1,1,2,2,1]
dy=[-2,-1,1,2,2,1,-1,-2]

cnt=0
for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx>=0 and nx<8 and ny>=0 and ny<8: #해당 위치로 이동 가능한 경우
        cnt+=1

print(cnt)