import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

t = [[0, 0]]
d = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    t.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        w = t[i][0]
        v = t[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][m])