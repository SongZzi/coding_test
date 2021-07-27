import sys
sys.setrecursionlimit(10**7) #재귀 깊이 설정

T=int(input())
x=[-1,1,0,0] #상,하,좌,우
y=[0,0,-1,1] #상,하,좌,우

def dfs(b, a):
    visited[b][a]=1
    for i in range(4): #인접한 배추 상하좌우로 탐색
        next_a=a+x[i]
        next_b=b+y[i]
        if arr[next_b][next_a]==1 and visited[next_b][next_a]==0: #아직 방문하지 않은 곳인 경우
            dfs(next_b,next_a)

for i in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * (M+2) for _ in range(N+2)]
    visited = [[0] * (M+2) for _ in range(N+2)]
    cnt = 0
    for i in range(K):
        a,b=map(int, input().split())
        arr[b+1][a+1]=1

    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j]==1 and visited[i][j]==0: #아직 방문하지 않은 곳인 경우
                cnt+=1
                dfs(i,j)
    print(cnt)