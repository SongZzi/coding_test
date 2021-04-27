def solution(dartResult):
    answer = []
    result = 0
    new_dart = dartResult.replace("10", "Z")

    for i in range(len(new_dart)):
        if new_dart[i] == "Z":
            answer.append("10")
        else:
            answer.append(new_dart[i])

    bonus = ["S", "D", "T"]
    option1 = [0, 0, 0]
    option2 = [0, 0, 0]
    k = -1

    for i in range(len(answer)):
        if i == 2:
            if answer[i] == '*':
                option1[0] = 1
            elif answer[i] == '#':
                option2[0] = 1
        elif i == 4 or i == 5:
            if answer[i] == '*':
                option1[1] = 1
            elif answer[i] == '#':
                option2[1] = 1
        elif i == 6 or i == 7 or i == 8:
            if answer[i] == '*':
                option1[2] = 1
            elif answer[i] == '#':
                option2[2] = 1

    for i in range(len(answer)):
        number = 0
        for n in range(len(bonus)):
            if answer[i] == bonus[n]:
                number = int(answer[i - 1]) ** (n + 1)
                k = k + 1
                if option2[k] == 1:
                    number = number * (-1)
                for j in range(k, len(option1)):
                    if k == 0:
                        if j < 2 and option1[j] == 1:
                            number = number * 2
                    else:
                        if option1[j] == 1:
                            number = number * 2
                result = result + number

    return result