#모험가 길드

#모험가 수 n 입력받기
n=int(input())
#각 모험가의 공포도 값 입력받기
arr=list(map(int, input().split()))
arr.sort() #오름차순 정렬

cnt=0 #현재 그룹에 포함된 모험가 수
result=0 #총 그룹 수

for i in range(len(arr)):
    cnt+=1
    if cnt >= arr[i]: #현재 그룹에 포함된 모험가 수 >= 현재 공포도, 그룹 결성
        result+=1 #총 그룹수 증가
        cnt=0 #현재 그룹에 포함된 모험가 수 초기화

print(result)