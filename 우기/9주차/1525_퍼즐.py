import sys
from copy import deepcopy
from collections import deque


def flat(state):
    ret = ""
    for row in state:
        for num in row:
            ret += str(num)
    return ret


def reshape(state):
    ret = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(state[i * 3 + j])
        ret.append(row)
    return ret


def get_next_state(state):
    ret = []
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    z = None
    for i in range(3):
        for j in range(3):
            if state[i][j] == '0':
                z = (i, j)

    for dx, dy in d:
        nx, ny = z[0] + dx, z[1] + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = deepcopy(state)
            new_state[nx][ny], new_state[z[0]][z[1]] = new_state[z[0]][z[1]], new_state[nx][ny]
            ret.append(new_state)

    return ret


target = "123456780"
start = []
for _ in range(3):
    start.append(sys.stdin.readline().rstrip().split())

q = deque()
visited = set()

q.append((flat(start), 0))
visited.add(flat(start))

c = 0
while q:
    x, cost = q.popleft()
    c += 1
    visited.add(x)
    if x == target:
        print(cost)
        exit(0)
        break

    curr_state = reshape(x)
    for next_state in get_next_state(curr_state):
        f_next_state = flat(next_state)
        if f_next_state not in visited:
            q.append((f_next_state, cost + 1))
            visited.add(f_next_state)

print(-1)
