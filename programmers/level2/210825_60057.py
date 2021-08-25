def solution(s):
    length = len(s) // 2
    result = s

    for i in range(1, length + 1):
        cnt = 1
        s_list = []
        string = s
        answer = ''

        if len(s) % i == 0:
            num = len(s) // i
        else:
            num = len(s) // i + 1

        for j in range(num): #문자열 num 단위로 자르고 배열에 담기
            s_list.append(string[:i])
            string = string[i:]

        for k in range(len(s_list) - 1): #문자열 압축하기
            if s_list[k] == s_list[k + 1]:
                cnt += 1
                if k == len(s_list) - 2:
                    answer += str(cnt) + s_list[k]
            else:
                if cnt != 1:
                    answer += str(cnt) + s_list[k]
                else:
                    answer += s_list[k]

                if k == len(s_list) - 2:
                    answer += s_list[k + 1]
                cnt = 1

        if len(result) >= len(answer): #압축한 문자열 중 가장 짧은 것 찾기
            result = answer

    return len(result)