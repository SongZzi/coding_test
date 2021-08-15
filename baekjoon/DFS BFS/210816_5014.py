F,S,G,U,D = map(int, input().split())

ud=[U,D*(-1)] # Up, Down
visited=[0]*(F+1)

def bfs(s,g):
    queue=[(s,0)]
    visited[s]=1
    while queue:
        s=queue[0][0]
        cnt=queue[0][1]
        if s==g: #S층->G층으로 갈 수 있는 경우
            return cnt
        queue.pop(0)
        for i in range(len(ud)):
            next_s=s+ud[i]
            if 1<=next_s<=F and visited[next_s]==0:
                queue.append((next_s,cnt+1))
                visited[next_s]=1
    return "use the stairs"

print(bfs(S,G))