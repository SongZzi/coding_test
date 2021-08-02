def dfs(n, computers, visited, x):
    visited[x] = 1
    for i in range(n):
        if computers[x][i] == 1 and visited[i] == 0: #아직 방문하지 않은 경우
            dfs(n, computers, visited, i)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            dfs(n, computers, visited, i)
            answer += 1

    return answer