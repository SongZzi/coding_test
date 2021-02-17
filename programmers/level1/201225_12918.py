def solution(s):
    answer = True

    if len(s) == 4 or len(s) == 6:
        answer = True
        if s.isdigit() == False:
            answer = False
    else:
        answer = False

    return answer