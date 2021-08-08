def solution(s):
    queue = []

    for i in range(len(s)):
        if s[i] == "(":
            queue.append(0)
        elif s[i] == ")":
            if len(queue) == 0:
                return False
            else:
                queue.pop()

    if len(queue) == 0:
        return True
    else:
        return False