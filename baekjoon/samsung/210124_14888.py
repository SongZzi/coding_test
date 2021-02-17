import itertools

n= input()

arr = list(map(int, input().split()))
op = list(map(int, input().split()))
operator = []
answer=[]

for i in range(op[0]):
    operator.append('+')
for i in range(op[1]):
    operator.append('-')
for i in range(op[2]):
    operator.append('x')
for i in range(op[3]):
    operator.append('/')

result=list(set(itertools.permutations(operator)))
value=0

for i in range(len(result)):
    value = arr[0]
    for j in range(1, len(arr)):
        if(result[i][j-1] == '+'):
            value=value+arr[j]
        elif(result[i][j-1] == '-'):
            value=value-arr[j]
        elif(result[i][j-1] == 'x'):
            value=value*arr[j]
        elif(result[i][j-1] == '/'):
            if(value<0 and arr[j]>0):
                value=abs(value)//arr[j]
                value=-1*value
            else:
                value = value//arr[j]

        if(j == len(arr)-1):
            answer.append(value)

print(max(answer))
print(min(answer))
