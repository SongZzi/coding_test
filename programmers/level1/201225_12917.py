def solution(s):
    answer = []

    for i in range(len(s)):
        answer.append(s[i])

    answer.sort()
    answer.reverse()
    answer = ''.join(answer)

    return answer