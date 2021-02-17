def solution(n):
    answer = -1

    for i in range(n):
        if i * i == n and i < n // 2:
            answer = (i + 1) * (i + 1)
            break

    return answer

def solution(n):
    answer = 0
    sqrt = n ** (1 / 2)

    if sqrt % 1 == 0:
        answer = (sqrt + 1) ** 2
    else:
        answer = -1

    return answer