def solution(prices):
    answer = []

    for i in range(len(prices)):
        cnt = 0
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:  # 주식가격이 떨어진 경우
                cnt += 1
                break
            else:  # 주식가격이 떨어지지 않은 경우
                cnt += 1
        answer.append(cnt)

    return answer