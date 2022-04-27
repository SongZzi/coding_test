#미로 탈출
from collections import deque
#N,M
N,M=map(int, input().split())
visited=[[0]*M for i in range(N)]

graph=[]
#2차원 배열 입력받기
for i in range(N):
    graph.append(list(map(int, input())))

dx=[-1,1,0,0] #상,하,좌,우
dy=[0,0,-1,1] #상,하,좌,우

#bfs - deque 이용
queue=deque()
def bfs(x,y):
    queue.append((x,y))
    visited[x][y]=1
    while queue:
        x=queue[0][0]
        y=queue[0][1]
        queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if graph[nx][ny]==1 and visited[nx][ny]==0:
                    graph[nx][ny]=graph[x][y]+1
                    visited[nx][ny]=1
                    queue.append((nx,ny))

    return graph[N-1][M-1]

print(bfs(0,0))


