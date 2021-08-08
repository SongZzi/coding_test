def solution(people, limit):
    answer = 0
    people.sort(reverse=True) #내림차순 정렬
    j = len(people) - 1

    for i in range(len(people)):
        if i <= j:
            if people[i] + people[j] <= limit: #몸무게가 제일 작은 사람과 함께 구출할 수 있는 경우
                answer += 1
                people[j] = 250 #구출한 사람 구분하기 위함
                j -= 1
            else:
                answer += 1

    return answer