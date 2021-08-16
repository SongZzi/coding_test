A,P=map(int,input().split())
arr=[A]

def number(a,p):
    num=0
    a=str(a)
    for i in range(len(a)):
        num+=int(a[i])**p
    return num

while True:
    A=number(A,P)
    if A in arr: #반복되는 부분을 찾은 경우
        result=arr.index(A)
        break
    arr.append(A)

print(result)
