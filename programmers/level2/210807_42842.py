import math

divisor_list = []

def carpet_size(w, h, brown, yellow):
    if w * 2 + h * 2 - 4 == brown and (w - 2) * (h - 2) == yellow:
        return True

def divisor(x):
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if i >= x // i:
                divisor_list.append((i, x // i))
            else:
                divisor_list.append((x // i, i))

def solution(brown, yellow):
    answer = []
    divisor(brown + yellow)

    for i in range(len(divisor_list)):
        if carpet_size(divisor_list[i][0], divisor_list[i][1], brown, yellow) == True:
            answer.append(divisor_list[i][0])
            answer.append(divisor_list[i][1])

    return answer