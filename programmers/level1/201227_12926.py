def solution(s, n):
    answer = ''

    for a in range(len(s)):
        num = ord(s[a]) + n
        if ord(s[a]) >= 65 and ord(s[a]) < 91:
            if ord(s[a]) + n > 90:
                answer = answer + chr(ord(s[a]) - 25 + n - 1)
            else:
                answer = answer + chr(ord(s[a]) + n)
        elif ord(s[a]) >= 97 and ord(s[a]) < 123:
            if ord(s[a]) + n > 122:
                answer = answer + chr(ord(s[a]) - 25 + n - 1)
            else:
                answer = answer + chr(ord(s[a]) + n)
        else:
            answer = answer + ' '

    return answer