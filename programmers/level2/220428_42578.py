#시간 초과 해결 - dictionary
def solution(clothes):
    answer = 1
    d = dict()  # dictionary 선언

    for i in range(len(clothes)):
        key = clothes[i][1]
        if key not in d:  # dictionary에 해당 key가 없는 경우
            d[key] = [clothes[i][0]]  # value - list 형태
        else:  # dictionary에 해당 key가 있는 경우
            d[key].append(clothes[i][0])

    for key in d:
        answer *= len(d[key]) + 1  # (value: 위장하기 위해 입는 경우의 수) + (1: 안 입는 경우)

    # 아무것도 입지 않은 경우 하나 제외
    return answer - 1