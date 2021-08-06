#heapq 사용 -> 효율성테스트 통과
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while scoville[0] < K:
        if len(scoville) == 1: #모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
            return -1
        cnt += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)

    return cnt