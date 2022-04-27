#음료수 얼려 먹기

#N,M을 공백을 기준으로 구분하여 입력받기
N,M=map(int, input().split())

#2차원 리스트에 map 정보 입력받기
graph=[]
for i in range(N):
    graph.append(list(map(int, input())))

dx=[-1,1,0,0] #상,하,좌,우
dy=[0,0,-1,1] #상,하,좌,우

#dfs
def dfs(x,y):
    global num
    num=0
    if graph[x][y]==0:
        num+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            graph[x][y]=1 #방문 표시
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if graph[nx][ny]==0:
                    dfs(nx,ny)
    return num

result=0
for i in range(N):
    for j in range(M):
        if dfs(i,j)>0:
            result+=1

print(result)