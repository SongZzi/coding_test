#풀이1 - '1'개수 구하는 함수 직접 구현
def count1(n):
    total = 0
    for num in n:
        if num == '1':
            total += 1
    return total

def solution(n):
    bin_num = count1(bin(n))

    while True:
        n += 1
        if count1(bin(n)) == bin_num:
            return n

#풀이2 - count() 사용
def solution(n):
    bin_num = bin(n).count('1')

    while True:
        n += 1
        if bin(n).count('1') == bin_num:
            return n