#풀이1 - replace() 사용
def solution(s):
    a = 0
    b = 0
    while len(s) != 1:
        a += 1
        for n in s:
            if n == '0':
                s = s.replace('0', '')
                b += 1
        s = bin(len(s))[2:]

    return [a, b]

#풀이2 - count() 사용
def solution(s):
    a = 0
    b = 0
    while len(s) != 1:
        a += 1
        b += s.count('0')
        s = bin(s.count('1'))[2:]

    return [a, b]