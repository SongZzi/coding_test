#문자열 재정렬

s=input()
result=[]
num=0

#문자열 하나씩 확인
for x in s:
    if x.isalpha(): #알파벳인 경우
        result.append(x)
    else: #숫자인 경우
        num+=int(x)

result.sort() #알파벳 오름차순 정렬

#숫자가 하나라도 존재하는 경우
if num!=0:
    result.append(str(num))

print(''.join(result)) #리스트를 문자열로 변환