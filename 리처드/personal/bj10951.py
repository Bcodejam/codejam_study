import sys

input = sys.stdin.readline

while 1:
    try:
        a,b = map(int, input().rstrip().split())
        print(a+b)
    except:
        break
