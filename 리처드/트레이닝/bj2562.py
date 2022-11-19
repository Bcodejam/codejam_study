import sys

input = sys.stdin.readline

ans = 0
ind = 0
for i in range(9):
    val = int(input().rstrip())
    if val > ans:
        ind = i+1
        ans = val
print(ans)
print(ind)