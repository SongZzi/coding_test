#풀이
n=int(input())

for i in range(n):
    k = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]  # row=2인 2차원 배열 입력
    arr[0][1]=arr[0][1]+arr[1][0] #대각선 왼쪽값 더하기
    arr[1][1]=arr[1][1]+arr[0][0]
    for j in range(2,k):
        arr[0][j]=max(arr[1][j-1],arr[1][j-2])+arr[0][j] #대각선 왼쪽값과 그것의 왼쪽값 중 최대값 선택
        arr[1][j]=max(arr[0][j-1],arr[0][j-2])+arr[1][j]
    print(max(arr[0][k-1],arr[1][k-1]))

