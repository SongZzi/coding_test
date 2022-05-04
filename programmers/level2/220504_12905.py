# 시간 초과 해결 - dp
def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                # 현재의 위치에서 가능한 최대 크기의 정사각형의 한 변의 길이 구하기
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1

    # 가장 큰 정사각형의 한 변의 길이 구하기
    for i in range(n):
        answer = max(answer, max(board[i]))

    return answer ** 2