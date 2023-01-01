import sys, copy
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input().rstrip())

list_n = [[0]*n for _ in range(n)]

mi, ma = float('inf'), 0
for i in range(n):
    a = list(map(int, input().rstrip().split()))
    for j in range(n):
        list_n[j][i] = a[j]
        mi = min(mi, a[j])
        ma = max(ma, a[j])

def func(j,i,li):
    li[j][i] = 0

    for a,b in [(j+1,i),(j-1,i),(j,i+1),(j,i-1)]:
        if 0<=a<n and 0<=b<n and li[a][b] > 0:
            func(a,b,li)

    return
ans = 0
for k in range(max(mi-1,0), ma+1):
    list_n_tmp = copy.deepcopy(list_n)
    for i in range(n):
        for j in range(n):
            if list_n_tmp[j][i] < k:
                list_n_tmp[j][i] = 0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if list_n_tmp[j][i] > 0:
                func(j,i,list_n_tmp)
                cnt += 1
    ans = max(ans, cnt)

print(ans)