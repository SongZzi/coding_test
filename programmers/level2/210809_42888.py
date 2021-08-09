#정확성: 75.0/100.0 (나머지 시간초과)
def solution(record):
    answer = []
    arr = []
    user_id = [] #유저아이디
    nickname = [] #닉네임

    for i in range(len(record)):
        arr.append(record[i].split())
        if arr[i][0] == "Enter":
            if arr[i][1] not in user_id:
                user_id.append(arr[i][1])
                nickname.append(arr[i][2])
            else:
                nickname[user_id.index(arr[i][1])] = arr[i][2]
        elif arr[i][0] == "Change":
            nickname[user_id.index(arr[i][1])] = arr[i][2]

    for i in range(len(arr)):
        if arr[i][0] == "Enter":
            answer.append(nickname[user_id.index(arr[i][1])] + "님이 들어왔습니다.")
        elif arr[i][0] == "Leave":
            answer.append(nickname[user_id.index(arr[i][1])] + "님이 나갔습니다.")

    return answer