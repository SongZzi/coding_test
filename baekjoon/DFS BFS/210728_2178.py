#DFS->BFS 시간초과 해결
N,M=map(int, input().split())
arr=[list(map(int, input())) for i in range(N)] #2차원 배열 입력받기
listarr=[[0]*(M+2) for i in range(N+2)]
cost=[[0]*(M+2) for i in range(N+2)]
visited=[[0]*(M+2) for i in range(N+2)]

x=[-1,1,0,0] #상,하,좌,우
y=[0,0,-1,1] #상,하,좌,우

for i in range(N+2): #2차원 배열 테두리 0으로 채우기
    if i>0 and i<N+1:
        for j in range(M+2):
            if j>0 and j<M+1:
                listarr[i][j]=arr[i-1][j-1]

def bfs(a,b):
    queue=[(a,b)]
    visited[a][b]=1 #방문한 곳 1로 표시
    while queue:
        a=queue[0][0]
        b=queue[0][1]
        queue.pop(0)
        for i in range(4):
            next_a=a+x[i]
            next_b=b+y[i]
            if listarr[next_a][next_b]==1 and visited[next_a][next_b]==0: #아직 방문하지 않은 곳인 경우
                queue.append((next_a,next_b))
                cost[next_a][next_b]=cost[a][b]+1
                visited[next_a][next_b]=1

cost[1][1]=1 #시작 위치
bfs(1,1) #(1,1)에서 출발
print(cost[N][M])