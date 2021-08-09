#딕셔너리(dictionary) -> 시간초과 해결
def solution(record):
    answer = []
    arr = []
    user_info = {}  #딕셔너리(dictionary) 선언

    for i in range(len(record)):
        arr.append(record[i].split())
        if arr[i][0] == "Enter" or arr[i][0] == "Change":
            user_info[arr[i][1]] = arr[i][2] #Key=유저아이디, Value=닉네임

    for i in range(len(arr)):
        if arr[i][0] == "Enter":
            answer.append(user_info[arr[i][1]] + "님이 들어왔습니다.")
        elif arr[i][0] == "Leave":
            answer.append(user_info[arr[i][1]] + "님이 나갔습니다.")

    return answer