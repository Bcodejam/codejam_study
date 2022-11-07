import sys

input = sys.stdin.readline

n, l = map(int, input().rstrip().split())

list_n = list(map(int, input().rstrip().split()))

ans = 1
list_n.sort()
top = list_n.pop(0)

while list_n:
    val = list_n.pop(0)
    if val-top > l-1:
        top = val
        ans += 1

print(ans)