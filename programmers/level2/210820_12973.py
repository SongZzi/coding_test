#시간초과
def solution(s):
    i = -1

    while True:
        i += 1
        if i == len(s) - 2:
            break
        elif s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
            i = -1
            if len(s) == 2:
                return 1

    return 0