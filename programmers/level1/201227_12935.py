def solution(arr):
    answer = []
    new = []

    for a in arr:
        new.append(a)

    new.sort()

    if len(arr) == 0:
        answer.append(-1)
    elif len(arr) == 1 and arr[0] == 10:
        answer.append(-1)
    else:
        arr.remove(new[0])
        answer = arr

    return answer