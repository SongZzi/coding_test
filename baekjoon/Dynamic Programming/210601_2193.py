n=int(input())
arr=[1,1]

for i in range(2, n):
    number=arr[i-2]+arr[i-1]
    arr.append(number)
print(arr[-1])