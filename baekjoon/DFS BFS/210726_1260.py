N,M,V=map(int, input().split())
arr=[[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    arr[a][b]=1
    arr[b][a]=1
visited=[0]*(N+1)

def dfs(V):
    print(V, end=' ')
    visited[V]=1 # 방문한 곳 1로 표시
    for i in range(1, N+1):
        next=arr[V][i]
        if next==1 and visited[i]==0: # 아직 방문하지 않은 곳인 경우
            dfs(i)

def bfs(V):
    queue=[V]
    visited[V]=0 # 방문한 곳 0으로 표시
    while queue:
        V=queue[0]
        print(V, end=' ')
        queue.pop(0)
        for i in range(1, N+1):
            next=arr[V][i]
            if next==1 and visited[i]==1: # 아직 방문하지 않은 곳인 경우
                queue.append(i)
                visited[i]=0

dfs(V)
print()
bfs(V)