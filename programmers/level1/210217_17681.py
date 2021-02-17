def solution(n, arr1, arr2):
    answer = []
    value1 = []
    value2 = []
    res = ""

    for i in range(int(n)):
        for m in range(int(n)):
            value1.append(0)
            value2.append(0)

        a = format(arr1[i], 'b')
        b = format(arr2[i], 'b')
        x = len(a)
        y = len(b)

        for j in range(int(n), int(n) - len(a), -1):
            value1[j - 1] = int(a[x - 1])
            x = x - 1

        for k in range(int(n), int(n) - len(b), -1):
            value2[k - 1] = int(b[y - 1])
            y = y - 1

        res = ""
        for z in range(int(n)):
            if value1[z] == 1 or value2[z] == 1:
                res = res + "#"
            elif value1[z] == 0 and value2[z] == 0:
                res = res + " "
        answer.append(str(res))

        value1 = []
        value2 = []

    return answer