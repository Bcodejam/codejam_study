import sys

input = sys.stdin.readline

n = int(input().rstrip())

map_n = [[' ' for i in range(n)] for j in range(n)]

def func(l: int, x, y):
    if l == 3:
        for i in range(3):
            for j in range(3):
                if not(i == 1 and j == 1):
                    map_n[x+i][y+j] = '*'
        return
    else:
        div = l//3
        for i in range(3):
            for j in range(3):
                if not(i == 1 and j == 1):
                    func(div, x+(i*div), y+(j*div))

func(n, 0, 0)

for i in range(n):
    for j in range(n):
        print(map_n[i][j], end='')
    print()