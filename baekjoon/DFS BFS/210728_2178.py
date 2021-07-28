#시간초과
import sys
sys.setrecursionlimit(10**7)

N,M=map(int, input().split())
arr=[list(map(int, input())) for i in range(N)] #2차원 배열 입력받기
listarr=[[0]*(M+2) for i in range(N+2)]
cost=[[99999]*(M+2) for i in range(N+2)]

x=[-1,1,0,0] #상,하,좌,우
y=[0,0,-1,1] #상,하,좌,우

for i in range(N+2): #입력 받은 배열 옮기기
    if i>0 and i<N+1:
        for j in range(M+2):
            if j>0 and j<M+1:
                listarr[i][j]=arr[i-1][j-1]

def dfs(a,b):
    for i in range(4):
        next_a=a+x[i]
        next_b=b+y[i]
        if listarr[next_a][next_b]==1 and cost[a][b]+1<cost[next_a][next_b]:
            cost[next_a][next_b]=cost[a][b]+1
            dfs(next_a,next_b)

cost[1][1]=1 #시작 위치
dfs(1,1) #(1,1)에서 출발
print(cost[N][M])
