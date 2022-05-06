def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices) - 1):
        cnt = 0
        for j in range(i + 1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:  # 주식 가격이 떨어지는 경우
                break
        answer[i] = cnt

    return answer