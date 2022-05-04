#효율성 테스트-시간초과
def solution(board):
    answer = 0

    def findBox(x, y):
        length = 2
        while True:
            flag = True
            for i in range(0, length):
                for j in range(0, length):
                    nx = x + i
                    ny = y + j
                    if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0]):
                        if board[nx][ny] == 0:
                            return length - 1
                    else:
                        return length - 1
            length += 1

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                answer = max(findBox(i, j), answer)

    return answer ** 2