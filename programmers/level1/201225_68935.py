def solution(n):
    answer = 0
    arr = []

    while True:
        arr.append(str(n % 3))
        n = n // 3
        if n == 0:
            break

    answer = ''.join(arr)
    answer = int(answer, 3)

    return answer