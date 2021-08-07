import math
from itertools import permutations

def is_prime_number(x): #소수 판별 함수
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    arr = []
    num_list = []

    for num in numbers: #입력받은 문자열 각각 배열에 담기
        arr.append(num)

    for i in range(1, len(numbers) + 1):
        new_arr = list(permutations(arr, i))
        for j in range(len(new_arr)):
            num = "".join(new_arr[j])
            if num[0] != '0' and num not in num_list:
                num_list.append(num) #조합으로 만들 수 있는 숫자 num_list에 담기

    for n in num_list:
        if int(n) > 1 and is_prime_number(int(n)) == True: #소수인 경우
            answer += 1

    return answer