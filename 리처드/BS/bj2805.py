import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

list_n = list(map(int, input().rstrip().split()))

list_n.sort(reverse=True)

cur_h = list_n[0]
ans = 0
tot_l = 0

while True:
    if ans >= m:
        break
    if tot_l != n:


print(cur_h)