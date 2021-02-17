def solution(n):
    answer = 0
    arr = []
    num = str(n)

    for i in range(len(num)):
        arr.append(num[i])

    arr.sort()
    arr.reverse()
    answer = ''.join(arr)

    return int(answer)