from collections import deque
#nxm, k=이동 횟수 입력받기
n,m,k=map(int, input().split())
#지도에 쓰여있는 수 2차원 배열 입력받기
array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

#주사위 초기화
dice=[[0,2,0],[4,1,3],[0,5,0],[0,6,0]]

dx=[-1,1,0,0]#상,하,좌,우
dy=[0,0,-1,1]#상,하,좌,우

#(x,y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 구하기 - bfs(x,y)
queue=deque()
def bfs(x,y):
    # 방문 여부 검사 배열
    visited = [[0] * m for i in range(n)]
    num=0
    queue.append((x,y))
    visited[x][y]=1
    while queue:
        num+=1
        x=queue[0][0]
        y=queue[0][1]
        queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if array[nx][ny]==array[x][y] and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    queue.append((nx,ny))
    return num

#주사위 방향 함수
def dice_direction(x,y,direction):
    if direction=='e':
        if y+1>=m:
            return 'w'
        else:
            return direction
    elif direction=='w':
        if y-1<0:
            return 'e'
        else:
            return direction
    elif direction=='s':
        if x+1>=n:
            return 'n'
        else:
            return direction
    elif direction=='n':
        if x-1<0:
            return 's'
        else:
            return direction
#주사위 이동 함수
def dice_num(i,x,y):
    dx=x
    dy=y
    if i==0 or direction=='e': #주사위 처음 이동 방향 - 동쪽 방향
        d1 = dice[1][0]
        d2 = dice[1][1]
        d3 = dice[1][2]
        d4 = dice[3][1]
        dice[1][1] = d1
        dice[1][2] = d2
        dice[3][1] = d3
        dice[1][0] = d4
        dy+=1
    elif direction=='w': #서쪽 방향
        d1 = dice[1][0]
        d2 = dice[1][1]
        d3 = dice[1][2]
        d4 = dice[3][1]
        dice[3][1] = d1
        dice[1][0] = d2
        dice[1][1] = d3
        dice[1][2] = d4
        dy-=1
    elif direction=='s': #남쪽 방향
        d1 = dice[0][1]
        d2 = dice[1][1]
        d3 = dice[2][1]
        d4 = dice[3][1]
        dice[1][1] = d1
        dice[2][1] = d2
        dice[3][1] = d3
        dice[0][1] = d4
        dx+=1
    elif direction=='n': #북쪽 방향
        d1 = dice[0][1]
        d2 = dice[1][1]
        d3 = dice[2][1]
        d4 = dice[3][1]
        dice[3][1] = d1
        dice[0][1] = d2
        dice[1][1] = d3
        dice[2][1] = d4
        dx-=1
    return dice[3][1], dx, dy

#k 이동 횟수 만큼 돌리기
a=0
b=0
score=0
for i in range(k):
    if i==0:
        direction='e'
    direction=dice_direction(a,b,direction)
    A,a,b=dice_num(i,a,b) #주사위의 아랫면에 있는 정수 A
    C=bfs(a,b) #(x,y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C 점수 획득
    B=array[a][b] #칸 (x,y)에 있는 정수 B
    if A>B: #90도 시계방향 회전
        if direction == 'e':
            direction='s'
        elif direction == 'w':
            direction='n'
        elif direction == 's':
            direction='w'
        elif direction == 'n':
            direction='e'
    elif A<B: #90도 반시계방향 회전
        if direction == 'e':
            direction='n'
        elif direction == 'w':
            direction='s'
        elif direction == 's':
            direction='e'
        elif direction == 'n':
            direction='w'
    score+=B*C

print(score)