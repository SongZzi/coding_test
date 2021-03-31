n=int(input())

for i in range(1, n):
    print('*'*i+' '*(n-i)+' '*(n-i)+'*'*i)
for j in range(n, 0, -1):
    print('*'*j+' '*(n-j)+' '*(n-j)+'*'*j)