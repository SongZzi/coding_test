n=int(input())
arr=[]
dp=[0 for i in range(101)]

for i in range(n):
    arr.append(int(input()))

dp[1]=1
dp[2]=1
dp[3]=1
dp[4]=2
dp[5]=2
for i in range(6, 101):
    dp[i]=dp[i-5]+dp[i-1]

for i in range(n):
    print(dp[arr[i]])