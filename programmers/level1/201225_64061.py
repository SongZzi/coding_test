def solution(board, moves):
    answer = 0
    arr = []

    for m in range(len(moves)):
        for n in range(len(board)):
            if board[n][moves[m] - 1] != 0:
                arr.append(board[n][moves[m] - 1])
                board[n][moves[m] - 1] = 0

                if len(arr) >= 2 and arr[len(arr) - 1] == arr[len(arr) - 2]:
                    arr.pop()
                    arr.pop()
                    answer = answer + 2
                break

    return answer