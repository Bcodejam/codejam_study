import sys

input = sys.stdin.readline

n = int(input().rstrip())

map_n = []

for i in range(n):
    map_n.append(list(input().rstrip()))

def func(n, x, y):
    if n == 1:
        return map_n[x][y]
    chk = True
    s = ''
    st_val = map_n[x][y]
    for i in range(n):
        for j in range(n):
            if st_val != map_n[x+i][y+j]:
                chk = False
    if chk:
        return st_val
    else:
        return "(" + func(n//2, x, y) + func(n//2, x, y + n//2) + func(n//2, x + n//2, y) + func(n//2, x + n//2, y + n//2) + ")"

print(func(n, 0, 0))