def solution(strings, n):
    answer = []
    arr = []

    for i in range(len(strings)):
        arr.append(strings[i][n])
    arr.sort()
    strings.sort()

    for a in arr:
        for b in strings:
            if b[n] == a:
                answer.append(b)
                strings.remove(b)
                break

    return answer