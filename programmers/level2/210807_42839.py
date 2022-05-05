import itertools
import math

# 소수 판별 함수
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):  # 2부터 x의 제곱근까지 모든 수를 확인
        if x % i == 0:
            return False  # 소수 아님
    return True  # 소수 맞음

def solution(numbers):
    answer = 0
    arr = []

    for i in range(1, len(numbers) + 1):
        num = list(itertools.permutations(list(numbers), i))  # 순열 - itertools.permutations
        for j in range(len(num)):
            if int(''.join(num[j])) not in arr:
                arr.append(int(''.join(num[j])))  # 조합 가능한 모든 숫자 담기

    for i in range(len(arr)):
        if arr[i] > 1 and is_prime_number(arr[i]) == True:  # 소수인 경우
            answer += 1

    return answer