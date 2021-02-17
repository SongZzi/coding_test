def solution(numbers):
    answer = []
    num = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                num = numbers[i] + numbers[j]
                answer.append(num)

    answer = list(set(answer))
    answer.sort()

    return answer