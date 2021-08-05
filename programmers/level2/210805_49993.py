#풀이1
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

#풀이2
def solution(skill, skill_trees):
    result = 0

    for i in range(len(skill_trees)):
        skill_list = list(skill)

        for n in skill_trees[i]:
            if n in skill_list:
                if n != skill_list[0]:
                    break
                else:
                    skill_list.pop(0)
        else:
            result += 1

    return result