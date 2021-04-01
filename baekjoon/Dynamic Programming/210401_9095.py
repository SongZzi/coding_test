n=int(input())

for i in range(0, n):
    dp=[0,1,2,4]
    m=int(input())
    for j in range(4, m+1):
        dp.append(dp[j-1]+dp[j-2]+dp[j-3])
    print(dp[m])
    dp=[]
