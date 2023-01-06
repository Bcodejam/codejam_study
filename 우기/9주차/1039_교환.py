import sys
from collections import deque

read = sys.stdin.readline

ans = -1
n, k = map(int, read().rstrip().split())
q = deque()
visited = set()

q.append((n, 0))
visited.add((n, 0))

while q:
    x, cost = q.popleft()

    if cost == k:
        ans = max(ans, x)
        continue

    xs = list(str(x))
    for i in range(len(xs)):
        for j in range(len(xs)):
            if i == j:
                continue

            nxs = xs[:]
            nxs[i], nxs[j] = nxs[j], nxs[i]

            if nxs[0] == "0":
                continue

            nx = int("".join(nxs))
            ncost = cost + 1
            nstate = (nx, ncost)

            if nstate not in visited:
                q.append(nstate)
                visited.add(nstate)

print(ans)
