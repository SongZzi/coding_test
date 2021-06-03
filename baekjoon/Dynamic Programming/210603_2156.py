#풀이
n=int(input())
num=[0]
dp=[0]

for i in range(n):
    num.append(int(input()))

dp.append(num[1])
if n>1:
    dp.append(num[1]+num[2])
for i in range(3, n+1):
    dp.append(max(num[i]+num[i-1]+dp[i-3], num[i]+dp[i-2], dp[i-1]))

print(dp[-1])
