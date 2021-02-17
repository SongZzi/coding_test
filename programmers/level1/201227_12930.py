def solution(s):
    answer = ''
    n = 0

    for i in range(len(s)):
        if s[i] == ' ':
            answer = answer + ' '
            n = 0
        else:
            if n % 2 == 0:
                if ord(s[i]) >= 97:
                    answer = answer + s[i].upper()
                    n = n + 1
                elif ord(s[i]) < 91:
                    answer = answer + s[i]
                    n = n + 1
            elif n % 2 != 0:
                if ord(s[i]) < 91:
                    answer = answer + s[i].lower()
                    n = n + 1
                elif ord(s[i]) >= 97:
                    answer = answer + s[i]
                    n = n + 1

    return answer