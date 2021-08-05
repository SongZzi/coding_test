def solution(skill, skill_trees):
    result = 0

    for i in range(len(skill_trees)):
        answer = 0
        order = []
        flag = 'true'
        for j in range(len(skill)):
            if skill[j] in skill_trees[i]:
                if flag == 'true':  # 가능한 스킬트리인 경우
                    order.append(skill_trees[i].index(skill[j]))
                else:  # 불가능한 스킬트리인 경우
                    answer = -1
                    break
            else:
                flag = 'false'

        if answer != -1 and order == sorted(order):
            result += 1

    return result