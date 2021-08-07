#재귀함수로 구현시 시간초과 발생 -> for문으로 구현
def solution(n):
    answer = 0
    a = 0
    b = 1
    for i in range(1, n):
        answer = a + b
        a = b
        b = answer

    return answer % 1234567