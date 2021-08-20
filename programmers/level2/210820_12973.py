#stack 사용 -> 시간초과 해결
def solution(s):
    stack = []

    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        elif s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])

    if len(stack) == 0:
        return 1
    else:
        return 0