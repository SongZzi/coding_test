#시간 초과
import itertools

def solution(numbers):
    answer = []
    arr = list(itertools.permutations(numbers, len(numbers)))

    for i in range(len(arr)):
        answer.append(int("".join(map(str, arr[i]))))

    return str(max(answer))