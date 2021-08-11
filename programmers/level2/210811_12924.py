def number(start, target):
    total = 0
    for i in range(start, target + 1):
        total += i
        if total == target:
            return True
        elif total > target:
            return False

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if number(i, n) == True: #연속한 자연수들로 표현할 수 있는 경우
            answer += 1

    return answer