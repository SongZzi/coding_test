#deque 사용 -> 시간초과 해결
from collections import deque

M,N=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(N)]

queue=deque() #deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            queue.append((i,j)) #queue에 익은 토마토 위치 넣기

def bfs():
    while queue:
        x=queue[0][0]
        y=queue[0][1]
        queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if arr[nx][ny]==0: #아직 방문하지 않은 경우
                    arr[nx][ny]=arr[x][y]+1
                    queue.append((nx,ny))

def result():
    answer = 0
    for num in arr:
        if 0 in num:
            answer = -1

    if answer == -1: #토마토가 모두 익지는 못하는 상황인 경우
        print(-1)
    else:
        print(max(map(max, arr)) - 1)

bfs()
result()
