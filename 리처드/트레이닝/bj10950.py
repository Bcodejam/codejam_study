import sys

input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n):
    a,b = map(int, input().rstrip().split())
    print(a+b)
