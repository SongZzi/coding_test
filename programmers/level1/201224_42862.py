def solution(n, lost, reserve):
    num = n - len(lost)

    for a in lost:
        if a in reserve:
            num = num + 1
            reserve.remove(a)
            continue
        elif a - 1 in reserve:
            num = num + 1
            reserve.remove(a - 1)
        elif a + 1 in reserve and lost.count(a + 1) == 0:
            num = num + 1
            reserve.remove(a + 1)

    return num