import sys

N,M=map(int, input().split())
arr=[list(sys.stdin.readline().strip()) for _ in range(M)] #문자열 M줄을 입력받아 리스트에 저장
visited=[[0]*(N) for _ in range(M)]

dx=[-1,1,0,0] #상,하,좌,우
dy=[0,0,-1,1] #상,하,좌,우

sum_w=sum_b=0

def bfs(x,y,T):
    num=0
    queue=[(x,y)]
    visited[x][y]=1 #방문한 곳 1로 표시
    while queue:
        num += 1
        x=queue[0][0]
        y=queue[0][1]
        queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<M and ny>=0 and ny<N:
                if arr[nx][ny]==T and visited[nx][ny]==0: #아직 방문하지 않은 곳인 경우
                    visited[nx][ny]=1
                    queue.append((nx,ny))
    return num #뭉쳐있는 병사들의 합

for i in range(M):
    for j in range(N):
        if arr[i][j]=='W' and visited[i][j]==0:
            sum_w+=bfs(i,j,'W')**2
        elif arr[i][j]=='B' and visited[i][j]==0:
            sum_b+=bfs(i,j,'B')**2

print(sum_w,sum_b)
