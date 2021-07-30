M=int(input())
N=int(input())
arr=[[0]*(M+1) for _ in range(M+1)]

for i in range(N):
    a,b=map(int, input().split())
    arr[a][b]=1
    arr[b][a]=1
visited=[0]*(M+1)

def bfs(V):
    answer=0
    queue=[V]
    visited[V]=1 #방문한 컴퓨터 1로 표시
    while queue:
        V=queue[0]
        queue.pop(0)
        for i in range(1, M+1):
            next=arr[V][i]
            if next==1 and visited[i]==0: #아직 방문하지 않은 컴퓨터인 경우
                visited[i]=1
                queue.append(i)
                answer+=1
    return answer #1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수

print(bfs(1))