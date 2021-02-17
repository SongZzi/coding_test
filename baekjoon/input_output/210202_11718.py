#풀이1
while True:
    try:
        print(input())
    except EOFError:
        break
#풀이2
import sys
for i in sys.stdin:
    print(i, end='')