import math

def solution(brown, yellow):
    answer = []

    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i == 0:  # i가 약수인 경우
            if (i + yellow // i) * 2 + 4 == brown:
                answer.append(i + 2)
                answer.append(yellow // i + 2)
                break

    answer.sort(reverse=True)  # 내림차순 정렬 (가로 길이 >= 세로 길이)
    return answer