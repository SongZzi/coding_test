#완전탐색
def solution(answers):
    answer = []
    result = [0, 0, 0]
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if p1[i % 5] == answers[i]:
            result[0] += 1
        if p2[i % 8] == answers[i]:
            result[1] += 1
        if p3[i % 10] == answers[i]:
            result[2] += 1

    for i in range(len(result)):
        if max(result) == result[i]:
            answer.append(i + 1)

    return answer