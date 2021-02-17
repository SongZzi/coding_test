#입력값 받기
n, m=input().split()
#Red 위치
x=0
y=0
#Blue 위치
z=0
w=0
#탐색할 위치
loc = 0
listArr=[]

for i in range(int(n)):
    inputStr = input()
    arr = list(inputStr)
    listArr.append(arr)

for i in range(len(listArr)):
    for j in range(len(listArr[i])):
        #print(listArr[i][j])
        if listArr[i][j] == "R":
            x = i
            y = j
        elif listArr[i][j] == "B":
            z=i
            w=j

a=x
b=y
num=0
while True:
    if(num<10):
        if (a - 1 > 0 and a - 1 < int(n) and b > 0 and b < int(m) and listArr[a - 1][b] == "O"):
            if loc == 1:
                print(num)
            else:
                print(num+1)
            break
        elif (a > 0 and a < int(n) and b + 1 > 0 and b + 1 < int(m) and listArr[a][b + 1] == "O"):
            if loc == 2:
                print(num)
            else:
                print(num + 1)
            break
        elif (a + 1 > 0 and a + 1 < int(n) and b > 0 and b < int(m) and listArr[a+1][b] == "O"):
            if loc == 3:
                print(num)
            else:
                print(num + 1)
            break
        elif (a > 0 and a < int(n) and b - 1 > 0 and b - 1 < int(m) and listArr[a][b - 1] == "O"):
            if loc == 4:
                print(num)
            else:
                print(num + 1)
            break
        elif(a-1>0 and a-1<int(n) and b>0 and b<int(m) and listArr[a-1][b] == "."):
            a=a-1
            print(loc)
            if loc != 1:
                num = num+1
            loc=1
            #print("top:",num)
            continue
        elif(a>0 and a<int(n) and b+1>0 and b+1<int(m) and listArr[a][b+1] == "."):
            b=b+1
            print(loc)
            if loc != 2:
                num = num + 1
            loc = 2
            #print("right:",num)
            continue
        elif(a+1>0 and a+1<int(n) and b>0 and b<int(m) and listArr[a+1][b] == "."):
            a=a+1
            print(loc)
            if loc != 3:
                num = num + 1
            loc = 3
            #print("bottom:",num)
            continue
        elif(a>0 and a<int(n) and b-1>0 and b-1<int(m) and listArr[a][b-1] == "."):
            b=b-1
            print(loc)
            if loc != 4:
                num = num + 1
            loc = 4
            #print("left:",num)
            continue

    elif(num >= 10):
        print(-1)
        break
