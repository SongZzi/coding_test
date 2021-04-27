def solution(dartResult):
    answer = []
    flag = 'false'
    for i in range(len(dartResult)):
        if flag == 'false':
            if dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T' or dartResult[i] == '*' or \
                    dartResult[i] == '#':
                answer.append(dartResult[i])
                flag = 'false'
            else:
                flag = 'true'
        elif flag == 'true':
            if dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T' or dartResult[i] == '*' or \
                    dartResult[i] == '#':
                answer.append(dartResult[i - 1])
                answer.append(dartResult[i])
                flag = 'false'
            else:
                answer.append(dartResult[i - 1:i + 1])
                flag = 'false'

    type1 = [0, 0, 0]
    type2 = [0, 0, 0]
    result = 0
    k = -1

    for i in range(len(answer)):
        if i == 2:
            if answer[i] == '*':
                type1[0] = 1
            elif answer[i] == '#':
                type2[0] = 1
        elif i == 4 or i == 5:
            if answer[i] == '*':
                type1[1] = 1
            elif answer[i] == '#':
                type2[1] = 1
        elif i == 6 or i == 7 or i == 8:
            if answer[i] == '*':
                type1[2] = 1
            elif answer[i] == '#':
                type2[2] = 1

    for i in range(len(answer)):
        number = 0
        if answer[i] == "S":
            k = k + 1
            number = int(answer[i - 1])
            if type2[k] == 1:
                number = number * (-1)
            for j in range(k, len(type1)):
                if k == 0:
                    if j < 2 and type1[j] == 1:
                        number = number * 2
                else:
                    if type1[j] == 1:
                        number = number * 2
            result = result + number
        elif answer[i] == "D":
            k = k + 1
            number = int(answer[i - 1]) ** 2
            if type2[k] == 1:
                number = number * (-1)
            for j in range(k, len(type1)):
                if k == 0:
                    if j < 2 and type1[j] == 1:
                        number = number * 2
                else:
                    if type1[j] == 1:
                        number = number * 2
            result = result + number
        elif answer[i] == "T":
            k = k + 1
            number = int(answer[i - 1]) ** 3
            if type2[k] == 1:
                number = number * (-1)
            for j in range(k, len(type1)):
                if k == 0:
                    if j < 2 and type1[j] == 1:
                        number = number * 2
                else:
                    if type1[j] == 1:
                        number = number * 2
            result = result + number

    return result