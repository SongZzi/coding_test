#풀이
n=int(input())
arr=list(map(int, input().split()))
dp=[1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[j]<arr[i]: #이전 값이 작은 경우
            dp[i]=max(dp[i], dp[j]+1) #현재 dp값과 이전 dp값 중 최대값 + 1

print(max(dp))

