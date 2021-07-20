def solution(phone_book):
    answer = True
    phone_book.sort()  #전화번호 숫자 오름차순으로 정렬

    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]) == True: #다음 전화번호의 접두어인 경우
            answer = False
            break

    return answer