#메모리초과
from collections import deque

N,K=map(int,input().split())
queue=deque()

def bfs(x):
    queue.append((x,0))
    while queue:
        x=queue[0][0]
        cnt=queue[0][1]
        if x==K:
            print(cnt)
            break
        queue.popleft()

        queue.append((x-1, cnt+1))
        queue.append((x+1, cnt+1))
        queue.append((x*2, cnt+1))

bfs(N)