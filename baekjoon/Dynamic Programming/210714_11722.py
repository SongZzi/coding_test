n=int(input())
arr=list(map(int, input().split()))
arr.reverse() #배열 순서 거꾸로 뒤집기
dp=[1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[j]<arr[i]: #현재값이 이전값보다 큰 경우
            dp[i]=max(dp[i], dp[j]+1) #현재dp값, 이전dp값+1 중 최대값

print(max(dp))