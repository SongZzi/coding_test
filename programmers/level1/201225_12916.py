def solution(s):
    answer = True
    t1 = 0
    t2 = 0

    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            t1 = t1 + 1
        elif s[i] == 'y' or s[i] == 'Y':
            t2 = t2 + 1

    if t1 == t2:
        answer = True
    else:
        answer = False

    return answer