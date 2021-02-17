def solution(answers):
    answer = []
    stud = []
    r1 = 0
    r2 = 0
    r3 = 0

    t1 = [1, 2, 3, 4, 5]
    t2 = [2, 1, 2, 3, 2, 4, 2, 5]
    t3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == p1[i]:
            r1 = r1 + 1
        if answers[i] == p2[i]:
            r2 = r2 + 1
        if answers[i] == p3[i]:
            r3 = r3 + 1
        if i != 0 and i % 4 == 0:
            p1.extend(t1)
        if i != 0 and i % 7 == 0:
            p2.extend(t2)
        if i != 0 and i % 9 == 0:
            p3.extend(t3)

    stud.append(r1)
    stud.append(r2)
    stud.append(r3)

    if max(stud) == r1:
        answer.append(1)
    if max(stud) == r2:
        answer.append(2)
    if max(stud) == r3:
        answer.append(3)

    return answer