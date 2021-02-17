n= input()

arr=[0 for _ in range(int(n))]

for i in range(int(n)):
    arr[i]=list(map(int, input().split()))

num=0
number=0
value=0
result=[]

while True:
    if(number < int(n)):
        if (number + arr[number][0] <= int(n)):
            if(number < int(n)-1):
                if(number>0 and arr[number+1][1] > arr[number][1] and (arr[number][0] != 1 or arr[number+1][0] != 1)):
                    value=value+arr[number][1]
                    if arr[number+1][0] == 1:
                        number=number+2
                    else:
                        number=number+arr[number+1][0]
                else:
                    value=value+arr[number][1]
                    if arr[number][0] == 1:
                        number= number+1
                    else:
                        number=number+arr[number][0]
            else:
                value = value + arr[number][1]
                if arr[number][0] == 1:
                    number = number + 1
                else:
                    number = number + arr[number][0]
        else:
            result.append(value)
            value=0
            if(num+1 < int(n)):
                num=num+1
                number=num
            else:
                break
    else:
        result.append(value)
        value = 0
        if (num + 1 < int(n)):
            num = num + 1
            number = num
        else:
            break

print(max(result))
