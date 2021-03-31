a, b=input().split()

day=[31,28,31,30,31,30,31,31,30,31,30,31]
result=['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
num=0

for i in range(1, int(a)):
    num=num+day[i-1]

print(result[(num+int(b))%7])