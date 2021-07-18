#효율성 테스트 x
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)

    for i in range(len(phone_book) - 1):
        for j in range(len(phone_book)):
            if i != j and len(phone_book[j]) > len(phone_book[i]) and phone_book[j].startswith(phone_book[i]) == True:
                answer = False
                break

    return answer