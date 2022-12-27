# coding=utf-8
import sys
sys.setrecursionlimit(15000)

# 상하좌우
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]


# 유효한 좌표인지 체크
def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n


# DFS 돌려서 카운트
def dfs(x, y, rain, visited):
    visited[x][y] = True

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny) and not visited[nx][ny]:
            if area[nx][ny] > rain:
                dfs(nx, ny, rain, visited)


ans = -1
n = int(sys.stdin.readline().rstrip())
area = []

# 최대 높이 저장
max_h = -1

for _ in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    max_h = max(max_h, max(row))
    area.append(row)

# 가능한 비의 양만큼 모두 계산
for r in range(max_h + 1):
    cnt = 0
    v = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 방문 안했으면 dfs 돌림
            if not v[i][j] and area[i][j] > r:
                cnt += 1
                dfs(i, j, r, v)

    # print(r, cnt)
    ans = max(ans, cnt)

print(ans)
