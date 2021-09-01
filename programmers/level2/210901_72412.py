#효율성테스트 시간초과
def solution(info, query):
    info_list = []
    query_list = []
    answer = [0] * len(query)

    for i in range(len(info)):
        string = info[i].split()
        info_list.append(string)

    for k in range(len(info_list)):
        for i in range(len(query)):
            string = query[i].split()
            num = 0
            for j in range(len(string)):
                flag = "true"
                if j == len(string) - 1:
                    if int(string[j]) > int(info_list[k][-1]):
                        flag = "false"
                elif string[j] != "and" and string[j] != "-":
                    if string[j] not in info_list[k]:
                        flag = "false"
                        break
            if flag == "true":
                answer[i] = answer[i] + 1

    return answer