def solution(priorities, location):
    answer = 0
    arr = [0] * len(priorities)
    arr[location] = 1  # 인쇄 요청한 문서의 위치 표시

    while True:
        if priorities[0] == max(priorities):  # 가장 앞에 있는 문서의 중요도가 가장 높은 경우
            priorities.pop(0)
            num = arr.pop(0)
            answer += 1
            if num == 1:  # 요청한 문서가 인쇄되는 경우
                break
        else:  # 나머지 인쇄 대기목록에 중요도가 더 높은 문서가 존재하는 경우
            priorities.append(priorities.pop(0))
            arr.append(arr.pop(0))

    return answer