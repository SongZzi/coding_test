num = 0 #전역변수로 사용

def dfs(numbers, target, total, i):
    global num
    if i >= len(numbers):
        if total == target: #타겟 넘버인 경우
            num += 1
            return
        return
    else:
        dfs(numbers, target, total + numbers[i], i + 1)
        dfs(numbers, target, total - numbers[i], i + 1)


def solution(numbers, target):
    global num
    dfs(numbers, target, 0, 0)
    answer = num

    return answer