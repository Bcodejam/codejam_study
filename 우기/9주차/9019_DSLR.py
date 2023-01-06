import sys
from collections import deque

read = sys.stdin.readline
ops = ["D", "S", "L", "R"]


def operation(v, ch):
    ret = int(v)
    if ch == 'D':
        ret *= 2
        ret %= 10000
    elif ch == 'S':
        ret -= 1
        if ret == -1:
            ret = 9999
    elif ch == 'L':
        ret = v[1] + v[2] + v[3] + v[0]
        ret = int(ret)
    elif ch == 'R':
        ret = v[3] + v[0] + v[1] + v[2]

    return str(ret).zfill(4)


def bfs(start, target):
    q = deque([(start, "")])
    visited = [False] * 10001

    while q:
        x, history = q.popleft()

        if x == target:
            print(history)
            return

        visited[int(x)] = True

        for op in ops:
            nx = operation(x, op)
            if not visited[int(nx)]:
                q.append((nx, history + op))
                visited[int(nx)] = True


tc = int(read())
for _ in range(tc):
    a, b = read().rstrip().split()
    a, b = str(a).zfill(4), str(b).zfill(4)
    bfs(a, b)