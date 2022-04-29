#곱하기 혹은 더하기

#문자열 s 입력받기
s=input()
#문자열 s -> int 배열로 변환
s=list(map(int, s))
#num에 첫번째 숫자 저장
num=s[0]

for i in range(1, len(s)):
    if num >= 2 and s[i] >= 2: #두 수 모두 2 이상인 경우 곱하기 수행
        num*=s[i]
    else:
        num+=s[i]

print(num)
