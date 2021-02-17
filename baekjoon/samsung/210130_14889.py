import itertools

n= input()

arr=[0 for _ in range(int(n))]
number=[]
for i in range(int(n)):
    arr[i]=list(map(int, input().split()))
    number.append(i+1)

result=list(set(itertools.combinations(number, int(n)//2)))

answer=[]
length=len(result[0])

answer=[]
for i in range(len(result)):
    ab = []
    ab.extend(number)
    for j in range(length):
        ab.remove(result[i][j])
    steam=0
    lteam=0

    steam = steam + arr[result[i][0] - 1][result[i][length-1] - 1]
    steam = steam + arr[result[i][length-1] - 1][result[i][0] - 1]

    lteam = lteam + arr[ab[0]-1][ab[len(ab)-1]-1]
    lteam = lteam + arr[ab[len(ab)-1]-1][ab[0]-1]
    if(length > 2):
        for j in range(length-1):
            steam = steam + arr[result[i][j] - 1][result[i][j + 1] - 1]
            steam = steam + arr[result[i][j + 1] - 1][result[i][j] - 1]
        for k in range(len(ab)-1):
            lteam = lteam + arr[ab[k] - 1][ab[k + 1] - 1]
            lteam = lteam + arr[ab[k + 1] - 1][ab[k] - 1]
    answer.append(abs(steam-lteam))

print(min(answer))



