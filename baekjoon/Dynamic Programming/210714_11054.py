n=int(input())
arr=list(map(int, input().split()))
dp1=[1 for i in range(n)]
dp2=[1 for i in range(n)]
dp=[0 for i in range(n)]
re_arr=list(reversed(arr))

for i in range(1, n):
    for j in range(i):
        if arr[j]<arr[i]:
            dp1[i]=max(dp1[i], dp1[j]+1) #가장 긴 증가하는 부분수열 dp 구하기
        if re_arr[j]<re_arr[i]:
            dp2[i]=max(dp2[i], dp2[j]+1) #거꾸로 가장 긴 증가하는 부분수열 dp 구하기

for i in range(n):
    dp[i]=dp1[i]+dp2[n-i-1] #dp에 dp1, dp2 뒤집은 값 합치기

print(max(dp)-1)
