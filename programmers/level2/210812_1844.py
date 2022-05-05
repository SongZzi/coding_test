from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]  # 상,하,좌,우
    dy = [0, 0, -1, 1]  # 상,하,좌,우

    queue = deque()

    # 최단거리 찾기 - bfs
    def bfs():
        queue.append((0, 0))
        visited[0][0] = 1
        while queue:
            x = queue[0][0]
            y = queue[0][1]
            queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        maps[nx][ny] = maps[x][y] + 1
                        queue.append((nx, ny))

    bfs()

    if maps[n - 1][m - 1] == 1:  # 상대 팀 진영에 도착할 수 없는 경우
        return -1
    else:
        return maps[n - 1][m - 1]