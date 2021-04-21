n=int(input())
dp=[0,9]

for i in range(2, n+1):
    dp.append(dp[i-1]*2-(i-1))

print(dp[n]%1000000000)