# itertools combination - 1번 테스트 케이스 시간초과
import itertools

def solution(clothes):
    answer = 0
    clothes_type = []
    # clothes_types 배열에 의상의 종류 담기
    for i in range(len(clothes)):
        if clothes[i][1] not in clothes_type:
            clothes_type.append(clothes[i][1])
    # 같은 종류인 의상 개수 배열에 담기
    graph = [0] * len(clothes_type)
    for i in range(len(clothes)):
        idx = clothes_type.index(clothes[i][1])
        graph[idx] += 1

    # 배열 원소들의 곱셈의 합 구하는 함수
    def mul(arr):
        sum = 0
        for i in range(len(arr)):
            ans = 1
            for j in range(len(arr[0])):
                ans *= arr[i][j]
            sum += ans
        return sum

    for i in range(1, len(clothes_type) + 1):
        arr = list(itertools.combinations(graph, i))
        answer += mul(arr)

    return answer