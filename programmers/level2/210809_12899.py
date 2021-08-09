#효율성 테스트 실패(시간초과)
from itertools import product

def solution(n):
    answer = ''
    total = 0
    i = 1

    while True:
        total += 3 ** i
        if total >= n:
            total -= 3 ** i
            arr = list(product(['1', '2', '4'], repeat=i)) #중복순열
            answer = ''.join(arr[n - total - 1])
            break
        i += 1

    return answer