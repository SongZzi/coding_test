#시간초과
M,N=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(N)]

queue=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            queue.append((i,j))

def bfs():
    while queue:
        x=queue[0][0]
        y=queue[0][1]
        queue.pop(0)

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if arr[nx][ny]==0:
                    arr[nx][ny]=arr[x][y]+1
                    queue.append((nx,ny))

def result():
    answer = 0
    for num in arr:
        if 0 in num:
            answer = -1

    if answer == -1:
        print(-1)
    else:
        print(max(map(max, arr)) - 1)

bfs()
result()
