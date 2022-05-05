import math

# 최소공배수(LCM) 함수
def LCM(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    n = arr[0]

    for i in range(1, len(arr)):
        n = LCM(n, arr[i])

    return n