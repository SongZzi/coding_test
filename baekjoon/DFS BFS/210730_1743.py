import sys
sys.setrecursionlimit(10**7) #DFS 재귀 깊이 설정

N,M,T=map(int, input().split())
arr=[[0]*M for _ in range(N)]
visited=[[0]*M for _ in range(N)]
answer=[]

dx=[-1,1,0,0] #상,하,좌,우
dy=[0,0,-1,1] #상,하,좌,우

for i in range(T):
    a,b=map(int, input().split())
    arr[a-1][b-1]=1

def dfs(x,y):
    global num
    num+=1
    visited[x][y]=1 #방문한 곳 1로 표시
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<N and ny>=0 and ny<M:
            if arr[nx][ny]==1 and visited[nx][ny]==0: #아직 방문하지 않은 곳인 경우
                dfs(nx,ny)
    return num

for i in range(N):
    for j in range(M):
        if arr[i][j]==1 and visited[i][j]==0:
            num=0
            answer.append(dfs(i,j))

print(max(answer))