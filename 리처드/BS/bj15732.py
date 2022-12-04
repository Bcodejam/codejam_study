import sys

input = sys.stdin.readline

n,k,d = map(int, input().rstrip().split())

list_n = []

for _ in range(k):
    list_n.append(list(map(int, input().rstrip().split())))
l = 0
r = 1000000
mid = (l+r)//2


def func(m):
    ret = 0
    for i in range(k):
        if list_n[i][0] <= m:
            ret += ((min(list_n[i][1], m) - list_n[i][0]) // list_n[i][2]) + 1
    return ret


while True:
    if r-l <= 1:
        break
    if func(mid) >= d:
        r = mid
        mid = (l + r) // 2
    else:
        l = mid
        mid = (r + l) //2
print(r)