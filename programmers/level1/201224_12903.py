def solution(s):
    answer = ''
    num = len(s)
    n = int(len(s) / 2)

    if (num % 2 == 0):
        answer = s[n - 1:n + 1]
    elif (num % 2 == 1):
        answer = s[n:n + 1]

    return answer