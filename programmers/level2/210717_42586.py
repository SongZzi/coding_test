def solution(progresses, speeds):
    answer = []
    arr = []

    for i in range(len(progresses)):  # 배포 가능 날짜 계산
        if (100 - progresses[i]) % speeds[i] > 0:
            arr.append((100 - progresses[i]) // speeds[i] + 1)
        else:
            arr.append((100 - progresses[i]) // speeds[i])

    max = arr[0]
    sum = 1

    for i in range(1, len(arr)):
        if max >= arr[i]:
            sum = sum + 1
        else:
            answer.append(sum)
            max = arr[i]
            sum = 1

    answer.append(sum)

    return answer