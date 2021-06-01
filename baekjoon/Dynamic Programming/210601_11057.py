n=int(input())
result=0
arr=[1,2,3,4,5,6,7,8,9,10]

if n==1:
    result=10
else:
    for i in range(1, n):
        array=[1]
        number = arr[0]
        for j in range(1, 10):
            number=number+arr[j]
            array.append(number)
        arr=[]
        arr.extend(array)
    result=array[-1]

print(result%10007)

