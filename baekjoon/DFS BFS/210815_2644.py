n=int(input())
a,b=map(int, input().split())
m=int(input())

graph=[[] for _ in range(n+1)] #인접리스트
visited=[0]*(n+1) #방문노드 검사

for i in range(m):
    x,y=map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(a,b):
    queue=[(a,0)]
    visited[a]=1
    while queue:
        a=queue[0][0]
        cnt=queue[0][1]
        if a==b:
            return cnt
        queue.pop(0)
        for i in range(len(graph[a])):
            next_a=graph[a][i]
            if visited[next_a]==0:
                queue.append((next_a, cnt+1))
                visited[next_a]=1
    return -1

print(bfs(a,b))
