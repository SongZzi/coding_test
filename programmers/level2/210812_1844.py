dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, maps, visited):
    queue = [(x, y, 1)]
    visited[x][y] = 1
    while queue:
        x = queue[0][0]
        y = queue[0][1]
        z = queue[0][2] #(x,y)에 도착하기 위한 최단 거리
        if x == len(maps) - 1 and y == len(maps[0]) - 1: #상대팀 진영에 도착한 경우
            return z
        queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, z + 1))
    return -1

def solution(maps):
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    answer = bfs(0, 0, maps, visited) #(0,0)부터 출발
    return answer