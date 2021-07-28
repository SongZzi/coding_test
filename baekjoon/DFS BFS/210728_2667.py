N=int(input())
arr=[list(map(int, input())) for _ in range(N)] #2차원 배열 입력받기
listarr=[[0]*(N+2) for _ in range(N+2)]
visited=[[0]*(N+2) for _ in range(N+2)]
cnt=[] #각 단지에 속하는 집의 수를 담기 위한 배열

x=[-1,1,0,0] #상,하,좌,우
y=[0,0,-1,1] #상,하,좌,우

for i in range(N+2): #2차원 배열 테두리 0으로 채우기
    if i>0 and i<N+1:
        for j in range(N+2):
            if j>0 and j<N+1:
                listarr[i][j]=arr[i-1][j-1]

def bfs(a,b):
    num=0
    queue=[(a,b)]
    visited[a][b]=1 #방문한 곳 1로 표시
    while queue:
        num+=1
        a=queue[0][0]
        b=queue[0][1]
        queue.pop(0)
        for i in range(4):
            next_a=a+x[i]
            next_b=b+y[i]
            if listarr[next_a][next_b]==1 and visited[next_a][next_b]==0: #아직 방문하지 않은 곳인 경우
                queue.append((next_a,next_b))
                visited[next_a][next_b]=1
    return num #단지에 속하는 집의 수 반환

for i in range(1, N+2):
    for j in range(1, N+2):
        if listarr[i][j]==1 and visited[i][j]==0:
            cnt.append(bfs(i,j))

#단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])