import numpy as np

def solution(citations):
    arr = []
    citations.sort()
    x = np.array(citations)
    h = [0]

    for i in range(max(citations)):
        arr = x[np.where(x >= i)]  # i번 이상 인용된 논문
        if len(arr) >= i and len(citations) - len(arr) <= i:  #i번 이상 인용된 논문이 i편 이상 & 나머지 논문이 i번 이하 인용된 경우
            h[0] = i

    return h[0]