def solution(n, words):
    word_list=[]
    num=0
    turn=1

    for i in range(len(words)):
        if num==n:
            num=0
            turn+=1
        num+=1
        if words[i] not in word_list:
            if i==len(words)-1: #주어진 단어로만으로는 탈락자가 발생하지 않는 경우
                return [0,0]
            elif i>0 and word_list[-1][-1] != words[i][0]: #앞사람이 말한 단어의 마지막 문자로 시작하는 단어가 아닌 경우
                break
            word_list.append(words[i])
        else: #이전에 등장했던 단어를 말한 경우
            break

    return [num,turn]