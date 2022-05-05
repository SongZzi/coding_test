def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(4):
            max_num = 0
            for k in range(4):
                if j != k:  # 연속해서 같은 열이 아닌 경우
                    max_num = max(max_num, land[i - 1][k])
            land[i][j] += max_num

    answer = max(land[len(land) - 1])  # 최고점

    return answer