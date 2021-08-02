import sys

dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

while True:
    M,N=map(int, input().split())
    if M==0 and N==0:
        break
    arr=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited=[[0]*M for _ in range(N)]
    answer=0

    def bfs(x,y):
        queue=[(x,y)]
        visited[x][y]=1
        while queue:
            x=queue[0][0]
            y=queue[0][1]
            queue.pop(0)
            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx>=0 and nx<N and ny>=0 and ny<M:
                    if arr[nx][ny]==1 and visited[nx][ny]==0:
                        visited[nx][ny]=1
                        queue.append((nx,ny))
        return 1

    for i in range(N):
        for j in range(M):
            if arr[i][j]==1 and visited[i][j]==0:
                answer+=bfs(i,j)

    print(answer)