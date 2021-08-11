#풀이1 - upper(), lower() 사용
def solution(s):
    answer = ''
    arr = []
    s = s.split(' ')

    for i in range(len(s)):
        arr.append(list(s[i]))

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j == 0 and arr[i][j].islower() == True:
                arr[i][j] = arr[i][j].upper()
            elif j > 0 and arr[i][j].isupper() == True:
                arr[i][j] = arr[i][j].lower()
        answer += ''.join(arr[i]) + ' '

    return answer[:-1]

#풀이2 - capitalize()사용
def solution(s):
    answer = ''
    s = s.split(' ')

    for i in range(len(s)):
        answer += s[i].capitalize() + " "

    return answer[:-1]