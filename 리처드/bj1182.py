import sys

input = sys.stdin.readline

n, s = map(int, input().rstrip().split())

list_n = list(map(int, input().rstrip().split()))

def func(sum, ind):
    if ind >= n:
        if sum == s: return 1
        else: return 0
    return func(sum+list_n[ind], ind+1) + func(sum, ind+1)

ans = func(0, 0)
if s == 0: print(ans-1)
else: print(ans)