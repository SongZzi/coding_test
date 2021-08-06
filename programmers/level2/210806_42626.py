#효율성테스트 실패
import sys
sys.setrecursionlimit(10 ** 7)

def solution(scoville, K):
    result = 0
    cnt = 0

    while min(scoville) < K:
        if len(scoville) == 1:  #모든 음식의 스코빌 지수를 k이상으로 만들 수 없는 경우
            cnt = -1
            break
        cnt += 1
        first = min(scoville)
        scoville.remove(first)
        second = min(scoville)
        scoville.remove(second)

        result = first + second * 2
        scoville.append(result)
    return cnt