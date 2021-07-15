n=int(input())
arr=list(map(int, input().split()))
dp=[1 for i in range(n)]

dp[0]=arr[0]

for i in range(1, n):
    dp[i]=arr[i]
    dp[i]=max(dp[i], dp[i-1]+arr[i]) #이전값들 합의 최대값과 현재값 중 최대값

print(max(dp))