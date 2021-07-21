# 풀이
def solution(numbers):
    arr = list(map(str, numbers))

    arr.sort(key=lambda x: x * 3, reverse=True)  # x*3 기준으로 내림차순 정렬

    return str(int(''.join(arr)))  # 모든값이 0인 경우 처리