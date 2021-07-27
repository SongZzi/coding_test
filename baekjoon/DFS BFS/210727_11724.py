#시간초과
N,M=map(int, input().split())
arr=[[0]*(N+1) for _ in range(N+1)]
cnt=0
for i in range(M):
    a,b=map(int, input().split())
    arr[a][b]=1
    arr[b][a]=1
visited=[0]*(N+1)

def bfs(V):
    queue=[V]
    visited[V]=1 #방문한 곳 1로 표시
    while queue:
        V=queue[0]
        queue.pop(0)
        for i in range(1,N+1):
            if arr[V][i]==1 and visited[i]==0: #아직 방문하지 않은 곳인 경우
                queue.append(i)
                visited[i]=1

for i in range(1, N+1):
    if visited[i]==0:
        bfs(i)
        cnt+=1

print(cnt)