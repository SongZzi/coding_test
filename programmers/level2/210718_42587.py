def solution(priorities, location):
    n = 0
    seq = []

    for i in range(len(priorities)):
        seq.append(i)

    while n < len(seq):
        if priorities[n] >= max(priorities):  # 가장 앞 문서의 중요도가 가장 높은 경우
            priorities[n] = -1
            n = n + 1
        else:  # 나머지 인쇄 대기목록에 중요도가 더 높은 문서가 존재하는 경우
            priorities.append(priorities[n])
            priorities.pop(n)
            seq.append(seq[n])
            seq.pop(n)

    return seq.index(location) + 1