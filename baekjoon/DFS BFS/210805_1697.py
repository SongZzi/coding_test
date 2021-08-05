from collections import deque

N,K=map(int,input().split())
visited=[0]*100001 #방문검사 확인을 위한 배열
queue=deque()

def bfs(x):
    queue.append((x,0))
    visited[x]=1
    while queue:
        x=queue[0][0]
        cnt=queue[0][1]
        queue.popleft()
        if x==K:
            print(cnt)
            break

        for nx in (x-1,x+1,x*2):
            if nx>=0 and nx<=100000 and visited[nx]==0: #범위설정 및 방문검사 -> 메모리초과 해결
                queue.append((nx,cnt+1))
                visited[nx]=1

bfs(N)