def solution(arr1, arr2):
    # arr1 = ixj / arr2 = jxk
    answer = [[] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for k in range(len(arr2[0])):
            num = 0
            for j in range(len(arr1[0])):
                num += arr1[i][j] * arr2[j][k]
            answer[i].append(num)

    return answer