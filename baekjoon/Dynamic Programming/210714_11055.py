n=int(input())
arr=list(map(int, input().split()))
dp=[0 for i in range(n)]

dp[0]=arr[0]

for i in range(1, n):
    dp[i]=arr[i]
    for j in range(i):
        if arr[j]<arr[i]: #현재 값이 이전 값보다 큰 경우
            dp[i]=max(dp[i],dp[j]+arr[i]) #현재 dp값과 이전 dp값+현재값 중 최대값

print(max(dp))