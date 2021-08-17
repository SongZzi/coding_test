N=int(input())
maps=[list(map(int, input().split())) for _ in range(N)]
result=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,h):
    queue=[(x,y)]
    visited[x][y]=1
    while queue:
        x=queue[0][0]
        y=queue[0][1]
        queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and maps[nx][ny]>h and visited[nx][ny]==0:
                visited[nx][ny]=1
                queue.append((nx,ny))
    return 1

for h in range(100): #물에 잠기는 높이(0~99)
    total=0
    visited = [[0] * N for _ in range(N)]
    for n in range(N):
        for m in range(N):
            if maps[n][m] > h and visited[n][m]==0: #물에 잠기지 않는 영역인 경우
                total+=bfs(n,m,h)
    result.append(total)

print(max(result))