#상하좌우

#nxn 공간 크기 입력받기
n=int(input())
#이동 방향 입력받기
# arr=list(map(str, input().split()))
arr=input().split()

dx=[-1,1,0,0] #상,하,좌,우
dy=[0,0,-1,1] #상,하,좌,우
move_types=['U','D','L','R']

x,y=0,0 #처음 위치

for i in range(len(arr)):
    for j in range(len(move_types)):
        if arr[i]==move_types[j]:
            nx=x+dx[j]
            ny=y+dy[j]
            if nx>=0 and nx<n and ny>=0 and ny<n: #공간을 벗어나지 않는 경우
                x=nx
                y=ny

print(x+1, y+1)