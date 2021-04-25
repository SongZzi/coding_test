def solution(N, stages):
    answer = []
    total = [0 for _ in range(N)]
    result = [0 for _ in range(N)]

    answer = stages
    answer.sort()

    num = len(answer)
    a = 0

    for i in range(1, N + 2):
        value1 = 0
        for j in range(len(answer)):
            if answer[j] == i:
                value1 = value1 + 1
                if i < N + 1 and j == len(answer) - 1:
                    total[a] = value1 / num
                    a = a + 1
            elif answer[j] > i:
                total[a] = value1 / num
                a = a + 1
                num = num - value1
                break

    for i in range(len(total)):
        number = 0

        for j in range(len(total)):
            if i == j:
                number = number
            elif i != j and total[i] < total[j]:
                number = number + 1

        for k in range(len(result)):
            if result[number] == 0:
                result[number] = i + 1
                break
            else:
                number = number + 1

    return result