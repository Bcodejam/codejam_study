import sys

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(depth, pos, acc):
    global ans, visited

    x, y = pos
    visited[x][y] = True
    # print(depth, pos, acc)

    if depth == n:
        ans += acc
        visited[x][y] = False
        return

    for i in range(4):
        dx, dy = d[i]
        nx, ny = x + dx, y + dy
        if not visited[nx][ny]:
            dfs(depth + 1, (nx, ny), acc * p[i])

    visited[x][y] = False


input_arr = sys.stdin.readline().rstrip().split()

ans = 0
n = int(input_arr[0])
p = [x / 100 for x in list(map(int, input_arr[1:]))]
visited = [[False for _ in range(50)] for _ in range(50)]

dfs(0, (25, 25), 1)
print(ans)
